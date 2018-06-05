MgNi POP File Example
=====================

Input: MgNi.POP
---------------

.. code-block:: yaml

    E-SYM CON P0=1E5 R0=8.314

    @@ THERMOCHEMICAL DATA IN LIQUID
    @@ 100-300

    TABLE 100
    C-N @@,1
    CH P LIQ=F 1
    S-R-S MG LIQ,,,,,
    S-C T=1073, P=P0, X(NI)=@1
    LABEL ALA1
    EXPERIMENT ACR(MG)=@2:5%
    TABLE_VALUE
     0.20230        0.771
     0.22600        0.722
     0.25400        0.672
     0.28390        0.623
     0.18470        0.746
     0.20840        0.710
     0.23580        0.667
     0.25950        0.626
     0.28900        0.570
     0.21590        0.709
     0.24690        0.656
     0.28040        0.600
     0.19450        0.740
     0.22560        0.681
     0.25880        0.635
     0.28950        0.577
     0.32410        0.519
     0.15000        0.822
     0.17210        0.787
     0.19280        0.748
     0.21300        0.708
     0.23170        0.678
     0.25270        0.640
     0.27040        0.607
     0.29050        0.577
     0.31020        0.550
     0.34380        0.506
    TABLE_END

    EN-SYM FUN HMRT=HMR/1000;
    TABLE 200
    C-N @@,1
    CH P LIQ=F 1
    S-R-S MG LIQ,,,,,
    S-R-S NI LIQ,,,,,
    S-C T=1005, P=P0, X(NI)=@1
    EXPERIMENT HMRT=@2:10%
    LABEL ALA2
    TABLE_VALUE
     0.04800       -2.880
     0.10200       -5.780
     0.15300       -8.010
     0.05300       -3.080
     0.09900       -5.490
     0.14600       -7.330
     0.19400       -9.170
     0.02700       -1.620
     0.05600       -3.200
     0.08500       -4.620
     0.05100       -3.220
     0.10500       -5.820
     0.15700       -7.940
    TABLE_END

    ent fun ph1=(hmr+hmr.x(ni)-x(ni)*hmr.x(ni))/1000;
    TABLE 300
    C-N @@,1
    CH P LIQ=F 1
    S-R-S MG LIQ,,,,,
    S-R-S NI LIQ,,,,,
    S-C T=1005, P=P0, X(NI)=@1
    EXPERIMENT PH1=@2:10%
    LABEL ALA3
    TABLE_VALUE
     0.02400      -60.360
     0.07500      -53.410
     0.12800      -44.960
     0.02700      -57.860
     0.07600      -52.630
     0.12200      -41.420
     0.17000      -39.540
     0.01300      -61.030
     0.04100      -54.390
     0.07000      -48.550
     0.02500      -63.440
     0.07800      -48.580
     0.13100      -42.170
    TABLE_END

    @@ WE NOW DEAL WITH 2 PHASE EQUILIBRIA
    @@ LIQ-FCC, LIQ-HCP_A3
    @@ REFERENCE
    @@ 1000-

    TABLE 1000
    C-N @@,1
    CH P LIQ HCP_A3=F 1
    S-C T=@1, P=P0
    EXPERIMENT X(LIQ,NI)=@2:5%
    EXPERIMENT X(HCP_A3,NI)<0.01:1E-2
    S-S-V X(HCP_A3,NI)=1E-3
    LABEL ALHC
    TABLE_VALUE
    900.7 .0235
    869.4 .052
    836.8 .0741
    812.1 .0938
    781.0 .1129
    TABLE_END


    TABLE 1100
    C-N @@,1
    CH P LIQ FCC=F 1
    S-C T=@1, P=P0
    EXPERIMENT X(LIQ,NI)=@2:5%
    EXPERIMENT X(FCC,NI)>0.98:1E-2
    S-S-V X(FCC,NI)=0.9999
    LABEL ALFC
    TABLE_VALUE
    1428 .8265
    1545 .8872
    1708 .9762
    TABLE_END



    @@NOW DEAL WITH THE EUTECTIC POINT ON THE NI RICH END
    C-N 2,1
    CH P LIQ,MGNI2,FCC=F 1
    S-C P=P0
    EXPERIMENT T=1370:2
    EXPERIMENT X(LIQ,NI)=0.803:5%
    LABEL AIEU




    @@THIS THEN DEALS WITH THE TWO PHASE EQUILIBRIA IN L+MGNI2
    TABLE 2000
    C-N @@,1
    CH P LIQ MGNI2=F 1
    S-C X(LIQ,NI)=@2, P=P0
    EXPERIMENT T=@1:5
    LABEL ALM2
    TABLE_VALUE
    1054.4 .3004
    1140.4 .3298
    1163.9 .3388
    1345 .3832
    1385 .4347
    1412 .4914
    1418 .554
    1417 .6236
    1418 .6536
    1413 .7012
    1370 .7349
    TABLE_END


    @@ THIS DEALS WITH THE PERITECTIC MG2NI REACTION
    C-N 10,1
    CH P LIQ,MGNI2,MG2NI=F 1
    S-C P=P0
    EXPERIMENT T=1033:2
    EXPERIMENT X(LIQ,NI)=0.29:5%
    LABEL APER


    @@THIS THEN TAKES CARE OF THE EUTECTIC ON THE MG RICH END
    C-N 11,1
    CH P LIQ,HCP_A3,MG2NI=F 1
    S-C P=P0
    EXPERIMENT T=779:2
    EXPERIMENT X(LIQ,NI)=0.113:5%
    LABEL AEMG

    @@THE FOLLOWING TABLE TAKES CARE OF THE LIQUID MG2NI TWO PHASE
    @@EQUILIBIA
    TABLE 3000
    C-N @@,1
    CH P LIQ MG2NI=F 1
    S-C X(LIQ,NI)=@2, P=P0
    EXPERIMENT T=@1:5
    LABEL AM2N
    TABLE_VALUE
    834.2 .1236
    879.9 .1393
    917.6 .1563
    960.6 .1836
    994.5 .2192
    1012.7 .2395
    1023.2 .2662
    TABLE_END


    @@ STABILITY EQUILIBRIA RESTRICTIONS
    TABLE 4000
    C-N @@,1
    CH P FCC MGNI2=F 1
    CH P MG2NI=D
    S-C T=@1, P=P0
    EXPERIMENT DGM(MG2NI)<0:1E-2
    LABEL AST1
    TABLE_VALUE
    1300
    1200
    1100
    1000
    900
    800
    700
    600
    500
    400
    300
    200
    TABLE_END

    TABLE 5000
    C-N @@,1
    CH P HCP_A3 MG2NI=F 1
    CH P MGNI2=D
    S-C T=@1, P=P0
    EXPERIMENT DGM(MGNI2)<0:1E-2
    LABEL AST2
    TABLE_VALUE
    700
    600
    500
    400
    300
    200
    TABLE_END

    E-SY FUNCTION GLDD=MU(NI).X(NI);
    TABLE 6000
    C-N @@,1
    CH P LIQ=F 1
    S-C T=2500, P=P0, X(NI)=@1
    EXPERIMENT GLDD>0:1E-2
    LABEL ALDD
    TABLE_VALUE
    0.1
    0.2
    0.3
    0.4
    0.5
    0.6
    0.7
    0.8
    0.9
    TABLE_END

    SAVE
    
Output
------

.. code-block:: python

    [
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