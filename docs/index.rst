.. popparsing documentation master file, created by
   sphinx-quickstart on Sat Mar 31 19:48:48 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==========
popparsing
==========

The popparsing package is used to turn a file with POP commands into
a JSON file that contains all information about each equilibrium set

Installation and Usage
======================

Prerequisites for the popparsing package
include the **pyparsing** and **sympy** packages.
To install, open up a terminal or
command prompt and enter ``pip install popparsing``.
To generate a JSON file from a POP file, enter in the command prompt 
``popparsing [input_file.pop] [output_file.json]`` where ``input_file.pop`` is 
a file with POP commands and extension .pop and ``output_file.json`` is the json file
to write to.

Input
=====

The popparsing package supports POP files with the following commands below.
The subsequent subsections are details of supported syntaxes 
of **only commands that affect the output of the pop file parser**.

+--------------------------+---------------------------+
|                 Affects the output?                  |
+--------------------------+---------------------------+
|           YES            |             NO            |
+==========================+===========================+
|``CHANGE_STATUS PHASE``   |``ADVANCED_OPTIONS``       |
+--------------------------+---------------------------+
|``CREATE_NEW_EQUILIBRIUM``|``CHANGE_STATUS COMPONENT``|
+--------------------------+---------------------------+
|``ENTER_SYMBOL CONSTANT`` |``COMMENT``                |
+--------------------------+---------------------------+
|``EXPERIMENT``            |``DEFINE_COMPONENTS``      |
+--------------------------+---------------------------+
|``LABEL_DATA``            |``ENTER_SYMBOL FUNCTION``  |
+--------------------------+---------------------------+
|``SET_CONDITION``         |``ENTER_SYMBOL TABLE``     |
+--------------------------+---------------------------+
|``SET_REFERENCE_STATE``   |``EVALUATE_FUNCTIONS``     |
+--------------------------+---------------------------+
|``TABLE_END``             |``EXPORT``                 |
+--------------------------+---------------------------+
|``TABLE_VALUES``          |``EXTERNAL``               |
+--------------------------+---------------------------+
|                          |``FLUSH_BUFFER``           |
+--------------------------+---------------------------+
|                          |``IMPORT``                 |
+--------------------------+---------------------------+
|                          |``SAVE``                   |
+--------------------------+---------------------------+
|                          |``SAVE_WORKSPACE``         |
+--------------------------+---------------------------+
|                          |``SAVE_WORKSPACES``        |
+--------------------------+---------------------------+
|                          |``SET_ALL_START_VALUES``   |
+--------------------------+---------------------------+
|                          |``SET_ALTERNATE_CONDITION``|
+--------------------------+---------------------------+
|                          |``SET_NUMERICAL_LIMITS``   |
+--------------------------+---------------------------+
|                          |``SET_START_VALUE``        |
+--------------------------+---------------------------+
|                          |``SET_WEIGHT``             |
+--------------------------+---------------------------+
|                          |``TABLE_HEAD``             |
+--------------------------+---------------------------+

CHANGE_STATUS PHASE
-------------------

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
----------------------

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
---------------------

The ``ENTER_SYMBOL CONSTANT`` command has one or multiple arguments separated by
either space or commas.  Each argument has the same syntax and assigns a constant 
value to a variable name, with the variable name to the left of the equal sign and
the numerical value to the right.  There must be no space between the variable name
and the equal sign or between the equal sign and the numerical value for each argument.
The supported abbreviation of the command is ``E-SYM CON``.

Valid Examples:

.. code-block:: yaml

    ENTER_SYMBOL CONSTANT P0=1E5 R0=8.314
    ENTER_SYMBOL CONSTANT P0=1E5,R0=8.314
    E-SYM CON P0=1E5 R0=8.314

EXPERIMENT
----------

The ``EXPERIMENT`` command has one or more arguments separated by 
spaces or commas.  The arguments only have one specific syntax with four parts in a specific order.
The first part is the variable name, and the second part is either an '=', '<', or '>'.  The third
part is either a numerical value or an '@' followed by an integer indicating the column number of the table
created by the TABLE_VALUES command the property or variable name corresponds to. (See :ref:`table_values` for 
more details) Finally, a ':' and a numerical value representing the error is placed after.  
The error value can optionally be followed by a % sign.  A supported abbreviation of the command is ``EXP``.

