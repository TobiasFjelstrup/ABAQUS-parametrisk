
##############################################################################
# Parametric ABAQUS model for boltgroup in Banedanmarks standard noise barrier
# Made by: TSFP
# First version: 0.1 30.09.2019
# Current version: 0.3 13.11.2019
#############################################################################

#Future parameters to be implemented: Adjustable mesh size, size of 
#"ConstrainedSketch dependant on geometry size."


#Imported functions necessary to make the ABAQUS script run.
# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *



#Missing features


Bf=400
Bt=400
Df=300
Dt=300
Tfod=25
Ttop=25
a=150
c=100
Lh=62
OEh=32
OEb=24.48
m=49.5
Hm=24
Lsp=50
Bsp=50
OEsp=32
Lb=230
Tsp=5

#post
h=152
b=160
t=8
r=15
d=6
Hp=300
e=29

#Pile
hp=210
bp=220
tp=11
rp=18
dp=7
Hpp=200
ep=0

#Half of bolt hole width
kk=16

#Distance between top and foot plate (tolerences should be included)
aind=110


#Parameter defining length of square used to construct bolt holes
Sh=(Lh-OEh)/2

#Help length to trim half circle in bolt hole
Ah=Sh-OEh/4

#Shear load divided by 6 (see Mathcad load) [N]
Pv=3588

#Moment divided by 6 and by h-t (see Mathcad load) [Nm]
PM=32243

#Pretensioning bolts [N]
Fp=158000

##############################################################################
 #                                   Footplate

#Footplate geometry definition. 
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1000.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(Bf/2, Df/2), 
    point2=(-Bf/2, -Df/2))

#Defining bolt hole size
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(Sh, kk), 
    point2=(-Sh, -kk))
mdb.models['Model-1'].sketches['__profile__'].ArcByCenterEnds(center=(Sh, 
    0.0), direction=CLOCKWISE, point1=(Sh, kk), point2=(Sh, -kk))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[8], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].EqualDistanceConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[4], entity2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[5], midpoint=
    mdb.models['Model-1'].sketches['__profile__'].vertices[8])
mdb.models['Model-1'].sketches['__profile__'].ArcByCenterEnds(center=(-Sh, 
    0.0), direction=COUNTERCLOCKWISE, point1=(-Sh, kk), point2=(-Sh, 
    -kk))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[9], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8])
mdb.models['Model-1'].sketches['__profile__'].EqualDistanceConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[6], entity2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[7], midpoint=
    mdb.models['Model-1'].sketches['__profile__'].vertices[9])

#Trimming away unessessary lines
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], point1=(
    -Sh, 0))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], point1=(
    Sh, 0))

#Moving bolt holes to correct positions
mdb.models['Model-1'].sketches['__profile__'].copyMove(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[9], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[11]), vector=(a,
    c))
mdb.models['Model-1'].sketches['__profile__'].copyMove(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[9], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[11]), vector=(a, 
    -c))
mdb.models['Model-1'].sketches['__profile__'].copyMove(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[9], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[11]), vector=(
    -a, c))
mdb.models['Model-1'].sketches['__profile__'].copyMove(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[9], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[11]), vector=(
    -a, -c))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[9], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[11], 
    mdb.models['Model-1'].sketches['__profile__'].constraints[43], 
    mdb.models['Model-1'].sketches['__profile__'].constraints[48], 
    mdb.models['Model-1'].sketches['__profile__'].constraints[53]))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Fodplade', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Fodplade'].BaseSolidExtrude(depth=Tfod, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']


##############################################################################
#                                    Topplate
#Footplate geometry definition. 
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1000.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(Bt/2, Dt/2), 
    point2=(-Bt/2, -Dt/2))

#Defining bolt hole size
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(kk, Sh), 
    point2=(-kk, -Sh))
mdb.models['Model-1'].sketches['__profile__'].ArcByCenterEnds(center=(0.0, 
    Sh), direction=COUNTERCLOCKWISE, point1=(kk, Sh), point2=(-kk, 
    Sh))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[8], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9])
mdb.models['Model-1'].sketches['__profile__'].EqualDistanceConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[7], entity2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[4], midpoint=
    mdb.models['Model-1'].sketches['__profile__'].vertices[8])
mdb.models['Model-1'].sketches['__profile__'].ArcByCenterEnds(center=(0.0, 
    -Sh), direction=CLOCKWISE, point1=(kk, -Sh), point2=(-kk, -Sh))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[9], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7])
mdb.models['Model-1'].sketches['__profile__'].EqualDistanceConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[5], entity2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[6], midpoint=
    mdb.models['Model-1'].sketches['__profile__'].vertices[9])

#Trimming away unessessary lines
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9], point1=(
    0, Sh))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], point1=(
    0, -Sh))

#Moving bolt holes to correct positions
mdb.models['Model-1'].sketches['__profile__'].copyMove(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[11]), vector=(a, 
    c))
