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


POP_TABLE_X_HMR_RESULTS=[{
    'phases' : {
        'BCC_A2' : {
            'status' : 'FIXED',
            'value' : 1.0
        }
    },
    'components' : ['U', 'Ti'],
    'conditions' : {
        'P' : 102325,
        'T' : 200,
        'X(Ti)' : [ 0.1, 0.2, 0.3,
                    0.4, 0.5, 0.6],
        'reference_states' : {
            'U' : 'BCC_A2',
            'Ti' : 'BCC_A2'
        }
    },
    'outputs' : ['HMR(BCC_A2)'],
    'values' : [ [2450, 3000, 2990, 2430, 1400, -65] ],
    'reference' : 'AHMR1'
}]

POP_TABLE_EXPERIMENT_FIRST_COLUMN_RESULTS=[{
    'phases' : {
        'LIQUID' : {
            'status' : 'FIXED',
            'value' : 1.0
        },
        'BCC' : {
            'status' : 'FIXED',
            'value' : 0.0
        }
    },
    'components' : ['Ti'],
    'conditions' : {
        'P' : 102325,
        'T' : [ 1406, 1420, 1445, 1446, 1495, 1563,
                1643, 1957, 2093, 2117, 2198],
        'reference_states' : {}
    },
    'outputs' : ['X(LIQUID,Ti)'],
    'values' : [[0.0, 0.0045, 0.01, 0.02, 0.03, 0.04,
                 0.05, 0.1, 0.15, 0.2, 0.3 ]],
    'reference' : 'AREV'
}]

