"""
Command Line Interface for popparsing
"""

import sys, json

from .conversion import convert_file


def main(infile, outfile):
    """
    The code that runs when script is run
    through the command prompt

    Syntax: popparsing [input_pop_filename] [output_filename]

    """
    dict_lst = convert_file(infile)
    # TODO: Can the JSONEncoder be removed in favor of json.dump?
    json_obj = json.JSONEncoder()
    with open(outfile, 'w') as fp:
        outstring = json_obj.encode(dict_lst)
        fp.write(outstring)


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        main(sys.argv[-2], sys.argv[-1])