Valid Examples:

.. code-block:: yaml

    $ Note: '@2' indicates that ACR(MG)
    $ corresponds to a list of values in the second column of
    $ the created table.
    EXPERIMENT ACR(MG)=@2:5% X(HCP_A3,ZR)=0.988:1E-2
    EXPERIMENT ACR(MG)=@2:5%,X(HCP_A3,ZR)=0.988:1E-2
    EXPERIMENT T=1370:2
    EXPERIMENT X(LIQ,NI)=0.803:5%

Note: The error value after the colon representing the is
is currently not included in the output, but both the colon 
and error value are necessary parts of the syntax.

LABEL_DATA
----------

The ``LABEL_DATA`` command has one argument which is just a string with
alphanumeric characters.  It is common to use the abbreviated version, ``LABEL``.

Examples: 

.. code-block:: yaml

    LABEL_DATA AHMR1
    LABEL ACP

SET_CONDITION
-------------

The ``SET_CONDITION`` command has one or more arguments separated by commas
or spaces.  Each argument has the same specific syntax: a variable or property
name, followed by an '=' sign, and then either a numerical value or an '@' followed
by an integer indicating the table column number the property or variable corresponds to.
(See :ref:`table_values` for details)  The supported abbreviation for the command is ``S-C``.

.. code-block:: yaml

    $ Note: '@1' indicates that X(NI)
    $ corresponds to a list of values in the first column of
    $ the created table.
    SET_CONDITION T=1073 P=P0 X(NI)=@1
    SET_CONDITION T=1073,P=P0,X(NI)=@1
    SET_CONDITION T=1073, P=P0, X(NI)=@1
    $ Temperature variable corresponds to a list of values 
    $ on the second colun of the created table
    S-C T=@2

SET_REFERENCE_STATE
-------------------

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

.. _table_values:

TABLE_VALUES and TABLE_END
--------------------------

The ``TABLE_VALUES`` command marks the start of the table while 
the ``TABLE_END`` command marks the end of it.  Each line between
the two commands must contain the same number of numerical values, or in
other words, each column in the constructed table must have the same number of
elements.  Additionally, these entered values are separated by spaces.  
The number of spaces before and after each numerical value is irrelevant.
These values will be used by variables that are assigned with an '@' followed
by an integer indicating which column of values in the table will be used.

Example:

.. code-block:: yaml

    $The values on the first column correspond to X(LIQUID,Ti)
    $The values on the second column correspond to temperature(T).
    SET_CONDITION T=@2
    EXPERIMENT X(LIQUID,Ti)=@1:0.01
    TABLE_VALUES
    0.00          1406
    0.0045        1420
    0.01          1445
    0.02          1446
    0.03          1495
    0.04          1563
    0.05          1643
    0.10          1957
    0.15          2093
    0.20          2117
    0.30          2198
    TABLE_END

Output
======

Main Equilibrium Dictionary
---------------------------

The output of the popparsing command is a JSON file
containing a list of dictionaries (one per equilibrium data set)
with each dictionary containing the following keys and values.
Each dictionary is created by a ``CREATE_NEW_EQUILIBRIUM`` command,
and the command lines between that particular line and either the next line
calling the ``CREATE_NEW_EQUILIBRIUM`` command or the end of the file determines
the contents of that dictionary.

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
|reference |The argument from the      |
|          |``LABEL`` command          |
+----------+---------------------------+

Example:

Input:

.. code-block:: yaml

    CREATE_NEW_EQUILIBRIUM @@,1
    CHANGE_STATUS PHASE LIQUID=DORMANT
    CREATE_NEW_EQUILIBRIUM @@,1
    
    
Output:

.. code-block:: python

    [
        #First C-N command creates a dictionary.
        #CHANGE_STATUS PHASE command inserts a 'phases' key 
        #in the first dictionary.
        {
            'phases' : {
                'LIQUID' : {
                    'status' : 'DORMANT'
                }
            }
        },
        #Second C-N command creates an empty dictionary.
        {
        }
    ]

Phases Sub-dictionary
---------------------

