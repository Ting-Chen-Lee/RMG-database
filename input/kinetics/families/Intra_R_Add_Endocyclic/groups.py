#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Endocyclic/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Rn"], products=["RnCyclic"], ownReverse=False)

reverse = "Ring_Open_Endo_Cycli_Radical"

recipe(actions=[
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*1', '1'],
])

boundaryAtoms = ["*1", "*2"]

entry(
    index = 1,
    label = "Rn",
    group = "OR{Rnx_cyclics, R3, R4, R5, R6plus}",
    kinetics = None,
)

entry(
    index = 2,
    label = "multiplebond_intra",
    group =
"""
1 *2 [Cd,Cdd,Ct,CO,N,CS]  u0 {2,[D,T]}
2 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {1,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "radadd_intra",
    group = 
"""
1 *1 R!H u1
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "R3",
    group = 
"""
1 *1 R!H                  u1 {2,S}
2 *2 [Cd,Ct,CO,N,CS]      u0 {1,S} {3,[D,T]}
3 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "R3_D",
    group = 
"""
1 *1 R!H      u1 {2,S}
2 *2 Cd       u0 {1,S} {3,D}
3 *3 [Cd,Cdd] u0 px c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "R3_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *2 Ct  u0 {1,S} {3,T}
3 *3 Ct  u0 px c0 {2,T}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "R3_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *2 CO  u0 {1,S} {3,D}
3 *3 O2d  u0 px c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "R3_CS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *2 CS  u0 {1,S} {3,D}
3 *3 S2d u0 p2 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "R4",
    group = 
"""
1 *1 R!H                  u1 {2,[S,D,T,B]}
2 *4 R!H                  ux {1,[S,D,T,B]} {3,S}
3 *2 [Cd,Ct,CO,N,CS]      u0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "R4_S",
    group = 
"""
1 *1 R!H                u1 {2,S}
2 *4 R!H                u0 {1,S} {3,S}
3 *2 [Cd,Ct,CO,CS]      u0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,O2d,S2d,Cdd] u0 px c0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "R4_S_D",
    group = 
"""
1 *1 R!H      u1 {2,S}
2 *4 R!H      u0 {1,S} {3,S}
3 *2 Cd       u0 {2,S} {4,D}
4 *3 [Cd,Cdd] u0 px c0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 180,
    label = "R4_Cs_RR_D",
    group = 
"""
1 *1 Cs       u1 {2,S}
2 *4 Cs       u0 {1,S} {3,S} {5,S} {6,S}
3 *2 Cd       u0 {2,S} {4,D}
4 *3 [Cd,Cdd] u0 px c0 {3,D}
5    R        u0 {2,S}
6    R        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 181,
    label = "R4_Cs_HH_D",
    group = 
"""
1 *1 Cs       u1 {2,S}
2 *4 Cs       u0 {1,S} {3,S} {5,S} {6,S}
3 *2 Cd       u0 {2,S} {4,D}
4 *3 [Cd,Cdd] u0 px c0 {3,D}
5    H        u0 {2,S}
6    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "R4_S_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *2 Ct  u0 {2,S} {4,T}
4 *3 Ct  u0 px c0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "R4_S_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *2 CO  u0 {2,S} {4,D}
4 *3 O2d  u0 px c0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 170,
    label = "R4_S_CS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *2 CS  u0 {2,S} {4,D}
4 *3 S2d u0 px c0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "R4_D",
    group = 
"""
1 *1 Cd                 u1 {2,D}
2 *4 Cd                 u0 {1,D} {3,S}
3 *2 [Cd,Ct,CO,CS]      u0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,O2d,S2d,Cdd] u0 px c0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "R4_D_D",
    group = 
"""
1 *1 Cd       u1 {2,D}
2 *4 Cd       u0 {1,D} {3,S}
3 *2 Cd       u0 {2,S} {4,D}
4 *3 [Cd,Cdd] u0 px c0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "R4_D_T",
    group = 
"""
1 *1 Cd u1 {2,D}
2 *4 Cd u0 {1,D} {3,S}
3 *2 Ct u0 {2,S} {4,T}
4 *3 Ct u0 px c0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "R4_D_CO",
    group = 
"""
1 *1 Cd u1 {2,D}
2 *4 Cd u0 {1,D} {3,S}
3 *2 CO u0 {2,S} {4,D}
4 *3 O2d u0 px c0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 171,
    label = "R4_D_CS",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *2 CS  u0 {2,S} {4,D}
4 *3 S2d u0 px c0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "R4_T",
    group = 
"""
1 *1 Ct                 u1 {2,T}
2 *4 Ct                 u0 {1,T} {3,S}
3 *2 [Cd,Ct,CO,CS]      u0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,O2d,S2d,Cdd] u0 px c0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "R4_T_D",
    group = 
"""
1 *1 Ct       u1 {2,T}
2 *4 Ct       u0 {1,T} {3,S}
3 *2 Cd       u0 {2,S} {4,D}
4 *3 [Cd,Cdd] u0 px c0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "R4_T_T",
    group = 
"""
1 *1 Ct u1 {2,T}
2 *4 Ct u0 {1,T} {3,S}
3 *2 Ct u0 {2,S} {4,T}
4 *3 Ct u0 px c0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "R4_T_CO",
    group = 
"""
1 *1 Ct u1 {2,T}
2 *4 Ct u0 {1,T} {3,S}
3 *2 CO u0 {2,S} {4,D}
4 *3 O2d u0 px c0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 172,
    label = "R4_T_CS",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *2 CS  u0 {2,S} {4,D}
4 *3 S2d u0 px c0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "R5",
    group = 
"""
1 *1 R!H                   u1 {2,[S,D,T,B]}
2 *4 R!H                   ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *5 R!H                   ux {2,[S,D,T,B]} {4,[S,D]}
4 *2 [Cd,Ct,CO,N,CS,Cdd]   u0 {3,[S,D]} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
""",
)

entry(
    index = 27,
    label = "R5_SS",
    group = 
"""
1 *1 R!H                  u1 {2,S}
2 *4 R!H                  u0 {1,S} {3,S}
3 *5 R!H                  u0 {2,S} {4,S}
4 *2 [Cd,Ct,CO,N,CS]      u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, single.
""",
)

entry(
    index = 28,
    label = "R5_SS_D",
    group = 
"""
1 *1 R!H      u1 {2,S}
2 *4 R!H      u0 {1,S} {3,S}
3 *5 R!H      u0 {2,S} {4,S}
4 *2 Cd       u0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 px c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 182,
    label = "R5_CsCs_RR_D",
    group = 