WORKING_MG_NI_POP_RESULTS=[
    {
        'phases' : {
            'LIQ' : {
                'status' : 'FIXED',
                'value' : 1.0
            }
        },
        'components' : ['NI', 'MG'],
        'conditions' : {
            'T' : 1073,
            'P' : 100000,
            'X(NI)' : [
                0.20230, 0.22600, 0.25400,
                0.28390, 0.18470, 0.20840,
                0.23580, 0.25950, 0.28900,
                0.21590, 0.24690, 0.28040,
                0.19450, 0.22560, 0.25880,
                0.28950, 0.32410, 0.15000,
                0.17210, 0.19280, 0.21300,
                0.23170, 0.25270, 0.27040,
                0.29050, 0.31020, 0.34380
            ],
            'reference_states' : {
                'MG' : 'LIQ'
            }
        },
        'outputs' : ['ACR(MG)'],
        'values' : [[
            0.771, 0.722, 0.672,
            0.623, 0.746, 0.710,
            0.667, 0.626, 0.570,
            0.709, 0.656, 0.600,
            0.740, 0.681, 0.635,
            0.577, 0.519, 0.822,
            0.787, 0.748, 0.708,
            0.678, 0.640, 0.607,
            0.577, 0.550, 0.506
        ]],
        'reference' : 'ALA1'
    },
    {
        'phases' : {
            'LIQ' : {
                'status' : 'FIXED',
                'value' : 1.0
            }
        },
        'components' : ['MG', 'NI'],
        'conditions' : {
            'T' : 1005,
            'P' : 100000,
            'X(NI)' : [
                0.04800, 0.10200, 0.15300,
                0.05300, 0.09900, 0.14600,
                0.19400, 0.02700, 0.05600,
                0.08500, 0.05100, 0.10500,
                0.15700
            ],
            'reference_states' : {
                'MG' : 'LIQ',
                'NI' : 'LIQ'
            }
        },
        'outputs' : ['HMRT'],
        'values' : [[
            -2.880, -5.780, -8.010,
            -3.080, -5.490, -7.330,
            -9.170, -1.620, -3.200,
            -4.620, -3.220, -5.820,
            -7.940
        ]],
        'reference' : 'ALA2'
    },
    {
        'phases' : {
            'LIQ' : {
                'status' : 'FIXED',
                'value' : 1.0
            }
        },
        'components' : ['MG', 'NI'],
        'conditions' : {
            'T' : 1005,
            'P' : 100000,
            'X(NI)' : [
                0.02400, 0.07500, 0.12800,
                0.02700, 0.07600, 0.12200,
                0.17000, 0.01300, 0.04100,
                0.07000, 0.02500, 0.07800,
                0.13100
            ],
            'reference_states' : {
                'MG' : 'LIQ',
                'NI' : 'LIQ'
            }
        },
        'outputs' : ['PH1'],
        'values' : [[
            -60.360, -53.410, -44.960,
            -57.860, -52.630, -41.420,
            -39.540, -61.030, -54.390,
            -48.550, -63.440, -48.580,
            -42.170
        ]],
        'reference' : 'ALA3'
    },
    {
        'phases' : {
            'LIQ' : {
                'status' : 'FIXED',
                'value' : 1.0
            },
            'HCP_A3' : {
                'status' : 'FIXED',
                'value' : 1.0
            }
        },
        'components' : ['NI'],
        'conditions' : {
            'T' : [ 900.7, 869.4, 836.8, 812.1, 781.0 ],
            'P' : 100000,
            'reference_states' : {
            }
        },
        'outputs' : ['X(LIQ,NI)', 'X(HCP_A3,NI)'],
        'values' : [[ 0.0235, 0.052, 0.0741, 0.0938, 0.1129 ], 
                    { 'equality' : '<', 'value' : 0.01 }],
        'reference' : 'ALHC'
    },
    {
        'phases' : {
            'LIQ' : {
                'status' : 'FIXED',
                'value' : 1.0
            },
            'FCC' : {
                'status' : 'FIXED',
                'value' : 1.0
            }
        },
        'components' : ['NI'],
        'conditions' : {
            'T' : [ 1428, 1545, 1708 ],
            'P' : 100000,
            'reference_states' : {
            }
        },
        'outputs' : ['X(LIQ,NI)', 'X(FCC,NI)'],
        'values' : [[ 0.8265, 0.8872, 0.9762 ], 
                    { 'equality' : '>', 'value' : 0.98 }],
        'reference' : 'ALFC'
    },
    {
        'phases' : {
            'LIQ' : {
                'status' : 'FIXED',
                'value' : 1.0
            },
            'MGNI2' : {
                'status' : 'FIXED',
                'value' : 1.0
            },
            'FCC' : {
                'status' : 'FIXED',
                'value' : 1.0
            }
        },
        'components' : ['NI'],
        'conditions' : {
            'P' : 100000,
            'reference_states' : {
            }
        },
        'outputs' : [ 'T', 'X(LIQ,NI)' ],
        'values' : [ 1370, 0.803 ],
        'reference' : 'AIEU'
    },
    {
        'phases' : {
            'LIQ' : {
                'status' : 'FIXED',
                'value' : 1.0
            },
            'MGNI2' : {
                'status' : 'FIXED',
                'value' : 1.0
            }
        },
        'components' : ['NI'],
        'conditions' : {
            'X(LIQ,NI)' : [ 0.3004, 0.3298, 0.3388, 0.3832,
                            0.4347, 0.4914, 0.5540, 0.6236,
                            0.6536, 0.7012, 0.7349 ],
            'P' : 100000,
            'reference_states' : {
            }
        },
        'outputs' : ['T'],
        'values' : [[ 1054.4, 1140.4, 1163.9, 1345, 1385, 
                      1412, 1418, 1417, 1418, 1413, 1370 ]],
        'reference' : 'ALM2'
    },
    {
        'phases' : {
            'LIQ' : {
                'status' : 'FIXED',
                'value' : 1.0
            },
            'MGNI2' : {
                'status' : 'FIXED',
                'value' : 1.0
            },
            'MG2NI' : {
                'status' : 'FIXED',
                'value' : 1.0
            }
        },
        'components' : ['NI'],
        'conditions' : {
            'P' : 100000,
            'reference_states' : {
            }
        },
        'outputs' : [ 'T', 'X(LIQ,NI)' ],
        'values' : [ 1033, 0.29 ],
        'reference' : 'APER'
    },
    {
        'phases' : {
            'LIQ' : {
                'status' : 'FIXED',
                'value' : 1.0
            },
            'HCP_A3' : {
                'status' : 'FIXED',
                'value' : 1.0
            },
            'MG2NI' : {
                'status' : 'FIXED',
                'value' : 1.0
            }
        },
        'components' : ['NI'],
        'conditions' : {
            'P' : 100000,
            'reference_states' : {
            }
        },
        'outputs' : [ 'T', 'X(LIQ,NI)' ],
        'values' : [ 779, 0.113 ],
        'reference' : 'AEMG'
    },
    {
        'phases' : {
            'LIQ' : {
                'status' : 'FIXED',
                'value' : 1.0
            },
            'MG2NI' : {
                'status' : 'FIXED',
                'value' : 1.0
            }
        },
        'components' : ['NI'],
        'conditions' : {
            'X(LIQ,NI)' : [ 0.1236, 0.1393, 0.1563,
                            0.1836, 0.2192, 0.2395,
                            0.2662 ],
            'P' : 100000,
            'reference_states' : {
            }
        },
        'outputs' : ['T'],
        'values' : [[ 834.2, 879.9, 917.6, 960.6,
                      994.5, 1012.7, 1023.2 ]],
        'reference' : 'AM2N'
    },
    {
        'phases' : {
            'FCC' : {
                'status' : 'FIXED',
                'value' : 1.0
            },
            'MGNI2' : {
                'status' : 'FIXED',
                'value' : 1.0
            },
            'MG2NI' : {
                'status' : 'DORMANT'
            }
        },
        'components' : [],
        'conditions' : {
            'T' : list(range(1300, 100, -100)),
            'P' : 100000,
            'reference_states' : {
            }
        },
        'outputs' : ['DGM(MG2NI)'],
        'values' : [ { 'equality' : '<', 'value' : 0 } ],
        'reference' : 'AST1'
    },
    {
        'phases' : {
            'HCP_A3' : {
                'status' : 'FIXED',
                'value' : 1.0
            },
            'MG2NI' : {
                'status' : 'FIXED',
                'value' : 1.0
            },
            'MGNI2' : {
                'status' : 'DORMANT'
            }
        },
        'components' : [],
        'conditions' : {
            'T' : list(range(700, 100, -100)),
            'P' : 100000,
            'reference_states' : {
            }
        },
        'outputs' : ['DGM(MGNI2)'],
        'values' : [{ 'equality' : '<', 'value' : 0 }],
        'reference' : 'AST2'
    },
    {
        'phases' : {
            'LIQ' : {
                'status' : 'FIXED',
                'value' : 1.0
            }
        },
        'components' : ['NI'],
        'conditions' : {
            'T' : 2500,
            'P' : 100000,
            'X(NI)' : [ (x+1) / 10 for x in range(9) ],
            'reference_states' : {
            }
        },
        'outputs' : ['GLDD'],
        'values' : [ { 'equality' : '>', 'value' : 0 } ],
        'reference' : 'ALDD'
    }
]


