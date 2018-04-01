from .parsing import get_points_lst
from .formatting import convert_set


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

    Parameters
    ----------
    file_name: the name of the file to be converted

    Returns
    -------
    list - a list of equilibrium dictionaries
    """
    with open(file_name, 'r') as fp:
        pop_data = fp.read()
    return convert_pop_data(pop_data)