"""
1 *1 Cs       u1 {2,S}
2 *4 Cs       u0 {1,S} {3,S} {6,S} {7,S}
3 *5 Cs       u0 {2,S} {4,S} {8,S} {9,S}
4 *2 Cd       u0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 px c0 {4,D}
6    R        u0 {2,S}
7    R        u0 {2,S}
8    R        u0 {3,S}
9    R        u0 {3,S}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 carbon atoms.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 183,
    label = "R5_CsCs_RH_D",
    group = 
"""
1 *1 Cs       u1 {2,S}
2 *4 Cs       u0 {1,S} {3,S} {6,S} {7,S}
3 *5 Cs       u0 {2,S} {4,S} {8,S} {9,S}
4 *2 Cd       u0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 px c0 {4,D}
6    R        u0 {2,S}
7    H        u0 {2,S}
8    R        u0 {3,S}
9    H        u0 {3,S}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 carbon atoms.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 184,
    label = "R5_CsCs_HH_D",
    group = 
"""
1 *1 Cs       u1 {2,S}
2 *4 Cs       u0 {1,S} {3,S} {6,S} {7,S}
3 *5 Cs       u0 {2,S} {4,S} {8,S} {9,S}
4 *2 Cd       u0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 px c0 {4,D}
6    H        u0 {2,S}
7    H        u0 {2,S}
8    H        u0 {3,S}
9    H        u0 {3,S}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 carbon atoms.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 29,
    label = "R5_SS_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 Ct  u0 {3,S} {5,T}
5 *3 Ct  u0 px c0 {4,T}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 30,
    label = "R5_SS_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CO  u0 {3,S} {5,D}
5 *3 O2d  u0 px c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 327,
    label = "R5_SS_CS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CS  u0 {3,S} {5,D}
5 *3 S2d u0 px c0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "Cs-R5_SS_CS",
    group = 
"""
1 *1 Cs  u1 {2,S} {6,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CS  u0 {3,S} {5,D}
5 *3 S2d u0 px c0 {4,D}
6    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "H2-R5_SS_CS",
    group = 
"""
1 *1 Cs  u1 {2,S} {6,S} {7,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CS  u0 {3,S} {5,D}
5 *3 S2d u0 px c0 {4,D}
6    H   u0 {1,S}
7    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "R5_SM",
    group = 
"""
1 *1 R!H                  u1 {2,S}
2 *4 [Cd,Ct,Cb]           u0 {1,S} {3,[D,T,B]}
3 *5 [Cd,Ct,Cb]           u0 {2,[D,T,B]} {4,S}
4 *2 [Cd,Ct,CO,N,CS]      u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "R5_SD",
    group = 
"""
1 *1 R!H                  u1 {2,S}
2 *4 Cd                   u0 {1,S} {3,D}
3 *5 Cd                   u0 {2,D} {4,S}
4 *2 [Cd,Ct,CO,N,CS]      u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then double. (The next is a single)
""",
)

entry(
    index = 32,
    label = "R5_SD_D",
    group = 
"""
1 *1 R!H      u1 {2,S}
2 *4 Cd       u0 {1,S} {3,D}
3 *5 Cd       u0 {2,D} {4,S}
4 *2 Cd       u0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 px c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then double. (The next is a single)
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 33,
    label = "R5_SD_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cd  u0 {1,S} {3,D}
3 *5 Cd  u0 {2,D} {4,S}
4 *2 Ct  u0 {3,S} {5,T}
5 *3 Ct  u0 px c0 {4,T}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then double. (The next is a single)
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 34,
    label = "R5_SD_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cd  u0 {1,S} {3,D}
3 *5 Cd  u0 {2,D} {4,S}
4 *2 CO  u0 {3,S} {5,D}
5 *3 O2d  u0 px c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then double. (The next is a single)
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 35,
    label = "R5_SD_CS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cd  u0 {1,S} {3,D}
3 *5 Cd  u0 {2,D} {4,S}
4 *2 CS  u0 {3,S} {5,D}
5 *3 S2d u0 px c0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "R5_ST",
    group = 
"""
1 *1 R!H                  u1 {2,S}
2 *4 Ct                   u0 {1,S} {3,T}
3 *5 Ct                   u0 {2,T} {4,S}
4 *2 [Cd,Ct,CO,N,CS]      u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then triple. (The next is a single)
""",
)

entry(
    index = 40,
    label = "R5_ST_D",
    group = 
"""
1 *1 R!H      u1 {2,S}
2 *4 Ct       u0 {1,S} {3,T}
3 *5 Ct       u0 {2,T} {4,S}
4 *2 Cd       u0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 px c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then triple. (The next is a single)
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 44,
    label = "R5_ST_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Ct  u0 {1,S} {3,T}
3 *5 Ct  u0 {2,T} {4,S}
4 *2 Ct  u0 {3,S} {5,T}
5 *3 Ct  u0 px c0 {4,T}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then triple. (The next is a single)
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 45,
    label = "R5_ST_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Ct  u0 {1,S} {3,T}
3 *5 Ct  u0 {2,T} {4,S}
4 *2 CO  u0 {3,S} {5,D}
5 *3 O2d  u0 px c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then triple. (The next is a single)
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 173,
    label = "R5_ST_CS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Ct  u0 {1,S} {3,T}
3 *5 Ct  u0 {2,T} {4,S}
4 *2 CS  u0 {3,S} {5,D}
5 *3 S2d u0 px c0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "R5_MS",
    group = 
"""
1 *1 [Cd,Ct,Cb]            u1 {2,[D,T,B]}
2 *4 [Cd,Ct,Cb]            u0 {1,[D,T,B]} {3,S}
3 *5 R!H                   u0 {2,S} {4,[S,D]}
4 *2 [Cd,Ct,CO,N,CS,Cdd]   u0 {3,[S,D]} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "R5_DS",
    group = 
"""
1 *1 Cd                   u1 {2,D}
2 *4 Cd                   u0 {1,D} {3,S}
3 *5 R!H                  u0 {2,S} {4,S}
4 *2 [Cd,Ct,CO,N,CS]      u0 {3,S} {5,[D,T]}
5 *3 [Cd,Cdd,Ct,O2d,S2d,N] u0 px c0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are double, then single. (The next is a single)
""",
)

entry(
    index = 36,
    label = "R5_DS_D",
    group = 
"""
1 *1 Cd       u1 {2,D}
2 *4 Cd       u0 {1,D} {3,S}
3 *5 R!H      u0 {2,S} {4,S}
4 *2 Cd       u0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 px c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are double, then single. (The next is a single)
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 37,
    label = "R5_DS_T",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 Ct  u0 {3,S} {5,T}
5 *3 Ct  u0 px c0 {4,T}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are double, then single. (The next is a single)
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 38,
    label = "R5_DS_CO",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CO  u0 {3,S} {5,D}
5 *3 O2d  u0 px c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are double, then single. (The next is a single)
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 44,
    label = "R5_DS_CS",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CS  u0 {3,S} {5,D}
5 *3 S2d u0 px c0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "R5_TS",
    group = 
"""
1 *1 Ct                   u1 {2,T}
2 *4 Ct                   u0 {1,T} {3,S}
3 *5 R!H                  u0 {2,S} {4,S}
4 *2 [Cd,Ct,CO,N,CS]      u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are triple, then single. (The next is a single)
""",
)

