.. popparsing documentation master file, created by
   sphinx-quickstart on Sat Mar 31 19:48:48 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==========
popparsing
==========

The popparsing package is used to turn a file with POP commands into
a JSON file that contains all information about each equilibrium set

Installation
============

Prerequisites for the popparsing package
include the pyparsing and sympy packages

To install, open up a terminal or
command prompt and enter:

``pip install popparsing``

Usage
=====

To generate a JSON file from a POP file, enter in the command prompt 
``popparsing [input_file.pop] [output_file.json]`` where input_file.pop is 
a file with POP commands and extension .pop and output_file.json is the json file
to write to.

Input
-----

The popparsing package supports POP files with the following commands below.

CHANGE_STATUS PHASE
^^^^^^^^^^^^^^^^^^^

The ``CHANGE_STATUS PHASE`` command must have two arguments separated by an '='.
The first argument to the left of the equal sign is a list of phase names
separated by commas or spaces.  The second argument is either just a status string or
both a status string and a floating point value separated by a space.  A supported abbreviation
of the command is ``CH P``.  Status phase names ``FIXED``, ``DORMANT``, and ``ENTERED`` are supported
and can be abbreviated to any shorter length.  However, phase names abbreviations are 
currently not supported and must be typed exactly how it should appear on the equilibrium data set.

Valid Examples:

.. code-block:: yaml

    CHANGE_STATUS PHASE BCC HCP DEL=DORMANT
    CHANGE_STATUS PHASE BCC HCP DEL=FIXED 1
    CHANGE_STATUS PHASE BCC,HCP,DEL=FIXED 1
    CHANGE_STATUS PHASE BCC,HCP,DEL=FIX 1
    CHANGE_STATUS PHASE BCC, HCP, DEL = FIX 1
    CHANGE_STATUS PHASE BCC HCP DEL = FIX 1
    CH P BCC HCP DEL=F 1

CREATE_NEW_EQUILIBRIUM
^^^^^^^^^^^^^^^^^^^^^^

The ``CREATE_NEW_EQUILIBRIUM`` command must have two arguments.  The first
argument is unused by the pop file parser.  The second argument is an integer, which
is an initialization code that tells the parser how to initialize the equilibrium set.
A supported abbreviated version of the command is ``C-N``.  

Valid Examples:

.. code-block:: yaml

    CREATE_NEW_EQUILIBRIUM 108, 1
    CREATE_NEW_EQUILIBRIUM 108,1
    CREATE_NEW_EQUILIBRIUM 108 1
    C-N 108 1

Note: Only initialization code 1 is supported at the moment.

ENTER_SYMBOL CONSTANT
^^^^^^^^^^^^^^^^^^^^^

EXPERIMENT
^^^^^^^^^^

SET_CONDITION
^^^^^^^^^^^^^

SET_REFERENCE_STATE
^^^^^^^^^^^^^^^^^^^

The ``SET_REFERENCE_STATE`` command must have at least two arguments: 
the component name and the phase name respectively separated by either
comma or space.  The pop file parser does support additional arguments
after the first two, but currently, those arguments will not affect 
the output data.  The supported abbreviation of the command is ``S-R-S``.

Valid Examples:

.. code-block:: yaml

    SET_REFERENCE_STATE U BCC_A2,,,,,,
    SET_REFERENCE_STATE U,BCC_A2,,,,,,
    SET_REFERENCE_STATE U BCC_A2
    SET_REFERENCE_STATE U, BCC_A2
    SET_REFERENCE_STATE U BCC_A2 * 100000
    S-R-S U BCC_A2

TABLE_VALUES and TABLE_END
^^^^^^^^^^^^^^^^^^^^^^^^^^

Output
------

Main Equilibrium Dictionary
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The output of the popparsing command is a JSON file
containing a list of dictionaries (one per equilibrium data set)
with each dictionary containing the following keys and values.

+----------+---------------------------+
|Key       |Value                      |
+==========+===========================+
|phases    |A dictionary of phases and |
|          |their statuses and values  |
+----------+---------------------------+
|components|A list of elements involved|
|          |in the equilibrium set     |
+----------+---------------------------+
|conditions|A dictionary of conditions |
|          |and their values           |
|          |(a single number or a list |
|          |of values);                |
|          +---------------------------+
|          |Also contains the          |
|          |'reference_states' key     |
|          |which refers to a          |
|          |dictionary of components as|
|          |keys and phases as values  |
+----------+---------------------------+
|outputs   |A list of names of data    |
|          |that correspond to the list|
|          |the 'values' key point to  |
+----------+---------------------------+
|values    |A list of data (either a   |
|          |single number or a list)   |
+----------+---------------------------+

Phase Sub-dictionary
^^^^^^^^^^^^^^^^^^^^

The phases dictionary contains phase names
and a sub-dictionary of statuses and/or values
as values of each phase name.

+----------+-----------------------------+
|Key       |Value                        |
+==========+=============================+
|status    |One of the following strings:|
|          |``'FIXED'``, ``'ENTERED'``,  |
|          |``'DORMANT'``, ``'SUSPEND'`` |
+----------+-----------------------------+
|value     |An specified numerical value |
|          |for the phase (only if status|
|          |is ``FIXED`` or ``ENTERED``) |
+----------+-----------------------------+

Example
-------

The following input file will generate the following output file.

Input:

.. code-block:: yaml

    $===================================================
    $  BCC FORMATION ENTHALPIES X(TI)=0.1 TO 0.6
    $===================================================
    TABLE_HEAD 540
    CREATE_NEW_EQUILIBRIUM @@,1
    CHANGE_STATUS PHASE *=SUS
    CHANGE_STATUS PHASE BCC_A2=FIXED 1
    SET_REFERENCE_STATE U BCC_A2,,,,,,
    SET_REFERENCE_STATE Ti BCC_A2,,,,,,
    SET_CONDITION  P=102325 T=200
    SET_CONDITION X(Ti)=@1
    LABEL AHMR1
    EXPERIMENT HMR(BCC_A2)=@2:500
    TABLE_VALUES
    $ X(Ti)        HMR
    0.10          2450
    0.20          3000
    0.30          2990
    0.40          2430
    0.50          1400
    0.60           -65
    TABLE_END
    $ -----------

Output:

.. code-block:: python

    [
        {
            'phases': {
                'BCC_A2' : {
                    'status' : 'FIXED',
                    'value' : 1.0
                }
            }
            'components': [
                'Ti', 
                'U'
            ]
            'conditions': {
                'P': 102325.0
                'T': 200.0
                'X(Ti)': [
                    0.1,
                    0.2,
                    0.3,
                    0.4,
                    0.5,
                    0.6
                ]
                'reference_states': {
                    'U': 'BCC_A2',
                    'Ti': 'BCC_A2'
                }
            }
            'outputs': [ 'HMR(BCC_A2)' ]
            'values': [
                [
                    2450.0,
                    3000.0,
                    2990.0,
                    2430.0,
                    1400.0,
                    -65.0
                ]
            ]
        }
    ]
   
For a full example, see the :doc:`MgNi POP File Example <mgni>`.


.. toctree::
   :maxdepth: 2
   
   self

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api/modules
   mgni


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