The phases dictionary contains phase names as keys
and a sub-dictionary of statuses and/or values
as values.

+----------------------------------------+
|Dictionary for each phase               |
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

Example:

Input:

.. code-block:: yaml

    CREATE_NEW_EQUILIBRIUM @@,1
    CHANGE_STATUS PHASE LIQUID=DORMANT
    CHANGE_STATUS PHASE SPINEL=FIXED 1
    
    
Output:

.. code-block:: python

    [
        {
            'phases' : {
                'LIQUID' : {
                    'status' : 'DORMANT'
                }
                'SPINEL' : {
                    'status' : 'FIXED',
                    'value' : 1.0
                }
            }
        }
    ]

Conditions Sub-dictionary
-------------------------

The content of the dictionary that the 'conditions' key refers
to depends on the arguments of one or more ``SET_CONDITION`` commands. 
It will contain condition names as keys, and each value
will either be a floating point number or a list of
floating point numbers.  In addition to the condition names,
the 'conditions' dictionary will always contain a 'reference_states'
key which stores another dictionary.  The contents of the 'reference_states'
dictionary is determined by the arguments of each ``SET_REFERENCE_STATE`` command.  
It will have component names as keys and phase names as values.
If the ``SET_REFERENCE_STATE`` command is not used for the equilibrium
set, then the dictionary will be empty.

Example:

Input:

.. code-block:: yaml

    CREATE_NEW_EQUILIBRIUM @@,1
    SET_CONDITION T=@1 P=10000
    TABLE_VALUES
    100
    200
    300
    TABLE_END
    
    
Output:

.. code-block:: python

    [
        {
            'conditions' : {
                'T' : [ 100.0, 200.0, 300.0 ],
                'P' : 100000
            }
        }
    ]

Components List
---------------

The 'components' list consist of string elements of all
components found in the POP commands for the created equilibrium set.
The pop file parser finds these elements in the first arguments of 
``SET_REFERENCE_STATE`` commands and property names such as X(NI) and X(LIQ,NI)
in the ``SET_CONDITION`` and ``EXPERIMENT`` commands.

Example: The following input would yield ``['MG', 'NI']`` as a list of components
because of ``X(NI)`` and ``ACR(MG)``.

Input:

.. code-block:: yaml

    CREATE_NEW_EQUILIBRIUM @@,1
    SET_CONDITION X(NI)=0.1
    EXPERIMENT ACR(MG)=@1:5
    TABLE_VALUES
    0.1
    0.2
    0.3
    TABLE_END

Outputs and Values Lists
------------------------

The 'outputs' and 'values' keys refer
to two lists of the same size and are created by 
parsing the arguments of ``EXPERIMENT`` commands. Each n-th element
in the output list corresponds to the n-th element
of the values list.  The outputs list will simply
contains string type elements that represent the name
of the measured outputs.  Each element in the values 
list will be one of three data types: 
floating point number, dictionary, or list. 

Floating point values are used for equalities while dictionaries are used
for inequalities entered.  Specifically, if the element is 
a dictionary, it will have two keys: 'equality' and 'value'.
The 'equality' key will determine whether the inequality is '<'
or '>' while the 'value' key will store the numerical value.
Finally, lists are used for variables that correspond to a list
of numerical values in a specific column of a table created by
the ``TABLE_VALUES`` and ``TABLE_END`` commands.

Example:

Input:

.. code-block:: yaml

    CREATE_NEW_EQUILIBRIUM @@,1
    EXPERIMENT X(LIQUID,Ti)=@1:0.01
    EXPERIMENT LPFCC=4.02:5% DGMR(DEL)<0:0.001
    TABLE_VALUES
    0.01
    0.02
    0.03
    TABLE_END
    
Output:

.. code-block:: python

    [
        {
            'outputs' : [
                'X(LIQUID,Ti)', 
                'LPFCC', 
                'DGMR(DEL)'
            ]
            'values' : [
                [0.01, 0.02, 0.03], 
                4.02, 
                {
                    'equality' : '<', 
                    'value' : 0.0
                }
            ]
        }
    ]

Full Example
============

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
   
For another example, see the :doc:`MgNi POP File Example <mgni>`.


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