entry(
    index = 47,
    label = "R5_TS_D",
    group = 
"""
1 *1 Ct       u1 {2,T}
2 *4 Ct       u0 {1,T} {3,S}
3 *5 R!H      u0 {2,S} {4,S}
4 *2 Cd       u0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 px c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are triple, then single. (The next is a single)
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 48,
    label = "R5_TS_T",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 Ct  u0 {3,S} {5,T}
5 *3 Ct  u0 px c0 {4,T}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are triple, then single. (The next is a single)
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 49,
    label = "R5_TS_CO",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CO  u0 {3,S} {5,D}
5 *3 O2d  u0 px c0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are triple, then single. (The next is a single)
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 45,
    label = "R5_MM",
    group = 
"""
1 *1 [Cd,Cb]              u1 {2,[D,B]}
2 *4 [Cdd,Cbf]            u0 {1,[D,B]} {3,[D,B]}
3 *5 [Cd,Cb]              u0 {2,[D,B]} {4,S}
4 *2 [Cd,Ct,CO,N,CS]      u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "R6plus",
    group = "OR{R6, R7, R8, R9}",
    kinetics = None,
)

entry(
    index = 59,
    label = "R6",
    group = 
"""
1 *1 R!H                   u1 {2,[S,D,T,B]}
2 *4 R!H                   ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H                   ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *5 R!H                   ux {3,[S,D,T,B]} {5,[S,D]}
5 *2 [Cd,Ct,CO,N,CS,Cdd]   u0 {4,[S,D]} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "R6_RSR",
    group = 
"""
1 *1 R!H                  u1 {2,[S,D,T,B]}
2 *4 R!H                  u0 {1,[S,D,T,B]} {3,S}
3 *6 R!H                  u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H                  u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,N,CS]      u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "R6_SSR",
    group = 
"""
1 *1 R!H                u1 {2,S}
2 *4 R!H                u0 {1,S} {3,S}
3 *6 R!H                u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H                u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]      u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 px c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "R6_SSS",
    group = 
"""
1 *1 R!H                u1 {2,S}
2 *4 R!H                u0 {1,S} {3,S}
3 *6 R!H                u0 {2,S} {4,S}
4 *5 R!H                u0 {3,S} {5,S}
5 *2 [Cd,Ct,CO,CS]      u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 px c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "R6_SSS_D",
    group = 
"""
1 *1 R!H      u1 {2,S}
2 *4 R!H      u0 {1,S} {3,S}
3 *6 R!H      u0 {2,S} {4,S}
4 *5 R!H      u0 {3,S} {5,S}
5 *2 Cd       u0 {4,S} {6,D}
6 *3 [Cd,Cdd] u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 185,
    label = "R6_CsCsCs_RR_D",
    group = 
"""
1  *1 Cs       u1 {2,S}
2  *4 Cs       u0 {1,S} {3,S} {7,S} {8,S}
3  *6 Cs       u0 {2,S} {4,S} {9,S} {10,S}
4  *5 Cs       u0 {3,S} {5,S} {11,S} {12,S}
5  *2 Cd       u0 {4,S} {6,D}
6  *3 [Cd,Cdd] u0 px c0 {5,D}
7     R        u0 {2,S}
8     R        u0 {2,S}
9     R        u0 {3,S}
10    R        u0 {3,S}
11    R        u0 {4,S}
12    R        u0 {4,S}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 6 carbon atoms.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 186,
    label = "R6_CsCsCs_RH_D",
    group = 
"""
1  *1 Cs       u1 {2,S}
2  *4 Cs       u0 {1,S} {3,S} {7,S} {8,S}
3  *6 Cs       u0 {2,S} {4,S} {9,S} {10,S}
4  *5 Cs       u0 {3,S} {5,S} {11,S} {12,S}
5  *2 Cd       u0 {4,S} {6,D}
6  *3 [Cd,Cdd] u0 px c0 {5,D}
7     R        u0 {2,S}
8     H        u0 {2,S}
9     R        u0 {3,S}
10    H        u0 {3,S}
11    R        u0 {4,S}
12    H        u0 {4,S}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 6 carbon atoms.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 187,
    label = "R6_CsCsCs_HH_D",
    group = 
"""
1  *1 Cs       u1 {2,S}
2  *4 Cs       u0 {1,S} {3,S} {7,S} {8,S}
3  *6 Cs       u0 {2,S} {4,S} {9,S} {10,S}
4  *5 Cs       u0 {3,S} {5,S} {11,S} {12,S}
5  *2 Cd       u0 {4,S} {6,D}
6  *3 [Cd,Cdd] u0 px c0 {5,D}
7     H        u0 {2,S}
8     H        u0 {2,S}
9     H        u0 {3,S}
10    H        u0 {3,S}
11    H        u0 {4,S}
12    H        u0 {4,S}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 6 carbon atoms.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 64,
    label = "R6_SSS_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 Ct  u0 {4,S} {6,T}
6 *3 Ct  u0 px c0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "R6_SSS_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 CO  u0 {4,S} {6,D}
6 *3 O2d  u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "R6_SSM",
    group = 
"""
1 *1 R!H                u1 {2,S}
2 *4 R!H                u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb]         u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb]         u0 {3,[D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]      u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 px c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "R6_SSM_D",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Cd         u0 {4,S} {6,D}
6 *3 [Cd,Cdd]   u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "R6_SSM_T",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Ct         u0 {4,S} {6,T}
6 *3 Ct         u0 px c0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "R6_SSM_CO",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CO         u0 {4,S} {6,D}
6 *3 O2d         u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 174,
    label = "R6_SSM_CS",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CS         u0 {4,S} {6,D}
6 *3 S2d        u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "R6_MSR",
    group = 
"""
1 *1 [Cd,Ct,Cb]         u1 {2,[D,T,B]}
2 *4 [Cd,Ct,Cb]         u0 {1,[D,T,B]} {3,S}
3 *6 R!H                u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H                u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]      u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 px c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 163,
    label = "R6_MSR_D",
    group = 
"""
1 *1 [Cd,Ct,Cb]          u1 {2,[D,T,B]}
2 *4 [Cd,Ct,Cb]          u0 {1,[D,T,B]} {3,S}
3 *6 R!H                 u0 {2,S} {4,D}
4 *5 R!H                 u0 {3,D} {5,S}
5 *2 [Cd,Ct,CO,CS]       u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 px c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "R6_DSR",
    group = 
"""
1 *1 Cd                 u1 {2,D}
2 *4 Cd                 u0 {1,D} {3,S}
3 *6 R!H                u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H                u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]      u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 px c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "R6_DSS",
    group = 
