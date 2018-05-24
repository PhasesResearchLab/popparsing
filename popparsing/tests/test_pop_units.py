"""
Integration tests for bits of POP files
"""

import pytest

from ..conversion import convert_pop_data
from .testing_data import *
from .testing_results import *

def match_lists(lst1, lst2):
    assert sorted(lst1)==sorted(lst2)
    return True
    
def match_eq(dict1, dict2):
    assert match_lists(dict1['components'], dict2['components'])
    keys = ['phases', 'conditions', 
            'outputs', 'values', 'reference']
    for k in keys:
        assert dict1[k]==dict2[k]
    return True
    
def match_sets(lst1, lst2):
    assert len(lst1)==len(lst2)
    for i in range(len(lst1)):
        assert match_eq(lst1[i], lst2[i])
    return True

def test_activity_data_are_parsed():
    """Test that activity data can be parsed"""
    results = convert_pop_data(POP_ACTIVITY)
    assert match_sets(results, POP_ACTIVITY_RESULTS)


def test_driving_force_data_are_parsed():
    """Test that driving force data can be parsed"""
    #Does HCP go in the phases dictionary as well?
    result = convert_pop_data(POP_DRIVING_FORCE)
    assert match_sets(result, POP_DRIVING_FORCE_RESULTS)
    

def test_entropy_data_are_parsed():
    """Test that entropy data can be parsed"""
    #Do we want to omit empty dictionaries
    result = convert_pop_data(POP_ENTROPY)
    assert match_sets(result, POP_ENTROPY_RESULTS)


def test_eutectoid_data_are_parsed():
    """Test that three phase equilibria data can be parsed"""
    #Do alternate conditions also have to be in here?
    result = convert_pop_data(POP_EUTECTOID)
    assert match_sets(result, POP_EUTECTOID_RESULTS)


def test_gibbs_energy_data_are_parsed():
    """Test that Gibbs energy data can be parsed"""
    result = convert_pop_data(POP_GIBBS_ENERGY)
    assert match_sets(result, POP_GIBBS_ENERGY_RESULTS)


def test_heat_capacity_data_are_parsed():
    """Test that heat capacity data can be parsed"""
    result = convert_pop_data(POP_HEAT_CAPACITY)
    assert match_sets(result, POP_HEAT_CAPACITY_RESULTS)


def test_lattice_parameter_data_are_parsed():
    """Test that lattice parameter data can be parsed"""
    result = convert_pop_data(POP_LATTICE_PARAMETER)
    assert match_sets(result, POP_LATTICE_PARAMETER_RESULTS)
    result = convert_pop_data(POP_LATTICE_PARAMETER_ABBREVIATED_EXPERIMENT)
    assert match_sets(result, POP_LATTICE_PARAMETER_RESULTS)
    

def test_tables_are_parsed():
    """Test that data in tables can be parsed"""
    result = convert_pop_data(POP_TABLE_X_HMR)
    assert match_sets(result, POP_TABLE_X_HMR_RESULTS)


def test_tables_with_exp_first_are_parsed():
    """Test that tables with experimental data in the first column can be parsed"""
    result = convert_pop_data(POP_TABLE_EXPERIMENT_FIRST_COLUMN)
    match_sets(result, POP_TABLE_EXPERIMENT_FIRST_COLUMN_RESULTS)

def test_mg_ni_can_be_parsed():
    """Test that the (modified working) Mg-Ni file can be parsed"""
    result = convert_pop_data(WORKING_MG_NI_POP)
    assert match_sets(result, WORKING_MG_NI_POP_RESULTS)


def test_reference_states_are_parsed():
    """Test that reference state data can be parsed"""
    eq = convert_pop_data(POP_ACTIVITY)[0]
    #Did we want reference states in the conditions dicitonary?
    assert eq['conditions']['reference_states']['C'] == 'GRAPHITE'



def test_phase_status_can_be_fixed():
    """Test that the status of a phase can be fixed with a certain value"""
    eq = convert_pop_data(POP_ENTROPY)[0]
    assert eq['phases']['CUO']['status'] == 'FIXED'
    assert eq['phases']['CU2O']['status'] == 'FIXED'

    assert eq['phases']['CUO']['value'] == 0.0
    assert eq['phases']['CU2O']['value'] == 1.0



def test_phase_status_can_be_entered():
    """Test that the status of a phase can be entered with a certain value"""
    eq = convert_pop_data(POP_GIBBS_ENERGY)[0]
    assert eq['phases']['SPINEL']['status'] == 'ENTERED'
    assert eq['phases']['FCC']['status'] == 'DORMANT'
    assert eq['phases']['O2GAS']['status'] == 'DORMANT'
    assert eq['phases']['SPINEL']['value'] == 1.0

# TODO: write similar tests for DORMANT and SUSPENDED
# TODO: write tests that ensure that abbreviated status are properly parsed
# e.g. CH-S P CU2O=F 1 should give same result as
# CHANGE-STATUS PHASE CU2O=FIXED 1
# should be true for all statuses

def test_data_from_parrot_can_be_parsed():
    """Test that data output from PARROT can be parsed"""
    result = convert_pop_data(POP_FROM_PARROT)
    #assert match_sets(result, POP_FROM_PARROT_RESULTS)


@pytest.mark.xfail
def test_complex_conditions_can_be_parsed():
    """Conditions where constitutions are subtracted can be parsed"""
    result = convert_pop_data(POP_COMPLEX_CONDITIONS)


@pytest.mark.xfail
def test_expressions_as_conditions_can_be_parsed():
    """Conditions where constitutions are subtracted can be parsed"""
    result = convert_pop_data(POP_CONDITION_EXPRESSIONS)
