"""
A rough implementation of a script that converts parse results 
from pop_conversion.py to usable Espei JSON strings (that can
be written into Espei JSON files)
"""
from pop_conversion import main
from json import JSONEncoder

name = "Mgni.pop"
fp = open(name, 'r')
lst = main(fp.read())
symbols = lst[0]['symbols']
equilibria = lst[1:]


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
    Finds all components in the equlibrium data set
    """
    components = set()
    conditions = data['conditions']
    for key in conditions:
        sub_data = conditions[key]
        if type(sub_data)==dict and 'components' in sub_data:
            components.add(sub_data['components'][-1])
    if 'experiments' not in data:
        return list(components)
    experiments = data['experiments']
    for experiment in experiments:
        if 'phases' in experiment and len(experiment['phases']) > 1:
            components.add(experiment['phases'][-1])
    return list(components)

def parse_table(data, index):
    """
    Returns a list of all values of a table column
    Parameters:
        Data- the main equlibrium data structure
        Index- the table column to parse
    """
    if 'table_values' not in data:
        return []
    return list(map(lambda x : x[index], data['table_values']))
        
def condition_str(condition, phase, component):
    """
    Returns a string representation of
    a condition for a specific phase and component
    """
    return condition + '(' + phase + ',' + component + ')'

def get_phase_components(condition, phases, components):
    """
    Given a specific condition, a list of all phases, and a list of
    mixed phases and components:
        If there is only one element in the mixed list of components
        and phases, assume it is the only component and match with the first
        phase in the list of phases to return one phase_component string
        Otherwise, if there are multiple, assume the even_indexed elements(0,2,4,etc.)
        contains the phases and pair with the odd-indexed elements assumed to be components
        to return a list of phase-component strings for a specific condition/measurement(i.e. X(mole fraction))
    Parameters:
        condition(str): the specific condition to generate strings for
        phases(list): the equilibrium's list of phases
        components(list): a list of one component or mixed list of components and phases
    """
    results = []
    if len(components)==1:
        results.append(condition_str(condition, \
        phases[0], components[0]))
    else:
        for i in range(0, len(components), 2):
            results.append(condition_str(condition, \
            components[i], components[i+1]))
    return results

def parse_condition(data, condition_key):
    """
    If a condition key contains a data structure, properly parse 
    its value into a list of individual conditions and their identical value
    Note: this assumes that there is only one value for all phase-components in that one condition
    Parameters:
        data: the main equilibrium data structure
        condition_key: the specific condition to further parse
    Return:
        (list, str/int/float)- a tuplet of a list of separate components and a value
    """
    condition = data['conditions'][condition_key]
    phases = list(data['phases'].keys())
    components = condition['components']
    return get_phase_components(condition_key, phases, components), condition['value']		
    

def find_conditions(data):
    """
    Converts the conditions in the equilibrium data structures
    to condition values for the Espei JSON string
    """
    conditions = data['conditions']
    result = {}
    for key in conditions:
        value = conditions[key]
        if type(value)==dict:
            components, sub_val = parse_condition(data, key)
            if type(sub_val)==str and sub_val[0]=='@':
                index = int(sub_val[1:])-1
                sub_val = parse_table(data, index)
            for c in components:
                result[c] = sub_val
        elif value in symbols:
            #JSON Encoder does not support custom Float class
            result[key] = float(symbols[value])
        elif type(value)==str and value[0]=='@':
            index = int(value[1:])-1
            result[key]= parse_table(data, index)
        else:
            result[key] = value
    return result

def parse_experiments(data):
    """
    For the experiment in the data structure that has data recorded in a table column,
    the data type string and the list of table values is returned
    Return:
        (str, list)- the data type/units and the list of values
    """
    #TODO: Implement other experimental measurements and account for the degrees of freedom
    condition = ''
    table = None
    if 'experiments' not in data:
        return
    experiments = data['experiments']
    for case in experiments:
        if not str(case['symbol_repr'])[:3]=='col':
            continue
        index = int(str(case['symbol_repr'])[3:])-1
        condition = case['property']
        if 'phases' in case:
            components = case['phases']
            phases = list(data['phases'].keys())
            condition = get_phase_components(condition, phases, components)[0]
        tables = parse_table(data, index)
        return condition, tables
    return None, None
    
def findPhases(data):
    results = []
    phases = data['phases']
    for phase in phases:
        new_dict = {}
        new_dict['name'] = phase
        hints = {}
        #TODO: Ask about fixed vs. entered status implementation for pop_conversion.py
        hints['status'] = 'NULL'
        hints['quantity'] = phases[phase]
        new_dict['hints'] = hints
        results.append(new_dict)
    return results

def convert(data):
    """
    Main function that converts an equilibrium data structure to an ESPEI
    JSON string
    """
    result = {}
    result['phases'] = findPhases(data)
    result['components'] = find_components(data)
    result['conditions'] = find_conditions(data)
    result['output'], result['values'] = parse_experiments(data)
    return result
    #result['degrees_of_freedom']
    #encoder = JSONEncoder()
    #return encoder.encode(result)

def iterate(dataset, key):
    for data in dataset:
        print(data[key])
    
def main():
    data = []
    for e in equilibria:
        data.append(convert(e))
    return data
		
if __name__=='__main__':
    data = main()

#TODO: GET DEGREES OF FREEDOM
#TODO: GET OTHER EXPERIMENTAL VALUES
#TODO: GET SYMBOLS, LABELS, AND OTHER FUNCTIONS IN THE JSON STRING