"""
1 *1 Cd                 u1 {2,D}
2 *4 Cd                 u0 {1,D} {3,S}
3 *6 R!H                u0 {2,S} {4,S}
4 *5 R!H                u0 {3,S} {5,S}
5 *2 [Cd,Ct,CO,CS]      u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 px c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "R6_DSS_D",
    group = 
"""
1 *1 Cd       u1 {2,D}
2 *4 Cd       u0 {1,D} {3,S}
3 *6 R!H      u0 {2,S} {4,S}
4 *5 R!H      u0 {3,S} {5,S}
5 *2 Cd       u0 {4,S} {6,D}
6 *3 [Cd,Cdd] u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "R6_DSS_T",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 Ct  u0 {4,S} {6,T}
6 *3 Ct  u0 px c0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "R6_DSS_CO",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 CO  u0 {4,S} {6,D}
6 *3 O2d  u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "R6_DSM",
    group = 
"""
1 *1 Cd                 u1 {2,D}
2 *4 Cd                 u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb]         u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb]         u0 {3,[D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]      u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 px c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "R6_DSM_D",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Cd         u0 {4,S} {6,D}
6 *3 [Cd,Cdd]   u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "R6_DSM_T",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Ct         u0 {4,S} {6,T}
6 *3 Ct         u0 px c0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "R6_DSM_CO",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CO         u0 {4,S} {6,D}
6 *3 O2d         u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 156,
    label = "R6_DSM_CS",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CS         u0 {4,S} {6,D}
6 *3 S2d        u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "R6_TSR",
    group = 
"""
1 *1 Ct                 u1 {2,T}
2 *4 Ct                 u0 {1,T} {3,S}
3 *6 R!H                u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H                u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]      u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 px c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "R6_TSS",
    group = 
"""
1 *1 Ct                 u1 {2,T}
2 *4 Ct                 u0 {1,T} {3,S}
3 *6 R!H                u0 {2,S} {4,S}
4 *5 R!H                u0 {3,S} {5,S}
5 *2 [Cd,Ct,CO,CS]      u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 px c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "R6_TSS_D",
    group = 
"""
1 *1 Ct       u1 {2,T}
2 *4 Ct       u0 {1,T} {3,S}
3 *6 R!H      u0 {2,S} {4,S}
4 *5 R!H      u0 {3,S} {5,S}
5 *2 Cd       u0 {4,S} {6,D}
6 *3 [Cd,Cdd] u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "R6_TSS_T",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 Ct  u0 {4,S} {6,T}
6 *3 Ct  u0 px c0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "R6_TSS_CO",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 CO  u0 {4,S} {6,D}
6 *3 O2d  u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "R6_TSS_CS",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 CS  u0 {4,S} {6,D}
6 *3 S2d u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "R6_TSM",
    group = 
"""
1 *1 Ct                 u1 {2,T}
2 *4 Ct                 u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb]         u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb]         u0 {3,[D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]      u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 px c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "R6_TSM_D",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Cd         u0 {4,S} {6,D}
6 *3 [Cd,Cdd]   u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "R6_TSM_T",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Ct         u0 {4,S} {6,T}
6 *3 Ct         u0 px c0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "R6_TSM_CO",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CO         u0 {4,S} {6,D}
6 *3 O2d         u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "R6_TSM_CS",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CS         u0 {4,S} {6,D}
6 *3 S2d        u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "R6_SMS",
    group = 
"""
1 *1 R!H                   u1 {2,S}
2 *4 [Cd,Ct,Cb]            u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb]            u0 {2,[D,T,B]} {4,S}
4 *5 R!H                   u0 {3,S} {5,[S,D]}
5 *2 [Cd,Ct,CO,N,CS,Cdd]   u0 {4,[S,D]} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 98,
    label = "R6_SMS_D",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *5 R!H        u0 {3,S} {5,[S,D]}
5 *2 [Cd,Cdd]   u0 {4,[S,D]} {6,D}
6 *3 [Cd,Cdd]   u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 173,
    label = "R6_SBS_D",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,B}
3 *6 [Cd,Ct,Cb] u0 {2,B} {4,S}
4 *5 R!H        u0 {3,S} {5,[S,D]}
5 *2 [Cd,Cdd]   u0 {4,[S,D]} {6,D}
6 *3 [Cd,Cdd]   u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 189,
    label = "R6_SDS_D",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 Cd         u0 {1,S} {3,D}
3 *6 Cd	        u0 {2,D} {4,S}
4 *5 R!H        u0 {3,S} {5,[S,D]}
5 *2 [Cd,Cdd]   u0 {4,[S,D]} {6,D}
6 *3 [Cd,Cdd]   u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 99,
    label = "R6_SMS_T",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *5 R!H        u0 {3,S} {5,S}
5 *2 Ct         u0 {4,S} {6,T}
6 *3 Ct         u0 px c0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 100,
    label = "R6_SMS_CO",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *5 R!H        u0 {3,S} {5,S}
5 *2 CO         u0 {4,S} {6,D}
6 *3 O2d         u0 px c0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "R6_SMM",
    group = 
"""
1 *1 R!H            u1 {2,S}
2 *4 [Cd,Cb]        u0 {1,S} {3,[D,B]}
3 *6 [Cdd,Cbf]      u0 {2,[D,B]} {4,[D,B]}
4 *5 [Cd,Cb]        u0 {3,[D,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]  u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d] u0 px c0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 109,
    label = "R7",
    group = 
"""
1 *1 R!H                   u1 {2,[S,D,T,B]}
2 *4 R!H                   ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H                   ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H                   ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H                   ux {4,[S,D,T,B]} {6,S}
6 *2 [Cd,Ct,CO,N,CS]       u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 110,
    label = "R8",
    group = 
