"""
Integration tests for bits of POP files
"""

import pytest

from ..conversion import convert_pop_data
from .testing_data import *


def test_activity_data_are_parsed():
    """Test that activity data can be parsed"""
    result = convert_pop_data(POP_ACTIVITY)


def test_driving_force_data_are_parsed():
    """Test that driving force data can be parsed"""
    result = convert_pop_data(POP_DRIVING_FORCE)


def test_entropy_data_are_parsed():
    """Test that entropy data can be parsed"""
    result = convert_pop_data(POP_ENTROPY)


def test_eutectoid_data_are_parsed():
    """Test that three phase equilibria data can be parsed"""
    result = convert_pop_data(POP_EUTECTOID)


def test_gibbs_energy_data_are_parsed():
    """Test that Gibbs energy data can be parsed"""
    result = convert_pop_data(POP_GIBBS_ENERGY)


def test_heat_capacity_data_are_parsed():
    """Test that heat capacity data can be parsed"""
    result = convert_pop_data(POP_HEAT_CAPACITY)


def test_lattice_parameter_data_are_parsed():
    """Test that lattice parameter data can be parsed"""
    result = convert_pop_data(POP_LATTICE_PARAMETER)


def test_tables_are_parsed():
    """Test that data in tables can be parsed"""
    result = convert_pop_data(POP_TABLE_X_HMR)


def test_tables_with_exp_first_are_parsed():
    """Test that tables with experimental data in the first column can be parsed"""
    result = convert_pop_data(POP_TABLE_EXPERIMENT_FIRST_COLUMN)


def test_mg_ni_can_be_parsed():
    """Test that the (modified working) Mg-Ni file can be parsed"""
    result = convert_pop_data(WORKING_MG_NI_POP)


@pytest.mark.xfail
def test_reference_states_are_parsed():
    """Test that reference state data can be parsed"""
    eq = convert_pop_data(POP_ACTIVITY)[0]
    assert eq['reference_states']['C'] == 'GRAPHITE'


@pytest.mark.xfail
def test_phase_status_can_be_fixed():
    """Test that the status of a phase can be fixed with a certain value"""
    eq = convert_pop_data(POP_ENTROPY)[0]
    assert eq['phases']['CUO']['hints']['status'] == 'ENTERED'
    assert eq['phases']['CU2O']['hints']['status'] == 'ENTERED'

    assert eq['phases']['CU2O']['hints']['value'] == 0.0
    assert eq['phases']['CU2O']['hints']['value'] == 1.0


@pytest.mark.xfail
def test_phase_status_can_be_entered():
    """Test that the status of a phase can be entered with a certain value"""
    eq = convert_pop_data(POP_GIBBS_ENERGY)[0]
    assert eq['phases']['SPINEL']['hints']['status'] == 'ENTERED'
    assert eq['phases']['FCC']['hints']['status'] == 'DORMANT'
    assert eq['phases']['O2GAS']['hints']['status'] == 'DORMANT'

    assert eq['phases']['SPINEL']['hints']['value'] == 1.0

# TODO: write similar tests for DORMANT and SUSPENDED
# TODO: write tests that ensure that abbreviated status are properly parsed
# e.g. CH-S P CU2O=F 1 should give same result as
# CHANGE-STATUS PHASE CU2O=FIXED 1
# should be true for all statuses

@pytest.mark.xfail
def test_data_from_parrot_can_be_parsed():
    """Test that data output from PARROT can be parsed"""
    result = convert_pop_data(POP_FROM_PARROT)


@pytest.mark.xfail
def test_complex_conditions_can_be_parsed():
    """Conditions where constitutions are subtracted can be parsed"""
    result = convert_pop_data(POP_COMPLEX_CONDITIONS)


@pytest.mark.xfail
def test_expressions_as_conditions_can_be_parsed():
    """Conditions where constitutions are subtracted can be parsed"""
    result = convert_pop_data(POP_CONDITION_EXPRESSIONS)
