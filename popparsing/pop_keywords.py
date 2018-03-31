"""
This module defines valid POP keywords and handles abbreviations.
Not all are supported yet.
"""

import re

# Reference: Thermo-Calc Documentation Set
#            Data Optimization User Guide
#            POP-File Syntax (p 14)

POP_COMMANDS = sorted([ #comments refer to the page number in console mode reference

'ADVANCED_OPTIONS', # 125
'CHANGE_STATUS', # implementing # 135
'COMMENT', # implementing? # 40
'CREATE_NEW_EQUILIBRIUM', # implementing # 143
'DEFINE_COMPONENTS', # 143
'ENTER_SYMBOL', # implementing #195
'EVALUATE_FUNCTIONS', # 155
'EXPERIMENT', # implementing # 24
'EXPORT', # 26
'FLUSH_BUFFER', # 41
'IMPORT', # 27
'LABEL_DATA', # implementing # 28
'SAVE_WORKSPACE', #232
'SET_ALL_START_VALUES', # 162
'SET_ALTERNATE_CONDITION', #30
'SET_CONDITION', # implementing # 165
'SET_NUMERICAL_LIMITS', # 237
'SET_REFERENCE_STATE', # implementing # 169
'SET_START_VALUE', # 171
'SET_WEIGHT', # 33
'TABLE_HEAD', # implementing # 39
'TABLE_VALUES', # implementing # 39
'TABLE_END' # implementing # 39
])

POP_KEYWORDS = sorted([
    'FIXED',
    'DORMANT',
    'PHASES',
    'SPECIES',
    'COMPONENTS'
])

SYMBOL_KEYWORDS = sorted([
    'CONSTANT',
    'VARIABLE',
    'FUNCTION',
    'TABLE'
])

def expand_keyword(possible, candidate):
    """
    Expand an abbreviated keyword based on the provided list.
    From pycalphad.io.tdb_keywords
    Parameters
    ----------
    possible : list of str
        Possible keywords for 'candidate' to be matched against.
    candidate : str
        Abbreviated keyword to expand.
    Returns
    -------
    list of str of matching expanded keywords
    Examples
    --------
    None yet.
    """
    # Rewritten to escape each token in the split string, instead of the input
    # The reason is that Python 2.7 will escape underscore characters
    candidate_pieces = [re.escape(x) for x in \
        candidate.upper().replace('-', '_').split('_')]
    pattern = r'^'
    pattern += r'[^_\s]*_'.join(candidate_pieces)
    pattern += r'[^\s]*$'
    matches = [re.match(pattern, pxd) for pxd in possible]
    matches = [m.string for m in matches if m is not None]
    if len(matches) == 0:
        raise ValueError('{0} does not match {1}'.format(candidate, possible))

    return matches
