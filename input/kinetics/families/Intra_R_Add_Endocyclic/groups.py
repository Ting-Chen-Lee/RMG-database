#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Endocyclic/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Root"], products=["RnCyclic"], ownReverse=False)

reverse = "Ring_Open_Endo_Cycli_Radical"
reversible = True

recipe(actions=[
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*1', '1'],
])

boundaryAtoms = ["*1", "*2"]

entry(
    index = 0,
    label = "Root",
    group = 
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,CS,Cdd,N,O4dc,O4tc,S] u0 {2,[D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S]               u0 c0 {1,[D,T,B]}
3 *1 R!H                                    u1
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing",
    group = 
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,CS,Cdd,N,O4dc,O4tc,S] u0 r1 {2,[D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S]               u0 c0 {1,[D,T,B]}
3 *1 R!H                                    u1
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO",
    group = 
"""
1 *2 CO                       u0 r1 {2,[D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 R!H                      u1
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO",
    group = 
"""
1 *2 [Cdd,CS,Cd,Cb,Ct]        u0 r1 {2,[D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 R!H                      u1
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R",
    group = 
"""
1 *2 [Cdd,CS,Cd,Cb,Ct]        u0 r1 {2,[D,T,B]} {4,[S,D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 R!H                      u1
4    R!H                      ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R",
    group = 
"""
1 *2 [Cdd,CS,Cd,Cb,Ct]        u0 r1 {2,[D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 R!H                      u1
4    R!H                      ux {1,[S,D,T,B]}
5    R!H                      ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-5R!H-R_Int-6R!H-2CbCbfCdCddCtNOS",
    group = 
"""
1 *2 [Cdd,CS,Cd,Cb,Ct]        u0 r1 {2,[D,T,B]} {4,S} {5,[S,D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]} {6,[S,D,T,B]}
3 *1 R!H                      u1
4    R!H                      u0 {1,S}
5    C                        u0 r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    C                        u0 r1 {2,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R",
    group = 
"""
1 *2 [Cdd,CS,Cd,Cb,Ct]        u0 r1 {2,[D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 C                        u1 {6,[S,D,T,B]}
4    R!H                      ux {1,[S,D,T,B]}
5    R!H                      ux {1,[S,D,T,B]}
6    C                        u0 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H",
    group = 
"""
1 *2 [Cdd,CS,Cd,Cb,Ct]        u0 r1 {2,[D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 C                        u1 {6,S}
4    C                        u0 {1,[S,D,T,B]}
5    C                        u0 {1,[S,D,T,B]}
6    C                        u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R",
    group = 
"""
1 *2 [Cdd,CS,Cd,Cb,Ct]        u0 r1 {2,[D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 C                        u1 {6,S}
4    C                        u0 {1,[S,D,T,B]}
5    C                        u0 {1,[S,D,T,B]}
6    C                        u0 {3,S} {7,[S,D,T,B]}
7    C                        u0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R_Ext-5R!H-R_Int-8R!H-3R!H",
    group = 
"""
1 *2 [Cdd,CS,Cd,Cb,Ct]        u0 r1 {2,[D,T,B]} {4,S} {5,[S,D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 r1 {1,[D,T,B]}
3 *1 C                        u1 {6,S} {8,[S,D,T,B]}
4    C                        u0 {1,S}
5    C                        u0 r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
6    C                        u0 {3,S} {7,[S,D,T,B]}
7    C                        u0 {6,[S,D,T,B]}
8    C                        u0 r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_4R!H-inRing",
    group = 
"""
1 *2 [Cdd,CS,Cd,Cb,Ct]        u0 r1 {2,[D,T,B]} {4,[S,D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 C                        u1 {6,S}
4    C                        u0 r1 {1,[S,D,T,B]}
5    C                        u0 {1,S} {8,S}
6    C                        u0 {3,S} {7,S}
7    C                        u0 {6,S}
8    C                        u0 {5,S} {9,S}
9    C                        u0 {8,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_4R!H-inRing_1CSCbCdCddCt->Cd",
    group = 
"""
1 *2 Cd                       u0 r1 {2,[D,T,B]} {4,[S,D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 r1 {1,[D,T,B]}
3 *1 C                        u1 r0 {6,S}
4    C                        u0 r1 {1,[S,D,T,B]}
5    C                        u0 {1,S} {8,S}
6    C                        u0 {3,S} {7,S}
7    C                        u0 {6,S}
8    C                        u0 {5,S} {9,S}
9    C                        u0 {8,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_4R!H-inRing_N-1CSCbCdCddCt->Cd",
    group = 
"""
1 *2 Cb                       u0 r1 {2,[D,T,B]} {4,[S,D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 r1 {1,[D,T,B]}
3 *1 C                        u1 r0 {6,S}
4    C                        u0 r1 {1,[S,D,T,B]}
5    C                        u0 {1,S} {8,S}
6    C                        u0 {3,S} {7,S}
7    C                        u0 {6,S}
8    C                        u0 {5,S} {9,S}
9    C                        u0 {8,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-4R!H-inRing",
    group = 
"""
1 *2 Cb u0 r1 {2,B} {4,S} {5,B}
2 *3 Cb u0 c0 {1,B}
3 *1 C  u1 {6,S}
4    C  u0 r0 {1,S}
5    C  u0 {1,B} {8,B}
6    C  u0 {3,S} {7,[S,D,T,B]}
7    C  u0 {6,[S,D,T,B]}
8    C  u0 {5,B} {9,B}
9    C  u0 {8,B}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-4R!H-inRing_Ext-3R!H-R",
    group = 
"""
1  *2 Cb  u0 r1 {2,B} {4,S} {5,B}
2  *3 Cb  u0 c0 r1 {1,B}
3  *1 C   u1 r0 {6,S} {10,[S,D,T,B]}
4     C   u0 r0 {1,S}
5     C   u0 r1 {1,B} {8,B}
6     C   u0 r0 {3,S} {7,[S,D,T,B]}
7     C   u0 r0 {6,[S,D,T,B]}
8     C   u0 r1 {5,B} {9,B}
9     C   u0 r1 {8,B}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H",
    group = 
"""
1 *2 [Cdd,CS,Cd,Cb,Ct]        u0 r1 {2,[D,T,B]} {4,[S,D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 C                        u1 {6,S}
4    C                        u0 {1,[S,D,T,B]}
5    C                        u0 {1,S} {6,S}
6    C                        u0 {3,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_1CSCbCdCddCt->Cd",
    group = 
"""
1 *2 Cd                       u0 r1 {2,[D,T,B]} {4,[S,D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 C                        u1 {6,S}
4    C                        u0 r1 {1,[S,D,T,B]}
5    C                        u0 {1,S} {6,S}
6    C                        u0 {3,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-1CSCbCdCddCt->Cd",
    group = 
"""
1 *2 Cb                       u0 r1 {2,[D,T,B]} {4,[S,D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 C                        u1 {6,S}
4    C                        u0 r1 {1,[S,D,T,B]}
5    C                        u0 {1,S} {6,S}
6    C                        u0 {3,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H",
    group = 
"""
1 *2 Cb u0 r1 {2,B} {4,B} {5,S}
2 *3 Cb u0 c0 {1,B}
3 *1 C  u1 {6,S}
4    C  u0 {1,B}
5    C  u0 {1,S} {6,D}
6    C  u0 {3,S} {5,D}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1 *2 Cb  u0 r1 {2,B} {4,B} {5,S}
2 *3 Cb  u0 c0 r1 {1,B}
3 *1 C   u1 r0 {6,S} {7,[S,D,T,B]}
4    C   u0 r1 {1,B}
5    C   u0 r0 {1,S} {6,D}
6    C   u0 r0 {3,S} {5,D}
7    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_N-Sp-6R!H-3R!H",
    group = 
"""
1 *2 Cb  u0 r1 {2,B} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 *3 Cb  u0 c0 {1,B}
3 *1 C   u1 {6,D}
4    R!H ux {1,[S,D,T,B]}
5    R!H ux {1,[S,D,T,B]}
6    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_N-Sp-6R!H-3R!H_Ext-6R!H-R",
    group = 
"""
1 *2 Cb  u0 r1 {2,B} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 *3 Cb  u0 c0 r1 {1,B}
3 *1 C   u1 r0 {6,D}
4    R!H ux {1,[S,D,T,B]}
5    R!H ux {1,[S,D,T,B]}
6    C   u0 r0 {3,D} {7,S}
7    C   u0 r0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_1CSCbCdCddCt->Cd",
    group = 
"""
1 *2 Cd                       u0 r1 {2,[D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 r1 {1,[D,T,B]}
3 *1 R!H                      u1 r0
4    R!H                      ux {1,[S,D,T,B]}
5    R!H                      ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_N-1CSCbCdCddCt->Cd",
    group = 
"""
1 *2 Cb  u0 r1 {2,B} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 *3 Cb  u0 c0 {1,B}
3 *1 R!H u1
4    R!H ux {1,[S,D,T,B]}
5    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_N-1CSCbCdCddCt->Cd_3R!H->C",
    group = 
"""
1 *2 Cb  u0 r1 {2,B} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 *3 Cb  u0 c0 r1 {1,B}
3 *1 C   u1
4    R!H ux {1,[S,D,T,B]}
5    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_N-1CSCbCdCddCt->Cd_N-3R!H->C",
    group = 
"""
1 *2 Cb  u0 r1 {2,B} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 *3 Cb  u0 c0 r1 {1,B}
3 *1 O   u1
4    R!H ux {1,[S,D,T,B]}
5    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing",
    group = 
"""
1 *2 [Cdd,CS,Cd,Cb,Ct]        u0 r1 {2,[D,T,B]} {4,[S,D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 r1 {1,[D,T,B]}
3 *1 R!H                      u1
4    C                        u0 {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S} {6,S}
3 *1 C  u1
4    C  u0 {1,S}
5    C  u0 {2,S}
6    C  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-5R!H-R",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D} {5,S} {6,S}
3 *1 C   u1 r1
4    C   u0 r1 {1,S}
5    C   u0 r1 {2,S} {7,[S,D,T,B]}
6    C   u0 r1 {2,S}
7    R!H ux {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D} {5,S}
3 *1 C   u1 {6,[S,D,T,B]}
4    C   u0 {1,S}
5    R!H u0 {2,S}
6    C   u0 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D} {5,S}
3 *1 C   u1 {6,[S,D,T,B]}
4    C   u0 {1,S} {6,[S,D,T,B]}
5    R!H u0 {2,S}
6    C   u0 {3,[S,D,T,B]} {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D} {5,S}
3 *1 C   u1 {6,[S,D,T,B]}
4    C   u0 {1,S} {6,[S,D,T,B]}
5    R!H u0 {2,S} {7,[S,D,T,B]}
6    C   u0 {3,[S,D,T,B]} {4,[S,D,T,B]}
7    R!H u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Int-5R!H-3R!H",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 {5,S} {6,S}
4    C  u0 {1,S} {6,D}
5    C  u0 {2,S} {3,S} {7,[S,D,T,B]}
6    C  u0 {3,S} {4,D}
7    C  u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Int-5R!H-3R!H_Sp-7R!H-5R!H",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 {5,S} {6,S}
4    C  u0 {1,S} {6,D}
5    C  u0 {2,S} {3,S} {7,S}
6    C  u0 {3,S} {4,D}
7    C  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Int-5R!H-3R!H_Sp-7R!H-5R!H_Ext-5R!H-R",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D} {5,S}
3 *1 C   u1 r1 {5,S} {6,S}
4    C   u0 r1 {1,S} {6,D}
5    C   u0 r1 {2,S} {3,S} {7,S} {8,[S,D,T,B]}
6    C   u0 r1 {3,S} {4,D}
7    C   u0 {5,S}
8    R!H ux {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Int-5R!H-3R!H_Sp-7R!H-5R!H_Ext-7R!H-R",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D} {5,S}
3 *1 C   u1 r1 {5,S} {6,S}
4    C   u0 r1 {1,S} {6,D}
5    C   u0 r1 {2,S} {3,S} {7,S}
6    C   u0 r1 {3,S} {4,D}
7    C   u0 r0 {5,S} {8,[S,D,T,B]}
8    R!H ux {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Int-5R!H-3R!H_N-Sp-7R!H-5R!H",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 r1 {5,S} {6,S}
4    C  u0 r1 {1,S} {6,D}
5    C  u0 r1 {2,S} {3,S} {7,D}
6    C  u0 r1 {3,S} {4,D}
7    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Sp-7R!H=5R!H",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D} {5,S}
3 *1 C   u1 {6,[S,D,T,B]}
4    C   u0 {1,S} {6,[S,D,T,B]}
5    C   u0 {2,S} {7,D}
6    C   u0 {3,[S,D,T,B]} {4,[S,D,T,B]}
7    R!H u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Sp-7R!H=5R!H_6R!H-inRing",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 {6,S}
4    C  u0 {1,S} {6,[S,D,T,B]}
5    C  u0 {2,S} {7,D}
6    C  u0 r1 {3,S} {4,[S,D,T,B]}
7    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Sp-7R!H=5R!H_6R!H-inRing_3R!H-inRing",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 r1 {6,S}
4    C  u0 r1 {1,S} {6,[S,D,T,B]}
5    C  u0 r1 {2,S} {7,D}
6    C  u0 r1 {3,S} {4,[S,D,T,B]}
7    C  u0 r1 {5,D}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Sp-7R!H=5R!H_6R!H-inRing_N-3R!H-inRing",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 r0 {6,S}
4    C  u0 r1 {1,S} {6,[S,D,T,B]}
5    C  u0 r1 {2,S} {7,D}
6    C  u0 r1 {3,S} {4,[S,D,T,B]}
7    C  u0 r1 {5,D}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Sp-7R!H=5R!H_N-6R!H-inRing",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D} {5,S}
3 *1 C   u1 {6,[S,D,T,B]}
4    C   u0 {1,S} {6,S}
5    C   u0 {2,S} {7,D}
6    C   u0 r0 {3,[S,D,T,B]} {4,S}
7    R!H u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Sp-7R!H=5R!H_N-6R!H-inRing_Ext-4R!H-R",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D} {5,S}
3 *1 C   u1 r0 {6,[S,D,T,B]}
4    C   u0 r1 {1,S} {6,S} {8,[S,D,T,B]}
5    C   u0 r1 {2,S} {7,D}
6    C   u0 r0 {3,[S,D,T,B]} {4,S}
7    R!H u0 {5,D}
8    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_N-Sp-7R!H=5R!H",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D} {5,S}
3 *1 C   u1 {6,S}
4    C   u0 {1,S} {6,[S,D,T,B]}
5    R!H u0 {2,S} {7,S}
6    C   u0 {3,S} {4,[S,D,T,B]}
7    C   u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_N-Sp-7R!H=5R!H_3R!H-inRing",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D} {5,S}
3 *1 C   u1 r1 {6,S}
4    C   u0 {1,S} {6,D}
5    R!H u0 {2,S} {7,S}
6    C   u0 {3,S} {4,D}
7    C   u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_N-Sp-7R!H=5R!H_3R!H-inRing_Ext-5R!H-R",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D} {5,S}
3 *1 C   u1 r1 {6,S}
4    C   u0 r1 {1,S} {6,D}
5    R!H u0 r1 {2,S} {7,S} {8,[S,D,T,B]}
6    C   u0 r1 {3,S} {4,D}
7    C   u0 r1 {5,S}
8    R!H ux {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_N-Sp-7R!H=5R!H_3R!H-inRing_5R!H->C",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 r1 {6,S}
4    C  u0 {1,S} {6,D}
5    C  u0 {2,S} {7,S}
6    C  u0 {3,S} {4,D}
7    C  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_N-Sp-7R!H=5R!H_3R!H-inRing_5R!H->C_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D} {5,S}
3 *1 C   u1 r1 {6,S} {8,[S,D,T,B]}
4    C   u0 r1 {1,S} {6,D}
5    C   u0 r1 {2,S} {7,S}
6    C   u0 r1 {3,S} {4,D}
7    C   u0 r1 {5,S}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_N-Sp-7R!H=5R!H_3R!H-inRing_N-5R!H->C",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 r1 {6,S}
4    C  u0 r1 {1,S} {6,D}
5    O  u0 r1 {2,S} {7,S}
6    C  u0 r1 {3,S} {4,D}
7    C  u0 r1 {5,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_N-Sp-7R!H=5R!H_N-3R!H-inRing",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D} {5,S}
3 *1 C   u1 r0 {6,S}
4    C   u0 r1 {1,S} {6,[S,D,T,B]}
5    R!H u0 r1 {2,S} {7,S}
6    C   u0 {3,S} {4,[S,D,T,B]}
7    C   u0 r1 {5,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Sp-6R!H-4R!H",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 r1 {6,S}
4    C  u0 r1 {1,S} {6,S}
5    C  u0 r1 {2,S}
6    C  u0 r1 {3,S} {4,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_N-Sp-6R!H-4R!H",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 {6,S}
4    C  u0 {1,S} {6,[B,D]}
5    C  u0 {2,S}
6    C  u0 {3,S} {4,[B,D]}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_N-Sp-6R!H-4R!H_Ext-4R!H-R",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D} {5,S}
3 *1 C   u1 r1 {6,S}
4    C   u0 r1 {1,S} {6,[B,D]} {7,[S,D,T,B]}
5    C   u0 r1 {2,S}
6    C   u0 r1 {3,S} {4,[B,D]}
7    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Sp-6R!H=3R!H",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 {6,D}
4    C  u0 {1,S}
5    C  u0 {2,S}
6    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Sp-6R!H=3R!H_3R!H-inRing",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 r1 {6,D}
4    C  u0 {1,S}
5    C  u0 {2,S}
6    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Sp-6R!H=3R!H_3R!H-inRing_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D} {5,S}
3 *1 C   u1 r1 {6,D} {7,[S,D,T,B]}
4    C   u0 r1 {1,S}
5    C   u0 r1 {2,S}
6    C   u0 r1 {3,D}
7    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Sp-6R!H=3R!H_N-3R!H-inRing",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 r0 {6,D}
4    C  u0 {1,S}
5    C  u0 {2,S}
6    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Sp-6R!H=3R!H_N-3R!H-inRing_Int-5R!H-3R!H",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 r0 {5,[S,D,T,B]} {6,D}
4    C  u0 r1 {1,S}
5    C  u0 r1 {2,S} {3,[S,D,T,B]}
6    C  u0 r0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 {6,S}
4    C  u0 {1,S}
5    C  u0 {2,S}
6    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 {6,S}
4    C  u0 {1,S}
5    C  u0 {2,S} {7,S}
6    C  u0 {3,S}
7    C  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-6R!H",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 {6,S}
4    C  u0 r1 {1,S}
5    C  u0 r1 {2,S} {7,S}
6    C  u0 {3,S} {7,[S,D,T,B]}
7    C  u0 r1 {5,S} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 {6,S}
4    C  u0 {1,S} {7,D}
5    C  u0 {2,S} {7,S}
6    C  u0 {3,S}
7    C  u0 {4,D} {5,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-5R!H-3R!H",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 {5,S} {6,S}
4    C  u0 {1,S} {7,D}
5    C  u0 {2,S} {3,S} {7,S}
6    C  u0 {3,S}
7    C  u0 {4,D} {5,S}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-5R!H-3R!H_Ext-6R!H-R",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 {5,S} {6,S}
4    C  u0 {1,S} {7,D}
5    C  u0 {2,S} {3,S} {7,S}
6    C  u0 {3,S} {8,D}
7    C  u0 {4,D} {5,S}
8    C  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-5R!H-3R!H_Ext-6R!H-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D} {5,S}
3 *1 C   u1 {5,S} {6,S} {9,[S,D,T,B]}
4    C   u0 r1 {1,S} {7,D}
5    C   u0 r1 {2,S} {3,S} {7,S}
6    C   u0 {3,S} {8,D}
7    C   u0 r1 {4,D} {5,S}
8    C   u0 {6,D}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-5R!H-3R!H_Ext-6R!H-R_3R!H-inRing",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 r1 {5,S} {6,S}
4    C  u0 r1 {1,S} {7,D}
5    C  u0 r1 {2,S} {3,S} {7,S}
6    C  u0 {3,S} {8,D}
7    C  u0 r1 {4,D} {5,S}
8    C  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-5R!H-3R!H_Ext-6R!H-R_N-3R!H-inRing",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 r0 {5,S} {6,S}
4    C  u0 r1 {1,S} {7,D}
5    C  u0 r1 {2,S} {3,S} {7,S}
6    C  u0 {3,S} {8,D}
7    C  u0 r1 {4,D} {5,S}
8    C  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-6R!H-5R!H",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 {6,S}
4    C  u0 {1,S} {7,D}
5    C  u0 {2,S} {6,S} {7,S}
6    C  u0 {3,S} {5,S}
7    C  u0 {4,D} {5,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-6R!H-5R!H_3R!H-inRing",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 r1 {6,S}
4    C  u0 {1,S} {7,D}
5    C  u0 {2,S} {6,S} {7,S}
6    C  u0 {3,S} {5,S}
7    C  u0 {4,D} {5,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-6R!H-5R!H_3R!H-inRing_Ext-6R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 r1 {6,S}
4    C  u0 r1 {1,S} {7,D}
5    C  u0 r1 {2,S} {6,S} {7,S}
6    C  u0 r1 {3,S} {5,S} {8,S}
7    C  u0 r1 {4,D} {5,S}
8    C  u0 r1 {6,S} {9,S}
9    C  u0 r1 {8,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-6R!H-5R!H_3R!H-inRing_Ext-6R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 r1 {6,S}
4    C  u0 r1 {1,S} {7,D}
5    C  u0 r1 {2,S} {6,S} {7,S}
6    C  u0 r1 {3,S} {5,S} {8,S}
7    C  u0 r1 {4,D} {5,S}
8    C  u0 r1 {6,S} {9,[B,D,T]}
9    C  u0 r1 {8,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-6R!H-5R!H_N-3R!H-inRing",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 r0 {6,S}
4    C  u0 r1 {1,S} {7,D}
5    C  u0 r1 {2,S} {6,S} {7,S}
6    C  u0 {3,S} {5,S}
7    C  u0 r1 {4,D} {5,S}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D} {5,S}
3 *1 C   u1 {6,S} {8,[S,D,T,B]}
4    C   u0 r1 {1,S}
5    C   u0 r1 {2,S} {7,S}
6    C   u0 {3,S}
7    C   u0 r1 {5,S}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_3R!H-inRing",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 r1 {6,S}
4    C  u0 r1 {1,S}
5    C  u0 r1 {2,S} {7,S}
6    C  u0 {3,S}
7    C  u0 r1 {5,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_N-3R!H-inRing",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 r0 {6,S}
4    C  u0 r1 {1,S}
5    C  u0 r1 {2,S} {7,S}
6    C  u0 {3,S}
7    C  u0 r1 {5,S}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_N-Sp-7R!H-5R!H",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 {6,S}
4    C  u0 {1,S}
5    C  u0 {2,S} {7,D}
6    C  u0 {3,S}
7    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_N-Sp-7R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D} {5,S}
3 *1 C  u1 {6,S} {8,S}
4    C  u0 {1,S}
5    C  u0 {2,S} {7,D}
6    C  u0 {3,S}
7    C  u0 {5,D}
8    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D} {5,S}
3 *1 C   u1 r1 {6,S} {8,S}
4    C   u0 r1 {1,S}
5    C   u0 r1 {2,S} {7,D}
6    C   u0 r1 {3,S}
7    C   u0 r1 {5,D} {9,[S,D,T,B]}
8    C   u0 r1 {3,S}
9    R!H ux {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_1CSCbCdCddCt->Cd",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D}
3 *1 R!H u1
4    C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_1CSCbCdCddCt->Cd_Ext-4R!H-R_Ext-5R!H-R_Int-6R!H-3R!H_Ext-6R!H-R",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D}
3 *1 R!H u1 {6,[S,D,T,B]}
4    C   u0 r1 {1,S} {5,[S,D,T,B]}
5    C   u0 r1 {4,[S,D,T,B]} {6,S}
6    C   u0 r1 {3,[S,D,T,B]} {5,S} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_1CSCbCdCddCt->Cd_Ext-4R!H-R_Sp-5R!H-4R!H",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D}
3 *1 C  u1 r0
4    C  u0 r1 {1,S} {5,S}
5    C  u0 r1 {4,S}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_1CSCbCdCddCt->Cd_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    group = 
"""
1 *2 Cd u0 r1 {2,D} {4,S}
2 *3 Cd u0 c0 r1 {1,D}
3 *1 C  u1
4    C  u0 {1,S} {5,[B,D,T]}
5    C  u0 {4,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_1CSCbCdCddCt->Cd_Ext-4R!H-R_N-Sp-5R!H-4R!H_Ext-4R!H-R",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {4,S}
2 *3 Cd  u0 c0 r1 {1,D}
3 *1 C   u1
4    C   u0 r1 {1,S} {5,[B,D,T]} {6,[S,D,T,B]}
5    C   u0 r1 {4,[B,D,T]}
6    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_N-1CSCbCdCddCt->Cd",
    group = 
"""
1 *2 Cb u0 r1 {2,B} {4,B}
2 *3 Cb u0 c0 r1 {1,B}
3 *1 C  u1
4    C  u0 {1,B}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_N-1CSCbCdCddCt->Cd_Ext-3R!H-R",
    group = 
"""
1 *2 Cb  u0 r1 {2,B} {4,B}
2 *3 Cb  u0 c0 r1 {1,B}
3 *1 C   u1 {5,[S,D,T,B]}
4    C   u0 r1 {1,B}
5    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_N-2CbCbfCdCddCtNOS-inRing",
    group = 
"""
1 *2 [Cdd,CS,Cd,Cb,Ct]        u0 r1 {2,[D,T,B]} {4,[S,D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 r0 {1,[D,T,B]}
3 *1 C                        u1
4    C                        u0 r1 {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Int-3R!H-1CSCbCdCddCt_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd  u0 r1 {2,D} {3,S}
2 *3 Cd  u0 c0 r1 {1,D}
3 *1 C   u1 r1 {1,S} {4,S}
4    C   u0 r1 {3,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]}
6    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing",
    group = 
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,CS,Cdd,N,O4dc,O4tc,S] u0 r0 {2,[D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S]               u0 c0 {1,[D,T,B]}
3 *1 R!H                                    u1
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R",
    group = 
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,CS,Cdd,N,O4dc,O4tc,S] u0 r0 {2,[D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S]               u0 c0 {1,[D,T,B]} {4,[S,D,T,B]}
3 *1 R!H                                    u1
4    R!H                                    ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {6,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {1,S} {3,S}
""",
    kinetics = None,
)

entry(
    index = 92,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {6,S} {7,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {1,S} {3,S}
7    C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 93,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {6,S} {7,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {1,S} {3,S}
7    C   u0 {1,S} {8,D}
8    C   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 94,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {6,S} {7,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S} {9,[S,D,T,B]}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {1,S} {3,S}
7    C   u0 {1,S} {8,D}
8    C   u0 {7,D}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {9,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {1,S} {3,S}
7     C   u0 {1,S} {8,D}
8     C   u0 {7,D}
9     C   u0 {3,S} {10,[S,D,T,B]}
10    C   u0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S}
4     C  u0 {2,S}
5     C  u0 {2,S}
6     C  u0 {1,S} {3,S}
7     C  u0 {1,S} {8,D}
8     C  u0 {7,D}
9     C  u0 {3,S} {10,D}
10    C  u0 {9,D}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S} {11,S}
4     C  u0 {2,S}
5     C  u0 {2,S}
6     C  u0 {1,S} {3,S}
7     C  u0 {1,S} {8,D}
8     C  u0 {7,D}
9     C  u0 {3,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 98,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S} {11,S}
4     C  u0 {2,S} {12,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {1,S} {3,S}
7     C  u0 {1,S} {8,D}
8     C  u0 {7,D}
9     C  u0 {3,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {3,S}
12    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 99,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S} {11,S}
4     C  u0 {2,S} {12,D}
5     C  u0 {2,S}
6     C  u0 r0 {1,S} {3,S}
7     C  u0 r0 {1,S} {8,D}
8     C  u0 {7,D}
9     C  u0 r0 {3,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {3,S}
12    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 100,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S} {11,S}
4     C  u0 {2,S} {12,[B,S,T]}
5     C  u0 {2,S}
6     C  u0 r0 {1,S} {3,S}
7     C  u0 r0 {1,S} {8,D}
8     C  u0 {7,D}
9     C  u0 r0 {3,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {3,S}
12    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 101,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S}
4     C  u0 {2,S} {11,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {1,S} {3,S}
7     C  u0 {1,S} {8,D}
8     C  u0 {7,D}
9     C  u0 {3,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 102,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {9,S}
4     C  u0 r0 {2,S} {11,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {1,S} {3,S}
7     C  u0 r0 {1,S} {8,D}
8     C  u0 r0 {7,D}
9     C  u0 r0 {3,S} {10,D}
10    C  u0 r0 {9,D}
11    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 103,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {9,S}
4     C  u0 r0 {2,S} {11,[B,S,T]}
5     C  u0 r0 {2,S}
6     C  u0 r0 {1,S} {3,S}
7     C  u0 r0 {1,S} {8,D}
8     C  u0 r0 {7,D}
9     C  u0 r0 {3,S} {10,D}
10    C  u0 r0 {9,D}
11    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {9,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {1,S} {3,S}
7     C   u0 {1,S} {8,D}
8     C   u0 {7,D}
9     C   u0 {3,S} {10,T}
10    C   u0 {9,T}
""",
    kinetics = None,
)

entry(
    index = 105,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S}
4     C  u0 {2,S} {11,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {1,S} {3,S}
7     C  u0 {1,S} {8,D}
8     C  u0 {7,D}
9     C  u0 {3,S} {10,T}
10    C  u0 {9,T}
11    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 106,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S} {12,S}
4     C  u0 {2,S} {11,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {1,S} {3,S}
7     C  u0 {1,S} {8,D}
8     C  u0 {7,D}
9     C  u0 {3,S} {10,T}
10    C  u0 {9,T}
11    C  u0 {4,[S,D,T,B]}
12    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 107,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_Ext-3R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S} {12,S}
4     C  u0 {2,S} {11,D}
5     C  u0 {2,S}
6     C  u0 r0 {1,S} {3,S}
7     C  u0 r0 {1,S} {8,D}
8     C  u0 {7,D}
9     C  u0 r0 {3,S} {10,T}
10    C  u0 {9,T}
11    C  u0 {4,D}
12    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 108,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_Ext-3R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S} {12,S}
4     C  u0 {2,S} {11,T}
5     C  u0 {2,S}
6     C  u0 r0 {1,S} {3,S}
7     C  u0 r0 {1,S} {8,D}
8     C  u0 {7,D}
9     C  u0 r0 {3,S} {10,T}
10    C  u0 {9,T}
11    C  u0 {4,T}
12    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 109,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S}
4     C  u0 {2,S} {11,D}
5     C  u0 {2,S}
6     C  u0 {1,S} {3,S}
7     C  u0 {1,S} {8,D}
8     C  u0 {7,D}
9     C  u0 {3,S} {10,T}
10    C  u0 {9,T}
11    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 110,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S}
4     C  u0 {2,S} {11,T}
5     C  u0 {2,S}
6     C  u0 {1,S} {3,S}
7     C  u0 {1,S} {8,D}
8     C  u0 {7,D}
9     C  u0 {3,S} {10,T}
10    C  u0 {9,T}
11    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 111,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {9,S} {11,[S,D,T,B]}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {1,S} {3,S}
7     C   u0 {1,S} {8,D}
8     C   u0 {7,D}
9     C   u0 {3,S} {10,T}
10    C   u0 {9,T}
11    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 {2,S}
5     C   u0 {2,S}
6     C   u0 {1,S} {3,S}
7     C   u0 {1,S} {8,D}
8     C   u0 {7,D}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 {2,S} {11,[S,D,T,B]}
5     C   u0 {2,S}
6     C   u0 {1,S} {3,S}
7     C   u0 {1,S} {8,D}
8     C   u0 {7,D}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 {2,S} {11,D}
5     C   u0 {2,S}
6     C   u0 {1,S} {3,S}
7     C   u0 {1,S} {8,D}
8     C   u0 {7,D}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    C   u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 115,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 {2,S} {11,[B,S,T]}
5     C   u0 {2,S}
6     C   u0 {1,S} {3,S}
7     C   u0 {1,S} {8,D}
8     C   u0 {7,D}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    C   u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {1,S} {3,S}
7     C  u0 {1,S} {8,D}
8     C  u0 {7,D}
9     C  u0 {3,S}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 117,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {9,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {1,S} {3,S}
7     C  u0 r0 {1,S} {8,D}
8     C  u0 r0 {7,D}
9     C  u0 r0 {3,S}
10    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 118,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {9,S}
4     C  u0 r0 {2,S} {10,[B,S,T]}
5     C  u0 r0 {2,S}
6     C  u0 r0 {1,S} {3,S}
7     C  u0 r0 {1,S} {8,D}
8     C  u0 r0 {7,D}
9     C  u0 r0 {3,S}
10    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 119,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S} {7,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S}
4    C  u0 {2,S} {9,[S,D,T,B]}
5    C  u0 {2,S}
6    C  u0 {1,S} {3,S}
7    C  u0 {1,S} {8,D}
8    C  u0 {7,D}
9    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S} {7,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3 *1 C  u1 r0 {6,S}
4    C  u0 r0 {2,S} {9,D}
5    C  u0 r0 {2,S}
6    C  u0 r0 {1,S} {3,S}
7    C  u0 r0 {1,S} {8,D}
8    C  u0 r0 {7,D}
9    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 121,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S} {7,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3 *1 C  u1 r0 {6,S}
4    C  u0 r0 {2,S} {9,[B,S,T]}
5    C  u0 r0 {2,S}
6    C  u0 r0 {1,S} {3,S}
7    C  u0 r0 {1,S} {8,D}
8    C  u0 r0 {7,D}
9    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {6,S} {7,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S} {8,[S,D,T,B]}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {1,S} {3,S}
7    C   u0 {1,S}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 123,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {6,S} {7,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S} {8,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {1,S} {3,S}
7    C   u0 {1,S}
8    C   u0 {3,S} {9,[S,D,T,B]}
9    C   u0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 124,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S} {7,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S} {8,S}
4    C  u0 {2,S}
5    C  u0 {2,S}
6    C  u0 {1,S} {3,S}
7    C  u0 {1,S}
8    C  u0 {3,S} {9,D}
9    C  u0 {8,D}
""",
    kinetics = None,
)

entry(
    index = 125,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {8,S} {10,S}
4     C  u0 {2,S}
5     C  u0 {2,S}
6     C  u0 {1,S} {3,S}
7     C  u0 {1,S}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 126,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {8,S} {10,S}
4     C  u0 {2,S} {11,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {1,S} {3,S}
7     C  u0 {1,S}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
11    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 127,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {8,S} {10,S}
4     C  u0 r0 {2,S} {11,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {1,S} {3,S}
7     C  u0 r0 {1,S}
8     C  u0 r0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
11    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 128,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {8,S} {10,S}
4     C  u0 r0 {2,S} {11,[B,S,T]}
5     C  u0 r0 {2,S}
6     C  u0 r0 {1,S} {3,S}
7     C  u0 r0 {1,S}
8     C  u0 r0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
11    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 129,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {8,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {1,S} {3,S}
7     C  u0 {1,S}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 130,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {8,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {1,S} {3,S}
7     C  u0 r0 {1,S}
8     C  u0 r0 {3,S} {9,D}
9     C  u0 r0 {8,D}
10    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 131,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {8,S}
4     C  u0 r0 {2,S} {10,[B,S,T]}
5     C  u0 r0 {2,S}
6     C  u0 r0 {1,S} {3,S}
7     C  u0 r0 {1,S}
8     C  u0 r0 {3,S} {9,D}
9     C  u0 r0 {8,D}
10    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 132,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {6,S} {7,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S} {8,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {1,S} {3,S}
7    C   u0 {1,S}
8    C   u0 {3,S} {9,T}
9    C   u0 {8,T}
""",
    kinetics = None,
)

entry(
    index = 133,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {8,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {1,S} {3,S}
7     C  u0 {1,S}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 134,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {8,S} {11,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {1,S} {3,S}
7     C  u0 {1,S}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {4,[S,D,T,B]}
11    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 135,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {8,S} {11,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {1,S} {3,S}
7     C  u0 r0 {1,S}
8     C  u0 r0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {4,D}
11    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 136,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {8,S} {11,S}
4     C  u0 r0 {2,S} {10,T}
5     C  u0 r0 {2,S}
6     C  u0 r0 {1,S} {3,S}
7     C  u0 r0 {1,S}
8     C  u0 r0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {4,T}
11    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {8,S}
4     C  u0 {2,S} {10,D}
5     C  u0 {2,S}
6     C  u0 {1,S} {3,S}
7     C  u0 {1,S}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 138,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {8,S}
4     C  u0 {2,S} {10,T}
5     C  u0 {2,S}
6     C  u0 {1,S} {3,S}
7     C  u0 {1,S}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 139,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {8,S} {10,[S,D,T,B]}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {1,S} {3,S}
7     C   u0 {1,S}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 140,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {6,S} {7,S}
2 *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3 *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4    C   u0 {2,S}
5    C   u0 {2,S}
6    C   u0 {1,S} {3,S}
7    C   u0 {1,S}
8    R!H ux {3,[S,D,T,B]}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 141,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {10,[S,D,T,B]}
5     C   u0 {2,S}
6     C   u0 {1,S} {3,S}
7     C   u0 {1,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {10,D}
5     C   u0 {2,S}
6     C   u0 {1,S} {3,S}
7     C   u0 {1,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 143,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {6,S} {7,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {10,[B,S,T]}
5     C   u0 {2,S}
6     C   u0 {1,S} {3,S}
7     C   u0 {1,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 144,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S} {7,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S} {8,S}
4    C  u0 {2,S} {9,[S,D,T,B]}
5    C  u0 {2,S}
6    C  u0 {1,S} {3,S}
7    C  u0 {1,S}
8    C  u0 {3,S}
9    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 145,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S} {7,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3 *1 C  u1 r0 {6,S} {8,S}
4    C  u0 r0 {2,S} {9,D}
5    C  u0 r0 {2,S}
6    C  u0 r0 {1,S} {3,S}
7    C  u0 r0 {1,S}
8    C  u0 r0 {3,S}
9    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 146,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S} {7,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3 *1 C  u1 r0 {6,S} {8,S}
4    C  u0 r0 {2,S} {9,[B,S,T]}
5    C  u0 r0 {2,S}
6    C  u0 r0 {1,S} {3,S}
7    C  u0 r0 {1,S}
8    C  u0 r0 {3,S}
9    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 147,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S} {7,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S}
4    C  u0 {2,S} {8,[S,D,T,B]}
5    C  u0 {2,S}
6    C  u0 {1,S} {3,S}
7    C  u0 {1,S}
8    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S} {7,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3 *1 C  u1 r0 {6,S}
4    C  u0 r0 {2,S} {8,D}
5    C  u0 r0 {2,S}
6    C  u0 r0 {1,S} {3,S}
7    C  u0 r0 {1,S}
8    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 149,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S} {7,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3 *1 C  u1 r0 {6,S}
4    C  u0 r0 {2,S} {8,[B,S,T]}
5    C  u0 r0 {2,S}
6    C  u0 r0 {1,S} {3,S}
7    C  u0 r0 {1,S}
8    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 150,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S}
4    C  u0 {2,S} {7,[S,D,T,B]}
5    C  u0 {2,S}
6    C  u0 {1,S} {3,S}
7    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 151,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {6,S}
2 *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3 *1 C   u1 {6,S} {8,[S,D,T,B]}
4    C   u0 {2,S} {7,[S,D,T,B]}
5    C   u0 {2,S}
6    C   u0 {1,S} {3,S}
7    C   u0 {4,[S,D,T,B]}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 152,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S} {8,S}
4    C  u0 {2,S} {7,[S,D,T,B]}
5    C  u0 {2,S}
6    C  u0 {1,S} {3,S}
7    C  u0 {4,[S,D,T,B]}
8    C  u0 {3,S} {9,[S,D,T,B]}
9    C  u0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 153,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S} {8,S}
4    C  u0 {2,S} {7,[S,D,T,B]}
5    C  u0 {2,S}
6    C  u0 {1,S} {3,S}
7    C  u0 {4,[S,D,T,B]}
8    C  u0 {3,S} {9,D}
9    C  u0 {8,D}
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {8,S} {10,S}
4     C  u0 {2,S} {7,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {1,S} {3,S}
7     C  u0 {4,[S,D,T,B]}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Sp-7R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {8,S} {10,S}
4     C  u0 r0 {2,S} {7,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {1,S} {3,S}
7     C  u0 r0 {4,D}
8     C  u0 {3,S} {9,D}
9     C  u0 r0 {8,D}
10    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 156,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_N-Sp-7R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {8,S} {10,S}
4     C  u0 r0 {2,S} {7,T}
5     C  u0 r0 {2,S}
6     C  u0 r0 {1,S} {3,S}
7     C  u0 r0 {4,T}
8     C  u0 {3,S} {9,D}
9     C  u0 r0 {8,D}
10    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Sp-7R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S} {8,S}
4    C  u0 {2,S} {7,D}
5    C  u0 {2,S}
6    C  u0 {1,S} {3,S}
7    C  u0 {4,D}
8    C  u0 {3,S} {9,D}
9    C  u0 {8,D}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_N-Sp-7R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S} {8,S}
4    C  u0 {2,S} {7,T}
5    C  u0 {2,S}
6    C  u0 {1,S} {3,S}
7    C  u0 {4,T}
8    C  u0 {3,S} {9,D}
9    C  u0 {8,D}
""",
    kinetics = None,
)

entry(
    index = 159,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S} {8,S}
4    C  u0 {2,S} {7,[S,D,T,B]}
5    C  u0 {2,S}
6    C  u0 {1,S} {3,S}
7    C  u0 {4,[S,D,T,B]}
8    C  u0 {3,S} {9,T}
9    C  u0 {8,T}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {8,S} {10,S}
4     C  u0 {2,S} {7,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {1,S} {3,S}
7     C  u0 {4,[S,D,T,B]}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Sp-7R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {8,S} {10,S}
4     C  u0 r0 {2,S} {7,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {1,S} {3,S}
7     C  u0 r0 {4,D}
8     C  u0 {3,S} {9,T}
9     C  u0 r0 {8,T}
10    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_N-Sp-7R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {6,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {8,S} {10,S}
4     C  u0 r0 {2,S} {7,T}
5     C  u0 r0 {2,S}
6     C  u0 r0 {1,S} {3,S}
7     C  u0 r0 {4,T}
8     C  u0 {3,S} {9,T}
9     C  u0 r0 {8,T}
10    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 163,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Sp-7R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S} {8,S}
4    C  u0 {2,S} {7,D}
5    C  u0 {2,S}
6    C  u0 {1,S} {3,S}
7    C  u0 {4,D}
8    C  u0 {3,S} {9,T}
9    C  u0 {8,T}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-Sp-7R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S} {8,S}
4    C  u0 {2,S} {7,T}
5    C  u0 {2,S}
6    C  u0 {1,S} {3,S}
7    C  u0 {4,T}
8    C  u0 {3,S} {9,T}
9    C  u0 {8,T}
""",
    kinetics = None,
)

entry(
    index = 165,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {6,S}
2 *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3 *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4    C   u0 {2,S} {7,[S,D,T,B]}
5    C   u0 {2,S}
6    C   u0 {1,S} {3,S}
7    C   u0 {4,[S,D,T,B]}
8    R!H ux {3,[S,D,T,B]}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=4R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {6,S}
2 *3 Cd  u0 c0 r0 {1,D} {4,S} {5,S}
3 *1 C   u1 r0 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4    C   u0 r0 {2,S} {7,D}
5    C   u0 r0 {2,S}
6    C   u0 r0 {1,S} {3,S}
7    C   u0 r0 {4,D}
8    R!H ux {3,[S,D,T,B]}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=4R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {6,S}
2 *3 Cd  u0 c0 r0 {1,D} {4,S} {5,S}
3 *1 C   u1 r0 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4    C   u0 r0 {2,S} {7,T}
5    C   u0 r0 {2,S}
6    C   u0 r0 {1,S} {3,S}
7    C   u0 r0 {4,T}
8    R!H ux {3,[S,D,T,B]}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 168,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Sp-7R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S} {8,S}
4    C  u0 {2,S} {7,D}
5    C  u0 {2,S}
6    C  u0 {1,S} {3,S}
7    C  u0 {4,D}
8    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 169,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_N-Sp-7R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S} {8,S}
4    C  u0 {2,S} {7,T}
5    C  u0 {2,S}
6    C  u0 {1,S} {3,S}
7    C  u0 {4,T}
8    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 170,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Sp-7R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S}
4    C  u0 {2,S} {7,D}
5    C  u0 {2,S}
6    C  u0 {1,S} {3,S}
7    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 171,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_N-Sp-7R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S}
4    C  u0 {2,S} {7,T}
5    C  u0 {2,S}
6    C  u0 {1,S} {3,S}
7    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 172,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {6,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S} {7,[S,D,T,B]}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {1,S} {3,S}
7    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 173,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-7R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {6,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S} {7,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {1,S} {3,S}
7    C   u0 {3,S} {8,[S,D,T,B]}
8    C   u0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 174,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {6,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S} {7,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {1,S} {3,S}
7    C   u0 {3,S} {8,D}
8    C   u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 175,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {6,S}
2 *3 Cd  u0 c0 r0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 r0 {6,S} {7,S} {9,[S,D,T,B]}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 r0 {1,S} {3,S}
7    C   u0 r0 {3,S} {8,D}
8    C   u0 {7,D}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 176,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {6,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S} {7,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {1,S} {3,S}
7    C   u0 {3,S} {8,T}
8    C   u0 {7,T}
""",
    kinetics = None,
)

entry(
    index = 177,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {6,S}
2 *3 Cd  u0 c0 r0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 r0 {6,S} {7,S} {9,[S,D,T,B]}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 r0 {1,S} {3,S}
7    C   u0 r0 {3,S} {8,T}
8    C   u0 {7,T}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 178,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {6,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {1,S} {3,S}
7    R!H ux {3,[S,D,T,B]}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 179,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,D}
7    C   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 180,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,D}
7    C   u0 {6,D} {8,S}
8    C   u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 181,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {9,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,D}
7    C   u0 {6,D} {8,S}
8    C   u0 {7,S}
9    C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 182,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {1,S} {10,D}
10    C   u0 {9,D}
""",
    kinetics = None,
)

entry(
    index = 183,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {11,[S,D,T,B]}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {1,S} {10,D}
10    C   u0 {9,D}
11    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 184,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {11,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {1,S} {10,D}
10    C   u0 {9,D}
11    C   u0 {3,S} {12,[S,D,T,B]}
12    C   u0 {11,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 185,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {3,S} {12,D}
12    C  u0 {11,D}
""",
    kinetics = None,
)

entry(
    index = 186,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S} {13,S}
4     C  u0 {2,S}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {3,S} {12,D}
12    C  u0 {11,D}
13    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 187,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S} {13,S}
4     C  u0 {2,S} {14,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {3,S} {12,D}
12    C  u0 {11,D}
13    C  u0 {3,S}
14    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 188,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-14R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {11,S} {13,S}
4     C  u0 {2,S} {14,D}
5     C  u0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 r0 {1,S} {10,D}
10    C  u0 {9,D}
11    C  u0 r0 {3,S} {12,D}
12    C  u0 {11,D}
13    C  u0 {3,S}
14    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 189,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-14R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {11,S} {13,S}
4     C  u0 {2,S} {14,[B,S,T]}
5     C  u0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 r0 {1,S} {10,D}
10    C  u0 {9,D}
11    C  u0 r0 {3,S} {12,D}
12    C  u0 {11,D}
13    C  u0 {3,S}
14    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 190,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {13,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {3,S} {12,D}
12    C  u0 {11,D}
13    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 191,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H_Ext-4R!H-R_Sp-13R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {11,S}
4     C  u0 r0 {2,S} {13,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {1,S} {10,D}
10    C  u0 r0 {9,D}
11    C  u0 r0 {3,S} {12,D}
12    C  u0 r0 {11,D}
13    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 192,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H_Ext-4R!H-R_N-Sp-13R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {11,S}
4     C  u0 r0 {2,S} {13,[B,S,T]}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {1,S} {10,D}
10    C  u0 r0 {9,D}
11    C  u0 r0 {3,S} {12,D}
12    C  u0 r0 {11,D}
13    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 193,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {11,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {1,S} {10,D}
10    C   u0 {9,D}
11    C   u0 {3,S} {12,T}
12    C   u0 {11,T}
""",
    kinetics = None,
)

entry(
    index = 194,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {13,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {3,S} {12,T}
12    C  u0 {11,T}
13    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 195,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-4R!H-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S} {14,S}
4     C  u0 {2,S} {13,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {3,S} {12,T}
12    C  u0 {11,T}
13    C  u0 {4,[S,D,T,B]}
14    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 196,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-4R!H-R_Ext-3R!H-R_Sp-13R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {11,S} {14,S}
4     C  u0 {2,S} {13,D}
5     C  u0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 r0 {1,S} {10,D}
10    C  u0 {9,D}
11    C  u0 r0 {3,S} {12,T}
12    C  u0 {11,T}
13    C  u0 {4,D}
14    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 197,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-4R!H-R_Ext-3R!H-R_N-Sp-13R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {11,S} {14,S}
4     C  u0 {2,S} {13,T}
5     C  u0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 r0 {1,S} {10,D}
10    C  u0 {9,D}
11    C  u0 r0 {3,S} {12,T}
12    C  u0 {11,T}
13    C  u0 {4,T}
14    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 198,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-4R!H-R_Sp-13R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {13,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {3,S} {12,T}
12    C  u0 {11,T}
13    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 199,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-4R!H-R_N-Sp-13R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {13,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {3,S} {12,T}
12    C  u0 {11,T}
13    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 200,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {11,S} {13,[S,D,T,B]}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {1,S} {10,D}
10    C   u0 {9,D}
11    C   u0 {3,S} {12,T}
12    C   u0 {11,T}
13    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 201,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {11,[S,D,T,B]} {12,[S,D,T,B]}
4     C   u0 {2,S}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {1,S} {10,D}
10    C   u0 {9,D}
11    R!H ux {3,[S,D,T,B]}
12    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 202,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {11,[S,D,T,B]} {12,[S,D,T,B]}
4     C   u0 {2,S} {13,[S,D,T,B]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {1,S} {10,D}
10    C   u0 {9,D}
11    R!H ux {3,[S,D,T,B]}
12    R!H ux {3,[S,D,T,B]}
13    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 203,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-13R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {11,[S,D,T,B]} {12,[S,D,T,B]}
4     C   u0 {2,S} {13,D}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {1,S} {10,D}
10    C   u0 {9,D}
11    R!H ux {3,[S,D,T,B]}
12    R!H ux {3,[S,D,T,B]}
13    C   u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 204,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-13R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {11,[S,D,T,B]} {12,[S,D,T,B]}
4     C   u0 {2,S} {13,[B,S,T]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {1,S} {10,D}
10    C   u0 {9,D}
11    R!H ux {3,[S,D,T,B]}
12    R!H ux {3,[S,D,T,B]}
13    C   u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 205,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {12,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {3,S}
12    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 206,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {11,S}
4     C  u0 r0 {2,S} {12,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {1,S} {10,D}
10    C  u0 r0 {9,D}
11    C  u0 r0 {3,S}
12    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 207,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {11,S}
4     C  u0 r0 {2,S} {12,[B,S,T]}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {1,S} {10,D}
10    C  u0 r0 {9,D}
11    C  u0 r0 {3,S}
12    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 208,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {11,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 209,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S}
4     C  u0 r0 {2,S} {11,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {1,S} {10,D}
10    C  u0 r0 {9,D}
11    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 210,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S}
4     C  u0 r0 {2,S} {11,[B,S,T]}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {1,S} {10,D}
10    C  u0 r0 {9,D}
11    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 211,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {10,[S,D,T,B]}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {1,S}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 212,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {10,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {1,S}
10    C   u0 {3,S} {11,[S,D,T,B]}
11    C   u0 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 213,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {10,S}
4     C  u0 {2,S}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S}
10    C  u0 {3,S} {11,D}
11    C  u0 {10,D}
""",
    kinetics = None,
)

entry(
    index = 214,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {10,S} {12,S}
4     C  u0 {2,S}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S}
10    C  u0 {3,S} {11,D}
11    C  u0 {10,D}
12    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 215,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {10,S} {12,S}
4     C  u0 {2,S} {13,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S}
10    C  u0 {3,S} {11,D}
11    C  u0 {10,D}
12    C  u0 {3,S}
13    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 216,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-13R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {10,S} {12,S}
4     C  u0 r0 {2,S} {13,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {1,S}
10    C  u0 r0 {3,S} {11,D}
11    C  u0 {10,D}
12    C  u0 {3,S}
13    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 217,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-13R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {10,S} {12,S}
4     C  u0 r0 {2,S} {13,[B,S,T]}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {1,S}
10    C  u0 r0 {3,S} {11,D}
11    C  u0 {10,D}
12    C  u0 {3,S}
13    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 218,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {10,S}
4     C  u0 {2,S} {12,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S}
10    C  u0 {3,S} {11,D}
11    C  u0 {10,D}
12    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 219,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-4R!H-R_Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {10,S}
4     C  u0 r0 {2,S} {12,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {1,S}
10    C  u0 r0 {3,S} {11,D}
11    C  u0 r0 {10,D}
12    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 220,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-4R!H-R_N-Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {10,S}
4     C  u0 r0 {2,S} {12,[B,S,T]}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {1,S}
10    C  u0 r0 {3,S} {11,D}
11    C  u0 r0 {10,D}
12    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 221,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {10,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {1,S}
10    C   u0 {3,S} {11,T}
11    C   u0 {10,T}
""",
    kinetics = None,
)

entry(
    index = 222,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {10,S}
4     C  u0 {2,S} {12,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S}
10    C  u0 {3,S} {11,T}
11    C  u0 {10,T}
12    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 223,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-4R!H-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {10,S} {13,S}
4     C  u0 {2,S} {12,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S}
10    C  u0 {3,S} {11,T}
11    C  u0 {10,T}
12    C  u0 {4,[S,D,T,B]}
13    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 224,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-4R!H-R_Ext-3R!H-R_Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {10,S} {13,S}
4     C  u0 r0 {2,S} {12,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {1,S}
10    C  u0 r0 {3,S} {11,T}
11    C  u0 {10,T}
12    C  u0 {4,D}
13    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 225,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-4R!H-R_Ext-3R!H-R_N-Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {10,S} {13,S}
4     C  u0 r0 {2,S} {12,T}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {1,S}
10    C  u0 r0 {3,S} {11,T}
11    C  u0 {10,T}
12    C  u0 {4,T}
13    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 226,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-4R!H-R_Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {10,S}
4     C  u0 {2,S} {12,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S}
10    C  u0 {3,S} {11,T}
11    C  u0 {10,T}
12    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 227,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-4R!H-R_N-Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {10,S}
4     C  u0 {2,S} {12,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S}
10    C  u0 {3,S} {11,T}
11    C  u0 {10,T}
12    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 228,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {10,S} {12,[S,D,T,B]}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {1,S}
10    C   u0 {3,S} {11,T}
11    C   u0 {10,T}
12    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 229,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 {2,S}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {1,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 230,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 {2,S} {12,[S,D,T,B]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {1,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
12    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 231,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 {2,S} {12,D}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {1,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
12    C   u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 232,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 {2,S} {12,[B,S,T]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {1,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
12    C   u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 233,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {10,S}
4     C  u0 {2,S} {11,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S}
10    C  u0 {3,S}
11    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 234,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {10,S}
4     C  u0 r0 {2,S} {11,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {1,S}
10    C  u0 r0 {3,S}
11    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 235,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {10,S}
4     C  u0 r0 {2,S} {11,[B,S,T]}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {1,S}
10    C  u0 r0 {3,S}
11    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 236,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 237,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {1,S}
10    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 238,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S}
4     C  u0 r0 {2,S} {10,[B,S,T]}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {1,S}
10    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 239,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S} {9,[S,D,T,B]}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,D}
7    C   u0 {6,D} {8,S}
8    C   u0 {7,S}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 240,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {9,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {3,S} {10,[S,D,T,B]}
10    C   u0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 241,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S}
4     C  u0 {2,S}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {3,S} {10,D}
10    C  u0 {9,D}
""",
    kinetics = None,
)

entry(
    index = 242,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S} {11,S}
4     C  u0 {2,S}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {3,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 243,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S} {11,S}
4     C  u0 {2,S} {12,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {3,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {3,S}
12    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 244,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {9,S} {11,S}
4     C  u0 r0 {2,S} {12,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {3,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {3,S}
12    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 245,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {9,S} {11,S}
4     C  u0 r0 {2,S} {12,[B,S,T]}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {3,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {3,S}
12    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 246,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S}
4     C  u0 {2,S} {11,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {3,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 247,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {9,S}
4     C  u0 r0 {2,S} {11,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {3,S} {10,D}
10    C  u0 r0 {9,D}
11    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 248,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {9,S}
4     C  u0 r0 {2,S} {11,[B,S,T]}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {3,S} {10,D}
10    C  u0 r0 {9,D}
11    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 249,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {9,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {3,S} {10,T}
10    C   u0 {9,T}
""",
    kinetics = None,
)

entry(
    index = 250,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S}
4     C  u0 {2,S} {11,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {3,S} {10,T}
10    C  u0 {9,T}
11    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 251,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S} {12,S}
4     C  u0 {2,S} {11,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {3,S} {10,T}
10    C  u0 {9,T}
11    C  u0 {4,[S,D,T,B]}
12    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 252,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_Ext-3R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {9,S} {12,S}
4     C  u0 r0 {2,S} {11,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {3,S} {10,T}
10    C  u0 {9,T}
11    C  u0 {4,D}
12    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 253,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_Ext-3R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {9,S} {12,S}
4     C  u0 r0 {2,S} {11,T}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {3,S} {10,T}
10    C  u0 {9,T}
11    C  u0 {4,T}
12    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 254,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S}
4     C  u0 {2,S} {11,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {3,S} {10,T}
10    C  u0 {9,T}
11    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 255,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S}
4     C  u0 {2,S} {11,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {3,S} {10,T}
10    C  u0 {9,T}
11    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 256,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {9,S} {11,[S,D,T,B]}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     C   u0 {3,S} {10,T}
10    C   u0 {9,T}
11    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 257,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 {2,S}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 258,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 {2,S} {11,[S,D,T,B]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 259,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 {2,S} {11,D}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    C   u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 260,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 {2,S} {11,[B,S,T]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D} {8,S}
8     C   u0 {7,S}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    C   u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 261,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {9,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S}
9     C  u0 {3,S}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 262,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {9,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {3,S}
10    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 263,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {9,S}
4     C  u0 r0 {2,S} {10,[B,S,T]}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {3,S}
10    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 264,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S}
4    C  u0 {2,S} {9,[S,D,T,B]}
5    C  u0 {2,S}
6    C  u0 {3,S} {7,D}
7    C  u0 {6,D} {8,S}
8    C  u0 {7,S}
9    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 265,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D}
2 *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3 *1 C  u1 r0 {6,S}
4    C  u0 r0 {2,S} {9,D}
5    C  u0 r0 {2,S}
6    C  u0 r0 {3,S} {7,D}
7    C  u0 r0 {6,D} {8,S}
8    C  u0 r0 {7,S}
9    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 266,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D}
2 *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3 *1 C  u1 r0 {6,S}
4    C  u0 r0 {2,S} {9,[B,S,T]}
5    C  u0 r0 {2,S}
6    C  u0 r0 {3,S} {7,D}
7    C  u0 r0 {6,D} {8,S}
8    C  u0 r0 {7,S}
9    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 267,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S}
4    C  u0 {2,S} {8,[S,D,T,B]}
5    C  u0 {2,S}
6    C  u0 {3,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 268,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {9,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3 *1 C   u1 {6,S}
4    C   u0 {2,S} {8,[S,D,T,B]}
5    C   u0 {2,S}
6    C   u0 {3,S} {7,D}
7    C   u0 {6,D}
8    C   u0 {4,[S,D,T,B]}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 269,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 {2,S} {8,[S,D,T,B]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {4,[S,D,T,B]}
9     R!H ux {1,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 270,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 {2,S} {8,[S,D,T,B]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {4,[S,D,T,B]}
9     C   u0 {1,S} {12,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
12    C   u0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 271,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {10,S} {11,S}
4     C  u0 {2,S} {8,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {4,[S,D,T,B]}
9     C  u0 {1,S} {12,D}
10    C  u0 {3,S} {13,S}
11    C  u0 {3,S}
12    C  u0 {9,D}
13    C  u0 {10,S}
""",
    kinetics = None,
)

entry(
    index = 272,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S} {14,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {10,S} {11,S}
4     C  u0 {2,S} {8,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {4,[S,D,T,B]}
9     C  u0 {1,S} {12,D}
10    C  u0 {3,S} {13,S}
11    C  u0 {3,S}
12    C  u0 {9,D}
13    C  u0 {10,S}
14    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 273,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S} {14,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {10,S} {11,S}
4     C  u0 {2,S} {8,D}
5     C  u0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D}
8     C  u0 {4,D}
9     C  u0 {1,S} {12,D}
10    C  u0 r0 {3,S} {13,S}
11    C  u0 {3,S}
12    C  u0 r0 {9,D}
13    C  u0 {10,S}
14    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 274,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S} {14,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {10,S} {11,S}
4     C  u0 {2,S} {8,T}
5     C  u0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D}
8     C  u0 {4,T}
9     C  u0 {1,S} {12,D}
10    C  u0 r0 {3,S} {13,S}
11    C  u0 {3,S}
12    C  u0 r0 {9,D}
13    C  u0 {10,S}
14    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 275,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-10R!H-R_Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {10,S} {11,S}
4     C  u0 {2,S} {8,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {4,D}
9     C  u0 {1,S} {12,D}
10    C  u0 {3,S} {13,S}
11    C  u0 {3,S}
12    C  u0 {9,D}
13    C  u0 {10,S}
""",
    kinetics = None,
)

entry(
    index = 276,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-10R!H-R_N-Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {10,S} {11,S}
4     C  u0 {2,S} {8,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {4,T}
9     C  u0 {1,S} {12,D}
10    C  u0 {3,S} {13,S}
11    C  u0 {3,S}
12    C  u0 {9,D}
13    C  u0 {10,S}
""",
    kinetics = None,
)

entry(
    index = 277,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S} {13,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 {2,S} {8,[S,D,T,B]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {4,[S,D,T,B]}
9     C   u0 {1,S} {12,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
12    C   u0 {9,S}
13    C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 278,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S} {13,S}
2  *3 Cd  u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C   u1 r0 {6,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 r0 {2,S} {8,D}
5     C   u0 r0 {2,S}
6     C   u0 r0 {3,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 r0 {4,D}
9     C   u0 r0 {1,S} {12,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
12    C   u0 r0 {9,S}
13    C   u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 279,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S} {13,S}
2  *3 Cd  u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C   u1 r0 {6,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 r0 {2,S} {8,T}
5     C   u0 r0 {2,S}
6     C   u0 r0 {3,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 r0 {4,T}
9     C   u0 r0 {1,S} {12,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
12    C   u0 r0 {9,S}
13    C   u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 280,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 {2,S} {8,D}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {4,D}
9     C   u0 {1,S} {12,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
12    C   u0 {9,S}
""",
    kinetics = None,
)

entry(
    index = 281,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 {2,S} {8,T}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {4,T}
9     C   u0 {1,S} {12,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
12    C   u0 {9,S}
""",
    kinetics = None,
)

entry(
    index = 282,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,[S,D,T,B]} {12,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 {2,S} {8,[S,D,T,B]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {4,[S,D,T,B]}
9     R!H ux {1,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 283,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,[S,D,T,B]} {12,[S,D,T,B]}
2  *3 Cd  u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C   u1 r0 {6,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 r0 {2,S} {8,D}
5     C   u0 r0 {2,S}
6     C   u0 r0 {3,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 r0 {4,D}
9     R!H ux {1,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 284,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,[S,D,T,B]} {12,[S,D,T,B]}
2  *3 Cd  u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C   u1 r0 {6,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 r0 {2,S} {8,T}
5     C   u0 r0 {2,S}
6     C   u0 r0 {3,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 r0 {4,T}
9     R!H ux {1,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 285,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 {2,S} {8,D}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {4,D}
9     C   u0 {1,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 286,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 {2,S} {8,T}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {4,T}
9     C   u0 {1,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 287,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Sp-10R!H=9R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {8,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {4,[S,D,T,B]}
9     C  u0 {1,S} {10,D}
10    C  u0 {9,D}
""",
    kinetics = None,
)

entry(
    index = 288,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-11R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S} {13,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {8,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {4,[S,D,T,B]}
9     C  u0 {1,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {3,S} {12,S}
12    C  u0 {11,S}
13    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 289,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-11R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S} {13,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {11,S}
4     C  u0 r0 {2,S} {8,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D}
8     C  u0 r0 {4,D}
9     C  u0 r0 {1,S} {10,D}
10    C  u0 r0 {9,D}
11    C  u0 r0 {3,S} {12,S}
12    C  u0 {11,S}
13    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 290,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-11R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S} {13,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {11,S}
4     C  u0 r0 {2,S} {8,T}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D}
8     C  u0 r0 {4,T}
9     C  u0 r0 {1,S} {10,D}
10    C  u0 r0 {9,D}
11    C  u0 r0 {3,S} {12,S}
12    C  u0 {11,S}
13    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 291,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Sp-10R!H=9R!H_Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {8,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {4,D}
9     C  u0 {1,S} {10,D}
10    C  u0 {9,D}
""",
    kinetics = None,
)

entry(
    index = 292,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Sp-10R!H=9R!H_N-Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {8,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {4,T}
9     C  u0 {1,S} {10,D}
10    C  u0 {9,D}
""",
    kinetics = None,
)

entry(
    index = 293,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {8,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {4,[S,D,T,B]}
9     C  u0 {1,S} {10,S}
10    C  u0 {9,S}
""",
    kinetics = None,
)

entry(
    index = 294,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {8,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {4,[S,D,T,B]}
9     C  u0 {1,S} {10,S}
10    C  u0 {9,S}
11    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 295,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S} {12,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {8,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {4,[S,D,T,B]}
9     C  u0 {1,S} {10,S}
10    C  u0 {9,S}
11    C  u0 {3,S}
12    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 296,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S} {12,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {8,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {4,D}
9     C  u0 {1,S} {10,S}
10    C  u0 {9,S}
11    C  u0 {3,S}
12    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 297,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S} {12,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {8,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {4,T}
9     C  u0 {1,S} {10,S}
10    C  u0 {9,S}
11    C  u0 {3,S}
12    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 298,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {8,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {4,D}
9     C  u0 {1,S} {10,S}
10    C  u0 {9,S}
11    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 299,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {8,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {4,T}
9     C  u0 {1,S} {10,S}
10    C  u0 {9,S}
11    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 300,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S} {11,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {8,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {4,[S,D,T,B]}
9     C  u0 {1,S} {10,S}
10    C  u0 {9,S}
11    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 301,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S} {11,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S}
4     C  u0 r0 {2,S} {8,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D}
8     C  u0 r0 {4,D}
9     C  u0 r0 {1,S} {10,S}
10    C  u0 r0 {9,S}
11    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 302,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S} {11,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S}
4     C  u0 r0 {2,S} {8,T}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,D}
7     C  u0 r0 {6,D}
8     C  u0 r0 {4,T}
9     C  u0 r0 {1,S} {10,S}
10    C  u0 r0 {9,S}
11    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 303,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {8,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {4,D}
9     C  u0 {1,S} {10,S}
10    C  u0 {9,S}
""",
    kinetics = None,
)

entry(
    index = 304,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_N-Sp-8R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {8,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {4,T}
9     C  u0 {1,S} {10,S}
10    C  u0 {9,S}
""",
    kinetics = None,
)

entry(
    index = 305,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,D}
7    C   u0 {6,D}
8    R!H ux {3,[S,D,T,B]}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 306,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {1,S} {11,[S,D,T,B]}
11    C   u0 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 307,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-8R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {8,S} {9,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {12,S}
9     C   u0 {3,S}
10    C   u0 {1,S} {11,D}
11    C   u0 {10,D}
12    C   u0 {8,S}
""",
    kinetics = None,
)

entry(
    index = 308,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-8R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,S} {13,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 r0 {6,S} {8,S} {9,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 r0 {3,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 r0 {3,S} {12,S}
9     C   u0 {3,S}
10    C   u0 r0 {1,S} {11,D}
11    C   u0 {10,D}
12    C   u0 r0 {8,S}
13    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 309,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,S} {12,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {1,S} {11,S}
11    C   u0 {10,S}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 310,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 r0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 r0 {6,S} {8,S} {9,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 r0 {3,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 r0 {3,S}
9     C   u0 r0 {3,S} {10,S}
10    C   u0 r0 {9,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 311,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {8,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,D}
7    C   u0 {6,D}
8    C   u0 {1,S} {9,D}
9    C   u0 {8,D}
""",
    kinetics = None,
)

entry(
    index = 312,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S} {12,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 r0 {6,S} {10,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 r0 {3,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 r0 {1,S} {9,D}
9     C   u0 {8,D}
10    C   u0 {3,S} {11,S}
11    C   u0 r0 {10,S}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 313,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {8,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,D}
7    C   u0 {6,D}
8    C   u0 {1,S} {9,S}
9    C   u0 {8,S}
""",
    kinetics = None,
)

entry(
    index = 314,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {10,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {1,S} {9,S}
9     C   u0 {8,S}
10    C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 315,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 r0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {10,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {1,S} {9,S}
9     C   u0 r0 {8,S}
10    C   u0 r0 {3,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 316,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {1,S} {9,S}
9     C   u0 {8,S}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 317,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,[B,S,T]}
7    C   u0 {6,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 318,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,T}
7    C   u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 319,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {8,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,T}
7    C   u0 {6,T}
8    C   u0 {1,S} {9,D}
9    C   u0 {8,D}
""",
    kinetics = None,
)

entry(
    index = 320,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 321,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {13,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,[S,D,T,B]}
11    C  u0 {3,S} {12,S}
12    C  u0 {11,S}
13    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 322,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {13,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S} {14,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,[S,D,T,B]}
11    C  u0 {3,S} {12,S}
12    C  u0 {11,S}
13    C  u0 {1,S}
14    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 323,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {13,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S} {14,S}
4     C  u0 {2,S} {10,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 r0 {6,T}
8     C  u0 {1,S} {9,D}
9     C  u0 r0 {8,D}
10    C  u0 r0 {4,D}
11    C  u0 {3,S} {12,S}
12    C  u0 r0 {11,S}
13    C  u0 {1,S}
14    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 324,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {13,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S} {14,S}
4     C  u0 {2,S} {10,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 r0 {6,T}
8     C  u0 {1,S} {9,D}
9     C  u0 r0 {8,D}
10    C  u0 r0 {4,T}
11    C  u0 {3,S} {12,S}
12    C  u0 r0 {11,S}
13    C  u0 {1,S}
14    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 325,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {13,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {10,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,D}
11    C  u0 {3,S} {12,S}
12    C  u0 {11,S}
13    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 326,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {13,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {10,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,T}
11    C  u0 {3,S} {12,S}
12    C  u0 {11,S}
13    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 327,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {11,[S,D,T,B]} {12,[S,D,T,B]}
4     C   u0 {2,S} {10,[S,D,T,B]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {1,S} {9,D}
9     C   u0 {8,D}
10    C   u0 {4,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
12    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 328,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {11,[S,D,T,B]} {12,[S,D,T,B]}
4     C   u0 {2,S} {10,D}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {1,S} {9,D}
9     C   u0 {8,D}
10    C   u0 {4,D}
11    R!H ux {3,[S,D,T,B]}
12    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 329,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {11,[S,D,T,B]} {12,[S,D,T,B]}
4     C   u0 {2,S} {10,T}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {1,S} {9,D}
9     C   u0 {8,D}
10    C   u0 {4,T}
11    R!H ux {3,[S,D,T,B]}
12    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 330,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {10,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 331,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {10,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 332,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S} {12,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {10,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {1,S} {9,D}
9     C   u0 {8,D}
10    C   u0 {3,S} {11,S}
11    C   u0 {10,S}
12    C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 333,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S} {12,S}
2  *3 Cd  u0 c0 r0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 r0 {6,S} {10,S} {13,[S,D,T,B]}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 r0 {3,S} {7,T}
7     C   u0 r0 {6,T}
8     C   u0 r0 {1,S} {9,D}
9     C   u0 r0 {8,D}
10    C   u0 r0 {3,S} {11,S}
11    C   u0 {10,S}
12    C   u0 r0 {1,S}
13    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 334,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S}
2  *3 Cd  u0 c0 r0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 r0 {6,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 r0 {3,S} {7,T}
7     C   u0 r0 {6,T}
8     C   u0 r0 {1,S} {9,D}
9     C   u0 r0 {8,D}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 335,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {8,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,T}
7    C   u0 {6,T}
8    C   u0 {1,S} {9,S}
9    C   u0 {8,S}
""",
    kinetics = None,
)

entry(
    index = 336,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,S}
9     C  u0 {8,S}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 337,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,S}
9     C  u0 {8,S} {11,S}
10    C  u0 {4,[S,D,T,B]}
11    C  u0 {9,S}
""",
    kinetics = None,
)

entry(
    index = 338,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {12,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,S}
9     C  u0 {8,S} {11,S}
10    C  u0 {4,[S,D,T,B]}
11    C  u0 {9,S}
12    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 339,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {13,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {12,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,S}
9     C  u0 {8,S} {11,S}
10    C  u0 {4,[S,D,T,B]}
11    C  u0 {9,S}
12    C  u0 {3,S}
13    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 340,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {13,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {12,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 r0 {1,S} {9,S}
9     C  u0 {8,S} {11,S}
10    C  u0 {4,D}
11    C  u0 r0 {9,S}
12    C  u0 {3,S}
13    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 341,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {13,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {12,S}
4     C  u0 r0 {2,S} {10,T}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 r0 {1,S} {9,S}
9     C  u0 {8,S} {11,S}
10    C  u0 {4,T}
11    C  u0 r0 {9,S}
12    C  u0 {3,S}
13    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 342,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {12,S}
4     C  u0 {2,S} {10,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,S}
9     C  u0 {8,S} {11,S}
10    C  u0 {4,D}
11    C  u0 {9,S}
12    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 343,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {12,S}
4     C  u0 {2,S} {10,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,S}
9     C  u0 {8,S} {11,S}
10    C  u0 {4,T}
11    C  u0 {9,S}
12    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 344,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {12,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,S}
9     C  u0 {8,S} {11,S}
10    C  u0 {4,[S,D,T,B]}
11    C  u0 {9,S}
12    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 345,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {12,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,T}
7     C  u0 r0 {6,T}
8     C  u0 r0 {1,S} {9,S}
9     C  u0 r0 {8,S} {11,S}
10    C  u0 r0 {4,D}
11    C  u0 r0 {9,S}
12    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 346,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {12,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S}
4     C  u0 r0 {2,S} {10,T}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,T}
7     C  u0 r0 {6,T}
8     C  u0 r0 {1,S} {9,S}
9     C  u0 r0 {8,S} {11,S}
10    C  u0 r0 {4,T}
11    C  u0 r0 {9,S}
12    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 347,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {10,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,S}
9     C  u0 {8,S} {11,S}
10    C  u0 {4,D}
11    C  u0 {9,S}
""",
    kinetics = None,
)

entry(
    index = 348,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {10,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,S}
9     C  u0 {8,S} {11,S}
10    C  u0 {4,T}
11    C  u0 {9,S}
""",
    kinetics = None,
)

entry(
    index = 349,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,S}
9     C  u0 {8,S}
10    C  u0 {4,[S,D,T,B]}
11    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 350,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {12,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,S}
9     C  u0 {8,S}
10    C  u0 {4,[S,D,T,B]}
11    C  u0 {3,S}
12    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 351,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {12,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {10,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,S}
9     C  u0 {8,S}
10    C  u0 {4,D}
11    C  u0 {3,S}
12    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 352,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {12,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {10,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,S}
9     C  u0 {8,S}
10    C  u0 {4,T}
11    C  u0 {3,S}
12    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 353,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {10,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,S}
9     C  u0 {8,S}
10    C  u0 {4,D}
11    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 354,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {11,S}
4     C  u0 {2,S} {10,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,S}
9     C  u0 {8,S}
10    C  u0 {4,T}
11    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 355,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {11,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,S}
9     C  u0 {8,S}
10    C  u0 {4,[S,D,T,B]}
11    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 356,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {11,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,T}
7     C  u0 r0 {6,T}
8     C  u0 r0 {1,S} {9,S}
9     C  u0 r0 {8,S}
10    C  u0 r0 {4,D}
11    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 357,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {11,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S}
4     C  u0 r0 {2,S} {10,T}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,T}
7     C  u0 r0 {6,T}
8     C  u0 r0 {1,S} {9,S}
9     C  u0 r0 {8,S}
10    C  u0 r0 {4,T}
11    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 358,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {10,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,S}
9     C  u0 {8,S}
10    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 359,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {10,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {1,S} {9,S}
9     C  u0 {8,S}
10    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 360,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-9R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {1,S} {9,S}
9     C   u0 {8,S} {10,S}
10    C   u0 {9,S}
""",
    kinetics = None,
)

entry(
    index = 361,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-9R!H-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {11,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {1,S} {9,S}
9     C   u0 {8,S} {10,S}
10    C   u0 {9,S}
11    C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 362,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-9R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S} {12,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {11,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {1,S} {9,S}
9     C   u0 {8,S} {10,S}
10    C   u0 {9,S}
11    C   u0 r0 {3,S}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 363,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {1,S} {9,S}
9     C   u0 {8,S} {10,S}
10    C   u0 {9,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 364,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {10,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {1,S} {9,S}
9     C   u0 {8,S}
10    C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 365,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 r0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 r0 {6,S} {10,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 r0 {3,S} {7,T}
7     C   u0 r0 {6,T}
8     C   u0 r0 {1,S} {9,S}
9     C   u0 r0 {8,S}
10    C   u0 r0 {3,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 366,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {1,S} {9,S}
9     C   u0 {8,S}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 367,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,S}
7    C   u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 368,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S} {8,[S,D,T,B]}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,S}
7    C   u0 {6,S}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 369,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,S}
7    C   u0 {6,S}
8    R!H ux {3,[S,D,T,B]}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 370,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 371,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {1,S} {11,D}
11    C   u0 {10,D}
""",
    kinetics = None,
)

entry(
    index = 372,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {12,[S,D,T,B]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {1,S} {11,D}
11    C   u0 {10,D}
12    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 373,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,S} {13,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {12,[S,D,T,B]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {1,S} {11,D}
11    C   u0 {10,D}
12    C   u0 {4,[S,D,T,B]}
13    C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 374,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,S} {13,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {12,D}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 r0 {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {1,S} {11,D}
11    C   u0 r0 {10,D}
12    C   u0 {4,D}
13    C   u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 375,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,S} {13,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {12,T}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 r0 {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {1,S} {11,D}
11    C   u0 r0 {10,D}
12    C   u0 {4,T}
13    C   u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 376,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-4R!H-R_Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {12,D}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {1,S} {11,D}
11    C   u0 {10,D}
12    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 377,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-4R!H-R_N-Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {12,T}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {1,S} {11,D}
11    C   u0 {10,D}
12    C   u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 378,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,S} {12,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {1,S} {11,D}
11    C   u0 {10,D}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 379,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {11,[S,D,T,B]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {1,[S,D,T,B]}
11    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 380,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,[S,D,T,B]} {12,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {11,[S,D,T,B]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {1,[S,D,T,B]}
11    C   u0 {4,[S,D,T,B]}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 381,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,[S,D,T,B]} {12,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {11,D}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {1,[S,D,T,B]}
11    C   u0 {4,D}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 382,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,[S,D,T,B]} {12,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {11,T}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {1,[S,D,T,B]}
11    C   u0 {4,T}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 383,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {7,S} {10,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {11,[S,D,T,B]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 {1,S} {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {1,S}
11    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 384,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {7,S} {10,S}
2  *3 Cd  u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C   u1 r0 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 r0 {2,S} {11,D}
5     C   u0 r0 {2,S}
6     C   u0 r0 {3,S} {7,S}
7     C   u0 r0 {1,S} {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 r0 {1,S}
11    C   u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 385,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {7,S} {10,S}
2  *3 Cd  u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C   u1 r0 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 r0 {2,S} {11,T}
5     C   u0 r0 {2,S}
6     C   u0 r0 {3,S} {7,S}
7     C   u0 r0 {1,S} {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 r0 {1,S}
11    C   u0 r0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 386,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {11,D}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {1,S}
11    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 387,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,S}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {11,T}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {1,S}
11    C   u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 388,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {10,[S,D,T,B]} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {1,[S,D,T,B]}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 389,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {7,[S,D,T,B]} {10,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,S}
7     C   u0 {1,[S,D,T,B]} {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 390,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {10,[S,D,T,B]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 391,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D}
2  *3 Cd  u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C   u1 r0 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 r0 {2,S} {10,D}
5     C   u0 r0 {2,S}
6     C   u0 r0 {3,S} {7,S}
7     C   u0 r0 {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 392,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D}
2  *3 Cd  u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C   u1 r0 {6,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 r0 {2,S} {10,[B,S,T]}
5     C   u0 r0 {2,S}
6     C   u0 r0 {3,S} {7,S}
7     C   u0 r0 {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 393,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {9,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S} {8,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,S}
7    C   u0 {6,S}
8    C   u0 {3,S}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 394,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {8,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     C   u0 {3,S}
9     C   u0 {1,S} {10,D}
10    C   u0 {9,D}
""",
    kinetics = None,
)

entry(
    index = 395,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {8,S}
4     C  u0 {2,S} {11,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S}
9     C  u0 {1,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 396,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S} {12,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {8,S}
4     C  u0 {2,S} {11,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S}
9     C  u0 {1,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {4,[S,D,T,B]}
12    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 397,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S} {12,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {8,S}
4     C  u0 {2,S} {11,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S}
9     C  u0 {1,S} {10,D}
10    C  u0 r0 {9,D}
11    C  u0 {4,D}
12    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 398,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S} {12,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {8,S}
4     C  u0 {2,S} {11,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S}
9     C  u0 {1,S} {10,D}
10    C  u0 r0 {9,D}
11    C  u0 {4,T}
12    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 399,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {8,S}
4     C  u0 {2,S} {11,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S}
9     C  u0 {1,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 400,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {8,S}
4     C  u0 {2,S} {11,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S}
9     C  u0 {1,S} {10,D}
10    C  u0 {9,D}
11    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 401,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {8,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     C   u0 {3,S}
9     C   u0 {1,S} {10,D}
10    C   u0 {9,D}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 402,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,S}
4     C   u0 {2,S} {10,[S,D,T,B]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     C   u0 {3,S}
9     R!H ux {1,[S,D,T,B]}
10    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 403,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,[S,D,T,B]} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,S}
4     C   u0 {2,S} {10,[S,D,T,B]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     C   u0 {3,S}
9     R!H ux {1,[S,D,T,B]}
10    C   u0 {4,[S,D,T,B]}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 404,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,[S,D,T,B]} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,S}
4     C   u0 {2,S} {10,D}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     C   u0 {3,S}
9     R!H ux {1,[S,D,T,B]}
10    C   u0 {4,D}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 405,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,[S,D,T,B]} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S} {8,S}
4     C   u0 {2,S} {10,T}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     C   u0 {3,S}
9     R!H ux {1,[S,D,T,B]}
10    C   u0 {4,T}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 406,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {7,S} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {8,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,S}
7     C  u0 {1,S} {6,S}
8     C  u0 {3,S}
9     C  u0 {1,S}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 407,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {7,S} {9,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {8,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,S}
7     C  u0 r0 {1,S} {6,S}
8     C  u0 r0 {3,S}
9     C  u0 r0 {1,S}
10    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 408,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {7,S} {9,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3  *1 C  u1 r0 {6,S} {8,S}
4     C  u0 r0 {2,S} {10,T}
5     C  u0 r0 {2,S}
6     C  u0 r0 {3,S} {7,S}
7     C  u0 r0 {1,S} {6,S}
8     C  u0 r0 {3,S}
9     C  u0 r0 {1,S}
10    C  u0 r0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 409,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {8,S}
4     C  u0 {2,S} {10,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S}
9     C  u0 {1,S}
10    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 410,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S} {8,S}
4     C  u0 {2,S} {10,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S}
9     C  u0 {1,S}
10    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 411,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {9,[S,D,T,B]} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S} {8,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     C   u0 {3,S}
9     R!H ux {1,[S,D,T,B]}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 412,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {7,[S,D,T,B]} {9,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S} {8,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,S}
7    C   u0 {1,[S,D,T,B]} {6,S}
8    C   u0 {3,S}
9    C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 413,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S} {8,S}
4    C  u0 {2,S} {9,[S,D,T,B]}
5    C  u0 {2,S}
6    C  u0 {3,S} {7,S}
7    C  u0 {6,S}
8    C  u0 {3,S}
9    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 414,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D}
2 *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3 *1 C  u1 r0 {6,S} {8,S}
4    C  u0 r0 {2,S} {9,D}
5    C  u0 r0 {2,S}
6    C  u0 r0 {3,S} {7,S}
7    C  u0 r0 {6,S}
8    C  u0 r0 {3,S}
9    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 415,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D}
2 *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3 *1 C  u1 r0 {6,S} {8,S}
4    C  u0 r0 {2,S} {9,[B,S,T]}
5    C  u0 r0 {2,S}
6    C  u0 r0 {3,S} {7,S}
7    C  u0 r0 {6,S}
8    C  u0 r0 {3,S}
9    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 416,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {8,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,S}
7    C   u0 {6,S}
8    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 417,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {8,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,S}
7    C   u0 {6,S}
8    C   u0 {1,S} {9,[S,D,T,B]}
9    C   u0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 418,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Int-9R!H-7R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {8,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,S}
7    C   u0 {6,S} {9,[S,D,T,B]}
8    C   u0 {1,S} {9,[S,D,T,B]}
9    C   u0 r0 {7,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 419,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {1,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 420,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {11,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {1,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,[S,D,T,B]}
11    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 421,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {11,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {10,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {1,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,D}
11    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 422,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {11,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {10,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {1,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,T}
11    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 423,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {10,D}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {1,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 424,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S}
2  *3 Cd u0 c0 {1,D} {4,S} {5,S}
3  *1 C  u1 {6,S}
4     C  u0 {2,S} {10,T}
5     C  u0 {2,S}
6     C  u0 {3,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {1,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 425,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3  *1 C   u1 {6,S}
4     R!H ux {2,[S,D,T,B]}
5     R!H ux {2,[S,D,T,B]}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     C   u0 {1,S} {9,D}
9     C   u0 {8,D}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 426,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {8,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3 *1 C   u1 {6,S}
4    C   u0 {2,S} {9,[S,D,T,B]}
5    C   u0 {2,S}
6    C   u0 {3,S} {7,S}
7    C   u0 {6,S}
8    R!H ux {1,[S,D,T,B]}
9    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 427,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,[S,D,T,B]} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S}
4     C   u0 {2,S} {9,[S,D,T,B]}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     R!H ux {1,[S,D,T,B]}
9     C   u0 {4,[S,D,T,B]}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 428,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-9R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,[S,D,T,B]} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S}
4     C   u0 {2,S} {9,D}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     R!H ux {1,[S,D,T,B]}
9     C   u0 {4,D}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 429,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-9R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,[S,D,T,B]} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S} {5,S}
3  *1 C   u1 {6,S}
4     C   u0 {2,S} {9,T}
5     C   u0 {2,S}
6     C   u0 {3,S} {7,S}
7     C   u0 {6,S}
8     R!H ux {1,[S,D,T,B]}
9     C   u0 {4,T}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 430,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S} {8,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S}
4    C  u0 {2,S} {9,[S,D,T,B]}
5    C  u0 {2,S}
6    C  u0 {3,S} {7,S}
7    C  u0 {1,S} {6,S}
8    C  u0 {1,S}
9    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 431,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S} {8,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3 *1 C  u1 r0 {6,S}
4    C  u0 r0 {2,S} {9,D}
5    C  u0 r0 {2,S}
6    C  u0 r0 {3,S} {7,S}
7    C  u0 r0 {1,S} {6,S}
8    C  u0 r0 {1,S}
9    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 432,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S} {8,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3 *1 C  u1 r0 {6,S}
4    C  u0 r0 {2,S} {9,T}
5    C  u0 r0 {2,S}
6    C  u0 r0 {3,S} {7,S}
7    C  u0 r0 {1,S} {6,S}
8    C  u0 r0 {1,S}
9    C  u0 r0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 433,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {8,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S}
4    C  u0 {2,S} {9,D}
5    C  u0 {2,S}
6    C  u0 {3,S} {7,S}
7    C  u0 {6,S}
8    C  u0 {1,S}
9    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 434,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {8,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S}
4    C  u0 {2,S} {9,T}
5    C  u0 {2,S}
6    C  u0 {3,S} {7,S}
7    C  u0 {6,S}
8    C  u0 {1,S}
9    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 435,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {7,[S,D,T,B]} {8,S}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,S}
7    C   u0 {1,[S,D,T,B]} {6,S}
8    C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 436,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {8,[S,D,T,B]} {9,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 C   u1 {6,S}
4    R!H ux {2,[S,D,T,B]}
5    R!H ux {2,[S,D,T,B]}
6    C   u0 {3,S} {7,S}
7    C   u0 {6,S}
8    R!H ux {1,[S,D,T,B]}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 437,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3 *1 C  u1 {6,S}
4    C  u0 {2,S} {8,[S,D,T,B]}
5    C  u0 {2,S}
6    C  u0 {3,S} {7,S}
7    C  u0 {6,S}
8    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 438,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-4R!H-R_Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D}
2 *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3 *1 C  u1 r0 {6,S}
4    C  u0 r0 {2,S} {8,D}
5    C  u0 r0 {2,S}
6    C  u0 r0 {3,S} {7,S}
7    C  u0 r0 {6,S}
8    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 439,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D}
2 *3 Cd u0 c0 r0 {1,D} {4,S} {5,S}
3 *1 C  u1 r0 {6,S}
4    C  u0 r0 {2,S} {8,[B,S,T]}
5    C  u0 r0 {2,S}
6    C  u0 r0 {3,S} {7,S}
7    C  u0 r0 {6,S}
8    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 440,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,CS,Cdd,N,O4dc,O4tc,S] u0 r0 {2,[D,T,B]} {5,[S,D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S]               u0 c0 {1,[D,T,B]} {4,[S,D,T,B]}
3 *1 R!H                                    u1
4    C                                      u0 {2,[S,D,T,B]}
5    C                                      u0 {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 441,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,[S,D,T,B]}
4    C  u0 {2,S}
5    C  u0 {1,S} {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 442,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S}
4    C  u0 {2,S}
5    C  u0 {1,S} {3,S}
6    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 443,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S}
4    C  u0 {2,S}
5    C  u0 {1,S} {3,S}
6    C  u0 {1,S} {7,D}
7    C  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 444,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {5,S} {8,[S,D,T,B]}
4    C   u0 {2,S}
5    C   u0 {1,S} {3,S}
6    C   u0 {1,S} {7,D}
7    C   u0 {6,D}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 445,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S} {8,S}
4    C  u0 {2,S}
5    C  u0 {1,S} {3,S}
6    C  u0 {1,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S} {9,[S,D,T,B]}
9    C  u0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 446,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S} {8,S}
4    C  u0 {2,S}
5    C  u0 {1,S} {3,S}
6    C  u0 {1,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S} {9,D}
9    C  u0 {8,D}
""",
    kinetics = None,
)

entry(
    index = 447,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {5,S} {8,S} {10,S}
4     C  u0 {2,S}
5     C  u0 {1,S} {3,S}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 448,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {5,S} {8,S} {10,S}
4     C  u0 {2,S} {11,[S,D,T,B]}
5     C  u0 {1,S} {3,S}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
11    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 449,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 r0 {5,S} {8,S} {10,S}
4     C  u0 r0 {2,S} {11,D}
5     C  u0 r0 {1,S} {3,S}
6     C  u0 r0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 r0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
11    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 450,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 r0 {5,S} {8,S} {10,S}
4     C  u0 r0 {2,S} {11,[B,S,T]}
5     C  u0 r0 {1,S} {3,S}
6     C  u0 r0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 r0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
11    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 451,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {5,S} {8,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {1,S} {3,S}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 452,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {5,S} {8,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 r0 {1,S} {3,S}
6     C  u0 r0 {1,S} {7,D}
7     C  u0 r0 {6,D}
8     C  u0 r0 {3,S} {9,D}
9     C  u0 r0 {8,D}
10    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 453,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {5,S} {8,S}
4     C  u0 r0 {2,S} {10,[B,S,T]}
5     C  u0 r0 {1,S} {3,S}
6     C  u0 r0 {1,S} {7,D}
7     C  u0 r0 {6,D}
8     C  u0 r0 {3,S} {9,D}
9     C  u0 r0 {8,D}
10    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 454,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S} {8,S}
4    C  u0 {2,S}
5    C  u0 {1,S} {3,S}
6    C  u0 {1,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S} {9,T}
9    C  u0 {8,T}
""",
    kinetics = None,
)

entry(
    index = 455,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {5,S} {8,S} {10,S}
4     C  u0 {2,S}
5     C  u0 {1,S} {3,S}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 456,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {5,S} {8,S} {10,S}
4     C  u0 {2,S} {11,[S,D,T,B]}
5     C  u0 {1,S} {3,S}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S}
11    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 457,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 r0 {5,S} {8,S} {10,S}
4     C  u0 r0 {2,S} {11,D}
5     C  u0 r0 {1,S} {3,S}
6     C  u0 r0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 r0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S}
11    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 458,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 r0 {5,S} {8,S} {10,S}
4     C  u0 r0 {2,S} {11,[B,S,T]}
5     C  u0 r0 {1,S} {3,S}
6     C  u0 r0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 r0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S}
11    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 459,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {5,S} {8,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {1,S} {3,S}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 460,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {5,S} {8,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 r0 {1,S} {3,S}
6     C  u0 r0 {1,S} {7,D}
7     C  u0 r0 {6,D}
8     C  u0 r0 {3,S} {9,T}
9     C  u0 r0 {8,T}
10    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 461,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {5,S} {8,S}
4     C  u0 r0 {2,S} {10,[B,S,T]}
5     C  u0 r0 {1,S} {3,S}
6     C  u0 r0 {1,S} {7,D}
7     C  u0 r0 {6,D}
8     C  u0 r0 {3,S} {9,T}
9     C  u0 r0 {8,T}
10    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 462,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {5,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4    C   u0 {2,S}
5    C   u0 {1,S} {3,S}
6    C   u0 {1,S} {7,D}
7    C   u0 {6,D}
8    R!H ux {3,[S,D,T,B]}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 463,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {5,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {10,[S,D,T,B]}
5     C   u0 {1,S} {3,S}
6     C   u0 {1,S} {7,D}
7     C   u0 {6,D}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 464,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {5,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {10,D}
5     C   u0 {1,S} {3,S}
6     C   u0 {1,S} {7,D}
7     C   u0 {6,D}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 465,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {5,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {10,[B,S,T]}
5     C   u0 {1,S} {3,S}
6     C   u0 {1,S} {7,D}
7     C   u0 {6,D}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 466,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S} {8,S}
4    C  u0 {2,S} {9,[S,D,T,B]}
5    C  u0 {1,S} {3,S}
6    C  u0 {1,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S}
9    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 467,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {8,S}
4    C  u0 r0 {2,S} {9,D}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {1,S} {7,D}
7    C  u0 r0 {6,D}
8    C  u0 r0 {3,S}
9    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 468,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {8,S}
4    C  u0 r0 {2,S} {9,[B,S,T]}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {1,S} {7,D}
7    C  u0 r0 {6,D}
8    C  u0 r0 {3,S}
9    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 469,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S}
4    C  u0 {2,S} {8,[S,D,T,B]}
5    C  u0 {1,S} {3,S}
6    C  u0 {1,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 470,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S}
4    C  u0 r0 {2,S} {8,D}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {1,S} {7,D}
7    C  u0 r0 {6,D}
8    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 471,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S}
4    C  u0 r0 {2,S} {8,[B,S,T]}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {1,S} {7,D}
7    C  u0 r0 {6,D}
8    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 472,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {5,S} {7,[S,D,T,B]}
4    C   u0 {2,S}
5    C   u0 {1,S} {3,S}
6    C   u0 {1,S}
7    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 473,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S} {7,S}
4    C  u0 {2,S}
5    C  u0 {1,S} {3,S}
6    C  u0 {1,S}
7    C  u0 {3,S} {8,[S,D,T,B]}
8    C  u0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 474,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S} {7,S}
4    C  u0 {2,S}
5    C  u0 {1,S} {3,S}
6    C  u0 {1,S}
7    C  u0 {3,S} {8,D}
8    C  u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 475,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S} {7,S} {9,S}
4    C  u0 {2,S}
5    C  u0 {1,S} {3,S}
6    C  u0 {1,S}
7    C  u0 {3,S} {8,D}
8    C  u0 {7,D}
9    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 476,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {5,S} {7,S} {9,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {1,S} {3,S}
6     C  u0 {1,S}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D}
9     C  u0 {3,S}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 477,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {5,S} {7,S} {9,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 r0 {1,S} {3,S}
6     C  u0 r0 {1,S}
7     C  u0 r0 {3,S} {8,D}
8     C  u0 {7,D}
9     C  u0 {3,S}
10    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 478,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {5,S} {7,S} {9,S}
4     C  u0 r0 {2,S} {10,[B,S,T]}
5     C  u0 r0 {1,S} {3,S}
6     C  u0 r0 {1,S}
7     C  u0 r0 {3,S} {8,D}
8     C  u0 {7,D}
9     C  u0 {3,S}
10    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 479,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S} {7,S}
4    C  u0 {2,S} {9,[S,D,T,B]}
5    C  u0 {1,S} {3,S}
6    C  u0 {1,S}
7    C  u0 {3,S} {8,D}
8    C  u0 {7,D}
9    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 480,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {7,S}
4    C  u0 r0 {2,S} {9,D}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {1,S}
7    C  u0 r0 {3,S} {8,D}
8    C  u0 r0 {7,D}
9    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 481,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {7,S}
4    C  u0 r0 {2,S} {9,[B,S,T]}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {1,S}
7    C  u0 r0 {3,S} {8,D}
8    C  u0 r0 {7,D}
9    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 482,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S} {7,S}
4    C  u0 {2,S}
5    C  u0 {1,S} {3,S}
6    C  u0 {1,S}
7    C  u0 {3,S} {8,T}
8    C  u0 {7,T}
""",
    kinetics = None,
)

entry(
    index = 483,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S} {7,S} {9,S}
4    C  u0 {2,S}
5    C  u0 {1,S} {3,S}
6    C  u0 {1,S}
7    C  u0 {3,S} {8,T}
8    C  u0 {7,T}
9    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 484,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {5,S} {7,S} {9,S}
4     C  u0 {2,S} {10,[S,D,T,B]}
5     C  u0 {1,S} {3,S}
6     C  u0 {1,S}
7     C  u0 {3,S} {8,T}
8     C  u0 {7,T}
9     C  u0 {3,S}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 485,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {5,S} {7,S} {9,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 r0 {1,S} {3,S}
6     C  u0 r0 {1,S}
7     C  u0 r0 {3,S} {8,T}
8     C  u0 {7,T}
9     C  u0 {3,S}
10    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 486,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {6,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {5,S} {7,S} {9,S}
4     C  u0 r0 {2,S} {10,[B,S,T]}
5     C  u0 r0 {1,S} {3,S}
6     C  u0 r0 {1,S}
7     C  u0 r0 {3,S} {8,T}
8     C  u0 {7,T}
9     C  u0 {3,S}
10    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 487,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S} {7,S}
4    C  u0 {2,S} {9,[S,D,T,B]}
5    C  u0 {1,S} {3,S}
6    C  u0 {1,S}
7    C  u0 {3,S} {8,T}
8    C  u0 {7,T}
9    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 488,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-4R!H-R_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {7,S}
4    C  u0 r0 {2,S} {9,D}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {1,S}
7    C  u0 r0 {3,S} {8,T}
8    C  u0 r0 {7,T}
9    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 489,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {7,S}
4    C  u0 r0 {2,S} {9,[B,S,T]}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {1,S}
7    C  u0 r0 {3,S} {8,T}
8    C  u0 r0 {7,T}
9    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 490,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
4    C   u0 {2,S}
5    C   u0 {1,S} {3,S}
6    C   u0 {1,S}
7    R!H ux {3,[S,D,T,B]}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 491,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
4    C   u0 {2,S} {9,[S,D,T,B]}
5    C   u0 {1,S} {3,S}
6    C   u0 {1,S}
7    R!H ux {3,[S,D,T,B]}
8    R!H ux {3,[S,D,T,B]}
9    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 492,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
4    C   u0 {2,S} {9,D}
5    C   u0 {1,S} {3,S}
6    C   u0 {1,S}
7    R!H ux {3,[S,D,T,B]}
8    R!H ux {3,[S,D,T,B]}
9    C   u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 493,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
4    C   u0 {2,S} {9,[B,S,T]}
5    C   u0 {1,S} {3,S}
6    C   u0 {1,S}
7    R!H ux {3,[S,D,T,B]}
8    R!H ux {3,[S,D,T,B]}
9    C   u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 494,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S} {7,S}
4    C  u0 {2,S} {8,[S,D,T,B]}
5    C  u0 {1,S} {3,S}
6    C  u0 {1,S}
7    C  u0 {3,S}
8    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 495,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {7,S}
4    C  u0 r0 {2,S} {8,D}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {1,S}
7    C  u0 r0 {3,S}
8    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 496,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {7,S}
4    C  u0 r0 {2,S} {8,[B,S,T]}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {1,S}
7    C  u0 r0 {3,S}
8    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 497,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S}
4    C  u0 {2,S} {7,[S,D,T,B]}
5    C  u0 {1,S} {3,S}
6    C  u0 {1,S}
7    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 498,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-7R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S}
4    C  u0 r0 {2,S} {7,D}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {1,S}
7    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 499,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-7R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S}
4    C  u0 r0 {2,S} {7,[B,S,T]}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {1,S}
7    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 500,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_4R!H-inRing",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,D}
4    C  u0 r1 {2,S}
5    C  u0 r0 {1,S} {3,D}
""",
    kinetics = None,
)

entry(
    index = 501,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,[S,D,T,B]}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 502,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {5,[S,D,T,B]} {6,[S,D,T,B]}
4    C   u0 r0 {2,S}
5    C   u0 {1,S} {3,[S,D,T,B]}
6    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 503,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,[S,D,T,B]} {6,[S,D,T,B]}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {3,[S,D,T,B]}
6    C  u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
7    C  u0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 504,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S} {6,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {3,S}
6    C  u0 {3,S} {7,D}
7    C  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 505,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S} {6,S} {8,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {3,S}
6    C  u0 {3,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 506,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S} {6,S} {8,S}
4    C  u0 r0 {2,S} {9,[S,D,T,B]}
5    C  u0 {1,S} {3,S}
6    C  u0 {3,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S}
9    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 507,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {6,S} {8,S}
4    C  u0 r0 {2,S} {9,D}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {3,S} {7,D}
7    C  u0 r0 {6,D}
8    C  u0 {3,S}
9    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 508,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {6,S} {8,S}
4    C  u0 r0 {2,S} {9,[B,S,T]}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {3,S} {7,D}
7    C  u0 r0 {6,D}
8    C  u0 {3,S}
9    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 509,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S} {6,S}
4    C  u0 r0 {2,S} {8,[S,D,T,B]}
5    C  u0 {1,S} {3,S}
6    C  u0 {3,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 510,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {6,S}
4    C  u0 r0 {2,S} {8,D}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {3,S} {7,D}
7    C  u0 r0 {6,D}
8    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 511,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {6,S}
4    C  u0 r0 {2,S} {8,[B,S,T]}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {3,S} {7,D}
7    C  u0 r0 {6,D}
8    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 512,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,[S,D,T,B]} {6,[S,D,T,B]}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {3,[S,D,T,B]}
6    C  u0 {3,[S,D,T,B]} {7,[B,S,T]}
7    C  u0 {6,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 513,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_3R!H-inRing",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 r1 {5,[S,D,T,B]} {6,[S,D,T,B]}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {3,[S,D,T,B]}
6    C  u0 {3,[S,D,T,B]} {7,[B,S,T]}
7    C  u0 {6,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 514,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-3R!H-inRing",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {6,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {3,S}
6    C  u0 {3,S} {7,T}
7    C  u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 515,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-3R!H-inRing_Ext-3R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {6,S} {8,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {3,S}
6    C  u0 {3,S} {7,T}
7    C  u0 {6,T}
8    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 516,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {6,S} {8,S}
4    C  u0 r0 {2,S} {9,[S,D,T,B]}
5    C  u0 {1,S} {3,S}
6    C  u0 {3,S} {7,T}
7    C  u0 {6,T}
8    C  u0 {3,S}
9    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 517,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {6,S} {8,S}
4    C  u0 r0 {2,S} {9,D}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {3,S} {7,T}
7    C  u0 r0 {6,T}
8    C  u0 {3,S}
9    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 518,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {6,S} {8,S}
4    C  u0 r0 {2,S} {9,[B,S,T]}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {3,S} {7,T}
7    C  u0 r0 {6,T}
8    C  u0 {3,S}
9    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 519,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-3R!H-inRing_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {6,S}
4    C  u0 r0 {2,S} {8,[S,D,T,B]}
5    C  u0 {1,S} {3,S}
6    C  u0 {3,S} {7,T}
7    C  u0 {6,T}
8    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 520,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-3R!H-inRing_Ext-4R!H-R_Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {6,S}
4    C  u0 r0 {2,S} {8,D}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {3,S} {7,T}
7    C  u0 r0 {6,T}
8    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 521,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-3R!H-inRing_Ext-4R!H-R_N-Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S} {6,S}
4    C  u0 r0 {2,S} {8,[B,S,T]}
5    C  u0 r0 {1,S} {3,S}
6    C  u0 r0 {3,S} {7,T}
7    C  u0 r0 {6,T}
8    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 522,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {5,S} {6,[S,D,T,B]} {7,[S,D,T,B]}
4    C   u0 r0 {2,S}
5    C   u0 {1,S} {3,S}
6    R!H ux {3,[S,D,T,B]}
7    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 523,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {5,S} {6,[S,D,T,B]} {7,[S,D,T,B]}
4    C   u0 r0 {2,S} {8,[S,D,T,B]}
5    C   u0 {1,S} {3,S}
6    R!H ux {3,[S,D,T,B]}
7    R!H ux {3,[S,D,T,B]}
8    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 524,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 r0 {5,S} {6,[S,D,T,B]} {7,[S,D,T,B]}
4    C   u0 r0 {2,S} {8,D}
5    C   u0 r0 {1,S} {3,S}
6    R!H ux {3,[S,D,T,B]}
7    R!H ux {3,[S,D,T,B]}
8    C   u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 525,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 r0 {5,S} {6,[S,D,T,B]} {7,[S,D,T,B]}
4    C   u0 r0 {2,S} {8,[B,S,T]}
5    C   u0 r0 {1,S} {3,S}
6    R!H ux {3,[S,D,T,B]}
7    R!H ux {3,[S,D,T,B]}
8    C   u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 526,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S} {6,S}
4    C  u0 r0 {2,S} {7,[S,D,T,B]}
5    C  u0 {1,S} {3,S}
6    C  u0 {3,S}
7    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 527,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-7R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 {5,S} {6,S}
4    C  u0 r0 {2,S} {7,D}
5    C  u0 {1,S} {3,S}
6    C  u0 {3,S}
7    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 528,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-7R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 {5,S} {6,S}
4    C  u0 r0 {2,S} {7,[B,S,T]}
5    C  u0 {1,S} {3,S}
6    C  u0 {3,S}
7    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 529,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {5,S}
4    C  u0 r0 {2,S} {6,[S,D,T,B]}
5    C  u0 {1,S} {3,S}
6    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 530,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-4R!H-R_Sp-6R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 {5,S}
4    C  u0 r0 {2,S} {6,D}
5    C  u0 {1,S} {3,S}
6    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 531,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-4R!H-R_N-Sp-6R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 {5,S}
4    C  u0 r0 {2,S} {6,[B,S,T]}
5    C  u0 {1,S} {3,S}
6    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 532,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_4R!H-inRing",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 r1 {2,S}
5    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 533,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_4R!H-inRing_Ext-5R!H-R_Int-6R!H-3R!H_Ext-4R!H-R_Sp-7R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {6,S}
4    C  u0 r1 {2,S} {7,D}
5    C  u0 {1,S} {6,D}
6    C  u0 {3,S} {5,D}
7    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 534,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_4R!H-inRing_Ext-5R!H-R_Int-6R!H-3R!H_Ext-4R!H-R_Sp-7R!H=4R!H_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {6,S}
4    C  u0 r1 {2,S} {7,D}
5    C  u0 r0 {1,S} {6,D}
6    C  u0 {3,S} {5,D}
7    C  u0 r1 {4,D} {8,S}
8    C  u0 r1 {7,S} {9,S}
9    C  u0 r1 {8,S}
""",
    kinetics = None,
)

entry(
    index = 535,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_4R!H-inRing_Ext-5R!H-R_Int-6R!H-3R!H_Ext-4R!H-R_Sp-7R!H=4R!H_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {6,S}
4    C  u0 r1 {2,S} {7,D}
5    C  u0 r0 {1,S} {6,D}
6    C  u0 {3,S} {5,D}
7    C  u0 r1 {4,D} {8,S}
8    C  u0 r1 {7,S} {9,[B,D,T]}
9    C  u0 r1 {8,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 536,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_4R!H-inRing_Ext-5R!H-R_Int-6R!H-3R!H_Ext-4R!H-R_N-Sp-7R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {6,S}
4    C  u0 r1 {2,S} {7,S}
5    C  u0 {1,S} {6,D}
6    C  u0 r0 {3,S} {5,D}
7    C  u0 r1 {4,S}
""",
    kinetics = None,
)

entry(
    index = 537,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing",
    group = 
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,CS,Cdd,N,O4dc,O4tc,S] u0 r0 {2,[D,T,B]} {5,[S,D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S]               u0 c0 {1,[D,T,B]} {4,[S,D,T,B]}
3 *1 R!H                                    u1
4    C                                      u0 r0 {2,[S,D,T,B]}
5    C                                      u0 {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 538,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 R!H u1
4    C   u0 r0 {2,S}
5    C   u0 {1,S} {6,D}
6    C   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 539,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_3R!H->S",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 S  u1
4    C  u0 r0 {2,S}
5    C  u0 r0 {1,S} {6,D}
6    C  u0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 540,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,D}
6    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 541,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {3,S} {8,D}
8    C  u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 542,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {3,S} {8,D}
8    C  u0 {7,D} {9,S}
9    C  u0 {8,S}
""",
    kinetics = None,
)

entry(
    index = 543,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {10,[S,D,T,B]}
4     C   u0 r0 {2,S}
5     C   u0 {1,S} {6,D}
6     C   u0 {5,D}
7     C   u0 {3,S} {8,D}
8     C   u0 {7,D} {9,S}
9     C   u0 {8,S}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 544,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {10,S}
4     C  u0 r0 {2,S}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D} {9,S}
9     C  u0 {8,S}
10    C  u0 {3,S} {11,[S,D,T,B]}
11    C  u0 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 545,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_Sp-11R!H=10R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {10,S}
4     C  u0 r0 {2,S}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D} {9,S}
9     C  u0 {8,S}
10    C  u0 {3,S} {11,D}
11    C  u0 {10,D}
""",
    kinetics = None,
)

entry(
    index = 546,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-3C-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {10,S} {12,S}
4     C  u0 r0 {2,S}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D} {9,S}
9     C  u0 {8,S}
10    C  u0 {3,S} {11,D}
11    C  u0 {10,D}
12    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 547,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-3C-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {10,S} {12,S}
4     C  u0 r0 {2,S} {13,[S,D,T,B]}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D} {9,S}
9     C  u0 {8,S}
10    C  u0 {3,S} {11,D}
11    C  u0 {10,D}
12    C  u0 {3,S}
13    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 548,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-3C-R_Ext-4R!H-R_Sp-13R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 {7,S} {10,S} {12,S}
4     C  u0 r0 {2,S} {13,D}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D} {9,S}
9     C  u0 {8,S}
10    C  u0 {3,S} {11,D}
11    C  u0 {10,D}
12    C  u0 {3,S}
13    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 549,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-3C-R_Ext-4R!H-R_N-Sp-13R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 {7,S} {10,S} {12,S}
4     C  u0 r0 {2,S} {13,[B,S,T]}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D} {9,S}
9     C  u0 {8,S}
10    C  u0 {3,S} {11,D}
11    C  u0 {10,D}
12    C  u0 {3,S}
13    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 550,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {10,S}
4     C  u0 r0 {2,S} {12,[S,D,T,B]}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D} {9,S}
9     C  u0 {8,S}
10    C  u0 {3,S} {11,D}
11    C  u0 {10,D}
12    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 551,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-4R!H-R_Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {7,S} {10,S}
4     C  u0 r0 {2,S} {12,D}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 r0 {3,S} {8,D}
8     C  u0 r0 {7,D} {9,S}
9     C  u0 r0 {8,S}
10    C  u0 r0 {3,S} {11,D}
11    C  u0 r0 {10,D}
12    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 552,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-4R!H-R_N-Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {7,S} {10,S}
4     C  u0 r0 {2,S} {12,[B,S,T]}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 r0 {3,S} {8,D}
8     C  u0 r0 {7,D} {9,S}
9     C  u0 r0 {8,S}
10    C  u0 r0 {3,S} {11,D}
11    C  u0 r0 {10,D}
12    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 553,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_N-Sp-11R!H=10R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {10,S}
4     C  u0 r0 {2,S}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D} {9,S}
9     C  u0 {8,S}
10    C  u0 {3,S} {11,T}
11    C  u0 {10,T}
""",
    kinetics = None,
)

entry(
    index = 554,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-3C-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {10,S} {12,S}
4     C  u0 r0 {2,S}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D} {9,S}
9     C  u0 {8,S}
10    C  u0 {3,S} {11,T}
11    C  u0 {10,T}
12    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 555,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-3C-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {10,S} {12,S}
4     C  u0 r0 {2,S} {13,[S,D,T,B]}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D} {9,S}
9     C  u0 {8,S}
10    C  u0 {3,S} {11,T}
11    C  u0 {10,T}
12    C  u0 {3,S}
13    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 556,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-3C-R_Ext-4R!H-R_Sp-13R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 {7,S} {10,S} {12,S}
4     C  u0 r0 {2,S} {13,D}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D} {9,S}
9     C  u0 {8,S}
10    C  u0 {3,S} {11,T}
11    C  u0 {10,T}
12    C  u0 {3,S}
13    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 557,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-3C-R_Ext-4R!H-R_N-Sp-13R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 {7,S} {10,S} {12,S}
4     C  u0 r0 {2,S} {13,[B,S,T]}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D} {9,S}
9     C  u0 {8,S}
10    C  u0 {3,S} {11,T}
11    C  u0 {10,T}
12    C  u0 {3,S}
13    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 558,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {10,S}
4     C  u0 r0 {2,S} {12,[S,D,T,B]}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D} {9,S}
9     C  u0 {8,S}
10    C  u0 {3,S} {11,T}
11    C  u0 {10,T}
12    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 559,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-4R!H-R_Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {7,S} {10,S}
4     C  u0 r0 {2,S} {12,D}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 r0 {3,S} {8,D}
8     C  u0 r0 {7,D} {9,S}
9     C  u0 r0 {8,S}
10    C  u0 r0 {3,S} {11,T}
11    C  u0 r0 {10,T}
12    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 560,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-4R!H-R_N-Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {7,S} {10,S}
4     C  u0 r0 {2,S} {12,[B,S,T]}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 r0 {3,S} {8,D}
8     C  u0 r0 {7,D} {9,S}
9     C  u0 r0 {8,S}
10    C  u0 r0 {3,S} {11,T}
11    C  u0 r0 {10,T}
12    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 561,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_3C-inRing",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 r1 {7,S} {10,S}
4     C  u0 r0 {2,S}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D} {9,S}
9     C  u0 {8,S}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 562,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_N-3C-inRing",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {10,[S,D,T,B]}
4     C   u0 r0 {2,S}
5     C   u0 {1,S} {6,D}
6     C   u0 {5,D}
7     C   u0 {3,S} {8,D}
8     C   u0 {7,D} {9,S}
9     C   u0 {8,S}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 563,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_N-3C-inRing_Ext-3C-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 r0 {2,S}
5     C   u0 {1,S} {6,D}
6     C   u0 {5,D}
7     C   u0 {3,S} {8,D}
8     C   u0 {7,D} {9,S}
9     C   u0 {8,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 564,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_N-3C-inRing_Ext-3C-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 r0 {2,S} {12,[S,D,T,B]}
5     C   u0 {1,S} {6,D}
6     C   u0 {5,D}
7     C   u0 {3,S} {8,D}
8     C   u0 {7,D} {9,S}
9     C   u0 {8,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
12    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 565,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_N-3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 r0 {2,S} {12,D}
5     C   u0 r0 {1,S} {6,D}
6     C   u0 r0 {5,D}
7     C   u0 r0 {3,S} {8,D}
8     C   u0 r0 {7,D} {9,S}
9     C   u0 r0 {8,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
12    C   u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 566,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_N-3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 r0 {2,S} {12,[B,S,T]}
5     C   u0 r0 {1,S} {6,D}
6     C   u0 r0 {5,D}
7     C   u0 r0 {3,S} {8,D}
8     C   u0 r0 {7,D} {9,S}
9     C   u0 r0 {8,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
12    C   u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 567,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_N-3C-inRing_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 r0 {7,S} {10,S}
4     C  u0 r0 {2,S} {11,[S,D,T,B]}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D} {9,S}
9     C  u0 {8,S}
10    C  u0 {3,S}
11    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 568,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_N-3C-inRing_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {7,S} {10,S}
4     C  u0 r0 {2,S} {11,D}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 r0 {3,S} {8,D}
8     C  u0 r0 {7,D} {9,S}
9     C  u0 r0 {8,S}
10    C  u0 r0 {3,S}
11    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 569,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_N-3C-inRing_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {7,S} {10,S}
4     C  u0 r0 {2,S} {11,[B,S,T]}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 r0 {3,S} {8,D}
8     C  u0 r0 {7,D} {9,S}
9     C  u0 r0 {8,S}
10    C  u0 r0 {3,S}
11    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 570,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S}
4     C  u0 r0 {2,S} {10,[S,D,T,B]}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D} {9,S}
9     C  u0 {8,S}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 571,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 {7,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D} {9,S}
9     C  u0 {8,S}
10    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 572,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 {7,S}
4     C  u0 r0 {2,S} {10,[B,S,T]}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D} {9,S}
9     C  u0 {8,S}
10    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 573,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-3C-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S}
5     C   u0 {1,S} {6,D}
6     C   u0 {5,D}
7     C   u0 {3,S} {8,D}
8     C   u0 {7,D}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 574,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-3C-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {12,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S} {10,S}
4     C  u0 r0 {2,S}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D}
9     C  u0 {3,S}
10    C  u0 {3,S} {11,S}
11    C  u0 {10,S}
12    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 575,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-3C-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {12,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S} {10,S}
4     C  u0 r0 {2,S} {13,[S,D,T,B]}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D}
9     C  u0 {3,S}
10    C  u0 {3,S} {11,S}
11    C  u0 {10,S}
12    C  u0 {1,S}
13    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 576,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-3C-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-13R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {12,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S} {10,S}
4     C  u0 r0 {2,S} {13,D}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D}
9     C  u0 r0 {3,S}
10    C  u0 {3,S} {11,S}
11    C  u0 r0 {10,S}
12    C  u0 {1,S}
13    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 577,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-3C-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-13R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {12,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S} {10,S}
4     C  u0 r0 {2,S} {13,[B,S,T]}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D}
9     C  u0 r0 {3,S}
10    C  u0 {3,S} {11,S}
11    C  u0 r0 {10,S}
12    C  u0 {1,S}
13    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 578,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-3C-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S} {11,[S,D,T,B]}
5     C   u0 {1,S} {6,D}
6     C   u0 {5,D}
7     C   u0 {3,S} {8,D}
8     C   u0 {7,D}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 579,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S} {11,D}
5     C   u0 r0 {1,S} {6,D}
6     C   u0 r0 {5,D}
7     C   u0 r0 {3,S} {8,D}
8     C   u0 r0 {7,D}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    C   u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 580,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S} {11,[B,S,T]}
5     C   u0 r0 {1,S} {6,D}
6     C   u0 r0 {5,D}
7     C   u0 r0 {3,S} {8,D}
8     C   u0 r0 {7,D}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    C   u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 581,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {11,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S}
4     C  u0 r0 {2,S}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D}
9     C  u0 {3,S} {10,S}
10    C  u0 {9,S}
11    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 582,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {11,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S}
4     C  u0 r0 {2,S} {12,[S,D,T,B]}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D}
9     C  u0 {3,S} {10,S}
10    C  u0 {9,S}
11    C  u0 {1,S}
12    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 583,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {11,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 r0 {7,S} {9,S}
4     C  u0 r0 {2,S} {12,D}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 r0 {3,S} {8,D}
8     C  u0 r0 {7,D}
9     C  u0 {3,S} {10,S}
10    C  u0 r0 {9,S}
11    C  u0 {1,S}
12    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 584,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {11,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 r0 {7,S} {9,S}
4     C  u0 r0 {2,S} {12,[B,S,T]}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 r0 {3,S} {8,D}
8     C  u0 r0 {7,D}
9     C  u0 {3,S} {10,S}
10    C  u0 r0 {9,S}
11    C  u0 {1,S}
12    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 585,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S} {9,[S,D,T,B]}
5    C  u0 {1,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {3,S} {8,D}
8    C  u0 {7,D}
9    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 586,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S} {9,D}
5    C  u0 r0 {1,S} {6,D}
6    C  u0 r0 {5,D}
7    C  u0 {3,S} {8,D}
8    C  u0 {7,D}
9    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 587,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S} {9,[B,S,T]}
5    C  u0 r0 {1,S} {6,D}
6    C  u0 r0 {5,D}
7    C  u0 {3,S} {8,D}
8    C  u0 {7,D}
9    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 588,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {3,S} {8,[B,S,T]}
8    C  u0 {7,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 589,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {3,S} {8,T}
8    C  u0 {7,T}
""",
    kinetics = None,
)

entry(
    index = 590,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {11,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S}
4     C  u0 r0 {2,S}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,T}
8     C  u0 {7,T}
9     C  u0 {3,S} {10,S}
10    C  u0 {9,S}
11    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 591,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3C-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {11,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S} {12,S}
4     C  u0 r0 {2,S}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,T}
8     C  u0 {7,T}
9     C  u0 {3,S} {10,S}
10    C  u0 {9,S}
11    C  u0 {1,S}
12    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 592,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3C-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {11,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S} {12,S}
4     C  u0 r0 {2,S} {13,[S,D,T,B]}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,T}
8     C  u0 {7,T}
9     C  u0 {3,S} {10,S}
10    C  u0 {9,S}
11    C  u0 {1,S}
12    C  u0 {3,S}
13    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 593,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3C-R_Ext-4R!H-R_Sp-13R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {11,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {7,S} {9,S} {12,S}
4     C  u0 r0 {2,S} {13,D}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 r0 {3,S} {8,T}
8     C  u0 r0 {7,T}
9     C  u0 r0 {3,S} {10,S}
10    C  u0 {9,S}
11    C  u0 r0 {1,S}
12    C  u0 {3,S}
13    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 594,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3C-R_Ext-4R!H-R_N-Sp-13R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {11,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {7,S} {9,S} {12,S}
4     C  u0 r0 {2,S} {13,[B,S,T]}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 r0 {3,S} {8,T}
8     C  u0 r0 {7,T}
9     C  u0 r0 {3,S} {10,S}
10    C  u0 {9,S}
11    C  u0 r0 {1,S}
12    C  u0 {3,S}
13    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 595,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {11,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S}
4     C  u0 r0 {2,S} {12,[S,D,T,B]}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,T}
8     C  u0 {7,T}
9     C  u0 {3,S} {10,S}
10    C  u0 {9,S}
11    C  u0 {1,S}
12    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 596,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {11,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {7,S} {9,S}
4     C  u0 r0 {2,S} {12,D}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 r0 {3,S} {8,T}
8     C  u0 r0 {7,T}
9     C  u0 r0 {3,S} {10,S}
10    C  u0 r0 {9,S}
11    C  u0 r0 {1,S}
12    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 597,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {11,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {7,S} {9,S}
4     C  u0 r0 {2,S} {12,[B,S,T]}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 r0 {3,S} {8,T}
8     C  u0 r0 {7,T}
9     C  u0 r0 {3,S} {10,S}
10    C  u0 r0 {9,S}
11    C  u0 r0 {1,S}
12    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 598,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S}
5     C   u0 {1,S} {6,D}
6     C   u0 {5,D}
7     C   u0 {3,S} {8,T}
8     C   u0 {7,T}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 599,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S} {11,[S,D,T,B]}
5     C   u0 {1,S} {6,D}
6     C   u0 {5,D}
7     C   u0 {3,S} {8,T}
8     C   u0 {7,T}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 600,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S} {11,D}
5     C   u0 r0 {1,S} {6,D}
6     C   u0 r0 {5,D}
7     C   u0 r0 {3,S} {8,T}
8     C   u0 r0 {7,T}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    C   u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 601,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S} {11,[B,S,T]}
5     C   u0 r0 {1,S} {6,D}
6     C   u0 r0 {5,D}
7     C   u0 r0 {3,S} {8,T}
8     C   u0 r0 {7,T}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    C   u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 602,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S} {9,[S,D,T,B]}
5    C  u0 {1,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {3,S} {8,T}
8    C  u0 {7,T}
9    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 603,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-4R!H-R_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {7,S}
4    C  u0 r0 {2,S} {9,D}
5    C  u0 r0 {1,S} {6,D}
6    C  u0 r0 {5,D}
7    C  u0 r0 {3,S} {8,T}
8    C  u0 r0 {7,T}
9    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 604,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {7,S}
4    C  u0 r0 {2,S} {9,[B,S,T]}
5    C  u0 r0 {1,S} {6,D}
6    C  u0 r0 {5,D}
7    C  u0 r0 {3,S} {8,T}
8    C  u0 r0 {7,T}
9    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 605,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {3,S} {8,S}
8    C  u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 606,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {7,S} {9,[S,D,T,B]}
4    C   u0 r0 {2,S}
5    C   u0 {1,S} {6,D}
6    C   u0 {5,D}
7    C   u0 {3,S} {8,S}
8    C   u0 {7,S}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 607,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S}
5     C   u0 {1,S} {6,D}
6     C   u0 {5,D}
7     C   u0 {3,S} {8,S}
8     C   u0 {7,S}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 608,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S}
5     C   u0 {1,S} {6,D}
6     C   u0 {5,D}
7     C   u0 {3,S} {8,S}
8     C   u0 {7,S}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 609,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S} {12,[S,D,T,B]}
5     C   u0 {1,S} {6,D}
6     C   u0 {5,D}
7     C   u0 {3,S} {8,S}
8     C   u0 {7,S}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    C   u0 {1,S}
12    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 610,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S} {12,D}
5     C   u0 {1,S} {6,D}
6     C   u0 {5,D}
7     C   u0 {3,S} {8,S}
8     C   u0 {7,S}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    C   u0 {1,S}
12    C   u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 611,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-12R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S} {12,[B,S,T]}
5     C   u0 {1,S} {6,D}
6     C   u0 {5,D}
7     C   u0 {3,S} {8,S}
8     C   u0 {7,S}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    C   u0 {1,S}
12    C   u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 612,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S} {11,[S,D,T,B]}
5     C   u0 {1,S} {6,D}
6     C   u0 {5,D}
7     C   u0 {3,S} {8,S}
8     C   u0 {7,S}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 613,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S} {11,D}
5     C   u0 r0 {1,S} {6,D}
6     C   u0 r0 {5,D}
7     C   u0 r0 {3,S} {8,S}
8     C   u0 r0 {7,S}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    C   u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 614,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S} {11,[B,S,T]}
5     C   u0 r0 {1,S} {6,D}
6     C   u0 r0 {5,D}
7     C   u0 r0 {3,S} {8,S}
8     C   u0 r0 {7,S}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    C   u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 615,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {10,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S}
4     C  u0 r0 {2,S}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,S}
8     C  u0 {7,S}
9     C  u0 {3,S}
10    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 616,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {10,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S}
4     C  u0 r0 {2,S} {11,[S,D,T,B]}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,S}
8     C  u0 {7,S}
9     C  u0 {3,S}
10    C  u0 {1,S}
11    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 617,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {10,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S}
4     C  u0 r0 {2,S} {11,D}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,S}
8     C  u0 {7,S}
9     C  u0 {3,S}
10    C  u0 {1,S}
11    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 618,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {10,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S}
4     C  u0 r0 {2,S} {11,[B,S,T]}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,S}
8     C  u0 {7,S}
9     C  u0 {3,S}
10    C  u0 {1,S}
11    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 619,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S}
4     C  u0 r0 {2,S} {10,[S,D,T,B]}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,S}
8     C  u0 {7,S}
9     C  u0 {3,S}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 620,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {7,S} {9,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 r0 {3,S} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {3,S}
10    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 621,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {7,S} {9,S}
4     C  u0 r0 {2,S} {10,[B,S,T]}
5     C  u0 r0 {1,S} {6,D}
6     C  u0 r0 {5,D}
7     C  u0 r0 {3,S} {8,S}
8     C  u0 r0 {7,S}
9     C  u0 r0 {3,S}
10    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 622,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {9,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {3,S} {8,S}
8    C  u0 {7,S}
9    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 623,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S}
4     C  u0 r0 {2,S} {10,[S,D,T,B]}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 624,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S}
10    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 625,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S} {9,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S}
4     C  u0 r0 {2,S} {10,[B,S,T]}
5     C  u0 {1,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S} {8,S}
8     C  u0 {7,S}
9     C  u0 {1,S}
10    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 626,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S} {9,[S,D,T,B]}
5    C  u0 {1,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {3,S} {8,S}
8    C  u0 {7,S}
9    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 627,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-4R!H-R_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {7,S}
4    C  u0 r0 {2,S} {9,D}
5    C  u0 r0 {1,S} {6,D}
6    C  u0 r0 {5,D}
7    C  u0 r0 {3,S} {8,S}
8    C  u0 r0 {7,S}
9    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 628,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {7,S}
4    C  u0 r0 {2,S} {9,[B,S,T]}
5    C  u0 r0 {1,S} {6,D}
6    C  u0 r0 {5,D}
7    C  u0 r0 {3,S} {8,S}
8    C  u0 r0 {7,S}
9    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 629,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,CS,Cdd,N,O4dc,O4tc,S] u0 r0 {2,[D,T,B]} {5,[S,D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S]               u0 c0 {1,[D,T,B]} {4,[S,D,T,B]}
3 *1 C                                      u1
4    C                                      u0 r0 {2,[S,D,T,B]}
5    C                                      u0 {1,[S,D,T,B]} {6,[B,S,T]}
6    C                                      u0 {5,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 630,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R",
    group = 
"""
1 *2 Cd                       u0 r0 {2,D} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,D} {4,[S,D,T,B]}
3 *1 C                        u1
4    C                        u0 r0 {2,[S,D,T,B]}
5    C                        u0 {1,S} {6,[B,S,T]}
6    C                        u0 {5,[B,S,T]} {7,[S,D,T,B]}
7    C                        u0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 631,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,S}
7    C  u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 632,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {8,[S,D,T,B]}
4    C   u0 r0 {2,S}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S} {7,S}
7    C   u0 {6,S}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 633,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,S}
7    C  u0 {6,S}
8    C  u0 {3,S} {9,[S,D,T,B]}
9    C  u0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 634,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,S}
7    C  u0 {6,S}
8    C  u0 {3,S} {9,D}
9    C  u0 {8,D}
""",
    kinetics = None,
)

entry(
    index = 635,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 r0 {2,S}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 636,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 r0 {2,S} {11,[S,D,T,B]}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
11    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 637,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 r0 {2,S} {11,D}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
11    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 638,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {12,[S,D,T,B]}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {10,S}
4     C   u0 r0 {2,S} {11,D}
5     C   u0 r0 {1,S} {6,S}
6     C   u0 r0 {5,S} {7,S}
7     C   u0 r0 {6,S}
8     C   u0 {3,S} {9,D}
9     C   u0 r0 {8,D}
10    C   u0 r0 {3,S}
11    C   u0 {4,D}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 639,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 r0 {2,S} {11,T}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
11    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 640,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {12,[S,D,T,B]}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {10,S}
4     C   u0 r0 {2,S} {11,T}
5     C   u0 r0 {1,S} {6,S}
6     C   u0 r0 {5,S} {7,S}
7     C   u0 r0 {6,S}
8     C   u0 {3,S} {9,D}
9     C   u0 r0 {8,D}
10    C   u0 r0 {3,S}
11    C   u0 {4,T}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 641,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S}
4     C   u0 r0 {2,S}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,S}
7     C   u0 {6,S}
8     C   u0 {3,S} {9,D}
9     C   u0 {8,D}
10    C   u0 {3,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 642,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S}
4     C  u0 r0 {2,S} {10,[S,D,T,B]}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 643,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 644,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S}
4     C   u0 r0 {2,S} {10,D}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,S}
7     C   u0 {6,S}
8     C   u0 {3,S} {9,D}
9     C   u0 {8,D}
10    C   u0 {4,D}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 645,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S}
4     C  u0 r0 {2,S} {10,T}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 646,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S}
4     C   u0 r0 {2,S} {10,T}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,S}
7     C   u0 {6,S}
8     C   u0 {3,S} {9,D}
9     C   u0 {8,D}
10    C   u0 {4,T}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 647,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S}
4     C   u0 r0 {2,S}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,S}
7     C   u0 {6,S}
8     C   u0 {3,S} {9,D}
9     C   u0 {8,D}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 648,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,S}
7    C  u0 {6,S}
8    C  u0 {3,S} {9,T}
9    C  u0 {8,T}
""",
    kinetics = None,
)

entry(
    index = 649,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 r0 {2,S}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 650,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 r0 {2,S} {11,[S,D,T,B]}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S}
11    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 651,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 r0 {2,S} {11,D}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S}
11    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 652,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {12,[S,D,T,B]}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {10,S}
4     C   u0 r0 {2,S} {11,D}
5     C   u0 r0 {1,S} {6,S}
6     C   u0 r0 {5,S} {7,S}
7     C   u0 r0 {6,S}
8     C   u0 {3,S} {9,T}
9     C   u0 r0 {8,T}
10    C   u0 r0 {3,S}
11    C   u0 {4,D}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 653,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 r0 {2,S} {11,T}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S}
11    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 654,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {12,[S,D,T,B]}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {10,S}
4     C   u0 r0 {2,S} {11,T}
5     C   u0 r0 {1,S} {6,S}
6     C   u0 r0 {5,S} {7,S}
7     C   u0 r0 {6,S}
8     C   u0 {3,S} {9,T}
9     C   u0 r0 {8,T}
10    C   u0 r0 {3,S}
11    C   u0 {4,T}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 655,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S}
4     C   u0 r0 {2,S}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,S}
7     C   u0 {6,S}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    C   u0 {3,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 656,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S}
4     C  u0 r0 {2,S} {10,[S,D,T,B]}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 657,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 658,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S}
4     C   u0 r0 {2,S} {10,D}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,S}
7     C   u0 {6,S}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    C   u0 {4,D}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 659,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S}
4     C  u0 r0 {2,S} {10,T}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,S}
7     C  u0 {6,S}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 660,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S}
4     C   u0 r0 {2,S} {10,T}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,S}
7     C   u0 {6,S}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    C   u0 {4,T}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 661,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S}
4     C   u0 r0 {2,S}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,S}
7     C   u0 {6,S}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 662,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {7,S} {8,[S,D,T,B]}
4    C   u0 r0 {2,S}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S} {7,S}
7    C   u0 {3,S} {6,S}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 663,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {7,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4    C   u0 r0 {2,S}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S} {7,S}
7    C   u0 {3,S} {6,S}
8    R!H ux {3,[S,D,T,B]}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 664,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 r0 {2,S} {10,[S,D,T,B]}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,S}
7     C   u0 {3,S} {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 665,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 r0 {2,S} {10,D}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,S}
7     C   u0 {3,S} {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 666,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 r0 {2,S} {10,D}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,S}
7     C   u0 {3,S} {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {4,D}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 667,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 r0 {2,S} {10,T}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,S}
7     C   u0 {3,S} {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 668,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 r0 {2,S} {10,T}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,S}
7     C   u0 {3,S} {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {4,T}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 669,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 r0 {2,S}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,S}
7     C   u0 {3,S} {6,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 670,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S} {8,S}
4    C  u0 r0 {2,S} {9,[S,D,T,B]}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,S}
7    C  u0 {3,S} {6,S}
8    C  u0 {3,S}
9    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 671,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-4R!H-R_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S} {8,S}
4    C  u0 r0 {2,S} {9,D}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,S}
7    C  u0 {3,S} {6,S}
8    C  u0 {3,S}
9    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 672,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-4R!H-R_Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {8,S}
4     C   u0 r0 {2,S} {9,D}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,S}
7     C   u0 {3,S} {6,S}
8     C   u0 {3,S}
9     C   u0 {4,D}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 673,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S} {8,S}
4    C  u0 r0 {2,S} {9,T}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,S}
7    C  u0 {3,S} {6,S}
8    C  u0 {3,S}
9    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 674,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {8,S}
4     C   u0 r0 {2,S} {9,T}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,S}
7     C   u0 {3,S} {6,S}
8     C   u0 {3,S}
9     C   u0 {4,T}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 675,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {9,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {7,S} {8,S}
4    C   u0 r0 {2,S}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S} {7,S}
7    C   u0 {3,S} {6,S}
8    C   u0 {3,S}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 676,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 r0 {2,S} {8,[S,D,T,B]}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,S}
7    C  u0 {6,S}
8    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 677,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-4R!H-R_Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 r0 {2,S} {8,D}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,S}
7    C  u0 {6,S}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 678,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {9,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1
4    C   u0 r0 {2,S} {8,D}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S} {7,S}
7    C   u0 {6,S}
8    C   u0 {4,D}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 679,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 r0 {2,S} {8,T}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,S}
7    C  u0 {6,S}
8    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 680,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {9,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1
4    C   u0 r0 {2,S} {8,T}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S} {7,S}
7    C   u0 {6,S}
8    C   u0 {4,T}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 681,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {8,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1
4    C   u0 r0 {2,S}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S} {7,S}
7    C   u0 {6,S}
8    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 682,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H",
    group = 
"""
1 *2 Cd                       u0 r0 {2,D} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,D} {4,[S,D,T,B]}
3 *1 C                        u1
4    C                        u0 r0 {2,[S,D,T,B]}
5    C                        u0 {1,S} {6,[B,S,T]}
6    C                        u0 {5,[B,S,T]} {7,[B,D,T]}
7    C                        u0 {6,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 683,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_2CbCbfCdCddCtNOS->Cdd",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cdd u0 c0 r0 {1,D} {4,[S,D,T,B]}
3 *1 C   u1 r0
4    C   u0 r0 {2,[S,D,T,B]}
5    C   u0 {1,S} {6,[B,S,T]}
6    C   u0 {5,[B,S,T]} {7,[B,D,T]}
7    C   u0 {6,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 684,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,D}
7    C  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 685,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {8,[S,D,T,B]}
4    C   u0 r0 {2,S}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S} {7,D}
7    C   u0 {6,D}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 686,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S} {9,[S,D,T,B]}
9    C  u0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 687,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S} {9,D}
9    C  u0 {8,D}
""",
    kinetics = None,
)

entry(
    index = 688,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 r0 {2,S}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 689,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 r0 {2,S} {11,[S,D,T,B]}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
11    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 690,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 r0 {2,S} {11,D}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
11    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 691,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {12,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S}
4     C   u0 r0 {2,S} {11,D}
5     C   u0 r0 {1,S} {6,S}
6     C   u0 r0 {5,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 {3,S} {9,D}
9     C   u0 r0 {8,D}
10    C   u0 r0 {3,S}
11    C   u0 {4,D}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 692,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 r0 {2,S} {11,T}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
11    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 693,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {12,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S}
4     C   u0 r0 {2,S} {11,T}
5     C   u0 r0 {1,S} {6,S}
6     C   u0 r0 {5,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 {3,S} {9,D}
9     C   u0 r0 {8,D}
10    C   u0 r0 {3,S}
11    C   u0 {4,T}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 694,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S}
4     C   u0 r0 {2,S}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,D}
9     C   u0 {8,D}
10    C   u0 {3,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 695,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S}
4     C  u0 r0 {2,S} {10,[S,D,T,B]}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 696,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 697,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S}
4     C   u0 r0 {2,S} {10,D}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,D}
9     C   u0 {8,D}
10    C   u0 {4,D}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 698,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S}
4     C  u0 r0 {2,S} {10,T}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 699,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S}
4     C   u0 r0 {2,S} {10,T}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,D}
9     C   u0 {8,D}
10    C   u0 {4,T}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 700,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S}
4     C   u0 r0 {2,S}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,D}
9     C   u0 {8,D}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 701,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S} {9,T}
9    C  u0 {8,T}
""",
    kinetics = None,
)

entry(
    index = 702,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 r0 {2,S}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 703,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 r0 {2,S} {11,[S,D,T,B]}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S}
11    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 704,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 r0 {2,S} {11,D}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S}
11    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 705,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {12,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S}
4     C   u0 r0 {2,S} {11,D}
5     C   u0 r0 {1,S} {6,S}
6     C   u0 r0 {5,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 {3,S} {9,T}
9     C   u0 r0 {8,T}
10    C   u0 r0 {3,S}
11    C   u0 {4,D}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 706,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 r0 {2,S} {11,T}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S}
11    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 707,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {12,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S}
4     C   u0 r0 {2,S} {11,T}
5     C   u0 r0 {1,S} {6,S}
6     C   u0 r0 {5,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 {3,S} {9,T}
9     C   u0 r0 {8,T}
10    C   u0 r0 {3,S}
11    C   u0 {4,T}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 708,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S}
4     C   u0 r0 {2,S}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    C   u0 {3,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 709,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S}
4     C  u0 r0 {2,S} {10,[S,D,T,B]}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 710,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 711,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S}
4     C   u0 r0 {2,S} {10,D}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    C   u0 {4,D}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 712,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {8,S}
4     C  u0 r0 {2,S} {10,T}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 713,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S}
4     C   u0 r0 {2,S} {10,T}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    C   u0 {4,T}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 714,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S}
4     C   u0 r0 {2,S}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 715,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {8,[S,D,T,B]} {9,[S,D,T,B]}
4    C   u0 r0 {2,S}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S} {7,D}
7    C   u0 {6,D}
8    R!H ux {3,[S,D,T,B]}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 716,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 r0 {2,S} {10,[S,D,T,B]}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,D}
7     C   u0 {6,D}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 717,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 r0 {2,S} {10,D}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,D}
7     C   u0 {6,D}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 718,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 r0 {2,S} {10,D}
5     C   u0 r0 {1,S} {6,S}
6     C   u0 r0 {5,S} {7,D}
7     C   u0 r0 {6,D}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {4,D}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 719,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 r0 {2,S} {10,T}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,D}
7     C   u0 {6,D}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 720,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 r0 {2,S} {10,T}
5     C   u0 r0 {1,S} {6,S}
6     C   u0 r0 {5,S} {7,D}
7     C   u0 r0 {6,D}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    C   u0 {4,T}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 721,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 r0 {2,S}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,D}
7     C   u0 {6,D}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 722,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 r0 {2,S} {9,[S,D,T,B]}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S}
9    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 723,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 r0 {2,S} {9,D}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S}
9    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 724,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S}
4     C   u0 r0 {2,S} {9,D}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S}
9     C   u0 {4,D}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 725,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 r0 {2,S} {9,T}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S}
9    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 726,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {8,S}
4     C   u0 r0 {2,S} {9,T}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S}
9     C   u0 {4,T}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 727,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {9,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {8,S}
4    C   u0 r0 {2,S}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S} {7,D}
7    C   u0 {6,D}
8    C   u0 {3,S}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 728,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 r0 {2,S} {8,[S,D,T,B]}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 729,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-4R!H-R_Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 r0 {2,S} {8,D}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 730,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {9,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1
4    C   u0 r0 {2,S} {8,D}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S} {7,D}
7    C   u0 {6,D}
8    C   u0 {4,D}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 731,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-4R!H-R_N-Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 r0 {2,S} {8,T}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 732,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {9,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1
4    C   u0 r0 {2,S} {8,T}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S} {7,D}
7    C   u0 {6,D}
8    C   u0 {4,T}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 733,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {8,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1
4    C   u0 r0 {2,S}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S} {7,D}
7    C   u0 {6,D}
8    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 734,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_2CbCbfCdCddCtNOS->Cdd",
    group = 
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,CS,Cdd,N,O4dc,O4tc,S] u0 r0 {2,[D,T,B]} {5,[S,D,T,B]}
2 *3 Cdd                                    u0 c0 {1,[D,T,B]} {4,[S,D,T,B]}
3 *1 C                                      u1
4    C                                      u0 r0 {2,[S,D,T,B]}
5    C                                      u0 r0 {1,[S,D,T,B]} {6,S}
6    C                                      u0 r0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 735,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd",
    group = 
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,CS,Cdd,N,O4dc,O4tc,S] u0 r0 {2,[D,T,B]} {5,[S,D,T,B]}
2 *3 [Cd,Ct]                                u0 c0 {1,[D,T,B]} {4,S}
3 *1 C                                      u1
4    C                                      u0 r0 {2,S}
5    C                                      u0 {1,[S,D,T,B]} {6,S}
6    C                                      u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 736,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {7,[S,D,T,B]}
4    C   u0 r0 {2,S}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S}
7    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 737,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {3,S} {8,[S,D,T,B]}
8    C  u0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 738,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {3,S} {8,D}
8    C  u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 739,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S} {9,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {3,S} {8,D}
8    C  u0 {7,D}
9    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 740,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S}
4     C  u0 r0 {2,S} {10,[S,D,T,B]}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D}
9     C  u0 {3,S}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 741,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D}
9     C  u0 {3,S}
10    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 742,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {9,S}
4     C   u0 r0 {2,S} {10,D}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S}
7     C   u0 {3,S} {8,D}
8     C   u0 r0 {7,D}
9     C   u0 r0 {3,S}
10    C   u0 {4,D}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 743,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S}
4     C  u0 r0 {2,S} {10,T}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S}
7     C  u0 {3,S} {8,D}
8     C  u0 {7,D}
9     C  u0 {3,S}
10    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 744,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {9,S}
4     C   u0 r0 {2,S} {10,T}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S}
7     C   u0 {3,S} {8,D}
8     C   u0 r0 {7,D}
9     C   u0 r0 {3,S}
10    C   u0 {4,T}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 745,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,S}
4     C   u0 r0 {2,S}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S}
7     C   u0 {3,S} {8,D}
8     C   u0 {7,D}
9     C   u0 {3,S}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 746,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S} {9,[S,D,T,B]}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {3,S} {8,D}
8    C  u0 {7,D}
9    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 747,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S} {9,D}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {3,S} {8,D}
8    C  u0 {7,D}
9    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 748,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R_Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S}
4     C   u0 r0 {2,S} {9,D}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S}
7     C   u0 {3,S} {8,D}
8     C   u0 {7,D}
9     C   u0 {4,D}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 749,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S} {9,T}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {3,S} {8,D}
8    C  u0 {7,D}
9    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 750,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S}
4     C   u0 r0 {2,S} {9,T}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S}
7     C   u0 {3,S} {8,D}
8     C   u0 {7,D}
9     C   u0 {4,T}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 751,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {9,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {7,S}
4    C   u0 r0 {2,S}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S}
7    C   u0 {3,S} {8,D}
8    C   u0 {7,D}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 752,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {3,S} {8,T}
8    C  u0 {7,T}
""",
    kinetics = None,
)

entry(
    index = 753,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S} {9,S}
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {3,S} {8,T}
8    C  u0 {7,T}
9    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 754,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S}
4     C  u0 r0 {2,S} {10,[S,D,T,B]}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S}
7     C  u0 {3,S} {8,T}
8     C  u0 {7,T}
9     C  u0 {3,S}
10    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 755,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S}
4     C  u0 r0 {2,S} {10,D}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S}
7     C  u0 {3,S} {8,T}
8     C  u0 {7,T}
9     C  u0 {3,S}
10    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 756,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {9,S}
4     C   u0 r0 {2,S} {10,D}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S}
7     C   u0 {3,S} {8,T}
8     C   u0 r0 {7,T}
9     C   u0 r0 {3,S}
10    C   u0 {4,D}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 757,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {5,S}
2  *3 Cd u0 c0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S}
4     C  u0 r0 {2,S} {10,T}
5     C  u0 {1,S} {6,S}
6     C  u0 {5,S}
7     C  u0 {3,S} {8,T}
8     C  u0 {7,T}
9     C  u0 {3,S}
10    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 758,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {9,S}
4     C   u0 r0 {2,S} {10,T}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S}
7     C   u0 {3,S} {8,T}
8     C   u0 r0 {7,T}
9     C   u0 r0 {3,S}
10    C   u0 {4,T}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 759,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,S}
4     C   u0 r0 {2,S}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S}
7     C   u0 {3,S} {8,T}
8     C   u0 {7,T}
9     C   u0 {3,S}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 760,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S} {9,[S,D,T,B]}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {3,S} {8,T}
8    C  u0 {7,T}
9    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 761,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-4R!H-R_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S} {9,D}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {3,S} {8,T}
8    C  u0 {7,T}
9    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 762,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-4R!H-R_Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S}
4     C   u0 r0 {2,S} {9,D}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S}
7     C   u0 {3,S} {8,T}
8     C   u0 {7,T}
9     C   u0 {4,D}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 763,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S} {9,T}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {3,S} {8,T}
8    C  u0 {7,T}
9    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 764,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D} {4,S}
3  *1 C   u1 {7,S}
4     C   u0 r0 {2,S} {9,T}
5     C   u0 {1,S} {6,S}
6     C   u0 {5,S}
7     C   u0 {3,S} {8,T}
8     C   u0 {7,T}
9     C   u0 {4,T}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 765,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {9,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {7,S}
4    C   u0 r0 {2,S}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S}
7    C   u0 {3,S} {8,T}
8    C   u0 {7,T}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 766,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {7,[S,D,T,B]} {8,[S,D,T,B]}
4    C   u0 r0 {2,S}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S}
7    R!H ux {3,[S,D,T,B]}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 767,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {7,[S,D,T,B]} {8,[S,D,T,B]}
4    C   u0 r0 {2,S} {9,[S,D,T,B]}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S}
7    R!H ux {3,[S,D,T,B]}
8    R!H ux {3,[S,D,T,B]}
9    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 768,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {7,[S,D,T,B]} {8,[S,D,T,B]}
4    C   u0 r0 {2,S} {9,D}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S}
7    R!H ux {3,[S,D,T,B]}
8    R!H ux {3,[S,D,T,B]}
9    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 769,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,[S,D,T,B]} {8,[S,D,T,B]}
4     C   u0 r0 {2,S} {9,D}
5     C   u0 r0 {1,S} {6,S}
6     C   u0 r0 {5,S}
7     R!H ux {3,[S,D,T,B]}
8     R!H ux {3,[S,D,T,B]}
9     C   u0 {4,D}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 770,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {7,[S,D,T,B]} {8,[S,D,T,B]}
4    C   u0 r0 {2,S} {9,T}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S}
7    R!H ux {3,[S,D,T,B]}
8    R!H ux {3,[S,D,T,B]}
9    C   u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 771,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {5,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,[S,D,T,B]} {8,[S,D,T,B]}
4     C   u0 r0 {2,S} {9,T}
5     C   u0 r0 {1,S} {6,S}
6     C   u0 r0 {5,S}
7     R!H ux {3,[S,D,T,B]}
8     R!H ux {3,[S,D,T,B]}
9     C   u0 {4,T}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 772,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {9,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {7,[S,D,T,B]} {8,[S,D,T,B]}
4    C   u0 r0 {2,S}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S}
7    R!H ux {3,[S,D,T,B]}
8    R!H ux {3,[S,D,T,B]}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 773,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S} {8,[S,D,T,B]}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {3,S}
8    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 774,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S} {8,D}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {3,S}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 775,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {9,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {7,S}
4    C   u0 r0 {2,S} {8,D}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S}
7    C   u0 {3,S}
8    C   u0 {4,D}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 776,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 r0 {2,S} {8,T}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {3,S}
8    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 777,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {9,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {7,S}
4    C   u0 r0 {2,S} {8,T}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S}
7    C   u0 {3,S}
8    C   u0 {4,T}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 778,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {8,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1 {7,S}
4    C   u0 r0 {2,S}
5    C   u0 {1,S} {6,S}
6    C   u0 {5,S}
7    C   u0 {3,S}
8    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 779,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct",
    group = 
"""
1 *2 Ct      u0 r0 {2,[D,T,B]} {5,[S,D,T,B]}
2 *3 [Cd,Ct] u0 c0 {1,[D,T,B]} {4,S}
3 *1 C       u1
4    C       u0 r0 {2,S}
5    C       u0 {1,[S,D,T,B]} {6,S}
6    C       u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 780,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct",
    group = 
"""
1 *2 [Cdd,Cd] u0 r0 {2,D} {5,[S,D,T,B]}
2 *3 Cd       u0 c0 {1,D} {4,S}
3 *1 C        u1
4    C        u0 r0 {2,S}
5    C        u0 {1,[S,D,T,B]} {6,S}
6    C        u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 781,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct_Ext-1CdCdd-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {7,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 782,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct_Ext-1CdCdd-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {7,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 r0 {2,S} {8,[S,D,T,B]}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {1,S}
8    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 783,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct_Ext-1CdCdd-R_Ext-4R!H-R_Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {7,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0
4    C  u0 r0 {2,S} {8,D}
5    C  u0 r0 {1,S} {6,S}
6    C  u0 r0 {5,S}
7    C  u0 {1,S}
8    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 784,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct_Ext-1CdCdd-R_Ext-4R!H-R_N-Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {7,S}
2 *3 Cd u0 c0 r0 {1,D} {4,S}
3 *1 C  u1 r0
4    C  u0 r0 {2,S} {8,[B,S,T]}
5    C  u0 r0 {1,S} {6,S}
6    C  u0 r0 {5,S}
7    C  u0 {1,S}
8    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 785,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct_1CdCdd->Cdd",
    group = 
"""
1 *2 Cdd u0 r0 {2,D} {5,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D} {4,S}
3 *1 C   u1
4    C   u0 r0 {2,S}
5    C   u0 {1,[S,D,T,B]} {6,S}
6    C   u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 786,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct_N-1CdCdd->Cdd",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 r0 {2,S}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 787,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct_N-1CdCdd->Cdd_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 r0 {2,S} {7,[S,D,T,B]}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 788,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct_N-1CdCdd->Cdd_Ext-4R!H-R_Sp-7R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 r0 {2,S} {7,D}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
7    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 789,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct_N-1CdCdd->Cdd_Ext-4R!H-R_N-Sp-7R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 r0 {2,S} {7,[B,S,T]}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
7    C  u0 r0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 790,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_2CbCbfCdCddCtNOS->Cdd",
    group = 
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,CS,Cdd,N,O4dc,O4tc,S] u0 r0 {2,[D,T,B]}
2 *3 Cdd                                    u0 c0 r0 {1,[D,T,B]} {4,[S,D,T,B]}
3 *1 C                                      u1 r0
4    C                                      u0 r0 {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 791,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_N-2CbCbfCdCddCtNOS->Cdd",
    group = 
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,CS,Cdd,N,O4dc,O4tc,S] u0 r0 {2,[D,T,B]}
2 *3 [Cd,Ct]                                u0 c0 {1,[D,T,B]} {4,S}
3 *1 C                                      u1
4    C                                      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 792,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_N-2CbCbfCdCddCtNOS->Cdd_1COCSCbCbfCdCddCtNO4dcO4tcS->Cd",
    group = 
"""
1 *2 Cd      u0 r0 {2,[D,T,B]}
2 *3 [Cd,Ct] u0 c0 {1,[D,T,B]} {4,S}
3 *1 C       u1
4    C       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 793,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_N-2CbCbfCdCddCtNOS->Cdd_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cd",
    group = 
"""
1 *2 Ct      u0 r0 {2,[D,T,B]}
2 *3 [Cd,Ct] u0 c0 {1,[D,T,B]} {4,S}
3 *1 C       u1
4    C       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 794,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R",
    group = 
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,CS,Cdd,N,O4dc,O4tc,S] u0 r0 {2,[D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S]               u0 c0 {1,[D,T,B]}
3 *1 R!H                                    u1 {4,[S,D,T,B]}
4    R!H                                    u0 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 795,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {4,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 R!H u1 {4,[S,D,T,B]}
4    C   u0 {1,S} {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 796,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {4,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S} {5,[S,D,T,B]}
4    C   u0 {1,S} {3,S}
5    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 797,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {4,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {1,S} {3,S}
5    C  u0 {3,S} {6,[S,D,T,B]}
6    C  u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 798,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {4,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {1,S} {3,S}
5    C  u0 {3,S} {6,S}
6    C  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 799,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_3R!H-inRing",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {4,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r1 {4,S} {5,S}
4    C  u0 {1,S} {3,S}
5    C  u0 {3,S} {6,S}
6    C  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 800,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_N-3R!H-inRing",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {4,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r0 {4,S} {5,S}
4    C  u0 {1,S} {3,S}
5    C  u0 {3,S} {6,S}
6    C  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 801,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {4,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {1,S} {3,S}
5    C  u0 {3,S} {6,[B,D,T]}
6    C  u0 {5,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 802,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-6R!H=5R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {4,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {1,S} {3,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 803,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-6R!H=5R!H_Ext-3R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {4,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S} {7,S}
4    C  u0 {1,S} {3,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 804,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-6R!H=5R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {4,S} {8,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S} {7,S}
4    C  u0 {1,S} {3,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {3,S}
8    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 805,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-6R!H=5R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {4,S} {8,S}
2 *3 Cd  u0 c0 r0 {1,D}
3 *1 C   u1 {4,S} {5,S} {7,S}
4    C   u0 {1,S} {3,S}
5    C   u0 {3,S} {6,D}
6    C   u0 {5,D}
7    C   u0 {3,S}
8    C   u0 r0 {1,S} {9,[S,D,T,B]}
9    R!H ux {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 806,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {4,S} {7,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {1,S} {3,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 807,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {4,S} {7,S}
2 *3 Cd  u0 c0 r0 {1,D}
3 *1 C   u1 r0 {4,S} {5,S}
4    C   u0 r0 {1,S} {3,S}
5    C   u0 r0 {3,S} {6,D}
6    C   u0 r0 {5,D}
7    C   u0 r0 {1,S} {8,[S,D,T,B]}
8    R!H ux {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 808,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-6R!H=5R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {4,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {1,S} {3,S}
5    C  u0 {3,S} {6,T}
6    C  u0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 809,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {4,S} {7,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {1,S} {3,S}
5    C  u0 {3,S} {6,T}
6    C  u0 {5,T}
7    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 810,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {4,S} {7,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {1,S} {3,S}
5    C  u0 {3,S} {6,T}
6    C  u0 {5,T}
7    C  u0 {1,S} {8,D}
8    C  u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 811,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {4,S} {7,S}
2 *3 Cd  u0 c0 r0 {1,D}
3 *1 C   u1 {4,S} {5,S} {9,[S,D,T,B]}
4    C   u0 {1,S} {3,S}
5    C   u0 {3,S} {6,T}
6    C   u0 {5,T}
7    C   u0 {1,S} {8,D}
8    C   u0 r0 {7,D}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 812,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {4,S} {7,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S} {5,S} {8,[S,D,T,B]}
4    C   u0 {1,S} {3,S}
5    C   u0 {3,S} {6,T}
6    C   u0 {5,T}
7    C   u0 {1,S}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 813,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-6R!H=5R!H_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {4,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S} {5,S} {7,[S,D,T,B]}
4    C   u0 {1,S} {3,S}
5    C   u0 {3,S} {6,T}
6    C   u0 {5,T}
7    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 814,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {4,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
4    C   u0 {1,S} {3,S}
5    R!H ux {3,[S,D,T,B]}
6    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 815,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {4,S} {7,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
4    C   u0 {1,S} {3,S}
5    R!H ux {3,[S,D,T,B]}
6    R!H ux {3,[S,D,T,B]}
7    C   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 816,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {4,S} {7,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 r0 {4,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
4    C   u0 r0 {1,S} {3,S}
5    R!H ux {3,[S,D,T,B]}
6    R!H ux {3,[S,D,T,B]}
7    C   u0 r0 {1,S} {8,[S,D,T,B]}
8    R!H ux {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 817,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {4,S} {6,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {1,S} {3,S}
5    C  u0 {3,S}
6    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 818,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {4,S} {6,S}
2 *3 Cd  u0 c0 r0 {1,D}
3 *1 C   u1 {4,S} {5,S}
4    C   u0 {1,S} {3,S}
5    C   u0 {3,S}
6    C   u0 r0 {1,S} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 819,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {4,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 R!H u1 {4,[S,D,T,B]}
4    C   u0 {1,S} {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 820,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-5R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {4,S}
2 *3 Cd  u0 c0 r0 {1,D}
3 *1 C   u1 {4,S}
4    C   u0 {1,S} {3,S} {5,[S,D,T,B]}
5    C   u0 r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 821,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {4,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 R!H u1 {4,[S,D,T,B]}
4    C   u0 {1,S} {3,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]}
6    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 822,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {4,S} {5,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {1,S} {3,S}
5    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 823,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-5R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {4,S} {5,S}
2 *3 Cd  u0 c0 r0 {1,D}
3 *1 C   u1 {4,S}
4    C   u0 {1,S} {3,S}
5    C   u0 r0 {1,S} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 824,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H",
    group = 
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,CS,Cdd,N,O4dc,O4tc,S] u0 r0 {2,[D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S]               u0 c0 {1,[D,T,B]}
3 *1 C                                      u1 {4,D}
4    R!H                                    u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 825,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd",
    group = 
"""
1 *2 Cdd u0 r0 {2,D}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,D}
4    C   u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 826,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Ext-1Cdd-R",
    group = 
"""
1 *2 Cdd u0 r0 {2,D} {6,[S,D,T,B]}
2 *3 Cd  u0 c0 r0 {1,D}
3 *1 C   u1 r0 {4,D}
4    C   u0 r0 {3,D} {5,[S,D,T,B]}
5    C   u0 r0 {4,[S,D,T,B]}
6    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 827,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-3R!H-R",
    group = 
"""
1 *2 Cdd u0 r0 {2,D}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,D} {5,[S,D,T,B]}
4    C   u0 {3,D}
5    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 828,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd",
    group = 
"""
1 *2 [Ct,CS,CO,Cd]            u0 r0 {2,[D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 C                        u1 {4,D}
4    R!H                      u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 829,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R",
    group = 
"""
1 *2 [Ct,CS,CO,Cd]            u0 r0 {2,[D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 C                        u1 {4,D}
4    R!H                      u0 {3,D}
5    C                        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 830,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R",
    group = 
"""
1 *2 [Ct,CS,CO,Cd]            u0 r0 {2,[D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 C                        u1 {4,D}
4    R!H                      u0 {3,D}
5    C                        u0 {1,S} {6,[S,D,T,B]}
6    C                        u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 831,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    group = 
"""
1 *2 [Ct,CS,CO,Cd]            u0 r0 {2,[D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 C                        u1 {4,D}
4    C                        u0 {3,D}
5    C                        u0 {1,S} {6,S}
6    C                        u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 832,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-4R!H-R",
    group = 
"""
1 *2 [Ct,CS,CO,Cd]            u0 r0 {2,[D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 r0 {1,[D,T,B]}
3 *1 C                        u1 r0 {4,D}
4    C                        u0 r0 {3,D} {7,[S,D,T,B]}
5    C                        u0 r0 {1,S} {6,S}
6    C                        u0 r0 {5,S}
7    R!H                      ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 833,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D}
3 *1 C  u1 r0 {4,D}
4    C  u0 r0 {3,D} {6,S}
5    C  u0 r0 {1,S} {6,S}
6    C  u0 r0 {4,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 834,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-1COCSCdCt-R",
    group = 
"""
1 *2 [Ct,CS,CO,Cd]            u0 r0 {2,[D,T,B]} {5,S} {7,[S,D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 C                        u1 {4,D}
4    C                        u0 {3,D}
5    C                        u0 {1,S} {6,S}
6    C                        u0 {5,S}
7    R!H                      ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 835,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_Sp-6R!H-5R!H_1COCSCdCt->Cd",
    group = 
"""
1 *2 Cd                       u0 r0 {2,[D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 C                        u1 {4,D}
4    C                        u0 {3,D}
5    C                        u0 {1,S} {6,S}
6    C                        u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 836,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_Sp-6R!H-5R!H_N-1COCSCdCt->Cd",
    group = 
"""
1 *2 Ct u0 r0 {2,T} {5,S}
2 *3 Ct u0 c0 {1,T}
3 *1 C  u1 {4,D}
4    C  u0 {3,D}
5    C  u0 {1,S} {6,S}
6    C  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 837,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_Sp-6R!H-5R!H_N-1COCSCdCt->Cd_Int-5R!H-4R!H",
    group = 
"""
1 *2 Ct u0 r0 {2,T} {5,S}
2 *3 Ct u0 c0 r0 {1,T}
3 *1 C  u1 r0 {4,D}
4    C  u0 r0 {3,D} {5,[S,D,T,B]}
5    C  u0 r0 {1,S} {4,[S,D,T,B]} {6,S}
6    C  u0 r0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 838,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    group = 
"""
1 *2 [Ct,CS,CO,Cd]            u0 r0 {2,[D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 C                        u1 {4,D}
4    R!H                      u0 {3,D}
5    C                        u0 {1,S} {6,[B,D,T]}
6    C                        u0 {5,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 839,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Int-6R!H-3R!H",
    group = 
"""
1 *2 [Ct,CS,CO,Cd]            u0 r0 {2,[D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 r0 {1,[D,T,B]}
3 *1 C                        u1 r0 {4,D} {6,[S,D,T,B]}
4    R!H                      u0 r0 {3,D}
5    C                        u0 {1,S} {6,[B,D,T]}
6    C                        u0 {3,[S,D,T,B]} {5,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 840,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_1COCSCdCt->Ct",
    group = 
"""
1 *2 Ct u0 r0 {2,T} {5,S}
2 *3 Ct u0 c0 {1,T}
3 *1 C  u1 {4,D}
4    C  u0 {3,D}
5    C  u0 {1,S} {6,[B,D,T]}
6    C  u0 {5,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 841,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_1COCSCdCt->Ct_Ext-4R!H-R",
    group = 
"""
1 *2 Ct  u0 r0 {2,T} {5,S}
2 *3 Ct  u0 c0 r0 {1,T}
3 *1 C   u1 r0 {4,D}
4    C   u0 r0 {3,D} {7,[S,D,T,B]}
5    C   u0 {1,S} {6,[B,D,T]}
6    C   u0 {5,[B,D,T]}
7    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 842,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-1COCSCdCt->Ct",
    group = 
"""
1 *2 [Cd,CO]                  u0 r0 {2,D} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,D}
3 *1 C                        u1 {4,D}
4    R!H                      u0 {3,D}
5    C                        u0 {1,S} {6,[B,D,T]}
6    C                        u0 {5,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 843,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-1COCSCdCt->Ct_Ext-3R!H-R",
    group = 
"""
1 *2 [Cd,CO]                  u0 r0 {2,D} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,D}
3 *1 C                        u1 {4,D} {7,S}
4    R!H                      u0 {3,D}
5    C                        u0 {1,S} {6,D}
6    C                        u0 {5,D}
7    C                        u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 844,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-1COCSCdCt->Ct_Ext-3R!H-R_1COCd->Cd",
    group = 
"""
1 *2 Cd                       u0 r0 {2,D} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,D}
3 *1 C                        u1 {4,D} {7,S}
4    R!H                      u0 {3,D}
5    C                        u0 r0 {1,S} {6,D}
6    C                        u0 r0 {5,D}
7    C                        u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 845,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-1COCSCdCt->Ct_Ext-3R!H-R_N-1COCd->Cd",
    group = 
"""
1 *2 CO                       u0 r0 {2,D} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,D}
3 *1 C                        u1 {4,D} {7,S}
4    R!H                      u0 {3,D}
5    C                        u0 r0 {1,S} {6,D}
6    C                        u0 r0 {5,D}
7    C                        u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 846,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-4R!H-R",
    group = 
"""
1 *2 [Ct,CS,CO,Cd]            u0 r0 {2,[D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 C                        u1 {4,D}
4    C                        u0 {3,D} {6,S}
5    C                        u0 {1,S}
6    C                        u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 847,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-4R!H-R_1COCSCdCt->Cd",
    group = 
"""
1 *2 Cd                       u0 r0 {2,[D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 r0 {1,[D,T,B]}
3 *1 C                        u1 r0 {4,D}
4    C                        u0 r0 {3,D} {6,S}
5    C                        u0 {1,S}
6    C                        u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 848,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-4R!H-R_N-1COCSCdCt->Cd",
    group = 
"""
1 *2 Ct                       u0 r0 {2,[D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 r0 {1,[D,T,B]}
3 *1 C                        u1 r0 {4,D}
4    C                        u0 r0 {3,D} {6,S}
5    C                        u0 {1,S}
6    C                        u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 849,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-3R!H-R",
    group = 
"""
1 *2 [Ct,CS,CO,Cd]            u0 r0 {2,[D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 C                        u1 {4,D} {6,S}
4    C                        u0 {3,D}
5    C                        u0 {1,S}
6    C                        u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 850,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-3R!H-R_Ext-6R!H-R",
    group = 
"""
1 *2 [Ct,CS,CO,Cd]            u0 r0 {2,[D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 r0 {1,[D,T,B]}
3 *1 C                        u1 r0 {4,D} {6,S}
4    C                        u0 r0 {3,D}
5    C                        u0 {1,S}
6    C                        u0 r0 {3,S} {7,[S,D,T,B]}
7    R!H                      ux {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 851,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-3R!H-R_1COCSCdCt->Cd",
    group = 
"""
1 *2 Cd                       u0 r0 {2,[D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 C                        u1 {4,D} {6,S}
4    C                        u0 {3,D}
5    C                        u0 {1,S}
6    C                        u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 852,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-3R!H-R_N-1COCSCdCt->Cd",
    group = 
"""
1 *2 Ct                       u0 r0 {2,[D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 C                        u1 {4,D} {6,S}
4    C                        u0 {3,D}
5    C                        u0 {1,S}
6    C                        u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 853,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_1COCSCdCt->Ct",
    group = 
"""
1 *2 Ct                       u0 r0 {2,[D,T,B]} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,[D,T,B]}
3 *1 C                        u1 {4,D}
4    C                        u0 {3,D}
5    C                        u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 854,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_N-1COCSCdCt->Ct",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D}
3 *1 C  u1 r0 {4,D}
4    C  u0 r0 {3,D}
5    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 855,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H",
    group = 
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,CS,Cdd,N,O4dc,O4tc,S] u0 r0 {2,[D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S]               u0 c0 {1,[D,T,B]}
3 *1 C                                      u1 {4,[B,S]}
4    C                                      u0 {3,[B,S]}
""",
    kinetics = None,
)

entry(
    index = 856,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R",
    group = 
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,CS,Cdd,N,O4dc,O4tc,S] u0 r0 {2,[D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S]               u0 c0 {1,[D,T,B]}
3 *1 C                                      u1 {4,[B,S]} {5,[S,D,T,B]}
4    C                                      u0 {3,[B,S]}
5    C                                      u0 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 857,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 858,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D} {7,S}
7    C  u0 {1,S} {6,S}
""",
    kinetics = None,
)

entry(
    index = 859,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {3,S} {8,[S,D,T,B]}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D} {7,S}
7    C  u0 {1,S} {6,S}
8    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 860,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {3,S} {8,D}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D} {7,S}
7    C  u0 {1,S} {6,S}
8    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 861,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-3R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S} {9,S}
4    C  u0 {3,S} {8,D}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D} {7,S}
7    C  u0 {1,S} {6,S}
8    C  u0 {4,D}
9    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 862,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {7,S} {10,S}
2  *3 Cd u0 c0 {1,D}
3  *1 C  u1 {4,S} {5,S} {9,S}
4     C  u0 {3,S} {8,D}
5     C  u0 {3,S} {6,D}
6     C  u0 {5,D} {7,S}
7     C  u0 {1,S} {6,S}
8     C  u0 {4,D}
9     C  u0 {3,S}
10    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 863,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {7,S} {10,S}
2  *3 Cd  u0 c0 {1,D}
3  *1 C   u1 {4,S} {5,S} {9,S}
4     C   u0 {3,S} {8,D}
5     C   u0 {3,S} {6,D}
6     C   u0 {5,D} {7,S}
7     C   u0 {1,S} {6,S}
8     C   u0 {4,D}
9     C   u0 {3,S}
10    C   u0 r0 {1,S} {11,[S,D,T,B]}
11    R!H ux {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 864,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S} {9,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {3,S} {8,D}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D} {7,S}
7    C  u0 {1,S} {6,S}
8    C  u0 {4,D}
9    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 865,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {7,S} {9,S}
2  *3 Cd  u0 c0 r0 {1,D}
3  *1 C   u1 r0 {4,S} {5,S}
4     C   u0 r0 {3,S} {8,D}
5     C   u0 r0 {3,S} {6,D}
6     C   u0 r0 {5,D} {7,S}
7     C   u0 r0 {1,S} {6,S}
8     C   u0 r0 {4,D}
9     C   u0 r0 {1,S} {10,[S,D,T,B]}
10    R!H ux {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 866,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {3,S} {8,T}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D} {7,S}
7    C  u0 {1,S} {6,S}
8    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 867,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S} {9,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {3,S} {8,T}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D} {7,S}
7    C  u0 {1,S} {6,S}
8    C  u0 {4,T}
9    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 868,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {7,S} {9,S}
2  *3 Cd u0 c0 {1,D}
3  *1 C  u1 {4,S} {5,S}
4     C  u0 {3,S} {8,T}
5     C  u0 {3,S} {6,D}
6     C  u0 {5,D} {7,S}
7     C  u0 {1,S} {6,S}
8     C  u0 {4,T}
9     C  u0 {1,S} {10,D}
10    C  u0 {9,D}
""",
    kinetics = None,
)

entry(
    index = 869,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {7,S} {9,S}
2  *3 Cd  u0 c0 {1,D}
3  *1 C   u1 {4,S} {5,S} {11,[S,D,T,B]}
4     C   u0 {3,S} {8,T}
5     C   u0 {3,S} {6,D}
6     C   u0 {5,D} {7,S}
7     C   u0 {1,S} {6,S}
8     C   u0 {4,T}
9     C   u0 {1,S} {10,D}
10    C   u0 r0 {9,D}
11    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 870,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {7,S} {9,S}
2  *3 Cd  u0 c0 {1,D}
3  *1 C   u1 {4,S} {5,S} {10,[S,D,T,B]}
4     C   u0 {3,S} {8,T}
5     C   u0 {3,S} {6,D}
6     C   u0 {5,D} {7,S}
7     C   u0 {1,S} {6,S}
8     C   u0 {4,T}
9     C   u0 {1,S}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 871,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {7,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S} {5,S} {9,[S,D,T,B]}
4    C   u0 {3,S} {8,T}
5    C   u0 {3,S} {6,D}
6    C   u0 {5,D} {7,S}
7    C   u0 {1,S} {6,S}
8    C   u0 {4,T}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 872,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_3R!H-inRing",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r1 {4,S} {5,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D} {7,S}
7    C  u0 {1,S} {6,S}
""",
    kinetics = None,
)

entry(
    index = 873,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_N-3R!H-inRing",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r0 {4,S} {5,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D} {7,S}
7    C  u0 {1,S} {6,S}
""",
    kinetics = None,
)

entry(
    index = 874,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_N-3R!H-inRing_Ext-3R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r0 {4,S} {5,S} {8,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D} {7,S}
7    C  u0 {1,S} {6,S}
8    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 875,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S} {9,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r0 {4,S} {5,S} {8,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D} {7,S}
7    C  u0 {1,S} {6,S}
8    C  u0 {3,S}
9    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 876,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {7,S} {9,S}
2  *3 Cd  u0 c0 r0 {1,D}
3  *1 C   u1 r0 {4,S} {5,S} {8,S}
4     C   u0 r0 {3,S}
5     C   u0 r0 {3,S} {6,D}
6     C   u0 r0 {5,D} {7,S}
7     C   u0 r0 {1,S} {6,S}
8     C   u0 {3,S}
9     C   u0 r0 {1,S} {10,[S,D,T,B]}
10    R!H ux {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 877,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_N-3R!H-inRing_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S} {8,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r0 {4,S} {5,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D} {7,S}
7    C  u0 {1,S} {6,S}
8    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 878,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_N-3R!H-inRing_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {7,S} {8,S}
2 *3 Cd  u0 c0 r0 {1,D}
3 *1 C   u1 r0 {4,S} {5,S}
4    C   u0 r0 {3,S}
5    C   u0 r0 {3,S} {6,D}
6    C   u0 r0 {5,D} {7,S}
7    C   u0 r0 {1,S} {6,S}
8    C   u0 r0 {1,S} {9,[S,D,T,B]}
9    R!H ux {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 879,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,[S,D,T,B]}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {1,[S,D,T,B]} {5,D}
""",
    kinetics = None,
)

entry(
    index = 880,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S} {7,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 881,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {8,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S} {7,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {3,S}
8    C  u0 {1,S} {9,[S,D,T,B]}
9    C  u0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 882,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-4R!H-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S}
2  *3 Cd u0 c0 {1,D}
3  *1 C  u1 {4,S} {5,S} {7,S}
4     C  u0 {3,S} {10,S}
5     C  u0 {3,S} {6,D}
6     C  u0 {5,D}
7     C  u0 {3,S}
8     C  u0 {1,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 883,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S} {11,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D}
3  *1 C   u1 {4,S} {5,S} {7,S}
4     C   u0 {3,S} {10,S}
5     C   u0 {3,S} {6,D}
6     C   u0 {5,D}
7     C   u0 {3,S}
8     C   u0 r0 {1,S} {9,D}
9     C   u0 {8,D}
10    C   u0 r0 {4,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 884,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 {1,D}
3  *1 C   u1 {4,S} {5,S} {7,S}
4     C   u0 {3,S}
5     C   u0 {3,S} {6,D}
6     C   u0 {5,D}
7     C   u0 {3,S}
8     C   u0 {1,S} {9,S}
9     C   u0 {8,S}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 885,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {9,[S,D,T,B]}
2 *3 Cd  u0 c0 r0 {1,D}
3 *1 C   u1 r0 {4,S} {5,S} {7,S}
4    C   u0 r0 {3,S}
5    C   u0 r0 {3,S} {6,D}
6    C   u0 r0 {5,D}
7    C   u0 r0 {3,S} {8,S}
8    C   u0 r0 {7,S}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 886,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S} {8,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {1,S}
8    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 887,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S} {8,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {1,S} {9,[S,D,T,B]}
8    C  u0 {1,S}
9    C  u0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 888,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Sp-9R!H=7R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S} {8,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {1,S} {9,D}
8    C  u0 {1,S}
9    C  u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 889,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Sp-9R!H=7R!H_Ext-4R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {7,S} {8,S}
2  *3 Cd  u0 c0 {1,D}
3  *1 C   u1 r0 {4,S} {5,S}
4     C   u0 r0 {3,S} {10,[S,D,T,B]}
5     C   u0 r0 {3,S} {6,D}
6     C   u0 r0 {5,D}
7     C   u0 {1,S} {9,D}
8     C   u0 r0 {1,S}
9     C   u0 {7,D}
10    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 890,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_N-Sp-9R!H=7R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S} {8,S}
2 *3 Cd u0 c0 r0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D}
7    C  u0 r0 {1,S} {9,[B,S,T]}
8    C  u0 {1,S}
9    C  u0 r0 {7,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 891,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {8,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S} {5,S}
4    C  u0 {3,S} {7,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {4,S}
8    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 892,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-5R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {8,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S} {5,S}
4    C   u0 {3,S} {7,S}
5    C   u0 {3,S} {6,D} {9,[S,D,T,B]}
6    C   u0 {5,D}
7    C   u0 {4,S}
8    C   u0 r0 {1,S}
9    R!H ux {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 893,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_3R!H-inRing",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {8,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r1 {4,S} {5,S}
4    C  u0 {3,S} {7,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {4,S}
8    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 894,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-3R!H-inRing",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {8,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r0 {4,S} {5,S}
4    C  u0 {3,S} {7,S}
5    C  u0 {3,S} {6,D}
6    C  u0 {5,D}
7    C  u0 {4,S}
8    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 895,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,CS,Cdd,N,O4dc,O4tc,S] u0 r0 {2,[D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S]               u0 c0 {1,[D,T,B]}
3 *1 C                                      u1 {4,[B,S]} {5,[S,D,T,B]}
4    C                                      u0 {3,[B,S]}
5    C                                      u0 {3,[S,D,T,B]} {6,[B,S,T]}
6    C                                      u0 {5,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 896,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R!H-inRing",
    group = 
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,CS,Cdd,N,O4dc,O4tc,S] u0 r0 {2,[D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S]               u0 c0 {1,[D,T,B]}
3 *1 C                                      u1 r1 {4,B} {5,B}
4    C                                      u0 {3,B}
5    C                                      u0 {3,B} {6,[B,S]}
6    C                                      u0 {5,[B,S]}
""",
    kinetics = None,
)

entry(
    index = 897,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R!H-inRing_1COCSCbCbfCdCddCtNO4dcO4tcS->Cd",
    group = 
"""
1 *2 Cd u0 r0 {2,D}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r1 {4,B} {5,B}
4    C  u0 {3,B}
5    C  u0 {3,B} {6,[B,S]}
6    C  u0 {5,[B,S]}
""",
    kinetics = None,
)

entry(
    index = 898,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R!H-inRing_1COCSCbCbfCdCddCtNO4dcO4tcS->Cd_Int-6R!H-1Cd",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,[S,D,T,B]}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r1 {4,B} {5,B}
4    C  u0 r1 {3,B}
5    C  u0 r1 {3,B} {6,[B,S]}
6    C  u0 r1 {1,[S,D,T,B]} {5,[B,S]}
""",
    kinetics = None,
)

entry(
    index = 899,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R!H-inRing_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cd",
    group = 
"""
1 *2 Ct u0 r0 {2,T}
2 *3 Ct u0 c0 {1,T}
3 *1 C  u1 r1 {4,B} {5,B}
4    C  u0 {3,B}
5    C  u0 {3,B} {6,[B,S]}
6    C  u0 {5,[B,S]}
""",
    kinetics = None,
)

entry(
    index = 900,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R!H-inRing_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cd_Ext-6R!H-R_Sp-7R!H-6R!H",
    group = 
"""
1 *2 Ct u0 r0 {2,T}
2 *3 Ct u0 c0 r0 {1,T}
3 *1 C  u1 r1 {4,B} {5,B}
4    C  u0 r1 {3,B}
5    C  u0 r1 {3,B} {6,[B,S]}
6    C  u0 r1 {5,[B,S]} {7,S}
7    C  u0 r1 {6,S}
""",
    kinetics = None,
)

entry(
    index = 901,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R!H-inRing_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cd_Ext-6R!H-R_N-Sp-7R!H-6R!H",
    group = 
"""
1 *2 Ct u0 r0 {2,T}
2 *3 Ct u0 c0 r0 {1,T}
3 *1 C  u1 r1 {4,B} {5,B}
4    C  u0 r1 {3,B}
5    C  u0 r1 {3,B} {6,[B,S]}
6    C  u0 r1 {5,[B,S]} {7,B}
7    C  u0 r1 {6,B}
""",
    kinetics = None,
)

entry(
    index = 902,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing",
    group = 
"""
1 *2 Cd u0 r0 {2,D}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r0 {4,S} {5,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,[B,S,T]}
6    C  u0 {5,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 903,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r0 {4,S} {5,S}
4    C  u0 {3,S} {7,[S,T]}
5    C  u0 {3,S} {6,[S,T]}
6    C  u0 {5,[S,T]}
7    C  u0 {4,[S,T]}
""",
    kinetics = None,
)

entry(
    index = 904,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {8,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 r0 {4,S} {5,S}
4    C   u0 {3,S} {7,[S,T]}
5    C   u0 {3,S} {6,[S,T]}
6    C   u0 {5,[S,T]}
7    C   u0 {4,[S,T]}
8    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 905,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {8,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r0 {4,S} {5,S}
4    C  u0 {3,S} {7,[S,T]}
5    C  u0 {3,S} {6,[S,T]}
6    C  u0 {5,[S,T]}
7    C  u0 {4,[S,T]}
8    C  u0 {1,S} {9,D}
9    C  u0 {8,D}
""",
    kinetics = None,
)

entry(
    index = 906,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd u0 r0 {2,D} {8,S} {10,S}
2  *3 Cd u0 c0 {1,D}
3  *1 C  u1 r0 {4,S} {5,S}
4     C  u0 {3,S} {7,[S,T]}
5     C  u0 {3,S} {6,[S,T]}
6     C  u0 {5,[S,T]}
7     C  u0 {4,[S,T]}
8     C  u0 {1,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 907,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S} {10,S}
2  *3 Cd  u0 c0 r0 {1,D}
3  *1 C   u1 r0 {4,S} {5,S} {11,[S,D,T,B]}
4     C   u0 r0 {3,S} {7,[S,T]}
5     C   u0 r0 {3,S} {6,[S,T]}
6     C   u0 r0 {5,[S,T]}
7     C   u0 {4,[S,T]}
8     C   u0 r0 {1,S} {9,D}
9     C   u0 {8,D}
10    C   u0 r0 {1,S}
11    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 908,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-3R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S}
2  *3 Cd  u0 c0 {1,D}
3  *1 C   u1 r0 {4,S} {5,S} {10,[S,D,T,B]}
4     C   u0 {3,S} {7,[S,T]}
5     C   u0 {3,S} {6,[S,T]}
6     C   u0 {5,[S,T]}
7     C   u0 {4,[S,T]}
8     C   u0 {1,S} {9,D}
9     C   u0 {8,D}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 909,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {8,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 r0 {4,S} {5,S} {9,S}
4    C   u0 {3,S} {7,[S,T]}
5    C   u0 {3,S} {6,[S,T]}
6    C   u0 {5,[S,T]}
7    C   u0 {4,[S,T]}
8    R!H ux {1,[S,D,T,B]}
9    C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 910,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,[S,D,T,B]} {10,[S,D,T,B]}
2  *3 Cd  u0 c0 r0 {1,D}
3  *1 C   u1 r0 {4,S} {5,S} {9,S}
4     C   u0 r0 {3,S} {7,[S,T]}
5     C   u0 r0 {3,S} {6,[S,T]}
6     C   u0 r0 {5,[S,T]}
7     C   u0 r0 {4,[S,T]}
8     R!H ux {1,[S,D,T,B]}
9     C   u0 r0 {3,S}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 911,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,[S,D,T,B]} {8,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r0 {4,S} {5,S} {9,S}
4    C  u0 {3,S} {7,[S,T]}
5    C  u0 {3,S} {6,[S,T]}
6    C  u0 {1,[S,D,T,B]} {5,[S,T]}
7    C  u0 {4,[S,T]}
8    C  u0 {1,S}
9    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 912,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {8,[S,D,T,B]} {9,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 r0 {4,S} {5,S}
4    C   u0 {3,S} {7,[S,T]}
5    C   u0 {3,S} {6,[S,T]}
6    C   u0 {5,[S,T]}
7    C   u0 {4,[S,T]}
8    R!H ux {1,[S,D,T,B]}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 913,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,[S,D,T,B]} {8,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r0 {4,S} {5,S}
4    C  u0 {3,S} {7,[S,T]}
5    C  u0 {3,S} {6,[S,T]}
6    C  u0 {1,[S,D,T,B]} {5,[S,T]}
7    C  u0 {4,[S,T]}
8    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 914,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-3R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 r0 {4,S} {5,S} {8,[S,D,T,B]}
4    C   u0 {3,S} {7,[S,T]}
5    C   u0 {3,S} {6,[S,T]}
6    C   u0 {5,[S,T]}
7    C   u0 {4,[S,T]}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 915,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-3R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r0 {4,S} {5,S} {7,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 916,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {8,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r0 {4,S} {5,S} {7,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {3,S}
8    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 917,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-8R!H-6R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {8,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r0 {4,S} {5,S} {7,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,S}
6    C  u0 {5,S} {8,S}
7    C  u0 {3,S}
8    C  u0 {1,S} {6,S}
""",
    kinetics = None,
)

entry(
    index = 918,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-8R!H-6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {8,S} {9,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r0 {4,S} {5,S} {7,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,S}
6    C  u0 {5,S} {8,S}
7    C  u0 {3,S}
8    C  u0 {1,S} {6,S}
9    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 919,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-8R!H-6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R",
    group = 
"""
1  *2 Cd  u0 r0 {2,D} {8,S} {9,S}
2  *3 Cd  u0 c0 {1,D}
3  *1 C   u1 r0 {4,S} {5,S} {7,S}
4     C   u0 {3,S}
5     C   u0 {3,S} {6,S}
6     C   u0 {5,S} {8,S}
7     C   u0 {3,S}
8     C   u0 r0 {1,S} {6,S}
9     C   u0 r0 {1,S} {10,[S,D,T,B]}
10    R!H ux {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 920,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {8,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 r0 {4,S} {5,S} {7,S}
4    C   u0 {3,S}
5    C   u0 {3,S} {6,S}
6    C   u0 {5,S} {9,[S,D,T,B]}
7    C   u0 {3,S}
8    C   u0 {1,S}
9    R!H ux {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 921,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {8,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 r0 {4,S} {5,S} {7,S}
4    C   u0 {3,S}
5    C   u0 {3,S} {6,S}
6    C   u0 {5,S}
7    C   u0 {3,S}
8    C   u0 {1,S} {9,[S,D,T,B]}
9    R!H ux {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 922,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {7,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 r0 {4,S} {5,S}
4    C   u0 {3,S}
5    C   u0 {3,S} {6,S}
6    C   u0 {5,S}
7    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 923,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r0 {4,S} {5,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,S}
6    C  u0 {5,S}
7    C  u0 {1,S} {8,[S,D,T,B]}
8    C  u0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 924,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Int-8R!H-6R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {7,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r0 {4,S} {5,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,S}
6    C  u0 {5,S} {8,[S,D,T,B]}
7    C  u0 {1,S} {8,[S,D,T,B]}
8    C  u0 r0 {6,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 925,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {7,S} {9,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 r0 {4,S} {5,S}
4    C   u0 {3,S}
5    C   u0 {3,S} {6,S}
6    C   u0 {5,S}
7    C   u0 {1,S} {8,D}
8    C   u0 {7,D}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 926,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {7,[S,D,T,B]} {8,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 r0 {4,S} {5,S}
4    C   u0 {3,S}
5    C   u0 {3,S} {6,S}
6    C   u0 {5,S}
7    R!H ux {1,[S,D,T,B]}
8    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 927,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {6,[S,D,T,B]} {7,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 r0 {4,S} {5,S}
4    C  u0 {3,S}
5    C  u0 {3,S} {6,S}
6    C  u0 {1,[S,D,T,B]} {5,S}
7    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 928,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,CS,Cdd,N,O4dc,O4tc,S] u0 r0 {2,D} {5,[S,D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S]               u0 c0 {1,D}
3 *1 C                                      u1 {4,S}
4    C                                      u0 {3,S}
5    R!H                                    ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 929,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,[S,D,T,B]} {6,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S}
4    C   u0 {3,S}
5    R!H ux {1,[S,D,T,B]}
6    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 930,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {5,[S,D,T,B]}
5    C  u0 {1,S} {4,[S,D,T,B]}
6    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 931,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-4R!H_Sp-5R!H-4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {5,S}
5    C  u0 {1,S} {4,S}
6    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 932,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-4R!H_Sp-5R!H-4R!H_Ext-4R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 r0 {4,S}
4    C   u0 r0 {3,S} {5,S} {7,[S,D,T,B]}
5    C   u0 r0 {1,S} {4,S}
6    C   u0 r0 {1,S}
7    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 933,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-4R!H_Sp-5R!H-4R!H_Ext-6R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S}
4    C   u0 {3,S} {5,S}
5    C   u0 {1,S} {4,S}
6    C   u0 {1,S} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 934,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-4R!H_N-Sp-5R!H-4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 r0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {5,[B,D,T]}
5    C  u0 {1,S} {4,[B,D,T]}
6    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 935,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-7R!H-4R!H",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,[S,D,T,B]} {6,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S}
4    C   u0 {3,S} {7,S}
5    R!H ux {1,[S,D,T,B]}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 936,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-7R!H-4R!H_Ext-7R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,[S,D,T,B]} {6,[S,D,T,B]}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S}
4    C   u0 {3,S} {7,S}
5    R!H ux {1,[S,D,T,B]}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {4,S} {8,[S,D,T,B]}
8    R!H ux {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 937,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-7R!H-4R!H_Ext-5R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S}
4    C   u0 {3,S} {7,S}
5    C   u0 {1,S} {8,[S,D,T,B]}
6    C   u0 {1,S}
7    C   u0 {4,S}
8    R!H ux {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 938,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-7R!H-4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {7,D}
5    C  u0 {1,S}
6    C  u0 {1,S}
7    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 939,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-7R!H-4R!H_Ext-5R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S} {6,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S}
4    C   u0 {3,S} {7,D}
5    C   u0 {1,S} {8,[S,D,T,B]}
6    C   u0 {1,S}
7    C   u0 {4,D}
8    R!H ux {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 940,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd",
    group = 
"""
1 *2 Cdd u0 r0 {2,D} {5,D}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S}
4    C   u0 {3,S}
5    C   u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 941,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_5R!H-inRing",
    group = 
"""
1 *2 Cdd u0 r0 {2,D} {5,D}
2 *3 Cd  u0 c0 r0 {1,D}
3 *1 C   u1 r0 {4,S}
4    C   u0 {3,S}
5    C   u0 r1 {1,D}
""",
    kinetics = None,
)

entry(
    index = 942,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_N-5R!H-inRing",
    group = 
"""
1 *2 Cdd u0 r0 {2,D} {5,D}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S}
4    C   u0 {3,S}
5    C   u0 r0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 943,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_N-5R!H-inRing_4R!H-inRing",
    group = 
"""
1 *2 Cdd u0 r0 {2,D} {5,D}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S}
4    C   u0 r1 {3,S}
5    C   u0 r0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 944,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_N-5R!H-inRing_N-4R!H-inRing",
    group = 
"""
1 *2 Cdd u0 r0 {2,D} {5,D}
2 *3 Cd  u0 c0 r0 {1,D}
3 *1 C   u1 r0 {4,S}
4    C   u0 r0 {3,S}
5    C   u0 r0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 945,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd",
    group = 
"""
1 *2 [CS,Cd]                  u0 r0 {2,D} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,D}
3 *1 C                        u1 {4,S}
4    C                        u0 {3,S}
5    C                        u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 946,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {6,[S,D,T,B]}
5    C  u0 {1,S}
6    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 947,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {6,S}
5    C  u0 {1,S}
6    C  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 948,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {6,S}
5    C  u0 {1,S} {6,S}
6    C  u0 {4,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 949,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-4R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S}
4    C   u0 {3,S} {6,S} {7,[S,D,T,B]}
5    C   u0 {1,S} {6,S}
6    C   u0 {4,S} {5,S}
7    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 950,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-4R!H-R_Ext-4R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 r0 {1,D}
3 *1 C   u1 r0 {4,S}
4    C   u0 r0 {3,S} {6,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
5    C   u0 r0 {1,S} {6,S}
6    C   u0 r0 {4,S} {5,S}
7    R!H ux {4,[S,D,T,B]}
8    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 951,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-6R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S}
4    C   u0 {3,S} {6,S}
5    C   u0 {1,S} {6,S}
6    C   u0 {4,S} {5,S} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 952,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-6R!H-R_Ext-6R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 r0 {1,D}
3 *1 C   u1 r0 {4,S}
4    C   u0 r0 {3,S} {6,S}
5    C   u0 r0 {1,S} {6,S}
6    C   u0 r0 {4,S} {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]}
8    R!H ux {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 953,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-5R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S}
4    C   u0 {3,S} {6,S}
5    C   u0 {1,S} {6,S} {7,[S,D,T,B]}
6    C   u0 {4,S} {5,S}
7    R!H ux {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 954,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 r0 {1,D}
3 *1 C   u1 r0 {4,S}
4    C   u0 r0 {3,S} {6,S}
5    C   u0 r0 {1,S} {6,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
6    C   u0 r0 {4,S} {5,S}
7    R!H ux {5,[S,D,T,B]}
8    R!H ux {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 955,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H_Ext-4R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S}
4    C   u0 {3,S} {6,S} {7,[S,D,T,B]}
5    C   u0 {1,S}
6    C   u0 {4,S}
7    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 956,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H_Ext-5R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S}
4    C   u0 {3,S} {6,S}
5    C   u0 {1,S} {7,[S,D,T,B]}
6    C   u0 {4,S}
7    R!H ux {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 957,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {6,[B,D,T]}
5    C  u0 {1,S}
6    C  u0 {4,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 958,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H_Ext-6R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {6,[B,D,T]}
5    C  u0 {1,S}
6    C  u0 {4,[B,D,T]} {7,[S,D,T,B]}
7    C  u0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 959,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H_Ext-6R!H-R_Ext-5R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {6,[B,D,T]}
5    C  u0 {1,S} {8,[S,D,T,B]}
6    C  u0 {4,[B,D,T]} {7,[S,D,T,B]}
7    C  u0 {6,[S,D,T,B]}
8    C  u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 960,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H_Ext-6R!H-R_Ext-5R!H-R_4R!H-inRing",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D}
3 *1 C  u1 r0 {4,S}
4    C  u0 r1 {3,S} {6,[B,D,T]}
5    C  u0 {1,S} {8,[S,D,T,B]}
6    C  u0 {4,[B,D,T]} {7,[S,D,T,B]}
7    C  u0 {6,[S,D,T,B]}
8    C  u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 961,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H_Ext-6R!H-R_Ext-5R!H-R_N-4R!H-inRing",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D}
3 *1 C  u1 r0 {4,S}
4    C  u0 r0 {3,S} {6,[B,D,T]}
5    C  u0 {1,S} {8,[S,D,T,B]}
6    C  u0 {4,[B,D,T]} {7,[S,D,T,B]}
7    C  u0 {6,[S,D,T,B]}
8    C  u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 962,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H_Ext-5R!H-R",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {6,D}
5    C  u0 {1,S} {7,D}
6    C  u0 {4,D}
7    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 963,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H_Ext-5R!H-R_Int-5R!H-4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D}
3 *1 C  u1 r0 {4,S}
4    C  u0 {3,S} {5,[S,D,T,B]} {6,D}
5    C  u0 {1,S} {4,[S,D,T,B]} {7,D}
6    C  u0 {4,D}
7    C  u0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 964,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H_Int-5R!H-4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 r0 {3,S} {5,[S,D,T,B]} {6,D}
5    C  u0 r0 {1,S} {4,[S,D,T,B]}
6    C  u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 965,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D}
3 *1 C  u1 r0 {4,S}
4    C  u0 r0 {3,S} {6,D}
5    C  u0 r0 {1,S} {6,S}
6    C  u0 r0 {4,D} {5,S}
""",
    kinetics = None,
)

entry(
    index = 966,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D}
3 *1 C  u1 r0 {4,S}
4    C  u0 {3,S} {6,D}
5    C  u0 {1,S} {6,[B,D,T]}
6    C  u0 {4,D} {5,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 967,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Int-5R!H-4R!H_Sp-5R!H-4R!H",
    group = 
"""
1 *2 [CS,Cd]                  u0 r0 {2,D} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,D}
3 *1 C                        u1 {4,S}
4    C                        u0 {3,S} {5,S}
5    C                        u0 {1,S} {4,S}
""",
    kinetics = None,
)

entry(
    index = 968,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Int-5R!H-4R!H_Sp-5R!H-4R!H_Ext-5R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 {1,D}
3 *1 C   u1 {4,S}
4    C   u0 {3,S} {5,S}
5    C   u0 {1,S} {4,S} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 969,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Int-5R!H-4R!H_Sp-5R!H-4R!H_Ext-5R!H-R_Ext-5R!H-R",
    group = 
"""
1 *2 Cd  u0 r0 {2,D} {5,S}
2 *3 Cd  u0 c0 r0 {1,D}
3 *1 C   u1 r0 {4,S}
4    C   u0 {3,S} {5,S}
5    C   u0 {1,S} {4,S} {6,[S,D,T,B]} {7,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]}
7    R!H ux {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 970,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Int-5R!H-4R!H_Sp-5R!H-4R!H_1CSCd->CS",
    group = 
"""
1 *2 CS                       u0 r0 {2,D} {5,S}
2 *3 [Cd,Ct,Cb,Cbf,Cdd,N,O,S] u0 c0 {1,D}
3 *1 C                        u1 {4,S}
4    C                        u0 {3,S} {5,S}
5    C                        u0 {1,S} {4,S}
""",
    kinetics = None,
)

entry(
    index = 971,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Int-5R!H-4R!H_Sp-5R!H-4R!H_N-1CSCd->CS",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D}
3 *1 C  u1 r0 {4,S}
4    C  u0 r0 {3,S} {5,S}
5    C  u0 r0 {1,S} {4,S}
""",
    kinetics = None,
)

entry(
    index = 972,
    label = "Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Int-5R!H-4R!H_N-Sp-5R!H-4R!H",
    group = 
"""
1 *2 Cd u0 r0 {2,D} {5,S}
2 *3 Cd u0 c0 r0 {1,D}
3 *1 C  u1 r0 {4,S}
4    C  u0 r0 {3,S} {5,D}
5    C  u0 r0 {1,S} {4,D}
""",
    kinetics = None,
)

tree(
"""
L1: Root
    L2: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing
        L3: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO
        L3: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO
            L4: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R
                L5: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R
                    L6: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-5R!H-R_Int-6R!H-2CbCbfCdCddCtNOS
                    L6: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R
                        L7: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H
                            L8: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R
                                L9: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R_Ext-5R!H-R_Int-8R!H-3R!H
                                L9: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_4R!H-inRing
                                    L10: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_4R!H-inRing_1CSCbCdCddCt->Cd
                                    L10: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_4R!H-inRing_N-1CSCbCdCddCt->Cd
                                L9: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-4R!H-inRing
                                    L10: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-4R!H-inRing_Ext-3R!H-R
                            L8: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H
                                L9: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_1CSCbCdCddCt->Cd
                                L9: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-1CSCbCdCddCt->Cd
                            L8: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H
                                L9: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_Sp-6R!H-3R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H_Ext-3R!H-R
                        L7: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_N-Sp-6R!H-3R!H
                            L8: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_Ext-3R!H-R_N-Sp-6R!H-3R!H_Ext-6R!H-R
                    L6: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_1CSCbCdCddCt->Cd
                    L6: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_N-1CSCbCdCddCt->Cd
                        L7: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_N-1CSCbCdCddCt->Cd_3R!H->C
                        L7: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_Ext-1CSCbCdCddCt-R_N-1CSCbCdCddCt->Cd_N-3R!H->C
                L5: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing
                    L6: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R
                        L7: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-5R!H-R
                    L6: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R
                        L7: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H
                            L8: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R
                                L9: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Int-5R!H-3R!H
                                    L10: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Int-5R!H-3R!H_Sp-7R!H-5R!H
                                        L11: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Int-5R!H-3R!H_Sp-7R!H-5R!H_Ext-5R!H-R
                                        L11: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Int-5R!H-3R!H_Sp-7R!H-5R!H_Ext-7R!H-R
                                    L10: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Int-5R!H-3R!H_N-Sp-7R!H-5R!H
                                L9: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Sp-7R!H=5R!H
                                    L10: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Sp-7R!H=5R!H_6R!H-inRing
                                        L11: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Sp-7R!H=5R!H_6R!H-inRing_3R!H-inRing
                                        L11: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Sp-7R!H=5R!H_6R!H-inRing_N-3R!H-inRing
                                    L10: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Sp-7R!H=5R!H_N-6R!H-inRing
                                        L11: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_Sp-7R!H=5R!H_N-6R!H-inRing_Ext-4R!H-R
                                L9: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_N-Sp-7R!H=5R!H
                                    L10: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_N-Sp-7R!H=5R!H_3R!H-inRing
                                        L11: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_N-Sp-7R!H=5R!H_3R!H-inRing_Ext-5R!H-R
                                        L11: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_N-Sp-7R!H=5R!H_3R!H-inRing_5R!H->C
                                            L12: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_N-Sp-7R!H=5R!H_3R!H-inRing_5R!H->C_Ext-3R!H-R
                                        L11: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_N-Sp-7R!H=5R!H_3R!H-inRing_N-5R!H->C
                                    L10: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Ext-5R!H-R_N-Sp-7R!H=5R!H_N-3R!H-inRing
                            L8: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_Sp-6R!H-4R!H
                            L8: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_N-Sp-6R!H-4R!H
                                L9: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-4R!H_N-Sp-6R!H-4R!H_Ext-4R!H-R
                        L7: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Sp-6R!H=3R!H
                            L8: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Sp-6R!H=3R!H_3R!H-inRing
                                L9: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Sp-6R!H=3R!H_3R!H-inRing_Ext-3R!H-R
                            L8: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Sp-6R!H=3R!H_N-3R!H-inRing
                                L9: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Sp-6R!H=3R!H_N-3R!H-inRing_Int-5R!H-3R!H
                        L7: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H
                            L8: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H
                                L9: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-6R!H
                                L9: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H
                                    L10: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-5R!H-3R!H
                                        L11: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-5R!H-3R!H_Ext-6R!H-R
                                            L12: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-5R!H-3R!H_Ext-6R!H-R_Ext-3R!H-R
                                            L12: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-5R!H-3R!H_Ext-6R!H-R_3R!H-inRing
                                            L12: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-5R!H-3R!H_Ext-6R!H-R_N-3R!H-inRing
                                    L10: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-6R!H-5R!H
                                        L11: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-6R!H-5R!H_3R!H-inRing
                                            L12: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-6R!H-5R!H_3R!H-inRing_Ext-6R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
                                            L12: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-6R!H-5R!H_3R!H-inRing_Ext-6R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
                                        L11: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Int-7R!H-4R!H_Int-6R!H-5R!H_N-3R!H-inRing
                                L9: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_Ext-3R!H-R
                                L9: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_3R!H-inRing
                                L9: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_Sp-7R!H-5R!H_N-3R!H-inRing
                            L8: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_N-Sp-7R!H-5R!H
                                L9: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_N-Sp-7R!H-5R!H_Ext-3R!H-R
                                    L10: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_N-Sp-6R!H=3R!H_Ext-5R!H-R_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R
                    L6: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_1CSCbCdCddCt->Cd
                        L7: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_1CSCbCdCddCt->Cd_Ext-4R!H-R_Ext-5R!H-R_Int-6R!H-3R!H_Ext-6R!H-R
                        L7: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_1CSCbCdCddCt->Cd_Ext-4R!H-R_Sp-5R!H-4R!H
                        L7: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_1CSCbCdCddCt->Cd_Ext-4R!H-R_N-Sp-5R!H-4R!H
                            L8: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_1CSCbCdCddCt->Cd_Ext-4R!H-R_N-Sp-5R!H-4R!H_Ext-4R!H-R
                    L6: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_N-1CSCbCdCddCt->Cd
                        L7: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_2CbCbfCdCddCtNOS-inRing_N-1CSCbCdCddCt->Cd_Ext-3R!H-R
                L5: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Ext-1CSCbCdCddCt-R_N-2CbCbfCdCddCtNOS-inRing
            L4: Root_1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_N-1COCOCOCOCOCOCSCSCSCSCSCSCbCbCbCbCbCbCbfCbfCbfCbfCbfCbfCdCdCdCdCdCdCddCddCddCddCddCddCtCtCtCtCtCtNNNNNNO4dcO4dcO4dcO4dcO4dcO4dcO4tcO4tcO4tcO4tcO4tcO4tcSSSSSS->CO_Int-3R!H-1CSCbCdCddCt_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R
    L2: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing
        L3: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R
            L4: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R
                L5: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-4R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-12R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-12R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-4R!H-R_Sp-11R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-4R!H-R_N-Sp-11R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_Ext-3R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_Ext-3R!H-R_Sp-11R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_Ext-3R!H-R_N-Sp-11R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_Sp-11R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_N-Sp-11R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-4R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-4R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Sp-10R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_N-Sp-10R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-4R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-8R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-8R!H=4R!H
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Sp-7R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_N-Sp-7R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Sp-7R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_N-Sp-7R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Sp-7R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_N-Sp-7R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Sp-7R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-Sp-7R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_Sp-7R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-3R!H-R_N-Sp-7R!H=4R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Sp-7R!H=4R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_N-Sp-7R!H=4R!H
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-7R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-3R!H-R
                L5: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H_Ext-3R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H_Ext-3R!H-R_Ext-4R!H-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-14R!H=4R!H
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-14R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H_Ext-4R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H_Ext-4R!H-R_Sp-13R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H_Ext-4R!H-R_N-Sp-13R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-4R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-4R!H-R_Ext-3R!H-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-4R!H-R_Ext-3R!H-R_Sp-13R!H=4R!H
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-4R!H-R_Ext-3R!H-R_N-Sp-13R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-4R!H-R_Sp-13R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-4R!H-R_N-Sp-13R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H_Ext-3R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-3R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-13R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-13R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-12R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-12R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-4R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-3R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-3R!H-R_Ext-4R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-13R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-13R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-4R!H-R_Sp-12R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-4R!H-R_N-Sp-12R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-4R!H-R_Ext-3R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-4R!H-R_Ext-3R!H-R_Sp-12R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-4R!H-R_Ext-3R!H-R_N-Sp-12R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-4R!H-R_Sp-12R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-4R!H-R_N-Sp-12R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-3R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-12R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-12R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-4R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-10R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-10R!H=4R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-12R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-12R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-4R!H-R_Sp-11R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-4R!H-R_N-Sp-11R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_Ext-3R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_Ext-3R!H-R_Sp-11R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_Ext-3R!H-R_N-Sp-11R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_Sp-11R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-4R!H-R_N-Sp-11R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-4R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-4R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-7R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-10R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-8R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-8R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-10R!H-R_Sp-8R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-10R!H-R_N-Sp-8R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-8R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-8R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-8R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-8R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-8R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-8R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Sp-8R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-8R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Sp-10R!H=9R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-11R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-11R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-8R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-11R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-8R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Sp-10R!H=9R!H_Sp-8R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Sp-10R!H=9R!H_N-Sp-8R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-8R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-8R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_Sp-8R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-8R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-8R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Sp-8R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_N-Sp-8R!H=4R!H
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-3R!H-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-8R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-8R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                L5: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Sp-10R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_N-Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-10R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-10R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-3R!H-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Ext-3R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-10R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-10R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-10R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-9R!H-R_N-Sp-10R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-10R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-3R!H-R_N-Sp-10R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-10R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-9R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-9R!H-R_Ext-3R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-9R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-12R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-12R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-4R!H-R_Sp-12R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-4R!H-R_N-Sp-12R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-11R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-11R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Sp-11R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_N-Sp-11R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-11R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-11R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-11R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-11R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-10R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Sp-10R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_N-Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-4R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Int-9R!H-7R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-4R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-10R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Sp-9R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-Sp-9R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Sp-9R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_N-Sp-9R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-9R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-9R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-1COCSCbCbfCdCddCtNO4dcO4tcS
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-4R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-4R!H-R_Sp-8R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-2CbCbfCdCddCtNOS-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-7R!H#6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H
            L4: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                L5: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-4R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-4R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R_Sp-9R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-4R!H-R_Sp-9R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-4R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-7R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-7R!H=4R!H
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_4R!H-inRing
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_Sp-8R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_3R!H-inRing
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-3R!H-inRing
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-3R!H-inRing_Ext-3R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-3R!H-inRing_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-3R!H-inRing_Ext-4R!H-R_Sp-8R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-3R!H-inRing_Ext-4R!H-R_N-Sp-8R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-3R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-4R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_Sp-7R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-4R!H-R_N-Sp-7R!H=4R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-4R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-4R!H-R_Sp-6R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-3R!H_N-4R!H-inRing_Ext-4R!H-R_N-Sp-6R!H=4R!H
                L5: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_4R!H-inRing
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_4R!H-inRing_Ext-5R!H-R_Int-6R!H-3R!H_Ext-4R!H-R_Sp-7R!H=4R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_4R!H-inRing_Ext-5R!H-R_Int-6R!H-3R!H_Ext-4R!H-R_Sp-7R!H=4R!H_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_4R!H-inRing_Ext-5R!H-R_Int-6R!H-3R!H_Ext-4R!H-R_Sp-7R!H=4R!H_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_4R!H-inRing_Ext-5R!H-R_Int-6R!H-3R!H_Ext-4R!H-R_N-Sp-7R!H=4R!H
                L5: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_3R!H->S
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_Sp-11R!H=10R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-3C-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-3C-R_Ext-4R!H-R
                                                        L15: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-3C-R_Ext-4R!H-R_Sp-13R!H=4R!H
                                                        L15: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-3C-R_Ext-4R!H-R_N-Sp-13R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-4R!H-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-4R!H-R_Sp-12R!H=4R!H
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_Sp-11R!H=10R!H_Ext-4R!H-R_N-Sp-12R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-3C-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-3C-R_Ext-4R!H-R
                                                        L15: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-3C-R_Ext-4R!H-R_Sp-13R!H=4R!H
                                                        L15: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-3C-R_Ext-4R!H-R_N-Sp-13R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-4R!H-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-4R!H-R_Sp-12R!H=4R!H
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-4R!H-R_N-Sp-12R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_3C-inRing
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_N-3C-inRing
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_N-3C-inRing_Ext-3C-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_N-3C-inRing_Ext-3C-R_Ext-4R!H-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_N-3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-12R!H=4R!H
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_N-3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-12R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_N-3C-inRing_Ext-4R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_N-3C-inRing_Ext-4R!H-R_Sp-11R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-3C-R_N-3C-inRing_Ext-4R!H-R_N-Sp-11R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-8R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-3C-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-3C-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-3C-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-3C-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-13R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-3C-R_Ext-10R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-13R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-3C-R_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-11R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_N-Sp-11R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-12R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-12R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R_Sp-9R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3C-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3C-R_Ext-4R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3C-R_Ext-4R!H-R_Sp-13R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3C-R_Ext-4R!H-R_N-Sp-13R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-12R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-9R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-12R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-11R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_N-Sp-11R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-4R!H-R_Sp-9R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-8R!H#7R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-12R!H=4R!H
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-12R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-4R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Sp-11R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_N-Sp-11R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-11R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-11R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-4R!H-R_Sp-10R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-3C-R_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-10R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-4R!H-R_Sp-9R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R!H->S_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-8R!H#7R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H
                                                        L15: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H
                                                        L15: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H
                                                        L15: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H
                                                        L15: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-3R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-4R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-4R!H-R_Sp-9R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-4R!H-R_Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3R!H-R_Int-7R!H-3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-4R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-4R!H-R_Sp-8R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_2CbCbfCdCddCtNOS->Cdd
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R
                                                        L15: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H
                                                            L16: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                        L15: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H
                                                            L16: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H
                                                        L15: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                                        L15: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R
                                                        L15: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H
                                                            L16: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-11R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                        L15: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H
                                                            L16: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-11R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H
                                                        L15: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                                        L15: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-4R!H-R_N-Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-4R!H-R_Sp-8R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-4R!H-R_N-Sp-8R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-Sp-7R!H-6R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_2CbCbfCdCddCtNOS->Cdd
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R_Sp-9R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R_Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H
                                                    L14: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-4R!H-R_N-Sp-10R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-4R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-4R!H-R_Sp-9R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-4R!H-R_Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H
                                                L13: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-4R!H-R_N-Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-9R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct_Ext-1CdCdd-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct_Ext-1CdCdd-R_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct_Ext-1CdCdd-R_Ext-4R!H-R_Sp-8R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct_Ext-1CdCdd-R_Ext-4R!H-R_N-Sp-8R!H=4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct_1CdCdd->Cdd
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct_N-1CdCdd->Cdd
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct_N-1CdCdd->Cdd_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct_N-1CdCdd->Cdd_Ext-4R!H-R_Sp-7R!H=4R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-2CbCbfCdCddCtNOS->Cdd_N-1COCOCOCSCSCSCbCbCbCbfCbfCbfCdCdCdCddCddCddCtCtCtNNNO4dcO4dcO4dcO4tcO4tcO4tcSSS->Ct_N-1CdCdd->Cdd_Ext-4R!H-R_N-Sp-7R!H=4R!H
            L4: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_2CbCbfCdCddCtNOS->Cdd
            L4: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_N-2CbCbfCdCddCtNOS->Cdd
                L5: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_N-2CbCbfCdCddCtNOS->Cdd_1COCSCbCbfCdCddCtNO4dcO4tcS->Cd
                L5: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-2CbCbfCdCddCtNOS-R_N-2CbCbfCdCddCtNOS->Cdd_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cd
        L3: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R
            L4: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS
                L5: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_3R!H-inRing
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_N-3R!H-inRing
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-6R!H=5R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-6R!H=5R!H_Ext-3R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-6R!H=5R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-6R!H=5R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-6R!H=5R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-3R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-6R!H=5R!H_Ext-3R!H-R
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-3R!H-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R
                L5: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-5R!H-R
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-4R!H-R_Ext-4R!H-R
                L5: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Int-4R!H-1COCSCbCbfCdCddCtNO4dcO4tcS_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-5R!H-R
            L4: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H
                L5: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Ext-1Cdd-R
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-3R!H-R
                L5: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_Sp-6R!H-5R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-4R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-1COCSCdCt-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_Sp-6R!H-5R!H_1COCSCdCt->Cd
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_Sp-6R!H-5R!H_N-1COCSCdCt->Cd
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_Sp-6R!H-5R!H_N-1COCSCdCt->Cd_Int-5R!H-4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Int-6R!H-3R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_1COCSCdCt->Ct
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_1COCSCdCt->Ct_Ext-4R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-1COCSCdCt->Ct
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-1COCSCdCt->Ct_Ext-3R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-1COCSCdCt->Ct_Ext-3R!H-R_1COCd->Cd
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-1COCSCdCt->Ct_Ext-3R!H-R_N-1COCd->Cd
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-4R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-4R!H-R_1COCSCdCt->Cd
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-4R!H-R_N-1COCSCdCt->Cd
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-3R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-3R!H-R_Ext-6R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-3R!H-R_1COCSCdCt->Cd
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_Ext-3R!H-R_N-1COCSCdCt->Cd
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_1COCSCdCt->Ct
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_Sp-4R!H=3R!H_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-1COCSCdCt-R_N-1COCSCdCt->Ct
            L4: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H
                L5: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_Sp-8R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-3R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-10R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R_Ext-3R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-3R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_3R!H-inRing
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_N-3R!H-inRing
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_N-3R!H-inRing_Ext-3R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_N-3R!H-inRing_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-7R!H-6R!H_N-3R!H-inRing_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-4R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Sp-9R!H=7R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Sp-9R!H=7R!H_Ext-4R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_N-Sp-9R!H=7R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-5R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_3R!H-inRing
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-3R!H-inRing
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R!H-inRing
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R!H-inRing_1COCSCbCbfCdCddCtNO4dcO4tcS->Cd
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R!H-inRing_1COCSCbCbfCdCddCtNO4dcO4tcS->Cd_Int-6R!H-1Cd
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R!H-inRing_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cd
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R!H-inRing_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cd_Ext-6R!H-R_Sp-7R!H-6R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R!H-inRing_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cd_Ext-6R!H-R_N-Sp-7R!H-6R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R_Ext-3R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-3R!H-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-4R!H-R_Ext-3R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-3R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-8R!H-6R!H
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-8R!H-6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                            L12: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-8R!H-6R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-9R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-6R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-8R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Int-8R!H-6R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-7R!H-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R!H-inRing_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-6R!H-1COCSCbCbfCdCddCtNO4dcO4tcS
                L5: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-4R!H_Sp-5R!H-4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-4R!H_Sp-5R!H-4R!H_Ext-4R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-4R!H_Sp-5R!H-4R!H_Ext-6R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Int-5R!H-4R!H_N-Sp-5R!H-4R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-7R!H-4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-7R!H-4R!H_Ext-7R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_Sp-7R!H-4R!H_Ext-5R!H-R
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-7R!H-4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_Ext-4R!H-R_N-Sp-7R!H-4R!H_Ext-5R!H-R
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_5R!H-inRing
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_N-5R!H-inRing
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_N-5R!H-inRing_4R!H-inRing
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_N-5R!H-inRing_N-4R!H-inRing
                    L6: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-4R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-4R!H-R_Ext-4R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-6R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-6R!H-R_Ext-6R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-5R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H_Int-6R!H-5R!H_Ext-5R!H-R_Ext-5R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H_Ext-4R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_Sp-6R!H-4R!H_Ext-5R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H_Ext-6R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H_Ext-6R!H-R_Ext-5R!H-R
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H_Ext-6R!H-R_Ext-5R!H-R_4R!H-inRing
                                        L11: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H_Ext-6R!H-R_Ext-5R!H-R_N-4R!H-inRing
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H_Ext-5R!H-R
                                    L10: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H_Ext-5R!H-R_Int-5R!H-4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H_Int-5R!H-4R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H_Int-6R!H-5R!H_Sp-6R!H-5R!H
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Ext-4R!H-R_N-Sp-6R!H-4R!H_Int-6R!H-5R!H_N-Sp-6R!H-5R!H
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Int-5R!H-4R!H_Sp-5R!H-4R!H
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Int-5R!H-4R!H_Sp-5R!H-4R!H_Ext-5R!H-R
                                L9: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Int-5R!H-4R!H_Sp-5R!H-4R!H_Ext-5R!H-R_Ext-5R!H-R
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Int-5R!H-4R!H_Sp-5R!H-4R!H_1CSCd->CS
                            L8: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Int-5R!H-4R!H_Sp-5R!H-4R!H_N-1CSCd->CS
                        L7: Root_N-1COCSCbCbfCdCddCtNO4dcO4tcS-inRing_Ext-3R!H-R_N-Sp-4R!H=3R!H_Ext-1COCSCbCbfCdCddCtNO4dcO4tcS-R_N-1COCSCbCbfCdCddCtNO4dcO4tcS->Cdd_Int-5R!H-4R!H_N-Sp-5R!H-4R!H
"""
)

forbidden(
    label = "1_naphthyl_7_add_res1",
    group = 
"""
1     C u0 {2,[D,B]} {3,[S,B]} {4,[S,B]}
2     C u0 {1,[D,B]} {5,[S,B]} {6,[S,B]}
3     C u0 {1,[S,B]} {7,[D,B]}
4     C u0 {1,[S,B]} {9,[D,B]}
5     C u0 {2,[S,B]} {8,[D,B]}
6  *1 C u1 {2,[S,B]} {10,[D,B]}
7     C u0 {3,[D,B]} {8,[S,B]}
8  *3 C u0 {5,[D,B]} {7,[S,B]}
9     C u0 {4,[D,B]} {10,[S,B]}
10    C u0 {6,[D,B]} {9,[S,B]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Prevent a 1-naphthyl radical from attacking it's 7 site. Resonance form 1.
""",
)

forbidden(
    label = "1_naphthyl_7_add_res2",
    group = 
"""
1     C u0 {2,S} {3,S} {4,D}
2     C u0 {1,S} {5,S} {6,D}
3     C u0 {1,S} {7,D}
4     C u0 {1,D} {9,S}
5  *2 C u0 {2,S} {8,D}
6  *1 C u1 {2,D} {10,S}
7     C u0 {3,D} {8,S}
8  *3 C u0 {5,D} {7,S}
9     C u0 {4,S} {10,D}
10    C u0 {6,S} {9,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Prevent a 1-naphthyl radical from attacking it's 7 site. Resonance form 2.
""",
)

forbidden(
    label = "1_naphthyl_7_add_res3",
    group = 
"""
1     C u0 {2,S} {3,S} {4,D}
2     C u0 {1,S} {5,S} {6,D}
3     C u0 {1,S} {7,D}
4     C u0 {1,D} {9,S}
5  *1 C u1 {2,S} {8,D}
6     C u0 {2,D} {10,S}
7     C u0 {3,D} {8,S}
8     C u0 {5,D} {7,S}
9  *2 C u0 {4,S} {10,D}
10 *3 C u0 {6,S} {9,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Prevent a 1-naphthyl radical from attacking it's 7 site. Resonance form 3.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD1_res1",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,S} {6,D}
3    C u0 p0 c0 {1,D} {7,S}
4 *2 C u0 p0 c0 {2,S} {7,D}
5    C u0 p0 c0 {1,S} {9,D}
6    C u0 p0 c0 {2,D} {8,S}
7 *3 C u0 p0 c0 {3,S} {4,D}
8 *1 C u1 p0 c0 {6,S} {9,S}
9    C u0 p0 c0 {5,D} {8,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 5-membered ring tricyclic.
Resonance form 1.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD1_res2",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S}
4    C u0 p0 c0 {2,D} {7,S}
5 *2 C u0 p0 c0 {1,S} {9,D}
6    C u0 p0 c0 {2,S} {8,D}
7 *1 C u1 p0 c0 {3,S} {4,S}
8    C u0 p0 c0 {6,D} {9,S}
9 *3 C u0 p0 c0 {5,D} {8,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 5-membered ring tricyclic.
Resonance form 2.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD2_res1",
    group = 
"""
1 *2 C u0 p0 c0 {2,S} {3,S} {5,D}
2    C u0 p0 c0 {1,S} {4,S} {6,D}
3 *1 C u1 p0 c0 {1,S} {7,S}
4    C u0 p0 c0 {2,S} {7,D}
5 *3 C u0 p0 c0 {1,D} {9,S}
6    C u0 p0 c0 {2,D} {8,S}
7    C u0 p0 c0 {3,S} {4,D}
8    C u0 p0 c0 {6,S} {9,D}
9    C u0 p0 c0 {5,S} {8,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 3-membered ring tricyclic.
Resonance form 1.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD2_res2",
    group = 
"""
1 *2 C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,S} {6,D}
3 *3 C u0 p0 c0 {1,D} {7,S}
4    C u0 p0 c0 {2,S} {7,D}
5 *1 C u1 p0 c0 {1,S} {9,S}
6    C u0 p0 c0 {2,D} {8,S}
7    C u0 p0 c0 {3,S} {4,D}
8    C u0 p0 c0 {6,S} {9,D}
9    C u0 p0 c0 {5,S} {8,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 3-membered ring tricyclic.
Resonance form 2.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD2_res3",
    group = 
"""
1    C u0 p0 c0 {2,D} {3,S} {5,S}
2    C u0 p0 c0 {1,D} {4,S} {6,S}
3 *1 C u1 p0 c0 {1,S} {7,S}
4    C u0 p0 c0 {2,S} {7,D}
5 *3 C u0 p0 c0 {1,S} {9,D}
6    C u0 p0 c0 {2,S} {8,D}
7    C u0 p0 c0 {3,S} {4,D}
8    C u0 p0 c0 {6,D} {9,S}
9 *2 C u0 p0 c0 {5,D} {8,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 3-membered ring tricyclic.
Resonance form 3.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD3_res1",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,S} {5,D}
2    C u0 p0 c0 {1,S} {4,S} {6,D}
3 *1 C u1 p0 c0 {1,S} {7,S}
4 *3 C u0 p0 c0 {2,S} {7,D}
5    C u0 p0 c0 {1,D} {9,S}
6    C u0 p0 c0 {2,D} {8,S}
7 *2 C u0 p0 c0 {3,S} {4,D}
8    C u0 p0 c0 {6,S} {9,D}
9    C u0 p0 c0 {5,S} {8,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,4, and 3-membered ring tricyclic.
Resonance form 1.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD3_res2",
    group = 
"""
1    C u0 p0 c0 {2,D} {3,S} {5,S}
2    C u0 p0 c0 {1,D} {4,S} {6,S}
3 *1 C u1 p0 c0 {1,S} {7,S}
4 *3 C u0 p0 c0 {2,S} {7,D}
5    C u0 p0 c0 {1,S} {9,D}
6    C u0 p0 c0 {2,S} {8,D}
7 *2 C u0 p0 c0 {3,S} {4,D}
8    C u0 p0 c0 {6,D} {9,S}
9    C u0 p0 c0 {5,D} {8,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,4, and 3-membered ring tricyclic.
Resonance form 2.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD3_res3",
    group = 
"""
1    C u0 p0 c0 {2,B} {3,S} {5,B}
2    C u0 p0 c0 {1,B} {4,S} {6,B}
3 *1 C u1 p0 c0 {1,S} {7,S}
4 *3 C u0 p0 c0 {2,S} {7,D}
5    C u0 p0 c0 {1,B} {9,B}
6    C u0 p0 c0 {2,B} {8,B}
7 *2 C u0 p0 c0 {3,S} {4,D}
8    C u0 p0 c0 {6,B} {9,B}
9    C u0 p0 c0 {5,B} {8,B}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,4, and 3-membered ring tricyclic.
Resonance form3.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD4_res1",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,S} {6,D}
3    C u0 p0 c0 {1,D} {7,S}
4 *2 C u0 p0 c0 {2,S} {7,D}
5 *1 C u1 p0 c0 {1,S} {9,S}
6    C u0 p0 c0 {2,D} {8,S}
7 *3 C u0 p0 c0 {3,S} {4,D}
8    C u0 p0 c0 {6,S} {9,D}
9    C u0 p0 c0 {5,S} {8,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 4-membered ring tricyclic.
Resonance form 1.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD4_res2",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S}
4    C u0 p0 c0 {2,D} {7,S}
5 *3 C u0 p0 c0 {1,S} {9,D}
6    C u0 p0 c0 {2,S} {8,D}
7 *1 C u1 p0 c0 {3,S} {4,S}
8    C u0 p0 c0 {6,D} {9,S}
9 *2 C u0 p0 c0 {5,D} {8,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 4-membered ring tricyclic.
Resonance form 2.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD5_res1",
    group = 
"""
1    C u0 {2,S} {3,S} {6,D}
2    C u0 {1,S} {4,S} {5,D}
3    C u0 {1,S} {7,S}
4 *2 C u0 {2,S} {7,D}
5    C u0 {2,D} {8,S}
6    C u0 {1,D} {9,S}
7 *3 C u0 {3,S} {4,D}
8    C u0 {5,S} {9,D}
9 *1 C u1 {6,S} {8,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from  ring-closing to form a highly strained tricyclic. Resonance form 1.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD5_res2",
    group = 
"""
1    C u0 {2,B} {3,S} {6,B}
2    C u0 {1,B} {4,S} {5,B}
3    C u0 {1,S} {7,S}
4 *2 C u0 {2,S} {7,D}
5    C u0 {2,B} {8,B}
6    C u0 {1,B} {9,B}
7 *3 C u0 {3,S} {4,D}
8    C u0 {5,B} {9,B}
9 *1 C u1 {6,B} {8,B}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid an indenyl radical from  ring-closing to form a highly strained tricyclic. Resonance form 2.
""",
)

forbidden(
    label = "Rn0c6_beta_long_phenyl",
    group = 
"""
1 *1 C u1 {2,[D,B]} {6,[S,B]}
2    C u0 {1,[D,B]} {3,[S,B]}
3 *3 C u0 {2,[S,B]} {4,[D,B]}
4 *2 C u0 {3,[D,B]} {5,[S,B]}
5    C u0 {4,[S,B]} {6,[D,B]}
6    C u0 {1,[S,B]} {5,[D,B]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a phenyl radical from doing a ring closure on itself to form a fused 3 and 5 membered ring.
""",
)

forbidden(
    label = "Rn0c6_beta_short_phenyl",
    group = 
"""
1 *1 C u1 {2,[S,B]} {6,[D,B]}
2 *2 C u0 {1,[S,B]} {3,[D,B]}
3 *3 C u0 {2,[D,B]} {4,[S,B]}
4    C u0 {3,[S,B]} {5,[D,B]}
5    C u0 {4,[D,B]} {6,[S,B]}
6    C u0 {1,[D,B]} {5,[S,B]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a phenyl radical from doing a ring closure on itself to form a fused 3 and 5 membered ring.
""",
)

forbidden(
    label = "Rn0c6_gamma_phenyl",
    group = 
"""
1 *1 C u1 {2,[D,B]} {6,[S,B]}
2    C u0 {1,[D,B]} {3,[S,B]}
3 *2 C u0 {2,[S,B]} {4,[D,B]}
4 *3 C u0 {3,[D,B]} {5,[S,B]}
5    C u0 {4,[S,B]} {6,[D,B]}
6    C u0 {1,[S,B]} {5,[D,B]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a phenyl radical from doing a ring closure on itself to form a fused 4 and 4 membered ring.
""",
)

forbidden(
    label = "Rn1c6_beta_long_phenyl",
    group = 
"""
1 *4 C u0 {2,[D,B]} {3,[S,B]} {7,S}
2    C u0 {1,[D,B]} {4,[S,B]}
3 *2 C u0 {1,[S,B]} {5,[D,B]}
4    C u0 {2,[S,B]} {6,[D,B]}
5 *3 C u0 {3,[D,B]} {6,[S,B]}
6    C u0 {4,[D,B]} {5,[S,B]}
7 *1 C u1 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a carbon radical 1 carbon away from a phenyl side group from adding to the meta-position 
because the TS would be far too strained.
""",
)

forbidden(
    label = "Rn1c6_beta_short_phenyl",
    group = 
"""
1 *4 C u0 {2,[D,B]} {3,[S,B]} {7,S}
2    C u0 {1,[D,B]} {4,[S,B]}
3 *2 C u0 {1,[S,B]} {5,[D,B]}
4    C u0 {2,[S,B]} {6,[D,B]}
5 *3 C u0 {3,[D,B]} {6,[S,B]}
6    C u0 {4,[D,B]} {5,[S,B]}
7 *1 C u1 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a carbon radical 1 carbon away from a phenyl side group from adding to the meta-position 
because the TS would be far too strained.
""",
)

forbidden(
    label = "Rn1c6_gamma_phenyl",
    group = 
"""
1 *4 C u0 {2,[D,B]} {3,[S,B]} {7,S}
2 *5 C u0 {1,[D,B]} {4,[S,B]}
3    C u0 {1,[S,B]} {5,[D,B]}
4 *2 C u0 {2,[S,B]} {6,[D,B]}
5    C u0 {3,[D,B]} {6,[S,B]}
6 *3 C u0 {4,[D,B]} {5,[S,B]}
7 *1 C u1 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a carbon radical 1 carbon away from a phenyl side group from adding to the para-position 
because the TS would be far too strained.
""",
)

forbidden(
    label = "Rn2c6_beta_long_phenyl",
    group = 
"""
1 *6 C u0 {2,[S,B]} {3,[D,B]} {6,S}
2 *7 C u0 {1,[S,B]} {4,[D,B]}
3    C u0 {1,[D,B]} {5,[S,B]}
4 *5 C u0 {2,[D,B]} {7,[S,B]}
5 *3 C u0 {3,[S,B]} {7,[D,B]}
6 *4 C u0 {1,S} {8,[S,D,T]}
7 *2 C u0 {4,[S,B]} {5,[D,B]}
8 *1 C u1 {6,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a carbon radical 2 carbons away from a phenyl side group from adding to the meta-position 
because the TS would be far too strained.
""",
)

forbidden(
    label = "Rn2c6_beta_short_phenyl",
    group = 
"""
1 *5 C u0 {2,[D,B]} {3,[S,B]} {6,S}
2    C u0 {1,[D,B]} {4,[S,B]}
3 *2 C u0 {1,[S,B]} {5,[D,B]}
4    C u0 {2,[S,B]} {7,[D,B]}
5 *3 C u0 {3,[D,B]} {7,[S,B]}
6 *4 C u0 {1,S} {8,[S,D,T]}
7    C u0 {4,[D,B]} {5,[S,B]}
8 *1 C u1 {6,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a carbon radical 2 carbons away from a phenyl side group from adding to the meta-position 
because the TS would be far too strained.
""",
)

forbidden(
    label = "Rn2c6_gamma_phenyl",
    group = 
"""
1 *6 C u0 {2,[D,B]} {3,[S,B]} {6,S}
2 *5 C u0 {1,[D,B]} {4,[S,B]}
3    C u0 {1,[S,B]} {5,[D,B]}
4 *2 C u0 {2,[S,B]} {7,[D,B]}
5    C u0 {3,[D,B]} {7,[S,B]}
6 *4 C u0 {1,S} {8,[S,D,T]}
7 *3 C u0 {4,[D,B]} {5,[S,B]}
8 *1 C u1 {6,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a carbon radical 2 carbons away from a phenyl side group from adding to the para-position 
because the TS would be far too strained.
""",
)

forbidden(
    label = "Rn3c6_beta_long_phenyl",
    group = 
"""
1 *7 C u0 {2,[S,B]} {3,[D,B]} {4,S}
2 *8 C u0 {1,[S,B]} {5,[D,B]}
3    C u0 {1,[D,B]} {6,[S,B]}
4 *6 C u0 {1,S} {8,[S,D,T]}
5 *5 C u0 {2,[D,B]} {7,[S,B]}
6 *3 C u0 {3,[S,B]} {7,[D,B]}
7 *2 C u0 {5,[S,B]} {6,[D,B]}
8 *4 C u0 {4,[S,D,T]} {9,[S,D,T]}
9 *1 C u1 {8,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a carbon radical 3 carbons away from a phenyl side group from adding to the meta-position 
because the TS would be far too strained.
""",
)

forbidden(
    label = "Rn3c6_beta_short_phenyl",
    group = 
"""
1 *5 C u0 {2,[D,B]} {3,[S,B]} {4,S}
2    C u0 {1,[D,B]} {5,[S,B]}
3 *2 C u0 {1,[S,B]} {6,[D,B]}
4 *6 C u0 {1,S} {8,[S,D,T]}
5    C u0 {2,[S,B]} {7,[D,B]}
6 *3 C u0 {3,[D,B]} {7,[S,B]}
7    C u0 {5,[D,B]} {6,[S,B]}
8 *4 C u0 {4,[S,D,T]} {9,[S,D,T]}
9 *1 C u1 {8,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a carbon radical 3 carbons away from a phenyl side group from adding to the meta-position 
because the TS would be far too strained.
""",
)

forbidden(
    label = "Rn3c6_gamma_phenyl",
    group = 
"""
1 *7 C u0 {2,[S,B]} {3,[D,B]} {4,S}
2    C u0 {1,[S,B]} {5,[D,B]}
3 *5 C u0 {1,[D,B]} {6,[S,B]}
4 *6 C u0 {1,S} {8,[S,D,T]}
5    C u0 {2,[D,B]} {7,[S,B]}
6 *2 C u0 {3,[S,B]} {7,[D,B]}
7 *3 C u0 {5,[S,B]} {6,[D,B]}
8 *4 C u0 {4,[S,D,T]} {9,[S,D,T]}
9 *1 C u1 {8,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid a carbon radical 3 carbons away from a phenyl side group from adding to the para-position 
because the TS would be far too strained.
""",
)

forbidden(
    label = "bond31",
    group = 
"""
1 *3 R!H u0 c0 {2,[S,D]}
2 *1 R!H u1 {1,[S,D]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "bond31rad",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *1 R!H u1 {1,[S,D]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "product34_to_product57",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,S} {4,S}
2    C u0 p0 c0 {1,S} {3,S} {5,S}
3 *1 C u1 p0 c0 {1,S} {2,S}
4 *3 C u0 p0 c0 {1,S} {6,D}
5    C u0 p0 c0 {2,S} {7,D}
6 *2 C u0 p0 c0 {4,D} {7,S}
7    C u0 p0 c0 {5,D} {6,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid product34 in vinylCPD_H library from ring closing to form a fused 6, 3, and 3-membered ring tricyclic.
""",
)

forbidden(
    label = "product45_to_product56",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,S} {5,S}
2    C u0 p0 c0 {1,S} {4,S} {6,S}
3 *2 C u0 p0 c0 {1,S} {4,D}
4 *3 C u0 p0 c0 {2,S} {3,D}
5    C u0 p0 c0 {1,S} {7,D}
6 *1 C u1 p0 c0 {2,S} {7,S}
7    C u0 p0 c0 {5,D} {6,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Forbid product45 in vinylCPD_H library from ring closing to form a fused 5, 4, and 3-membered ring tricyclic.
""",
)

forbidden(
    label = "s2_3_6_diene_0_2_self_ring_close_1_res_1",
    group = 
"""
1    C u0 {2,S} {3,S} {4,[S,D]}
2    C u0 {1,S} {3,S} {5,[S,D]}
3 *1 C u1 {1,S} {2,S}
4    C u0 {1,[S,D]} {6,S}
5    C u0 {2,[S,D]} {7,S}
6 *3 C u0 {4,S} {7,D}
7 *2 C u0 {5,S} {6,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Prevent a s2_3_6_diene_0_2 bicyclic (using polycyclic.py nomenclature) from undergoing a highly strained self-ring closure 
from the tip of the 3-member ring to one of the far corners of the 6. Resonance form 1.
""",
)

forbidden(
    label = "s2_3_6_diene_0_2_self_ring_close_1_res_2",
    group = 
"""
1 *2 C u0 {2,S} {3,D} {4,S}
2    C u0 {1,S} {3,S} {5,S}
3 *3 C u0 {1,D} {2,S}
4    C u0 {1,S} {6,D}
5    C u0 {2,S} {7,S}
6    C u0 {4,D} {7,S}
7 *1 C u1 {5,S} {6,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Prevent a s2_3_6_diene_0_2 bicyclic (using polycyclic.py nomenclature) from undergoing a highly strained self-ring closure 
from the tip of the 3-member ring to one of the far corners of the 6. Resonance form 2.
""",
)

forbidden(
    label = "s2_4_5_diene_1_5_self_ring_close_res1",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,S} {5,D}
2    C u0 p0 c0 {1,S} {4,S} {6,S}
3 *3 C u0 p0 c0 {1,S} {4,D}
4 *2 C u0 p0 c0 {2,S} {3,D}
5    C u0 p0 c0 {1,D} {7,S}
6    C u0 p0 c0 {2,S} {7,S}
7 *1 C u1 p0 c0 {5,S} {6,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Prevent a s2_4_5_diene_1_5 bicyclic (using polycyclic.py nomenclature) from undergoing a highly strained self-ring closure 
from the tip of the 5-member ring to the corner of the 4. Resonance form 1.
""",
)

forbidden(
    label = "s2_4_5_diene_1_5_self_ring_close_res2",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,S} {5,D}
2    C u0 p0 c0 {1,S} {4,S} {6,S}
3 *2 C u0 p0 c0 {1,S} {4,D}
4 *3 C u0 p0 c0 {2,S} {3,D}
5    C u0 p0 c0 {1,D} {7,S}
6    C u0 p0 c0 {2,S} {7,S}
7 *1 C u1 p0 c0 {5,S} {6,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Prevent a s2_4_5_diene_1_5 bicyclic (using polycyclic.py nomenclature) from undergoing a highly strained self-ring closure 
from the tip of the 5-member ring to the corner of the 4. Resonance form 2.
""",
)

forbidden(
    label = "s2_4_5_diene_1_5_self_ring_close_res3",
    group = 
"""
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,S} {6,S}
3    C u0 p0 c0 {1,D} {4,S}
4 *1 C u1 p0 c0 {2,S} {3,S}
5 *2 C u0 p0 c0 {1,S} {7,D}
6    C u0 p0 c0 {2,S} {7,S}
7 *3 C u0 p0 c0 {5,D} {6,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Prevent a s2_4_5_diene_1_5 bicyclic (using polycyclic.py nomenclature) from undergoing a highly strained self-ring closure 
from the tip of the 5-member ring to the corner of the 4. Resonance form 3.
""",
)

