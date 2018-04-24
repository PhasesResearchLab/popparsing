"""
Integration tests for bits of POP files
"""

import pytest

from ..conversion import convert_pop_data
from .testing_data import *

def match_lists(lst1, lst2):
    return sorted(lst1)==sorted(lst2)


def test_activity_data_are_parsed():
    """Test that activity data can be parsed"""
    results = convert_pop_data(POP_ACTIVITY)
    assert len(results)==1
    eq = results[0]
    assert eq['phases']=={
        'FCC_A1' : {
            'status' : 'FIXED',
            'value' : 1.0
        },
        'GRAPHITE': {
            'status' : 'DORMANT'
        }
        
    }
    components = ['C', 'MN']
    assert match_lists(eq['components'], components)==True
    assert eq['conditions'] == {
        'P' : 101325,
        'T' : 1273,
        'X(MN)' : 0.03,
        'X(C)' : 0.03,
        'reference_states' : {
            'C' : 'GRAPHITE'
        }
    }
    assert eq['outputs']==['ACR(C)']
    assert eq['values']==[0.29]
    assert eq['reference']=='ACTI'


def test_driving_force_data_are_parsed():
    """Test that driving force data can be parsed"""
    result = convert_pop_data(POP_DRIVING_FORCE)
    assert len(result)==1
    eq = result[0]
    assert eq['phases']=={
        'ORT' : {
            'status' : 'FIXED',
            'value' : 1.0
        },
        'DEL' : {
            'status' : 'DORMANT'
        },
        #Does HCP go in here as well?
        #'HCP' : {
        #    'status' : 'SUSPENDED'
        #}
    }
    components = ['Ti', 'U']
    assert match_lists(eq['components'], components)==True
    assert eq['conditions']=={
        'P' : 102325,
        'T' : 673,
        'X(Ti)' : 0.03,
        'reference_states' : {
            #Does HCP go in the phases dictionary as well?
            'Ti' : 'HCP',
            'U' : 'ORT'
        }
    }
    outputs = ['DGMR(ORT)', 'DGMR(DEL)']
    values = [{ 'equality' : '>', 'value' : 0.0},
              { 'equality' : '<', 'value' : 0.0}]
    assert eq['outputs']==outputs
    assert eq['values']==values
    assert eq['reference']=='ADRIV'
    

def test_entropy_data_are_parsed():
    """Test that entropy data can be parsed"""
    result = convert_pop_data(POP_ENTROPY)
    assert len(result)==1
    eq = result[0]
    assert eq['phases']=={
        'CU2O' : {
            'status' : 'FIXED',
            'value' : 1.0
        },
        'CUO' : {
            'status' : 'FIXED',
            'value' : 0.0
        }
    }
    assert eq['components']==['C']
    assert eq['conditions']=={
        'P' : 101325,
        'T' : 298.15,
        #Do we want to omit empty dictionaries
        'reference_states' : {}
    }
    assert eq['outputs']==['S', 'ACR(C)']
    assert eq['values']==[92.36, 0.29]
    assert eq['reference']=='AENT'


def test_eutectoid_data_are_parsed():
    """Test that three phase equilibria data can be parsed"""
    result = convert_pop_data(POP_EUTECTOID)
    assert len(result)==1
    eq = result[0]
    assert eq['phases']=={
        'BCC' : {
            'status' : 'FIXED',
            'value' : 1.0
        },
        'HCP' : {
            'status' : 'FIXED',
            'value' : 1.0
        },
        'DEL' : {
            'status' : 'FIXED',
            'value' : 1.0
        }
    }
    assert eq['components']==['Ti']
    #Do alternate conditions also have to be in here?
    assert eq['conditions']=={
        'P' : 102325,
        #'X(HCP, Ti)' : 0.99
        #'X(DEL, Ti)' : 0.33
        #Do we want to omit empty dictionaries
        'reference_states' : {}
    }
    assert eq['outputs']==['X(BCC,Ti)', 'X(HCP,Ti)', 'X(DEL,Ti)']
    assert eq['values']==[ 0.85, 0.99, 0.33]
    assert eq['reference']=='AEUO'