mdb.models['Model-1'].sketches['__profile__'].copyMove(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[11]), vector=(
    -a, c))
mdb.models['Model-1'].sketches['__profile__'].copyMove(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[11]), vector=(
    -a, -c))
mdb.models['Model-1'].sketches['__profile__'].copyMove(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[11]), vector=(a, 
    -c))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[11], 
    mdb.models['Model-1'].sketches['__profile__'].constraints[48], 
    mdb.models['Model-1'].sketches['__profile__'].constraints[53]))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Topplade', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Topplade'].BaseSolidExtrude(depth=Ttop, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']


##############################################################################
#                                    Nut

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, 0.0), point1=(m/2, 0.0))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='nut', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['nut'].BaseSolidExtrude(depth=Hm, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

##############################################################################
#                                   Bolt

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, 0.0), point1=(OEb/2, 0.0))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='bolt', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['bolt'].BaseSolidExtrude(depth=Lb, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

##############################################################################
#                                    Washer

#mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=300.0)
#mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(Lsp/2, Bsp/2), 
#    point2=(-Lsp/2, -Bsp/2))
#mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
#    0.0, 0.0), point1=(OEh/2, 0.0))
#mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Washer', type=
#    DEFORMABLE_BODY)
#mdb.models['Model-1'].parts['Washer'].BaseSolidExtrude(depth=Tsp, sketch=
#    mdb.models['Model-1'].sketches['__profile__'])
#del mdb.models['Model-1'].sketches['__profile__']

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, 0.0), point1=(28.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, 0.0), point1=(OEb/2, 0.0))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Washer', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Washer'].BaseSolidExtrude(depth=Tsp, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

##############################################################################
#                                    Post
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=500.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-b/2, h/2), 
    point2=(b/2, h/2-t))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(d/2, h/2), 
    point2=(-d/2, -h/2+t))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-b/2, -h/2), 
    point2=(b/2, -h/2+t))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3], point1=(
    0, h/2-t))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9], point1=(
    0, h/2-t))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], point1=(
    0, -h/2+t))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[11], point1=(
    0, -h/2+t))
mdb.models['Model-1'].sketches['__profile__'].FilletByRadius(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[16], curve2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], nearPoint1=(
    -r, -h/2+t), nearPoint2=(-d/2, 
    -r), radius=r)
mdb.models['Model-1'].sketches['__profile__'].FilletByRadius(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], curve2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[17], nearPoint1=(
    d/2, -r), nearPoint2=(r, 
    -h/2+t), radius=r)
mdb.models['Model-1'].sketches['__profile__'].FilletByRadius(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], curve2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[15], nearPoint1=(
    d/2, r), nearPoint2=(r, 
    h/2-t), radius=r)
mdb.models['Model-1'].sketches['__profile__'].FilletByRadius(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], curve2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[14], nearPoint1=(
    -d/2, r), nearPoint2=(-r, 
    h/2-t), radius=r)
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='HE160A', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['HE160A'].BaseSolidExtrude(depth=Hp, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']


##############################################################################
#                                    Pile

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=500.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-bp/2, hp/2), 
    point2=(bp/2, hp/2-tp))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(dp/2, hp/2), 
    point2=(-dp/2, -hp/2+tp))
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-bp/2, -hp/2), 
    point2=(bp/2, -hp/2+tp))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3], point1=(
    0, hp/2-tp))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9], point1=(
    0, h/2-t))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], point1=(
    0, -hp/2+tp))
mdb.models['Model-1'].sketches['__profile__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[11], point1=(
    0, -hp/2+tp))
mdb.models['Model-1'].sketches['__profile__'].FilletByRadius(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[16], curve2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], nearPoint1=(
    -rp, -hp/2+tp), nearPoint2=(-dp/2, 
    -rp), radius=rp)
mdb.models['Model-1'].sketches['__profile__'].FilletByRadius(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], curve2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[17], nearPoint1=(
    dp/2, -rp), nearPoint2=(rp, 
    -hp/2+tp), radius=rp)
mdb.models['Model-1'].sketches['__profile__'].FilletByRadius(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], curve2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[15], nearPoint1=(
    dp/2, rp), nearPoint2=(rp, 
    hp/2-tp), radius=rp)
