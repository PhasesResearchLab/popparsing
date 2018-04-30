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

The popparsing package supports POP files with the following commands:

+---------------------------+
|Command                    |
+===========================+
|``CREATE_NEW_EQUILIBRIUM`` |
+---------------------------+
|``CHANGE_STATUS PHASE``    |
+---------------------------+
|``SET_REFERENCE_STATE``    |
+---------------------------+
|``SET_CONDITION``          |
+---------------------------+
|``TABLE_VALUES``           |
+---------------------------+
|``TABLE_END``              |
+---------------------------+

Output
------

Main Equilibrium Dictionary
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The output of the popparsing command is a JSON file
containing a list of dictionaries (one per equilibrium data set)
with the following keys and values.

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
|          |(a single number or a list)|
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



.. code-block:: json

   {
   }

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api/modules


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