"""
1 *1 R!H                   u1 {2,[S,D,T,B]}
2 *4 R!H                   ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H                   ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H                   ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H                   ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H                   ux {5,[S,D,T,B]} {7,S}
7 *2 [Cd,Ct,CO,N,CS]       u0 {6,S} {8,[D,T]}
8 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {7,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 111,
    label = "R9",
    group = 
"""
1 *1 R!H                   u1 {2,[S,D,T,B]}
2 *4 R!H                   ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H                   ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H                   ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H                   ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *9 R!H                   ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *5 R!H                   ux {6,[S,D,T,B]} {8,S}
8 *2 [Cd,Ct,CO,N,CS]       u0 {7,S} {9,[D,T]}
9 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {8,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "R9_SSSSSD",
    group = 
"""
1 *1 R!H                  u1 {2,S}
2 *4 R!H                  u0 {1,S} {3,S}
3 *6 R!H                  u0 {2,S} {4,S}
4 *7 R!H                  u0 {3,S} {5,S}
5 *8 R!H                  u0 {4,S} {6,S}
6 *9 R!H                  u0 {5,S} {7,D}
7 *5 R!H                  u0 {6,D} {8,S}
8 *2 [Cd,Ct,CO,N,CS]      u0 {7,S} {9,[D,T]}
9 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {8,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "R9_SDSSSD",
    group = 
"""
1 *1 R!H                  u1 {2,S}
2 *4 R!H                  u0 {1,S} {3,D}
3 *6 R!H                  u0 {2,D} {4,S}
4 *7 R!H                  u0 {3,S} {5,S}
5 *8 R!H                  u0 {4,S} {6,S}
6 *9 R!H                  u0 {5,S} {7,D}
7 *5 R!H                  u0 {6,D} {8,S}
8 *2 [Cd,Ct,CO,N,CS]      u0 {7,S} {9,[D,T]}
9 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {8,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "doublebond_intra",
    group = 
"""
1 *2 [Cd,Cdd] u0 {2,D}
2 *3 [Cd,Cdd] u0 px c0 {1,D}
""",
    kinetics = None,
    longDesc = 
u"""
Note that nodes below this currently do not match allenic type Cdd atoms for *3,
so this is the most specific group that will match such a molecule.
""",
)

entry(
    index = 115,
    label = "doublebond_intra_pri",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S}
2 *3 Cd u0 px c0 {1,D}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "doublebond_intra_pri_2H",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S}
2 *3 Cd u0 px c0 {1,D} {4,S} {5,S}
3    H  u0 {1,S}
4    H  u0 {2,S}
5    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 117,
    label = "doublebond_intra_pri_HNd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 px c0 {1,D} {4,S} {5,S}
3    H        u0 {1,S}
4    H        u0 {2,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 118,
    label = "doublebond_intra_pri_HDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 px c0 {1,D} {4,S} {5,S}
3    H                u0 {1,S}
4    H                u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 119,
    label = "doublebond_intra_pri_HCd",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S}
2 *3 Cd u0 px c0 {1,D} {4,S} {5,S}
3    H  u0 {1,S}
4    H  u0 {2,S}
5    Cd u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "doublebond_intra_pri_HCt",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S}
2 *3 Cd u0 px c0 {1,D} {4,S} {5,S}
3    H  u0 {1,S}
4    H  u0 {2,S}
5    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 121,
    label = "doublebond_intra_pri_NdNd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 px c0 {1,D} {4,S} {5,S}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {2,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "doublebond_intra_pri_NdDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 px c0 {1,D} {4,S} {5,S}
3    H                u0 {1,S}
4    [Cs,O,S]         u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 123,
    label = "doublebond_intra_pri_NdCd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 px c0 {1,D} {4,S} {5,S}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {2,S}
5    Cd       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 124,
    label = "doublebond_intra_pri_NdCt",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 px c0 {1,D} {4,S} {5,S}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {2,S}
5    Ct       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 125,
    label = "doublebond_intra_pri_DeDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 px c0 {1,D} {4,S} {5,S}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 126,
    label = "doublebond_intra_secNd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 px c0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 127,
    label = "doublebond_intra_secNd_2H",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 px c0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    H        u0 {2,S}
5    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 128,
    label = "doublebond_intra_secNd_HNd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 px c0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    H        u0 {2,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 129,
    label = "doublebond_intra_secNd_HDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 px c0 {1,D} {4,S} {5,S}
3    [Cs,O,S]         u0 {1,S}
4    H                u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 130,
    label = "doublebond_intra_secNd_HCd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 px c0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    H        u0 {2,S}
5    Cd       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 131,
    label = "doublebond_intra_secNd_HCt",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 px c0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    H        u0 {2,S}
5    Ct       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 132,
    label = "doublebond_intra_secNd_NdNd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 px c0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {2,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 133,
    label = "doublebond_intra_secNd_NdDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 px c0 {1,D} {4,S} {5,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cs,O,S]         u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 134,
    label = "doublebond_intra_secNd_NdCd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 px c0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {2,S}
5    Cd       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 135,
    label = "doublebond_intra_secNd_NdCt",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 px c0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {2,S}
5    Ct       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 136,
    label = "doublebond_intra_secNd_DeDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 px c0 {1,D} {4,S} {5,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "doublebond_intra_secDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 px c0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 138,
    label = "doublebond_intra_secDe_2H",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 px c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {2,S}
5    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 139,
    label = "doublebond_intra_secDe_HNd",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 px c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {2,S}
5    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 140,
    label = "doublebond_intra_secDe_HDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 px c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 141,
    label = "doublebond_intra_secDe_HCd",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 px c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {2,S}
5    Cd               u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "doublebond_intra_secDe_HCt",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 px c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {2,S}
5    Ct               u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 143,
    label = "doublebond_intra_secDe_NdNd",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 px c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {2,S}
5    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 144,
    label = "doublebond_intra_secDe_NdDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 px c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 145,
    label = "doublebond_intra_secDe_NdCd",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 px c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {2,S}
5    Cd               u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 146,
    label = "doublebond_intra_secDe_NdCt",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 px c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {2,S}
5    Ct               u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 147,
    label = "doublebond_intra_secDe_DeDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 px c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "triplebond_intra",
    group = 
"""
1 *2 Ct u0 {2,T}
2 *3 Ct u0 px c0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 135,
    label = "triplebond_intra_H",
    group = 
"""
1 *2 Ct u0 {2,T}
2 *3 Ct u0 px c0 {1,T} {3,S}
3    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 136,
    label = "triplebond_intra_Nd",
    group = 
"""
1 *2 Ct       u0 {2,T}
2 *3 Ct       u0 px c0 {1,T} {3,S}
3    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "triplebond_intra_De",
    group = 
"""
1 *2 Ct               u0 {2,T}
2 *3 Ct               u0 px c0 {1,T} {3,S}
3    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 138,
    label = "carbonyl_intra",
    group = 
"""
1 *2 CO u0 {2,D}
2 *3 O2d u0 px c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 139,
    label = "carbonyl_intra_H",
    group = 
"""
1 *2 CO u0 {2,D} {3,S}
2 *3 O2d u0 px c0 {1,D}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 140,
    label = "carbonyl_intra_Nd",
    group = 
"""
1 *2 CO       u0 {2,D} {3,S}
2 *3 O2d       u0 px c0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 141,
    label = "carbonyl_intra_De",
    group = 
"""
1 *2 CO               u0 {2,D} {3,S}
2 *3 O2d               u0 px c0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "thiyl_intra",
    group = 
