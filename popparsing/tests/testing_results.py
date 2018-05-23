POP_ACTIVITY_RESULTS=[{
    'phases' : {
        'FCC_A1' : {
            'status' : 'FIXED',
            'value' : 1.0
        },
        'GRAPHITE' : {
            'status' : 'DORMANT'
        }
    },
    'components' : ['C', 'MN'],
    'conditions' : {
        'P' : 101325,
        'T' : 1273,
        'X(MN)' : 0.03,
        'X(C)' : 0.03,
        'reference_states' : {
            'C' : 'GRAPHITE'
        }
    },
    'outputs' : ['ACR(C)'],
    'values' : [0.29],
    'reference' : 'ACTI'
}]

POP_DRIVING_FORCE_RESULTS=[{
    'phases' : {
        'ORT' : {
            'status' : 'FIXED',
            'value' : 1.0
        },
        'DEL' : {
            'status' : 'DORMANT'
        },
        #Does HCP go in here as well?
        #'HCP' : {
        #   'status' : 'SUSPENDED'
        #}
    },
    'components' : ['Ti', 'U'],
    'conditions' : {
        'P' : 102325,
        'T' : 673,
        'X(Ti)' : 0.03,
        'reference_states' : {
            #Does HCP go in the phases dictionary as well?
            'Ti' : 'HCP',
            'U' : 'ORT'
        }
    },
    'outputs' : ['DGMR(ORT)', 'DGMR(DEL)'],
    'values' : [{'equality' : '>', 'value' : 0.0},
                {'equality' : '<', 'value' : 0.0}],
    'reference' : 'ADRIV'
}]

POP_ENTROPY_RESULTS=[{
    'phases' : {
        'CU2O' : {
            'status' : 'FIXED',
            'value' : 1.0
        },
        'CUO' : {
            'status' : 'FIXED',
            'value' : 0.0
        }
    },
    'components' : ['C'],
    'conditions' : {
        'P' : 101325,
        'T' : 298.15,
        #Do we want to omit empty dictionaries
        'reference_states' : {}
    },
    'outputs' : ['S', 'ACR(C)'],
    'values' : [92.36, 0.29],
    'reference' : 'AENT'

}]

POP_EUTECTOID_RESULTS=[{
    'phases' : {
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
    },
    'components' : ['Ti'],
    'conditions' : {
        'P' : 102325,
        #Do alternate conditions also have to be in here?
        #'X(HCP, Ti)' : 0.99
        #'X(DEL, Ti)' : 0.33
        #Do we want to omit empty dictionaries
        'reference_states' : {}
    },
    'outputs' : ['T', 'X(BCC,Ti)', 'X(HCP,Ti)', 'X(DEL,Ti)'],
    'values' : [928, 0.85, 0.99, 0.33],
    'reference' : 'AEUO'
}]

POP_GIBBS_ENERGY_RESULTS=[{
    'phases' : {
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
    },
    'components' : ['O', 'NI', 'AL'],
    'conditions' : {
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
    },
    'outputs' : ['GM'],
    'values' : [-298911],
    'reference' : 'AGEN'
}]

POP_HEAT_CAPACITY_RESULTS=[{
    'phases' : {
        'SPINEL' : {
            'status' : 'ENTERED',
            'value' : 1.0
        }
    },
    'components' : ['FE', 'MG', 'O'],
    'conditions' : {
        'P' : 101325,
        'N(FE)' : 2,
        'N(MG)' : 1,
        'N(O)' : 4,
        'T' : 800,
        'reference_states' : {}
    },
    'outputs' : ['CP'],
    'values' : [207],
    'reference' : 'ACP'
}]

POP_LATTICE_PARAMETER_RESULTS=[{
    'phases' : {
        'FCC_A1' : {
            'status' : 'ENTERED',
            'value' : 1.0
        }
    },
    'components' : ['CR'],
    'conditions' : {
        'P' : 101325,
        'N' : 1,
        'T' : 298.15,
        'X(CR)' : 0.05,
        'reference_states' : {}
    },
    'outputs' : ['LPFCC'],
    'values' : [4.02],
    'reference' : 'ALAT'
}]

'''
POP_TABLE_X_HMR_RESULTS=[{
    'phases' : {
    },
    'components' : [],
    'conditions' : {
    },
    'outputs' : [],
    'values' : [],
    'reference' : 
}]

POP_TABLE_EXPERIMENT_FIRST_COLUMN_RESULTS=[{
    'phases' : {
    },
    'components' : [],
    'conditions' : {
    },
    'outputs' : [],
    'values' : [],
    'reference' : 
}]

WORKING_MG_NI_POP_RESULTS=[]

POP_FROM_PARROT_RESULTS=[]

POP_COMPLEX_CONDITIONS_RESULTS=[]

POP_CONDITION_EXPRESSIONS_RESULTS=[{
    'phases' : {
    },
    'components' : [],
    'conditions' : {
    },
    'outputs' : [],
    'values' : [],
    'reference' : 
}]
'''