mdb.models['Model-1'].sketches['__profile__'].FilletByRadius(curve1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], curve2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[14], nearPoint1=(
    -dp/2, rp), nearPoint2=(-rp, 
    hp/2-tp), radius=rp)
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='HE200A', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['HE200A'].BaseSolidExtrude(depth=Hpp, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']


##############################################################################
#                         Connecting bolt with nuts

dis1=Hm+Tsp*2+Ttop

mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='bolt-1', part=
    mdb.models['Model-1'].parts['bolt'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='nut-1', 
    part=mdb.models['Model-1'].parts['nut'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='nut-2', 
    part=mdb.models['Model-1'].parts['nut'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='nut-3', 
    part=mdb.models['Model-1'].parts['nut'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='nut-4', 
   part=mdb.models['Model-1'].parts['nut'])
mdb.models['Model-1'].rootAssembly.translate(instanceList=('nut-4', ), 
    vector=(0.0, 0.0, dis1))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('nut-3', ), 
    vector=(0.0, 0.0, dis1+aind-Hm-Tsp*2))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('nut-2', ), 
    vector=(0.0, 0.0, dis1+aind+Tfod))
mdb.models['Model-1'].rootAssembly.InstanceFromBooleanMerge(domain=GEOMETRY, 
    instances=(mdb.models['Model-1'].rootAssembly.instances['bolt-1'], 
    mdb.models['Model-1'].rootAssembly.instances['nut-1'], 
    mdb.models['Model-1'].rootAssembly.instances['nut-2'], 
    mdb.models['Model-1'].rootAssembly.instances['nut-3'], 
    mdb.models['Model-1'].rootAssembly.instances['nut-4']), name='Bolt+nut', 
    originalInstances=SUPPRESS)
del mdb.models['Model-1'].rootAssembly.features['bolt-1']
del mdb.models['Model-1'].rootAssembly.features['nut-1']
del mdb.models['Model-1'].rootAssembly.features['nut-2']
del mdb.models['Model-1'].rootAssembly.features['nut-3']
del mdb.models['Model-1'].rootAssembly.features['nut-4']

##############################################################################
#                         Partitioning HE160A for load placement
#Datum plane
mdb.models['Model-1'].parts['HE160A'].DatumPlaneByOffset(flip=SIDE2, 
    isDependent=False, offset=b/5, plane=
    mdb.models['Model-1'].parts['HE160A'].faces[0])
mdb.models['Model-1'].parts['HE160A'].DatumPlaneByOffset(flip=SIDE2, 
    isDependent=False, offset=2*b/5, plane=
    mdb.models['Model-1'].parts['HE160A'].faces[0])
mdb.models['Model-1'].parts['HE160A'].DatumPlaneByOffset(flip=SIDE2, 
    isDependent=False, offset=3*b/5, plane=
    mdb.models['Model-1'].parts['HE160A'].faces[0])
mdb.models['Model-1'].parts['HE160A'].DatumPlaneByOffset(flip=SIDE2, 
    isDependent=False, offset=4*b/5, plane=
    mdb.models['Model-1'].parts['HE160A'].faces[0])
mdb.models['Model-1'].parts['HE160A'].DatumPlaneByOffset(flip=SIDE2, 
    isDependent=False, offset=t/2, plane=
    mdb.models['Model-1'].parts['HE160A'].faces[15])
mdb.models['Model-1'].parts['HE160A'].DatumPlaneByOffset(flip=SIDE2, offset=t/2
    , plane=mdb.models['Model-1'].parts['HE160A'].faces[7])
#Cell partition
mdb.models['Model-1'].parts['HE160A'].PartitionCellByDatumPlane(cells=
    mdb.models['Model-1'].parts['HE160A'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), datumPlane=mdb.models['Model-1'].parts['HE160A'].datums[2])
mdb.models['Model-1'].parts['HE160A'].PartitionCellByDatumPlane(cells=
    mdb.models['Model-1'].parts['HE160A'].cells.getSequenceFromMask(('[#2 ]', 
    ), ), datumPlane=mdb.models['Model-1'].parts['HE160A'].datums[3])
mdb.models['Model-1'].parts['HE160A'].PartitionCellByDatumPlane(cells=
    mdb.models['Model-1'].parts['HE160A'].cells.getSequenceFromMask(('[#8 ]', 
    ), ), datumPlane=mdb.models['Model-1'].parts['HE160A'].datums[4])
mdb.models['Model-1'].parts['HE160A'].PartitionCellByDatumPlane(cells=
    mdb.models['Model-1'].parts['HE160A'].cells.getSequenceFromMask(('[#21 ]', 
    ), ), datumPlane=mdb.models['Model-1'].parts['HE160A'].datums[5])
mdb.models['Model-1'].parts['HE160A'].PartitionCellByDatumPlane(cells=
    mdb.models['Model-1'].parts['HE160A'].cells.getSequenceFromMask(('[#12e ]', 
    ), ), datumPlane=mdb.models['Model-1'].parts['HE160A'].datums[6])
mdb.models['Model-1'].parts['HE160A'].PartitionCellByDatumPlane(cells=
    mdb.models['Model-1'].parts['HE160A'].cells.getSequenceFromMask((
    '[#3a40 ]', ), ), datumPlane=
    mdb.models['Model-1'].parts['HE160A'].datums[7])

##############################################################################
#              Partitioning Bolt+nut for pretensioning force
#Datum plane
mdb.models['Model-1'].parts['Bolt+nut'].DatumPlaneByOffset(flip=SIDE2, offset=
    Hm+Tsp+Ttop/2, plane=mdb.models['Model-1'].parts['Bolt+nut'].faces[16])
mdb.models['Model-1'].parts['Bolt+nut'].DatumPlaneByOffset(flip=SIDE2, offset=
    Hm+Tsp+Ttop+aind+Tfod/2, plane=mdb.models['Model-1'].parts['Bolt+nut'].faces[16])
#Cell partition
mdb.models['Model-1'].parts['Bolt+nut'].PartitionCellByDatumPlane(cells=
    mdb.models['Model-1'].parts['Bolt+nut'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), datumPlane=mdb.models['Model-1'].parts['Bolt+nut'].datums[2])
mdb.models['Model-1'].parts['Bolt+nut'].PartitionCellByDatumPlane(cells=
    mdb.models['Model-1'].parts['Bolt+nut'].cells.getSequenceFromMask(('[#2 ]', 
    ), ), datumPlane=mdb.models['Model-1'].parts['Bolt+nut'].datums[3])

##############################################################################
#                    Defining steel material and section

mdb.models['Model-1'].Material(name='Steel')
mdb.models['Model-1'].materials['Steel'].Elastic(table=((210000.0, 0.3), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='Steel', name='Steel', 
    thickness=None)

##############################################################################
#              Assigning steel sections to various parts
mdb.models['Model-1'].parts['Bolt+nut'].Set(cells=
    mdb.models['Model-1'].parts['Bolt+nut'].cells.getSequenceFromMask(('[#7 ]', 
    ), ), name='Bolt+nut')
mdb.models['Model-1'].parts['Bolt+nut'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Bolt+nut'].sets['Bolt+nut'], sectionName=
    'Steel', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Fodplade'].Set(cells=
    mdb.models['Model-1'].parts['Fodplade'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), name='Foot plate')
mdb.models['Model-1'].parts['Fodplade'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Fodplade'].sets['Foot plate'], sectionName=
    'Steel', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['HE160A'].Set(cells=
    mdb.models['Model-1'].parts['HE160A'].cells.getSequenceFromMask((
    '[#7ffff ]', ), ), name='HE160A')
mdb.models['Model-1'].parts['HE160A'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['HE160A'].sets['HE160A'], sectionName='Steel', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['HE200A'].Set(cells=
    mdb.models['Model-1'].parts['HE200A'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), name='Pile')
mdb.models['Model-1'].parts['HE200A'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['HE200A'].sets['Pile'], sectionName='Steel', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Topplade'].Set(cells=
    mdb.models['Model-1'].parts['Topplade'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), name='Top plate')
mdb.models['Model-1'].parts['Topplade'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Topplade'].sets['Top plate'], sectionName=
    'Steel', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Washer'].Set(cells=
    mdb.models['Model-1'].parts['Washer'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), name='Washer')
mdb.models['Model-1'].parts['Washer'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Washer'].sets['Washer'], sectionName='Steel', 
    thicknessAssignment=FROM_SECTION)

##############################################################################
#                        Seeding and meshing parts parts

mdb.models['Model-1'].parts['Bolt+nut'].setMeshControls(elemShape=TET, regions=
    mdb.models['Model-1'].parts['Bolt+nut'].cells.getSequenceFromMask(('[#7 ]', 
    ), ), technique=FREE)
mdb.models['Model-1'].parts['Bolt+nut'].setElementType(elemTypes=(ElemType(
    elemCode=C3D20R, elemLibrary=STANDARD), ElemType(elemCode=C3D15, 
    elemLibrary=STANDARD), ElemType(elemCode=C3D10, elemLibrary=STANDARD)), 
    regions=(mdb.models['Model-1'].parts['Bolt+nut'].cells.getSequenceFromMask(
    ('[#7 ]', ), ), ))
mdb.models['Model-1'].parts['Bolt+nut'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=7.4)
mdb.models['Model-1'].parts['Bolt+nut'].generateMesh()
mdb.models['Model-1'].parts['Fodplade'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=10.0)
mdb.models['Model-1'].parts['Fodplade'].generateMesh()
mdb.models['Model-1'].parts['HE160A'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=10.0)
mdb.models['Model-1'].parts['HE160A'].generateMesh()
mdb.models['Model-1'].parts['HE200A'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=10.0)
mdb.models['Model-1'].parts['HE200A'].generateMesh()
mdb.models['Model-1'].parts['Topplade'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=10.0)
mdb.models['Model-1'].parts['Topplade'].generateMesh()
mdb.models['Model-1'].parts['Washer'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=8.0)
mdb.models['Model-1'].parts['Washer'].generateMesh()

##############################################################################
#                   Adding steps for pretensioning and loads

mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].StaticStep(name='Pretensioning bolt', previous='Initial')
mdb.models['Model-1'].StaticStep(name='Outer Loads', previous=
    'Pretensioning bolt')


##############################################################################
#             Adding instances and moving them to correct positions

mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='HE160A-1', 
    part=mdb.models['Model-1'].parts['HE160A'])
mdb.models['Model-1'].rootAssembly.translate(instanceList=('HE160A-1', ), 
    vector=(Lh/2-OEh/2, -e-OEb/2+Lh/2, Tfod+Ttop+aind))

mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Fodplade-1', 
    part=mdb.models['Model-1'].parts['Fodplade'])
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Fodplade-1', ), 
    vector=(Lh/2-OEh/2, Lh/2-OEb/2, Ttop+aind))

mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Bolt+nut-2', 
    part=mdb.models['Model-1'].parts['Bolt+nut'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Bolt+nut-3', 
    part=mdb.models['Model-1'].parts['Bolt+nut'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Bolt+nut-4', 
    part=mdb.models['Model-1'].parts['Bolt+nut'])

mdb.models['Model-1'].rootAssembly.translate(instanceList=('Bolt+nut-4', ), 
    vector=(a, c+Lh/2-OEb/2, -Hm-Tsp))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Bolt+nut-3', ), 
    vector=(-a, c+Lh/2-OEb/2, -Hm-Tsp))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Bolt+nut-2', ), 
    vector=(a, -c+Lh/2-OEb/2, -Hm-Tsp))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Bolt+nut-1', ), 
    vector=(-a, -c+Lh/2-OEb/2, -Hm-Tsp))

