"""
This module handles conversion of POP files to JSON files in ESPEI format
"""

from sympy.parsing.sympy_parser import parse_expr
from pyparsing import *
from pop_keywords import expand_keyword, POP_COMMANDS

print("""WARNING! This module is VERY experimental. You will most likely get failures or incorrect answers.
You should check all of your data instead of assuming it is correct.
Please report any errors so that this module can be improved.""")


class ExperimentSet(dict):
    """
    Experiment set, which is a stored as a dictionary.

    The reason for the subclass is to store metadata about the experiment set while it is being
    constructed by parsing. Once it is constructed, there is no use for having a class because the
    data will be fully populated as a normal dictionary.
    """

    def update(self, E=None, **F):
        """
        Overrides dict update to return self (for lambda functions)
        """
        super(ExperimentSet, self).update(E, **F)
        return self


class POPCommand(CaselessKeyword):
    """
    Parser element for dealing with POP command abbreviations.
    """

    def parseImpl(self, instring, loc, doActions=True):
        # Find the end of the keyword by searching for an end character
        # TODO: how much of this do I need?
        start = loc
        endchars = ' ():,'
        loc = -1
        for charx in endchars:
            locx = instring.find(charx, start)
            if locx != -1:
                # match the end-character closest to the start character
                if loc != -1:
                    loc = min(loc, locx)
                else:
                    loc = locx
        # if no end character found, just match the whole thing
        if loc == -1:
            loc = len(instring)
        try:
            res = expand_keyword([self.match], instring[start:loc])
            if len(res) > 1:
                self.errmsg = '{0!r} is ambiguous: matches {1}' \
                    .format(instring[start:loc], res)
                raise ParseException(instring, loc, self.errmsg, self)
            # res[0] is the unambiguous expanded keyword
            # in principle, res[0] == self.match
            return loc, res[0]
        except ValueError:
            pass
        raise ParseException(instring, loc, self.errmsg, self)


def _pop_grammar():
    """
    Returns the pyparsing grammar for a POP file.
    """
    # pyparsing "constants"
    sCOMMA = Suppress(',')  # supresses
    int_number = Word(nums).setParseAction(lambda t: [int(t[0])])
    # matching float w/ regex is ugly but is recommended by pyparsing
    float_number = (Regex(r'[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?') | '0') \
        .setParseAction(lambda t: [float(t[0])])
    # symbol name, e.g., phase name or equilibrium name
    symbol_name = Word(alphanums + '_:', min=1)
    equalities = Word('=') ^ Word('<') ^ Word('>')
    pm = oneOf('+ -')
    label = Word('@' + nums)
    value = (float_number | int_number | label | symbol_name)
    const = Group(symbol_name + equalities + value)
    phases = Group(OneOrMore(symbol_name + Optional(sCOMMA))) | '*'
    prop_prefix = symbol_name + Suppress('(') + phases + Suppress(')')
    property = Group(prop_prefix + equalities + value)
    expr = Group(OneOrMore(prop_prefix | float_number | oneOf('. + - / * ( )') | symbol_name))
    arith_cond = Group(OneOrMore(Optional(Word(nums) + '*') + prop_prefix + Optional(
        pm)) + equalities + value)  # an arithmetic matcher for complex conditions
    error = Group(Suppress(':') + float_number + Optional('%'))
    sERROR = Suppress(error)
    cmd_equilibrium = POPCommand('CREATE_NEW_EQUILIBRIUM') + (Word('@@,') ^ int_number) + Optional(
        sCOMMA) + int_number
    # TODO: implement changing status of other things
    phase_statuses = ((POPCommand('FIXED') ^ POPCommand('ENTERED')) + float_number) | POPCommand(
        'DORMANT') | POPCommand('SUSPENDED')
    cmd_change_status = POPCommand('CHANGE_STATUS') + POPCommand('PHASE') + phases + Suppress(
        '=') + Group(phase_statuses)
    enter_const = POPCommand('CONSTANT') + Group(OneOrMore(const))
    enter_func_var = (POPCommand('FUNCTION') | POPCommand('VARIABLE')) + Group(symbol_name + '=' + expr)
    enter_table = POPCommand('TABLE')  # TODO: implement
    cmd_en_symbol = POPCommand('ENTER_SYMBOL') + (enter_const | enter_func_var | enter_table)
    cmd_table_head = POPCommand('TABLE_HEAD') + int_number
    cmd_table_values = POPCommand('TABLE_VALUES') + sCOMMA + Group(
        delimitedList(Group(OneOrMore(float_number)))) + Suppress(POPCommand('TABLE_END'))
    cmd_set_ref_state = POPCommand('SET_REFERENCE_STATE') + symbol_name + symbol_name + Optional(
        OneOrMore(sCOMMA))  # TODO: should these default values be handled?
    cmd_set_condition = POPCommand('SET_CONDITION') + OneOrMore(
        (arith_cond | property | const) + Optional(sERROR) + Optional(sCOMMA))
    cmd_label = POPCommand('LABEL_DATA') + OneOrMore(Word(alphanums))
    cmd_experiment_phase = POPCommand('EXPERIMENT') + OneOrMore(
        Group((property | const) + sERROR) + Optional(sCOMMA))
    cmd_start_value = POPCommand('SET_START_VALUE') + property
    cmd_save = POPCommand('SAVE_WORKSPACE')
    return (
               cmd_equilibrium | cmd_change_status | cmd_en_symbol | cmd_table_head | cmd_table_values |
               cmd_set_ref_state | cmd_set_condition | cmd_label |
               cmd_experiment_phase | cmd_start_value | cmd_save) + Optional(
        Suppress(';')) + stringEnd


