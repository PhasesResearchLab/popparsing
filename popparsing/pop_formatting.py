"""
A rough implementation of a script that converts parse results 
from pop_conversion.py to usable Espei JSON strings (that can
be written into Espei JSON files)
"""
import sys

from popparsing.pop_conversion import get_points_lst, unpack_parse_results


def add_table_index(data, index, value):
    """
    Adds information that indicates which table column belongs to which type of data
    Parameters:
        data- the main equilibrium data dictionary/parse results
        index- the index of the table column
        value- the type of data the table column records
	"""
    if "indexes" not in data:
        data["indexes"] = []
    while len(data["indexes"]) < index:
        data["indexes"].append('')
    data["indexes"][index - 1] = value


def find_components(data):
    """
    Finds all components in the equilibrium data set
    """
    components = set()
    if 'reference_states' in data:
        states = data['reference_states']
        for state in states:
            if 'component' in state:
                components.add(state['component'])
    if 'conditions' in data:
        conditions = data['conditions']
        for sub_data in conditions:
            if 'element' in sub_data:
                info = unpack_parse_results(sub_data['element'])
                components.add(info[-1])
    if 'experiments' in data:
        experiments = data['experiments']
        for experiment in experiments:
            if 'phases' in experiment:
                case = unpack_parse_results(experiment['phases'])
                if len(case) > 1:
                    components.add(case[-1])
    return list(components)

def parse_table(data, index):
    """
    Returns a list of all values of a table column
    Parameters:
        Data- the main equlibrium data structure
        Index- the table column(indexed from 0) to parse
    """
    if 'table_values' not in data:
        return []
    return list(map(lambda x : x[index], data['table_values']))
        
def condition_str(condition, phase, component):
    """
    Returns a string representation of
    a condition for a specific phase and component
    """
    if phase!=None:
        return condition + '(' + phase + ',' + component + ')'
    else:
        return condition + '(' + component + ')'
    

def find_conditions(data, symbols):
    """
    Converts the conditions in the equilibrium data structures
    to a format to put in the equilibrium dictionary
    """
    # for some reason symbols is passed a dictionary of {'symbols': {symbols dict}}
    # TODO: fix the root cause in get_points_lst
    symbols = symbols.get('symbols', {})
    conditions = data['conditions']
    result = {}
    for condition in conditions:
        name = condition['property']
        if 'element' in condition:
            lst = condition['element']
            component = lst[-1]
            phase = None
            if len(lst) > 1:
                phase = lst[-2]
            name = condition_str(name, phase, component)
        value = condition['symbol_repr']
        value_str = str(value)
        if value_str[:3]=='col':
            index = int(value_str[3:])-1
            value = parse_table(data, index)
        elif value in symbols.keys():
            #TODO: Find better global symbol implementation
            value = float(symbols[value])
        elif value_str in symbols.keys():
            value = float(symbols[value_str])
        else:
            #JSONEncoder may not support custom Float class
            #TODO: Decide if Float objects need to be converted to primitive float objects
            value = float(value)
        result[name] = value
    return result

def parse_experiments(data, symbols):
    """
    For the experiment in the data structure that has data recorded in a table column,
    the data type string and the list of table values is returned
    Return:
        (list, list)- a list of data types/units and 
        the list of elements each output corresponds to
    """
    #TODO: Implement other experimental measurements and account for the degrees of freedom
    outputs = []
    values = []
    if 'experiments' not in data:
        return
    experiments = data['experiments']
    for case in experiments:
        condition = case['property']
        if 'phases' in case:
            components = unpack_parse_results(case['phases'])
            element = components[-1]
            phase = None
            if len(components) > 1:
                phase = components[-2]
            condition = condition_str(condition, phase, element)
        value = case['symbol_repr']
        equality = case['equality']
        if str(value)[:3]=='col':
            index = int(str(case['symbol_repr'])[3:])-1
            value = parse_table(data, index)
        elif value in symbols:
            value = float(symbols[value])
        else:
            value = float(value)
        if equality != '=':
            new_dict = {
            'equality' : equality,
            'value' : value
            }
            value = new_dict
        outputs.append(condition)
        values.append(value)
    return outputs, values
    
def find_phases(data):
    """
    Finds different phases and their details 
    within a given parse result object
    """
    results = []
    phases = data['phases']
    for phase in phases:
        new_dict = {}
        new_dict['name'] = phase
        hints = {}
        #TODO: Ask about fixed vs. entered status implementation for pop_conversion.py
        if type(phases[phase])==str:
            hints['status'] = phases[phase]
        else:
            hints['status'] = 'ENTERED/FIXED'
            hints['quantity'] = phases[phase]
        new_dict['hints'] = hints
        results.append(new_dict)
    return results

def convert(data, symbols={}):
    """
    Converts a list of equilibriums into a list
    of formatted dictionaries, mainly used
    when converting a POP file into a list of dictionaries
    
    Parameters:
    ------------
    data: a single parse result object to convert to dictionary
    symbols(optional): a dictionary of labeled constants the data may need
    
    Return:
    --------
    dict: a single dictionary  
    """
    result = {}
    result['phases'] = find_phases(data)
    result['components'] = find_components(data)
    result['conditions'] = find_conditions(data, symbols)
    result['outputs'], result['values'] = parse_experiments(data, symbols)
    result['reference'] = data['label']
    return result
    
def convert_set(equilibria, symbols={}):
    """
    Converts a list of equilibriums into a list
    of formatted dictionaries, mainly used
    when converting a POP file into a list of dictionaries
    
    Parameters:
    ------------
    equilibria: a list of parse results to convert
    symbols(optional): a dictionary of labeled constants
    
    Return:
    ---------
    list: the list of equilibrium dictionaries
    """
    data = []
    for case in equilibria:
        data.append(convert(case, symbols))
    return data


def convert_pop_data(data):
    """

    Parameters
    ----------
    data : str

    Returns
    -------
    list
        A list of equilibrium dictionaries
    """
    lst = get_points_lst(data)
    symbols = lst[0]
    equilibria = lst[1:]
    return convert_set(equilibria, symbols)


def convert_file(file_name):
    """
    Converts a POP file with an inputted file name
    and converts each of its equilibrium into 
    a list of formatted dictionary
    
    Parameters:
    -----------
    file_name: the name of the file to be converted
    
    Return:
    -----------
    list - a list of equilibrium dictionaries
    """
    with open(file_name, 'r') as fp:
        pop_data = fp.read()
    return convert_pop_data(pop_data)

def main(infile, outfile):
    """
    The code that runs when script is run
    through the command prompt
    
    Syntax: python pop_formatting.py [input_pop_filename] [output_filename]
    
    """
    dict_lst = convert_file(infile)
    import json
    json_obj = json.JSONEncoder()
    fp = open(outfile, 'w')
    outstring = json_obj.encode(dict_lst)
    fp.write(outstring)
    fp.close()
		
if __name__=='__main__':
    if len(sys.argv)>=2:
        main(sys.argv[-2], sys.argv[-1])

#TODO: GET SYMBOLS, LABELS, AND OTHER FUNCTIONS IN THE JSON STRING
#TODO: GET POP_CONVERSION TO IMPLEMENT FIXED VS. ENTERED
#TODO: GET POP_CONVERSION TO IMPLEMENT DEGREES OF FREEDOM
