"""
popparsing
"""

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from .conversion import convert_pop_data, convert_file