def unpack_parse_results(parse_results):
    """
    Recursively unpacks parse results and return the unpacked result.

    Args:
        parse_results (ParseResults): a tuple of a list of values and dict of names. The list may contain nested ParseResults

    Returns:
        list: List of the intended structure
    """
    results_list = []
    for result in parse_results:
        if isinstance(result, ParseResults):
            results_list.append(unpack_parse_results(result))
        else:
            results_list.append(result)
    return results_list


def _unimplemented(*args, **kwargs):
    """
    Wrapper to raise NotImplementedError

    This should be used when a command that affects the data is unimplmented. If the command does not
    affect the data, then `_pass` should be used.
    """
    raise NotImplementedError


def _pass(*args, **kwargs):
    """
    Pass is intended for POP commands that do not impact the data

    Commands that do impact the data should use `_unimplemented`
    """
    return args[0]  # return the experiment unchanged


def _new_equilibrium(_, name, code):
    """

    Args:
        _ (ExperimentSet): The old experiment set. Will not be used.
        name (str): The name code given to the new equilibrium. Unused.
        code (The ): The initilization code for the equilibrium

    Returns:

    Possible initialization codes:
        0: suspend all phases and components
        1: enter all components only
        2: enter all
    """

    if code == 1:
        return ExperimentSet()
    else:
        _unimplemented()


def _process_phases(exp, status_type, phases, status):
    """
    Get the phases from change status

    Args:
        exp (ExperimentSet): The current experiment set
        status_type (str): What to change the status of e.g. a PHASE
        phases ([str]): A list of phase names
        status ([str, int?]): A string denoting the status with an optional int for the numerical representation

    Returns:

    """
    if status_type != 'PHASE': _unimplemented()
    if status[0] == 'FIXED' or status[0] == 'ENTERED':  # TODO: fixed vs entered in implementation?
        existing_phases = exp.get("phases", [])
        exp["phases"] = {phase: status[1] for phase in phases}
    elif status[0] == 'DORMANT' or status[0] == 'SUSPENDED':
        pass
    return exp

def construct_symbol(symbol_list):
    """
    Get a SymPy representation from brute force concatenating and parsing

    Args:
        symbol_list ([str*, float*, int*]): Strings, floats and/or ints describing the symbol symbolically

    Returns:
        Expr: A SymPy expression constructed from the SymPy parser
    """
    symbol_string = ''
    for s in symbol_list:
        if s == '.':
            s = '*d'  # handle derivatives. TODO: improve derivative handling
        elif '@' in str(s):
            print(type(s))
            s = str(s).replace('@', 'col')  # replace column reference, '@' with 'col'
            print(str(s))
        if isinstance(s, ParseResults):
            s = unpack_parse_results(s)
            new_s = '_'
            for sub_s in s:
                new_s = ''.join([new_s, sub_s])
            s = new_s
        symbol_string = ''.join([symbol_string,str(s)])
    expr = parse_expr(symbol_string)
    return expr

def _process_symbols(exp, symbol_type, symbols):
    """

    Args:
        exp (ExperimentSet): The current experiment set
        symbol_type (str): CONSTANT, FUNCTION, or TABLE
        symbols ([[str]]): List of symbol names and values usually ["SYM","=","VALUE"]

    Returns:
        ExperimentSet: the passed experiment set object
    """
    if symbol_type == 'CONSTANT':
        exp_symbols = exp.get('symbols', {})
        for symbol in symbols:
            # we are going to assume that the first value in an array is the symbol name,
            # the second is '=' and the remaining are symbolic and can be constructed with SymPy
            exp_symbols[symbol[0]] = construct_symbol(symbol[2:])
        exp["symbols"] = exp_symbols
    elif symbol_type == 'FUNCTION':
        exp_symbols = exp.get('symbols', {})
        # we are going to assume that the first value in an array is the symbol name,
        # the second is '=' and the remaining are symbolic and can be constructed with SymPy
        exp_symbols[symbols[0]] = construct_symbol(symbols[2])
        exp["symbols"] = exp_symbols
    elif symbol_type == 'TABLE':
        raise NotImplementedError

    return exp