POP_FROM_PARROT_RESULTS=[{
    'phases' : {
        'TETRAG_AD#1' : {
            'status' : 'DORMANT'
        },
        'DELTA' : {
            'status' : 'FIXED',
            'value' : 0.0
        },
        'HCP_A3' : {
            'status' : 'FIXED',
            'value' : 1.0
        }
    },
    #Note: Change status component not implemented yet
    'components' : ['NP', 'ZR', #VA
                    ],
    'conditions' : {
        'P' : 102325,
        'T' : 573,
        'reference_states' : {
            'NP' : 'ORTHO_AC',
            'ZR' : 'HCP_A3'
        }
    },
    'outputs' : ['X(HCP_A3,ZR)','DGMR(TETRAG_AD#1)'],
    'values' : [ 0.988, { 'equality' : '<', 'value' : 0 }]
}]

POP_CONDITION_EXPRESSIONS_RESULTS=[
    {
        'phases' : {
            'MGNI2' : {
                'status' : 'FIXED',
                'value' : 1.0
            }
        },
        'components' : ['MG'],
        'conditions' : {
            'P' : 101325,
            'T' : 298.15,
            '3*X(MG)' : 1
        },
        'outputs' : ['H'],
        'values' : [-59000],
        'reference' : 'AENF' 
    },
    {
        'phases' : {
            'MG2NI' : {
                'status' : 'FIXED',
                'value' : 1.0
            }
        },
        'components' : ['MG'],
        'conditions' : {
            'P' : 101325,
            'T' : 298.15,
            '3*X(MG)' : 2
        },
        'outputs' : ['H'],
        'values' : [-40000],
        'reference' : 'AENF'
    },
    {
        'phases' : {
            'MG2NI' : {
                'status' : 'FIXED',
                'value' : 1.0
            }
        },
        'components' : ['MG'],
        'conditions' : {
            'T' : list(range(335, 705, 10)),
            'P' : 101325,
            '3*X(MG)' : 2
        },
        'outputs' : ['CPM2N'],
        'values' : [[ 70.68, 71.25, 71.64, 71.94, 72.81,
                      72.99, 73.17, 73.68, 74.16, 74.46,
                      74.52, 75.15, 75.12, 75.27, 75.36,
                      75.93, 76.26, 76.23, 76.74, 76.86,
                      76.80, 76.83, 77.19, 77.43, 77.49,
                      77.79, 78.09, 78.21, 78.57, 78.63,
                      78.45, 79.08, 78.99, 79.20, 79.56,
                      79.62 ]],
        'reference' : 'AM2C'
    },
]

POP_COMPLEX_CONDITIONS_RESULTS=[{
    'phases' : {
        'LIQ' : {
            'status' : 'FIXED',
            'value' : 1.0
        },
        'MGNI2' : {
            'status' : 'FIXED',
            'value' : 1.0
        }
    },
    'components' : ['MG'],
    'conditions' : {
        'P' : 101325,
        'X(LIQ,MG)-X(MGNI2,MG)' : 0
    },
    'outputs' : ['T'],
    'values' : [1420],
    'reference' : 'ACM'
}]