"""
1 *2 CS u0 {2,D}
2 *3 S2d u0 px c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 143,
    label = "thiyl_intra_H",
    group = 
"""
1 *2 CS u0 {2,D} {3,S}
2 *3 S2d u0 px c0 {1,D}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 144,
    label = "thiyl_intra_Nd",
    group = 
"""
1 *2 CS       u0 {2,D} {3,S}
2 *3 S2d      u0 px c0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 145,
    label = "thiyl_intra_De",
    group = 
"""
1 *2 CS               u0 {2,D} {3,S}
2 *3 S2d              u0 px c0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 146,
    label = "radadd_intra_cs",
    group = 
"""
1 *1 Cs u1
""",
    kinetics = None,
)

entry(
    index = 147,
    label = "radadd_intra_cs2H",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "radadd_intra_csHNd",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S}
2    H        u0 {1,S}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 149,
    label = "radadd_intra_csHDe",
    group = 
"""
1 *1 Cs               u1 {2,S} {3,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 172,
    label = "radadd_intra_csHCb",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "radadd_intra_csHCd",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cd u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 165,
    label = "radadd_intra_csHCt",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "radadd_intra_csNdNd",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S}
2    [Cs,O,S] u0 {1,S}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "radadd_intra_csNdDe",
    group = 
"""
1 *1 Cs               u1 {2,S} {3,S}
2    [Cs,O,S]         u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 168,
    label = "radadd_intra_csNdCd",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S}
2    [Cs,O,S] u0 {1,S}
3    Cd       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 169,
    label = "radadd_intra_csNdCt",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S}
2    [Cs,O,S] u0 {1,S}
3    Ct       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 170,
    label = "radadd_intra_csDeDe",
    group = 
"""
1 *1 Cs               u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 153,
    label = "radadd_intra_O",
    group = 
"""
1 *1 O u1
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "radadd_intra_S",
    group = 
"""
1 *1 S u1
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "radadd_intra_Cb",
    group = 
"""
1 *1 Cb u1
""",
    kinetics = None,
)

entry(
    index = 156,
    label = "radadd_intra_cdsingle",
    group = 
"""
1 *1 Cd u1 {2,S}
2    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "radadd_intra_cdsingleH",
    group = 
"""
1 *1 Cd u1 {2,S}
2    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "radadd_intra_cdsingleNd",
    group = 
"""
1 *1 Cd       u1 {2,S}
2    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 159,
    label = "radadd_intra_cdsingleDe",
    group = 
"""
1 *1 Cd               u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "radadd_intra_cddouble",
    group = 
"""
1 *1 Cd u1 {2,D}
2    Cd u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "radadd_intra_CO",
    group = 
"""
1 *1 CO u1 {2,D}
2    O  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "radadd_intra_Ct",
    group = 
"""
1 *1 Ct u1 {2,T}
2    Ct u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 163,
    label = "R6_DSB_T",
    group = 