def test_gibbs_energy_data_are_parsed():
    """Test that Gibbs energy data can be parsed"""
    result = convert_pop_data(POP_GIBBS_ENERGY)
    assert len(result)==1
    eq = result[0]
    assert eq['phases']=={
        'SPINEL' : {
            'status' : 'ENTERED',
            'value' : 1.0
        },
        'FCC' : {
            'status' : 'DORMANT'
        },
        'O2GAS' : {
            'status' : 'DORMANT'
        }
    }
    components = ['O', 'NI', 'AL']
    assert match_lists(eq['components'], components)==True
    assert eq['conditions']=={
        'P' : 101325,
        'T' : 1000,
        'N(NI)' : 1,
        'N(AL)' : 2,
        'N(O)' : 4,
        'reference_states' : {
            'NI' : 'FCC',
            'AL' : 'FCC',
            'O' : 'O2GAS'
        }
    }
    assert eq['outputs']==['GM']
    assert eq['values']==[-298911]
    assert eq['reference']=='AGEN'


def test_heat_capacity_data_are_parsed():
    """Test that heat capacity data can be parsed"""
    result = convert_pop_data(POP_HEAT_CAPACITY)
    assert len(result)==1
    eq = result[0]
    assert eq['phases']=={
        'SPINEL' : {
            'status' : 'ENTERED',
            'value' : 1.0
        }
    }
    assert match_lists(eq['components'],['FE', 'MG', 'O'])==True
    assert eq['conditions']=={
        'P' : 101325,
        'N(FE)' : 2,
        'N(MG)' : 1,
        'N(O)' : 4,
        'T' : 800,
        'reference_states' : {}
    }
    assert eq['outputs']==['CP']
    assert eq['values']==[207]
    assert eq['reference']=='ACP'


def test_lattice_parameter_data_are_parsed():
    """Test that lattice parameter data can be parsed"""
    result = convert_pop_data(POP_LATTICE_PARAMETER)
    assert len(result)==1
    eq = result[0]
    assert eq['phases']=={
        'FCC_A1' : {
            'status' : 'ENTERED',
            'value' : 1.0
        }
    }
    assert eq['components']==['CR']
    assert eq['conditions']=={
        'P' : 101325,
        'N' : 1,
        'T' : 298.15,
        'reference_states' : {}
    }
    assert eq['outputs']==['LPFCC']
    assert eq['values']==[4.02]
    assert eq['reference']=='ALAT'
    
#@pytest.mark.xfail
def test_tables_are_parsed():
    """Test that data in tables can be parsed"""
    result = convert_pop_data(POP_TABLE_X_HMR)
    assert len(result)==1
    return
    eq = result[0]
    eq['phases']!=None
    eq['components']!=None
    eq['conditions']!=None
    eq['outputs']!=None
    eq['values']!=None
    eq['reference']!=None

#@pytest.mark.xfail
def test_tables_with_exp_first_are_parsed():
    """Test that tables with experimental data in the first column can be parsed"""
    result = convert_pop_data(POP_TABLE_EXPERIMENT_FIRST_COLUMN)
    assert len(result)==1
    return
    eq['phases']!=None
    eq['components']!=None
    eq['conditions']!=None
    eq['outputs']!=None
    eq['values']!=None
    eq['reference']!=None

#@pytest.mark.xfail
def test_mg_ni_can_be_parsed():
    """Test that the (modified working) Mg-Ni file can be parsed"""
    result = convert_pop_data(WORKING_MG_NI_POP)
    



def test_reference_states_are_parsed():
    """Test that reference state data can be parsed"""
    eq = convert_pop_data(POP_ACTIVITY)[0]
    #Did we want reference states in the conditions dicitonary?
    assert eq['conditions']['reference_states']['C'] == 'GRAPHITE'



def test_phase_status_can_be_fixed():
    """Test that the status of a phase can be fixed with a certain value"""
    eq = convert_pop_data(POP_ENTROPY)[0]
    assert eq['phases']['CUO']['hints']['status'] == 'ENTERED'
    assert eq['phases']['CU2O']['hints']['status'] == 'ENTERED'

    assert eq['phases']['CU2O']['hints']['value'] == 0.0
    assert eq['phases']['CU2O']['hints']['value'] == 1.0



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
