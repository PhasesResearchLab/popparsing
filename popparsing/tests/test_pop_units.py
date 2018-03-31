"""
Integration tests for bits of POP files
"""

import pytest

from popparsing.pop_formatting import convert_pop_data
from popparsing.tests.testing_data import *


def test_activity_data_are_parsed():
    """Test that activity data can be parsed"""
    convert_pop_data(POP_ACTIVITY)


def test_driving_force_data_are_parsed():
    """Test that driving force data can be parsed"""
    convert_pop_data(POP_DRIVING_FORCE)


def test_entropy_data_are_parsed():
    """Test that entropy data can be parsed"""
    convert_pop_data(POP_ENTROPY)


def test_eutectoid_data_are_parsed():
    """Test that three phase equilibria data can be parsed"""
    convert_pop_data(POP_EUTECTOID)


def test_gibbs_energy_data_are_parsed():
    """Test that Gibbs energy data can be parsed"""
    convert_pop_data(POP_GIBBS_ENERGY)


def test_heat_capacity_data_are_parsed():
    """Test that heat capacity data can be parsed"""
    convert_pop_data(POP_HEAT_CAPACITY)


def test_lattice_parameter_data_are_parsed():
    """Test that lattice parameter data can be parsed"""
    convert_pop_data(POP_LATTICE_PARAMETER)


def test_tables_are_parsed():
    """Test that data in tables can be parsed"""
    convert_pop_data(POP_TABLE_X_HMR)


def test_tables_with_exp_first_are_parsed():
    """Test that tables with experimental data in the first column can be parsed"""
    convert_pop_data(POP_TABLE_EXPERIMENT_FIRST_COLUMN)


def test_mg_ni_can_be_parsed():
    """Test that the (modified working) Mg-Ni file can be parsed"""
    convert_pop_data(WORKING_MG_NI_POP)


@pytest.mark.xfail
def test_data_from_parrot_can_be_parsed():
    """Test that data output from PARROT can be parsed"""
    convert_pop_data(POP_FROM_PARROT)


@pytest.mark.xfail
def test_complex_conditions_can_be_parsed():
    """Conditions where constitutions are subtracted can be parsed"""
    convert_pop_data(POP_COMPLEX_CONDITIONS)


@pytest.mark.xfail
def test_expressions_as_conditions_can_be_parsed():
    """Conditions where constitutions are subtracted can be parsed"""
    convert_pop_data(POP_CONDITION_EXPRESSIONS)