"""
1 *1 Cd u1 {2,D}
2 *4 Cd u0 {1,D} {3,S}
3 *6 Cb u0 {2,S} {4,B}
4 *5 Cb u0 {3,B} {5,S}
5 *2 Ct u0 {4,S} {6,T}
6 *3 Ct u0 px c0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "Rn3c6_alpha",
    group = 
"""
1    R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2    R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1  R!H u1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]} {7,[S,D,T,B]}
7 *5 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *2 R!H u0 {7,[S,D,T,B]} {9,[D,T]}
9 *3 R!H u0 {8,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 165,
    label = "Rn2c6_alpha",
    group = 
"""
1    R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2    R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]} {8,[S,D,T,B]}
8 *2 R!H u0 {6,[S,D,T,B]} {9,[D,T]}
9 *3 R!H u0 {8,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "Rnxc6_alpha",
    group = "OR{Rn3c6_alpha, Rn2c6_alpha}",
    kinetics = None,
)

entry(
    index = 167,
    label = "Rnxc6",
    group = "OR{Rnxc6_alpha}",
    kinetics = None,
)

entry(
    index = 168,
    label = "Rnx_cyclics",
    group = "OR{Rnxc6, Rnxc5}",
    kinetics = None,
)

entry(
    index = 169,
    label = "radadd_intra_csH(CdCdCd)",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cd u0 {1,S} {4,D}
4    Cd u0 {3,D} {5,S}
5    Cd u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 170,
    label = "doublebond_intra_CdCdd",
    group = 
"""
1 *3 Cd       u0 px c0 {2,D}
2 *2 Cdd      u0 {1,D}
""",
    kinetics = None,
    longDesc = 
u"""
""",
)

entry(
    index = 171,
    label = "Rn3c6b_alpha",
    group = 
"""
1    Cd u0 {2,D} {6,S}
2    Cd u0 {1,D} {3,S}
3    Cd ux {2,S} {4,D}
4    Cd ux {3,D} {5,S}
5 *1 Cd u1 {4,S} {6,D}
6 *4 Cd ux {5,D} {1,S} {7,[S,D,T,B]}
7 *5 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *2 R!H u0 {7,[S,D,T,B]} {9,[D,T]}
9 *3 R!H u0 {8,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 109,
    label = "R7_SDSD_D",
    group =
"""
1 *1 R!H                 u1 {2,S}
2 *4 R!H                 ux {1,S} {3,D}
3 *6 R!H                 ux {2,D} {4,S}
4 *7 R!H                 ux {3,S} {5,D}
5 *5 R!H                 ux {4,D} {6,S}
6 *2 [Cd,Ct,CO,N,CS]     u0 {5,S} {7,D}
7 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "Rnxc5",
    group = "OR{Rnxc5_beta}",
    kinetics = None,
)

entry(
    index = 166,
    label = "Rnxc5_beta",
    group = "OR{Rn2c5_beta}",
    kinetics = None,
)

entry(
    index = 165,
    label = "Rn2c5_beta",
    group =
"""
1    R!H u0 {5,[S,D,T,B]} {2,[S,D,T,B]}
2    R!H ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *1 R!H u1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *5 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux {4,[S,D,T,B]} {1,[S,D,T,B]} {6,[S,D,T,B]}
6 *2 R!H u0 {5,[S,D,T,B]} {7,[D,T]}
7 *3 R!H u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "R6_SMS(M)_D",
    group =
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *5 R!H        u0 {3,S} {5,S} {7,[D,T,B]}
5 *2 Cd         u0 {4,S} {6,D}
6 *3 [Cd,Cdd]   u0 px c0 {5,D}
7    R!H        u0 {4,[D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "R5_SB",
    group =
"""
1 *1 R!H                 u1 {2,S}
2 *4 Cb                  u0 {1,S} {3,B}
3 *5 Cb                  u0 {2,B} {4,S}
4 *2 [Cd,Ct,CO,N,CS]     u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 px c0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 168,
    label = "R6_DSB_D",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 Cb u0 {2,S} {4,B}
4 *5 Cb u0 {3,B} {5,S}
5 *2 Cd         u0 {4,S} {6,D}
6 *3 [Cd,Cdd]   u0 px c0 {5,D}
""",
    kinetics = None,
)

tree(
"""
L1: Rn
    L2: R3
        L3: R3_D
        L3: R3_T
        L3: R3_CO
        L3: R3_CS
    L2: R4
        L3: R4_S
            L4: R4_S_D
                L5: R4_Cs_RR_D
                    L6: R4_Cs_HH_D
            L4: R4_S_T
            L4: R4_S_CO
            L4: R4_S_CS
        L3: R4_D
            L4: R4_D_D
            L4: R4_D_T
            L4: R4_D_CO
            L4: R4_D_CS
        L3: R4_T
            L4: R4_T_D
            L4: R4_T_T
            L4: R4_T_CO
            L4: R4_T_CS
    L2: R5
        L3: R5_SS
            L4: R5_SS_D
                L5: R5_CsCs_RR_D
                    L6: R5_CsCs_RH_D
                        L7: R5_CsCs_HH_D
            L4: R5_SS_T
            L4: R5_SS_CO
            L4: R5_SS_CS
                L5: Cs-R5_SS_CS
                L5: H2-R5_SS_CS
        L3: R5_SM
            L4: R5_SD
                L5: R5_SD_D
                L5: R5_SD_T
                L5: R5_SD_CO
                L5: R5_SD_CS
            L4: R5_ST
                L5: R5_ST_D
                L5: R5_ST_T
                L5: R5_ST_CO
                L5: R5_ST_CS
            L4: R5_SB
        L3: R5_MS
            L4: R5_DS
                L5: R5_DS_D
                L5: R5_DS_T
                L5: R5_DS_CO
                L5: R5_DS_CS
            L4: R5_TS
                L5: R5_TS_D
                L5: R5_TS_T
                L5: R5_TS_CO
        L3: R5_MM
    L2: R6plus
        L3: R6
            L4: R6_RSR
                L5: R6_SSR
                    L6: R6_SSS
                        L7: R6_SSS_D
                            L8: R6_CsCsCs_RR_D
                                L9: R6_CsCsCs_RH_D
                                    L10: R6_CsCsCs_HH_D
                        L7: R6_SSS_T
                        L7: R6_SSS_CO
                    L6: R6_SSM
                        L7: R6_SSM_D
                        L7: R6_SSM_T
                        L7: R6_SSM_CO
                        L7: R6_SSM_CS
                L5: R6_MSR
                    L6: R6_DSR
                        L7: R6_DSS
                            L8: R6_DSS_D
                            L8: R6_DSS_T
                            L8: R6_DSS_CO
                        L7: R6_DSM
                            L8: R6_DSM_D
                            	L9: R6_DSB_D
                            L8: R6_DSM_T
                            	L9: R6_DSB_T
                            L8: R6_DSM_CO
                            L8: R6_DSM_CS
                    L6: R6_TSR
                        L7: R6_TSS
                            L8: R6_TSS_D
                            L8: R6_TSS_T
                            L8: R6_TSS_CO
                            L8: R6_TSS_CS
                        L7: R6_TSM
                            L8: R6_TSM_D
                            L8: R6_TSM_T
                            L8: R6_TSM_CO
                            L8: R6_TSM_CS
                    L6: R6_MSR_D
            L4: R6_SMS
                L5: R6_SMS_D
                    L6: R6_SMS(M)_D
                    L6: R6_SDS_D
                    L6: R6_SBS_D
                L5: R6_SMS_T
                L5: R6_SMS_CO
            L4: R6_SMM
        L3: R7
            L4: R7_SDSD_D
        L3: R8
        L3: R9
            L4: R9_SSSSSD
            L4: R9_SDSSSD
    L2: Rnx_cyclics
        L3: Rnxc5
            L4: Rnxc5_beta
                L5: Rn2c5_beta
        L3: Rnxc6
            L4: Rnxc6_alpha
                L5: Rn3c6_alpha
                    L6: Rn3c6b_alpha
                L5: Rn2c6_alpha
L1: multiplebond_intra
    L2: doublebond_intra
        L3: doublebond_intra_CdCdd
        L3: doublebond_intra_pri
            L4: doublebond_intra_pri_2H
            L4: doublebond_intra_pri_HNd
            L4: doublebond_intra_pri_HDe
                L5: doublebond_intra_pri_HCd
                L5: doublebond_intra_pri_HCt
            L4: doublebond_intra_pri_NdNd
            L4: doublebond_intra_pri_NdDe
                L5: doublebond_intra_pri_NdCd
                L5: doublebond_intra_pri_NdCt
            L4: doublebond_intra_pri_DeDe
        L3: doublebond_intra_secNd
            L4: doublebond_intra_secNd_2H
            L4: doublebond_intra_secNd_HNd
            L4: doublebond_intra_secNd_HDe
                L5: doublebond_intra_secNd_HCd
                L5: doublebond_intra_secNd_HCt
            L4: doublebond_intra_secNd_NdNd
            L4: doublebond_intra_secNd_NdDe
                L5: doublebond_intra_secNd_NdCd
                L5: doublebond_intra_secNd_NdCt
            L4: doublebond_intra_secNd_DeDe
        L3: doublebond_intra_secDe
            L4: doublebond_intra_secDe_2H
            L4: doublebond_intra_secDe_HNd
            L4: doublebond_intra_secDe_HDe
                L5: doublebond_intra_secDe_HCd
                L5: doublebond_intra_secDe_HCt
            L4: doublebond_intra_secDe_NdNd
            L4: doublebond_intra_secDe_NdDe
                L5: doublebond_intra_secDe_NdCd
                L5: doublebond_intra_secDe_NdCt
            L4: doublebond_intra_secDe_DeDe
    L2: triplebond_intra
        L3: triplebond_intra_H
        L3: triplebond_intra_Nd
        L3: triplebond_intra_De
    L2: carbonyl_intra
        L3: carbonyl_intra_H
        L3: carbonyl_intra_Nd
        L3: carbonyl_intra_De
    L2: thiyl_intra
        L3: thiyl_intra_H
        L3: thiyl_intra_Nd
        L3: thiyl_intra_De
L1: radadd_intra
    L2: radadd_intra_cs
        L3: radadd_intra_cs2H
        L3: radadd_intra_csHNd
        L3: radadd_intra_csHDe
            L4: radadd_intra_csHCd
               L5: radadd_intra_csH(CdCdCd)
            L4: radadd_intra_csHCt
            L4: radadd_intra_csHCb
        L3: radadd_intra_csNdNd
        L3: radadd_intra_csNdDe
            L4: radadd_intra_csNdCd
            L4: radadd_intra_csNdCt
        L3: radadd_intra_csDeDe
    L2: radadd_intra_O
    L2: radadd_intra_S
    L2: radadd_intra_Cb
    L2: radadd_intra_cdsingle
        L3: radadd_intra_cdsingleH
        L3: radadd_intra_cdsingleNd
        L3: radadd_intra_cdsingleDe
    L2: radadd_intra_cddouble
    L2: radadd_intra_CO
    L2: radadd_intra_Ct
"""
)

forbidden(
    label = "bond31",
    group = 
"""
1 *3 R!H u0 px c0 {2,[S,D]}
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
    label = "mb_intra_Rxc3",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {3,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclics in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclics in this family.
""",
)

forbidden(
    label = "mb_intra_Rxc4",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {4,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *5 R!H ux {3,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclics in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclics in this family.
""",
)

forbidden(
    label = "mb_intra_Rxc5",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {5,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H ux {4,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclics in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclics in this family.
""",
)

forbidden(
    label = "mb_intra_Rxc6",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclics in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclics in this family.
""",
)

forbidden(
    label = "mb_intra_Rxc7",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *5 R!H ux {6,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclics in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclics in this family.
""",
)

forbidden(
    label = "mb_intra_Rxc8",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *5 R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclics in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclics in this family.
""",
)

forbidden(
    label = "mb_intra_R1c3_beta",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {3,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux {2,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclics in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclics in this family.
""",
)

forbidden(
    label = "mb_intra_R1c4_beta",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {4,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux {3,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclics in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclics in this family.
""",
)

forbidden(
    label = "mb_intra_R1c5_beta",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {5,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux {4,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclics in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclics in this family.
""",
)

forbidden(
    label = "mb_intra_R1c6_beta",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclics in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclics in this family.
""",
)

forbidden(
    label = "mb_intra_R1c7_beta",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux {6,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclics in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclics in this family.
""",
)

forbidden(
    label = "mb_intra_R1c8_beta",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclics in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclics in this family.
""",
)

forbidden(
    label = "mb_intra_Rxc6_aromatic",
    group =
"""
1 *2 R!H u0 {2,D} {6,S}
2 *3 R!H u0 {1,D} {3,S}
3    R!H ux {2,S} {4,D}
4    R!H ux {3,D} {5,S}
5    R!H ux {4,S} {6,D}
6    R!H ux {5,D} {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclics in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclics in this family.
""",
)

forbidden(
    label = "Phenyl_self_3_5_ring_close_res1",
    group =
"""
1 *1 C u1 {2,D} {6,S}
2    C u0 {1,D} {3,S}
3 *3 C u0 {2,S} {4,D}
4 *2 C u0 {3,D} {5,S}
5    C u0 {4,S} {6,D}
6    C u0 {1,S} {5,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a phenyl radical from doing a ring closure on itself to form a fused 3 and 5 membered ring. Resonance form 1.
""",
)

forbidden(
    label = "Phenyl_self_3_5_ring_close_res2",
    group =
"""
1 *1 C u1 {2,S} {6,D}
2 *2 C u0 {1,S} {3,D}
3 *3 C u0 {2,D} {4,S}
4    C u0 {3,S} {5,D}
5    C u0 {4,D} {6,S}
6    C u0 {1,D} {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a phenyl radical from doing a ring closure on itself to form a fused 3 and 5 membered ring. Resonance form 2.
""",
)

forbidden(
    label = "Phenyl_self_4_4_ring_close_res1",
    group =
"""
1 *1 C u1 {2,D} {6,S}
2    C u0 {1,D} {3,S}
3 *2 C u0 {2,S} {4,D}
4 *3 C u0 {3,D} {5,S}
5    C u0 {4,S} {6,D}
6    C u0 {1,S} {5,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a phenyl radical from doing a ring closure on itself to form a fused 4 and 4 membered ring. Resonance form 1.
""",
)

##########
#Forbidden groups below prevent cyclics of different sizes (x) from doing ring closures on themselves to form
#bicyclics (sizes y and z) that share two atoms. Labels are formatted as cx_self_y_z_ring_close. Only
#Intra_R_Add_Exo family will be allowed to undergo such reactions.

forbidden(
    label = "c4_self_3_3_ring_close",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {4,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 {3,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c5_self_3_4_ring_close",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {5,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 {4,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c5_self_4_3_ring_close",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {5,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c6_self_3_5_ring_close",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 {5,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c6_self_4_4_ring_close",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c6_self_5_3_ring_close",
    group =
"""
1 *3 R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c7_self_3_6_ring_close",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 {6,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c7_self_4_5_ring_close",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c7_self_5_4_ring_close",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c7_self_6_3_ring_close",
    group =
"""
1 *3 R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c8_self_3_7_ring_close",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 {7,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c8_self_4_6_ring_close",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c8_self_5_5_ring_close",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c8_self_6_4_ring_close",
    group =
"""
1 *3 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c8_self_7_3_ring_close",
    group =
"""
1 *3 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c9_self_3_8_ring_close",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {9,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 {8,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c9_self_4_7_ring_close",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {9,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux {8,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c9_self_5_6_ring_close",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {9,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux {8,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c9_self_6_5_ring_close",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {9,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux {8,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c9_self_7_4_ring_close",
    group =
"""
1 *3 R!H u0 {2,[D,T]} {9,[S,D,T,B]}
2 *2 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux {8,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c9_self_8_3_ring_close",
    group =
"""
1 *3 R!H u0 {2,[D,T]} {9,[S,D,T,B]}
2 *2 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux {8,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c10_self_3_9_ring_close",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {10,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1 R!H u1 {9,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c10_self_4_8_ring_close",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {10,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H ux {9,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c10_self_5_7_ring_close",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {10,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H ux {9,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c10_self_6_6_ring_close",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {10,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H ux {9,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c10_self_7_5_ring_close",
    group =
"""
1 *3 R!H u0 {2,[D,T]} {10,[S,D,T,B]}
2 *2 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H ux {9,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c10_self_8_4_ring_close",
    group =
"""
1 *3 R!H u0 {2,[D,T]} {10,[S,D,T,B]}
2 *2 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H ux {9,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)

forbidden(
    label = "c10_self_9_3_ring_close",
    group =
"""
1 *3 R!H u0 {2,[D,T]} {10,[S,D,T,B]}
2 *2 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H ux {9,[S,D,T,B]} {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
If we allow cyclic self ring closure in both this family and Intra_R_Add_Exocyclic then we will get unwanted
duplicate reactions. Therefore, we forbid all cyclic self ring-closure (up to 10-membered rings) in this family.
""",
)
##########