#num_washers =  range(1,17,1)
#for nr in num_washers: 
#    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Washer-'+'nr', 
#              part=mdb.models['Model-1'].parts['Washer'])          
 
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Washer-1', 
    part=mdb.models['Model-1'].parts['Washer'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Washer-2', 
    part=mdb.models['Model-1'].parts['Washer'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Washer-3', 
    part=mdb.models['Model-1'].parts['Washer'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Washer-4', 
    part=mdb.models['Model-1'].parts['Washer'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Washer-5', 
    part=mdb.models['Model-1'].parts['Washer'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Washer-6', 
    part=mdb.models['Model-1'].parts['Washer'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Washer-7', 
    part=mdb.models['Model-1'].parts['Washer'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Washer-8', 
    part=mdb.models['Model-1'].parts['Washer'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Washer-9', 
    part=mdb.models['Model-1'].parts['Washer'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Washer-10', 
    part=mdb.models['Model-1'].parts['Washer'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Washer-11', 
    part=mdb.models['Model-1'].parts['Washer'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Washer-12', 
    part=mdb.models['Model-1'].parts['Washer'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Washer-13', 
    part=mdb.models['Model-1'].parts['Washer'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Washer-14', 
    part=mdb.models['Model-1'].parts['Washer'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Washer-15', 
    part=mdb.models['Model-1'].parts['Washer'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Washer-16', 
    part=mdb.models['Model-1'].parts['Washer'])

         
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Washer-16', ), 
    vector=(a, c+Lh/2-OEb/2, -Tsp))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Washer-15', ), 
    vector=(a, c+Lh/2-OEb/2, Ttop))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Washer-14', ), 
    vector=(a, c+Lh/2-OEb/2, Ttop+aind-Tsp))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Washer-13', ), 
    vector=(a, c+Lh/2-OEb/2, Ttop+aind+Tfod))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Washer-12', ), 
    vector=(-a, c+Lh/2-OEb/2, -Tsp))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Washer-11', ), 
    vector=(-a, c+Lh/2-OEb/2, Ttop))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Washer-10', ), 
    vector=(-a, c+Lh/2-OEb/2, Ttop+aind-Tsp))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Washer-9', ), 
    vector=(-a, c+Lh/2-OEb/2, Ttop+aind+Tfod))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Washer-8', ), 
    vector=(a, -c+Lh/2-OEb/2, -Tsp))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Washer-7', ), 
    vector=(a, -c+Lh/2-OEb/2, Ttop))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Washer-6', ), 
    vector=(a, -c+Lh/2-OEb/2, Ttop+aind-Tsp))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Washer-5', ), 
    vector=(a, -c+Lh/2-OEb/2, Ttop+aind+Tfod))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Washer-4', ), 
    vector=(-a, -c+Lh/2-OEb/2, -Tsp))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Washer-3', ), 
    vector=(-a, -c+Lh/2-OEb/2, Ttop))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Washer-2', ), 
    vector=(-a, -c+Lh/2-OEb/2, Ttop+aind-Tsp))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Washer-1', ), 
    vector=(-a, -c+Lh/2-OEb/2, Ttop+aind+Tfod))
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='HE200A-1', 
    part=mdb.models['Model-1'].parts['HE200A'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Topplade-1', 
    part=mdb.models['Model-1'].parts['Topplade'])