def _process_experiment(exp, experiments):
    exp_experiments = exp.get('experiments', [])
    for experiment in experiments:
        d = {}
        d["property"] = experiment[0]
        print(experiment)
        # directly create a symbolic equation with all of the
        if isinstance(experiment[1], ParseResults):
            # assume the format prop(phase) (=/>/<) symbol is followed
            d["phases"] = experiment[1]
            d["equality"] = experiment[2]
            d["symbol_repr"] = construct_symbol(experiment[3:])
        else:
            # assume prop (=/>/<) symbol
            d["equality"] = experiment[1]
            d["symbol_repr"] = construct_symbol(experiment[2:])
    exp["experiments"] = exp_experiments
    return exp

_POP_PROCESSOR = {
    'TABLE_HEAD': _pass,
    'TABLE_VALUES': lambda exp, table_values: exp.update(
        {"table_values": unpack_parse_results(table_values)}),
    'ADVANCED_OPTIONS': _pass,  # 125
    'CHANGE_STATUS': _process_phases,  # implementing # 135
    'COMMENT': _pass,  # implementing? # 40
    'CREATE_NEW_EQUILIBRIUM': _new_equilibrium,  # implementing # 143
    'DEFINE_COMPONENTS': _unimplemented,  # 143
    'ENTER_SYMBOL': _process_symbols,  # implementing #195
    'EVALUATE_FUNCTIONS': _pass,  # 155
    'EXPERIMENT': _process_experiment,  # implementing # 24
    'EXPORT': _pass,  # 26
    'FLUSH_BUFFER': _pass,  # 41
    'IMPORT': _pass,  # 27
    'LABEL_DATA': lambda exp, label: exp.update({"label": label}),  # implementing # 28
    'SAVE_WORKSPACE': _pass,  # 232
    'SET_ALL_START_VALUES': _pass,  # 162
    'SET_ALTERNATE_CONDITION': _pass,  # 30
    'SET_CONDITION': _unimplemented,  # implementing # 165
    'SET_NUMERICAL_LIMITS': _pass,  # 237
    'SET_REFERENCE_STATE': _unimplemented,  # implementing # 169
    'SET_START_VALUE': _unimplemented,  # 171
    'SET_WEIGHT': _pass,  # 33
}


def parsable(instring):
    """
    Return an easily parsable list of strings from an input string.
    """
    lines = instring
    lines = lines.replace('\t', ' ')
    lines = lines.strip()  # strips trailing and leading whitespace
    splitlines = lines.split('\n')  # split by newlines
    splitlines = [' '.join(k.split()) for k in splitlines if
                  k != '']  # separates everything by just one whitespace character
    splitlines = [l for l in splitlines if not (l.startswith("@@") or l.startswith("$"))]
    # Concatenate table values to table end on to one line
    #  very hacky, cannot handle cases where things are in an unexpected order or abbreviated.
    new_splitlines = []
    table_values_line = ''
    capture_values = False
    for line in splitlines:
        if line.startswith('TABLE_VALUE'):
            capture_values = True
            table_values_line = ''.join([table_values_line, line])
        elif line.startswith('TABLE_END'):
            capture_values = False
            table_values_line = ' '.join([table_values_line, line])
            new_splitlines.append(table_values_line)
            table_values_line = ''
        elif capture_values:
            table_values_line = ', '.join([table_values_line, line])
        else:
            new_splitlines.append(line)
    splitlines = new_splitlines
    return splitlines


def main(instring):
    # create an empty
    global_symbols = {}
    current_experiment_set = global_symbols
    data = [global_symbols]  # a list of dictionaries. New dictionaries are added when a new equilibrium is added.
    commands = parsable(instring)
    for command in commands:
        tokens = None
        try:
            tokens = _pop_grammar().parseString(command)
            new_experiment_set = _POP_PROCESSOR[tokens[0]](current_experiment_set, *tokens[1:])
            # if the new object is different than the old, then we want to make that current and add
            # it to the list of experiments
            if new_experiment_set is not current_experiment_set:
                current_experiment_set = new_experiment_set
                data.append(current_experiment_set)

        except ParseException:
            print("Failed while parsing: " + command)
            print("Tokens: " + str(tokens))
            raise
        except NotImplementedError:
            # print("The command {} is not implemented.".format(tokens[0]))
            pass
            # raise NotImplementedError("Command {} is not implemented for tokens {}".format(str(tokens[0]), str(tokens[1:])))
        print(tokens)
        print(command)
    print(data)


try:
    from mgni_test import *

    strs = [mgni_full_str, ca_bi]
    instring = ""
    for s in strs:
        instring = "\n".join([instring, s])
except ImportError:
    print('Failed to import mgni_test. Falling back to last argument to script')
    import sys

    f_arg = sys.argv[-1]
    with open(f_arg, 'r') as f:
        instring = f.read()

if __name__ == "__main__":
    main(instring)

# IMPLEMENTATION STEPS
# 1. Handle the syntax. Be able to parse everything. Start with Mg-Ni
# 2. Get the useful stuff from the parsed data
# 3. Reformat to JSON

# TODO: handle the global_symbols better. Should I make a global variable and just substitue them?

#CHANGELIST
#- Remove redundant experiment constant command
#- Suppress experimental and conditional error