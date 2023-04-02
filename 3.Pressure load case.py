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
# cylinder shape , 
# strain 50% , 
# alloy
# vary  ...... change hieght to 15 to 20....for....L / D from 1.5 , 1.6,1.7,1.8,19,2.0 
radius = 5
height = 15
Displ=-1.5
Modulus_E=107.37e3
Pois_ratio=0.3
Yield_stress = 169.01


mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
    -100.0), point2=(0.0, 100.0))
mdb.models['Model-1'].sketches['__profile__'].FixedConstraint(entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, 0.0), 
    point2=(10.0, 20.0))
mdb.models['Model-1'].sketches['__profile__'].CoincidentConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[0], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    3.89486694335938, -3.79907417297363), value=radius, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[3], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[0])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    13.9566116333008, 8.97228622436523), value=height, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[2], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[3])
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='CylindricalSpec', 
    type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['CylindricalSpec'].BaseSolidRevolve(angle=360.0, 
    flipRevolveDirection=OFF, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
	
	
del mdb.models['Model-1'].sketches['__profile__']
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
mdb.models['Model-1'].parts['CylindricalSpec'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['CylindricalSpec'].cells.getSequenceFromMask((
    '[#1 ]', ), ), point1=
    mdb.models['Model-1'].parts['CylindricalSpec'].InterestingPoint(
    mdb.models['Model-1'].parts['CylindricalSpec'].edges[0], MIDDLE), point2=
    mdb.models['Model-1'].parts['CylindricalSpec'].vertices[0], point3=
    mdb.models['Model-1'].parts['CylindricalSpec'].vertices[1])
mdb.models['Model-1'].parts['CylindricalSpec'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['CylindricalSpec'].cells.getSequenceFromMask((
    '[#3 ]', ), ), point1=
    mdb.models['Model-1'].parts['CylindricalSpec'].InterestingPoint(
    mdb.models['Model-1'].parts['CylindricalSpec'].edges[5], MIDDLE), point2=
    mdb.models['Model-1'].parts['CylindricalSpec'].InterestingPoint(
    mdb.models['Model-1'].parts['CylindricalSpec'].edges[6], MIDDLE), point3=
    mdb.models['Model-1'].parts['CylindricalSpec'].InterestingPoint(
    mdb.models['Model-1'].parts['CylindricalSpec'].edges[7], MIDDLE))
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
mdb.models['Model-1'].parts['CylindricalSpec'].Set(edges=
    mdb.models['Model-1'].parts['CylindricalSpec'].edges.getSequenceFromMask((
    '[#1 ]', ), ), name='centreline')
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
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((Modulus_E, Pois_ratio), ))