mdb.models['Model-1'].rootAssembly.translate(instanceList=('HE200A-1', ), 
    vector=(0.0, -ep, -Hpp))

##############################################################################
#                                   BC for pile (fixed)

mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['HE200A-1'].faces.getSequenceFromMask(
    ('[#20000 ]', ), ), name='Set-1')
mdb.models['Model-1'].EncastreBC(createStepName='Initial', localCsys=None, 
    name='Fixed pile', region=mdb.models['Model-1'].rootAssembly.sets['Set-1'])

##############################################################################
#                                   Connecting topplate and pile
mdb.models['Model-1'].rootAssembly.Surface(name='Pile top', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['HE200A-1'].faces.getSequenceFromMask(
    ('[#10000 ]', ), ))
mdb.models['Model-1'].rootAssembly.Surface(name='topplate bottom', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Topplade-1'].faces.getSequenceFromMask(
    ('[#200000 ]', ), ))
mdb.models['Model-1'].Tie(adjust=ON, master=
    mdb.models['Model-1'].rootAssembly.surfaces['Pile top'], name=
    'Pile and topplate', positionToleranceMethod=COMPUTED, slave=
    mdb.models['Model-1'].rootAssembly.surfaces['topplate bottom'], thickness=
    ON, tieRotations=ON)

##############################################################################
#                                   Connecting footplate and post

mdb.models['Model-1'].rootAssembly.Surface(name='Footplate top', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Fodplade-1'].faces.getSequenceFromMask(
    ('[#100000 ]', ), ))
mdb.models['Model-1'].rootAssembly.Surface(name='Post bottom', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['HE160A-1'].faces.getSequenceFromMask(
    ('[#2808a480 #30820a1 #30c0 #8 ]', ), ))
mdb.models['Model-1'].Tie(adjust=ON, master=
    mdb.models['Model-1'].rootAssembly.surfaces['Footplate top'], name=
    'Post and footplate', positionToleranceMethod=COMPUTED, slave=
    mdb.models['Model-1'].rootAssembly.surfaces['Post bottom'], thickness=ON, 
    tieRotations=ON)

##############################################################################
#                          Interaction between washers and plates
mdb.models['Model-1'].ContactProperty('Friction')
mdb.models['Model-1'].interactionProperties['Friction'].TangentialBehavior(
    dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, 
    formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, 
    pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, 
    table=((0.1, ), ), temperatureDependency=OFF)

mdb.models['Model-1'].rootAssembly.Surface(name='Plates top and bottom', 
    side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Fodplade-1'].faces.getSequenceFromMask(
    mask=('[#300000 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Topplade-1'].faces.getSequenceFromMask(
    mask=('[#300000 ]', ), ))
            
mdb.models['Model-1'].rootAssembly.Surface(name='Inside of washers', 
    side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Washer-12'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-4'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-8'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-16'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-6'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-14'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-2'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-10'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-3'].faces.getSequenceFromMask(
    mask=('[#8 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-11'].faces.getSequenceFromMask(
    mask=('[#8 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-7'].faces.getSequenceFromMask(
    mask=('[#8 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-15'].faces.getSequenceFromMask(
    mask=('[#8 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-5'].faces.getSequenceFromMask(
    mask=('[#8 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-13'].faces.getSequenceFromMask(
    mask=('[#8 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-9'].faces.getSequenceFromMask(
    mask=('[#8 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-1'].faces.getSequenceFromMask(
    mask=('[#8 ]', ), ))            
            
            
#mdb.models['Model-1'].rootAssembly.Surface(name='Inside of washers', 
#    side1Faces=
#    mdb.models['Model-1'].rootAssembly.instances['Washer-13'].faces.getSequenceFromMask(
#    mask=('[#40 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-5'].faces.getSequenceFromMask(
#    mask=('[#40 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-7'].faces.getSequenceFromMask(
#    mask=('[#40 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-15'].faces.getSequenceFromMask(
#    mask=('[#40 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-9'].faces.getSequenceFromMask(
#    mask=('[#40 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-11'].faces.getSequenceFromMask(
#    mask=('[#40 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-3'].faces.getSequenceFromMask(
#    mask=('[#40 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-1'].faces.getSequenceFromMask(
#    mask=('[#40 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-16'].faces.getSequenceFromMask(
#    mask=('[#20 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-12'].faces.getSequenceFromMask(
#    mask=('[#20 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-4'].faces.getSequenceFromMask(
#    mask=('[#20 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-8'].faces.getSequenceFromMask(
#    mask=('[#20 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-14'].faces.getSequenceFromMask(
#    mask=('[#20 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-6'].faces.getSequenceFromMask(
#    mask=('[#20 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-2'].faces.getSequenceFromMask(
#    mask=('[#20 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-10'].faces.getSequenceFromMask(
#    mask=('[#20 ]', ), ))
    
            
            
mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='Initial', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Friction', master=
    mdb.models['Model-1'].rootAssembly.surfaces['Plates top and bottom'], name=
    'Plates and washers', slave=
    mdb.models['Model-1'].rootAssembly.surfaces['Inside of washers'], sliding=
    FINITE, thickness=ON)

##############################################################################
#                          Interaction between washers and nuts


mdb.models['Model-1'].rootAssembly.Surface(name='Top of washers', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Washer-9'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-1'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-13'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-5'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-7'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-15'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-3'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-11'].faces.getSequenceFromMask(
    mask=('[#4 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-10'].faces.getSequenceFromMask(
    mask=('[#8 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-2'].faces.getSequenceFromMask(
    mask=('[#8 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-4'].faces.getSequenceFromMask(
    mask=('[#8 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-12'].faces.getSequenceFromMask(
    mask=('[#8 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-16'].faces.getSequenceFromMask(
    mask=('[#8 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-8'].faces.getSequenceFromMask(
    mask=('[#8 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-6'].faces.getSequenceFromMask(
    mask=('[#8 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Washer-14'].faces.getSequenceFromMask(
    mask=('[#8 ]', ), ))


#mdb.models['Model-1'].rootAssembly.Surface(name='Top of washers', side1Faces=
#    mdb.models['Model-1'].rootAssembly.instances['Washer-1'].faces.getSequenceFromMask(
#    mask=('[#20 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-9'].faces.getSequenceFromMask(
#    mask=('[#20 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-3'].faces.getSequenceFromMask(
#    mask=('[#20 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-11'].faces.getSequenceFromMask(
#    mask=('[#20 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-5'].faces.getSequenceFromMask(
#    mask=('[#20 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-13'].faces.getSequenceFromMask(
#    mask=('[#20 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-7'].faces.getSequenceFromMask(
#    mask=('[#20 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-15'].faces.getSequenceFromMask(
#    mask=('[#20 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-16'].faces.getSequenceFromMask(
#    mask=('[#40 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-12'].faces.getSequenceFromMask(
#    mask=('[#40 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-4'].faces.getSequenceFromMask(
#    mask=('[#40 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-8'].faces.getSequenceFromMask(
#    mask=('[#40 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-10'].faces.getSequenceFromMask(
#    mask=('[#40 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-2'].faces.getSequenceFromMask(
#    mask=('[#40 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-6'].faces.getSequenceFromMask(
#    mask=('[#40 ]', ), )+\
#    mdb.models['Model-1'].rootAssembly.instances['Washer-14'].faces.getSequenceFromMask(
#    mask=('[#40 ]', ), ))



mdb.models['Model-1'].rootAssembly.Surface(name='Inside of nuts', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Bolt+nut-3'].faces.getSequenceFromMask(
    mask=('[#12120 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Bolt+nut-1'].faces.getSequenceFromMask(
    mask=('[#12120 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Bolt+nut-4'].faces.getSequenceFromMask(
    mask=('[#12120 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Bolt+nut-2'].faces.getSequenceFromMask(
    mask=('[#12120 ]', ), ))

mdb.models['Model-1'].SurfaceToSurfaceContactStd(adjustMethod=NONE, 
    clearanceRegion=None, createStepName='Initial', datumAxis=None, 
    initialClearance=OMIT, interactionProperty='Friction', master=
    mdb.models['Model-1'].rootAssembly.surfaces['Top of washers'], name=
    'Washers and nuts', slave=
    mdb.models['Model-1'].rootAssembly.surfaces['Inside of nuts'], sliding=
    FINITE, thickness=ON)

##############################################################################
#                          Apllying outside loads
#Moment
mdb.models['Model-1'].rootAssembly.Set(name='Wind - moment - compression', 
    vertices=
    mdb.models['Model-1'].rootAssembly.instances['HE160A-1'].vertices.getSequenceFromMask(
    ('[#0 #2f200 ]', ), ))
mdb.models['Model-1'].ConcentratedForce(cf3=-PM, createStepName='Outer Loads', 
    distributionType=UNIFORM, field='', localCsys=None, name=
    'Wind - moment - compression', region=
    mdb.models['Model-1'].rootAssembly.sets['Wind - moment - compression'])

#Moment
mdb.models['Model-1'].rootAssembly.Set(name='Wind - moment - tension', 
    vertices=
    mdb.models['Model-1'].rootAssembly.instances['HE160A-1'].vertices.getSequenceFromMask(
    ('[#a66 ]', ), ))
mdb.models['Model-1'].ConcentratedForce(cf3=PM, createStepName='Outer Loads', 
    distributionType=UNIFORM, field='', localCsys=None, name=
    'Wind - moment - tension', region=
    mdb.models['Model-1'].rootAssembly.sets['Wind - moment - tension'])

#Shear
mdb.models['Model-1'].rootAssembly.Set(name='Wind - Shear', vertices=
    mdb.models['Model-1'].rootAssembly.instances['HE160A-1'].vertices.getSequenceFromMask(
    ('[#440000 #1c #400000 ]', ), ))
mdb.models['Model-1'].ConcentratedForce(cf2=Pv, createStepName='Outer Loads', 
    distributionType=UNIFORM, field='', localCsys=None, name='Wind - Shear', 
    region=mdb.models['Model-1'].rootAssembly.sets['Wind - Shear'])


##############################################################################
#                          Apllying inside bolt tensioning
mdb.models['Model-1'].rootAssembly.Surface(name='B1-top', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Bolt+nut-4'].faces.getSequenceFromMask(
    ('[#1 ]', ), ))
mdb.models['Model-1'].BoltLoad(boltMethod=APPLY_FORCE, createStepName=
    'Pretensioning bolt', datumAxis=None, magnitude=Fp, name='B1 - top', 
    region=mdb.models['Model-1'].rootAssembly.surfaces['B1-top'])
mdb.models['Model-1'].rootAssembly.Surface(name='B1 - bottom', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Bolt+nut-4'].faces.getSequenceFromMask(
    ('[#4 ]', ), ))
mdb.models['Model-1'].BoltLoad(boltMethod=APPLY_FORCE, createStepName=
    'Pretensioning bolt', datumAxis=None, magnitude=Fp, name='B1 - bottom', 
    region=mdb.models['Model-1'].rootAssembly.surfaces['B1 - bottom'])
mdb.models['Model-1'].rootAssembly.Surface(name='B2 - top', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Bolt+nut-3'].faces.getSequenceFromMask(
    ('[#1 ]', ), ))
mdb.models['Model-1'].BoltLoad(boltMethod=APPLY_FORCE, createStepName=
    'Pretensioning bolt', datumAxis=None, magnitude=Fp, name='B2 - top', 
    region=mdb.models['Model-1'].rootAssembly.surfaces['B2 - top'])
mdb.models['Model-1'].rootAssembly.Surface(name='B2 - bottom', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Bolt+nut-3'].faces.getSequenceFromMask(
    ('[#4 ]', ), ))
mdb.models['Model-1'].BoltLoad(boltMethod=APPLY_FORCE, createStepName=
    'Pretensioning bolt', datumAxis=None, magnitude=Fp, name=
    'B2 - bottom', region=
    mdb.models['Model-1'].rootAssembly.surfaces['B2 - bottom'])
mdb.models['Model-1'].loads['B1 - bottom'].setValues(magnitude=Fp)
mdb.models['Model-1'].loads['B1 - top'].setValues(magnitude=Fp)
mdb.models['Model-1'].rootAssembly.Surface(name='B3 - top', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Bolt+nut-1'].faces.getSequenceFromMask(
    ('[#1 ]', ), ))
mdb.models['Model-1'].BoltLoad(boltMethod=APPLY_FORCE, createStepName=
    'Pretensioning bolt', datumAxis=None, magnitude=Fp, name='B3 - top', 
    region=mdb.models['Model-1'].rootAssembly.surfaces['B3 - top'])
mdb.models['Model-1'].rootAssembly.Surface(name='B3 - bottom', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Bolt+nut-1'].faces.getSequenceFromMask(
    ('[#4 ]', ), ))
mdb.models['Model-1'].BoltLoad(boltMethod=APPLY_FORCE, createStepName=
    'Pretensioning bolt', datumAxis=None, magnitude=Fp, name=
    'B3 - bottom', region=
    mdb.models['Model-1'].rootAssembly.surfaces['B3 - bottom'])
mdb.models['Model-1'].rootAssembly.Surface(name='B4 - top', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Bolt+nut-2'].faces.getSequenceFromMask(
    ('[#1 ]', ), ))
mdb.models['Model-1'].BoltLoad(boltMethod=APPLY_FORCE, createStepName=
    'Pretensioning bolt', datumAxis=None, magnitude=Fp, name='B4 - top', 
    region=mdb.models['Model-1'].rootAssembly.surfaces['B4 - top'])
mdb.models['Model-1'].rootAssembly.Surface(name='B4 - bottom', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Bolt+nut-2'].faces.getSequenceFromMask(
    ('[#4 ]', ), ))
mdb.models['Model-1'].BoltLoad(boltMethod=APPLY_FORCE, createStepName=
    'Pretensioning bolt', datumAxis=None, magnitude=Fp, name=
    'B4 - bottom', region=
    mdb.models['Model-1'].rootAssembly.surfaces['B4 - bottom'])

#mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
#    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
#    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
#    multiprocessingMode=DEFAULT, name='ULSwind', nodalOutputPrecision=SINGLE, 
#    numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
#    ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
#mdb.jobs['ULSwind'].submit(consistencyChecking=OFF)








