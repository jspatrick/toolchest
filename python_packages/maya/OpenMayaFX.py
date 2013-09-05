import OpenMaya
import _OpenMayaFX
import new
import weakref

from maya._OpenMayaFX import *

class MnSolver(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def addNObject(*args, **kwargs):
        pass
    
    
    def createNSolver(*args, **kwargs):
        pass
    
    
    def makeAllCollide(*args, **kwargs):
        pass
    
    
    def removeAllCollisions(*args, **kwargs):
        pass
    
    
    def removeNObject(*args, **kwargs):
        pass
    
    
    def setAirDensity(*args, **kwargs):
        pass
    
    
    def setDisabled(*args, **kwargs):
        pass
    
    
    def setGravity(*args, **kwargs):
        pass
    
    
    def setGravityDir(*args, **kwargs):
        pass
    
    
    def setMaxIterations(*args, **kwargs):
        pass
    
    
    def setStartTime(*args, **kwargs):
        pass
    
    
    def setSubsteps(*args, **kwargs):
        pass
    
    
    def setWindDir(*args, **kwargs):
        pass
    
    
    def setWindNoiseIntensity(*args, **kwargs):
        pass
    
    
    def setWindSpeed(*args, **kwargs):
        pass
    
    
    def solve(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MnObject(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    fNObject = None
    
    fOwn = None
    
    thisown = None
    
    __swig_destroy__ = None


class MFnFluid(OpenMaya.MFnDagNode):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def create2D(*args, **kwargs):
        pass
    
    
    def create3D(*args, **kwargs):
        pass
    
    
    def density(*args, **kwargs):
        pass
    
    
    def emitIntoArrays(*args, **kwargs):
        pass
    
    
    def falloff(*args, **kwargs):
        pass
    
    
    def fuel(*args, **kwargs):
        pass
    
    
    def getColorMode(*args, **kwargs):
        pass
    
    
    def getColors(*args, **kwargs):
        pass
    
    
    def getCoordinateMode(*args, **kwargs):
        pass
    
    
    def getCoordinates(*args, **kwargs):
        pass
    
    
    def getDensityMode(*args, **kwargs):
        pass
    
    
    def getDimensions(*args, **kwargs):
        pass
    
    
    def getFalloffMode(*args, **kwargs):
        pass
    
    
    def getForceAtPoint(*args, **kwargs):
        pass
    
    
    def getFuelMode(*args, **kwargs):
        pass
    
    
    def getResolution(*args, **kwargs):
        pass
    
    
    def getTemperatureMode(*args, **kwargs):
        pass
    
    
    def getVelocity(*args, **kwargs):
        pass
    
    
    def getVelocityMode(*args, **kwargs):
        pass
    
    
    def gridSize(*args, **kwargs):
        pass
    
    
    def index(*args, **kwargs):
        pass
    
    
    def pressure(*args, **kwargs):
        pass
    
    
    def setColorMode(*args, **kwargs):
        pass
    
    
    def setCoordinateMode(*args, **kwargs):
        pass
    
    
    def setDensityMode(*args, **kwargs):
        pass
    
    
    def setFalloffMode(*args, **kwargs):
        pass
    
    
    def setFuelMode(*args, **kwargs):
        pass
    
    
    def setSize(*args, **kwargs):
        pass
    
    
    def setTemperatureMode(*args, **kwargs):
        pass
    
    
    def setVelocityMode(*args, **kwargs):
        pass
    
    
    def temperature(*args, **kwargs):
        pass
    
    
    def toGridIndex(*args, **kwargs):
        pass
    
    
    def updateGrid(*args, **kwargs):
        pass
    
    
    def velocityGridSizes(*args, **kwargs):
        pass
    
    
    def voxelCenterPosition(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kCenterGradient = None
    
    
    kConstant = None
    
    
    kDynamicColorGrid = None
    
    
    kDynamicGrid = None
    
    
    kFixed = None
    
    
    kGradient = None
    
    
    kGrid = None
    
    
    kNegXGradient = None
    
    
    kNegYGradient = None
    
    
    kNegZGradient = None
    
    
    kNoFalloffGrid = None
    
    
    kStaticColorGrid = None
    
    
    kStaticFalloffGrid = None
    
    
    kStaticGrid = None
    
    
    kUseShadingColor = None
    
    
    kXGradient = None
    
    
    kYGradient = None
    
    
    kZGradient = None
    
    
    kZero = None


class MFnParticleSystem(OpenMaya.MFnDagNode):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def acceleration(*args, **kwargs):
        pass
    
    
    def age(*args, **kwargs):
        pass
    
    
    def betterIllum(*args, **kwargs):
        pass
    
    
    def castsShadows(*args, **kwargs):
        pass
    
    
    def count(*args, **kwargs):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def deformedParticleShape(*args, **kwargs):
        pass
    
    
    def disableCloudAxis(*args, **kwargs):
        pass
    
    
    def emission(*args, **kwargs):
        pass
    
    
    def emit(*args, **kwargs):
        pass
    
    
    def evaluateDynamics(*args, **kwargs):
        pass
    
    
    def flatShaded(*args, **kwargs):
        pass
    
    
    def getPerParticleAttribute(*args, **kwargs):
        pass
    
    
    def hasEmission(*args, **kwargs):
        pass
    
    
    def hasLifespan(*args, **kwargs):
        pass
    
    
    def hasOpacity(*args, **kwargs):
        pass
    
    
    def hasRgb(*args, **kwargs):
        pass
    
    
    def isDeformedParticleShape(*args, **kwargs):
        pass
    
    
    def isPerParticleDoubleAttribute(*args, **kwargs):
        pass
    
    
    def isPerParticleIntAttribute(*args, **kwargs):
        pass
    
    
    def isPerParticleVectorAttribute(*args, **kwargs):
        pass
    
    
    def isValid(*args, **kwargs):
        pass
    
    
    def lifespan(*args, **kwargs):
        pass
    
    
    def mass(*args, **kwargs):
        pass
    
    
    def opacity(*args, **kwargs):
        pass
    
    
    def originalParticleShape(*args, **kwargs):
        pass
    
    
    def particleIds(*args, **kwargs):
        pass
    
    
    def particleName(*args, **kwargs):
        pass
    
    
    def position(*args, **kwargs):
        pass
    
    
    def position0(*args, **kwargs):
        pass
    
    
    def position1(*args, **kwargs):
        pass
    
    
    def primaryVisibility(*args, **kwargs):
        pass
    
    
    def radius(*args, **kwargs):
        pass
    
    
    def radius0(*args, **kwargs):
        pass
    
    
    def radius1(*args, **kwargs):
        pass
    
    
    def receiveShadows(*args, **kwargs):
        pass
    
    
    def renderType(*args, **kwargs):
        pass
    
    
    def rgb(*args, **kwargs):
        pass
    
    
    def saveInitialState(*args, **kwargs):
        pass
    
    
    def setCount(*args, **kwargs):
        pass
    
    
    def setPerParticleAttribute(*args, **kwargs):
        pass
    
    
    def surfaceShading(*args, **kwargs):
        pass
    
    
    def tailSize(*args, **kwargs):
        pass
    
    
    def threshold(*args, **kwargs):
        pass
    
    
    def velocity(*args, **kwargs):
        pass
    
    
    def visibleInReflections(*args, **kwargs):
        pass
    
    
    def visibleInRefractions(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kBlobby = None
    
    
    kCloud = None
    
    
    kMultiPoint = None
    
    
    kMultiStreak = None
    
    
    kNumeric = None
    
    
    kPoints = None
    
    
    kSpheres = None
    
    
    kSprites = None
    
    
    kStreak = None
    
    
    kTube = None


class MFnField(OpenMaya.MFnDagNode):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def attenuation(*args, **kwargs):
        pass
    
    
    def falloffCurve(*args, **kwargs):
        pass
    
    
    def getForceAtPoint(*args, **kwargs):
        pass
    
    
    def isFalloffCurveConstantOne(*args, **kwargs):
        pass
    
    
    def magnitude(*args, **kwargs):
        pass
    
    
    def maxDistance(*args, **kwargs):
        pass
    
    
    def perVertex(*args, **kwargs):
        pass
    
    
    def setAttenuation(*args, **kwargs):
        pass
    
    
    def setMagnitude(*args, **kwargs):
        pass
    
    
    def setMaxDistance(*args, **kwargs):
        pass
    
    
    def setPerVertex(*args, **kwargs):
        pass
    
    
    def setUseMaxDistance(*args, **kwargs):
        pass
    
    
    def useMaxDistance(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnPfxGeometry(OpenMaya.MFnDagNode):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def getBoundingBox(*args, **kwargs):
        pass
    
    
    def getLineData(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MDynamicsUtil(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def evalDynamics2dTexture(*args, **kwargs):
        pass
    
    
    def hasValidDynamics2dTexture(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MFnNObjectData(OpenMaya.MFnData):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def getCached(*args, **kwargs):
        pass
    
    
    def getCollide(*args, **kwargs):
        pass
    
    
    def getObjectPtr(*args, **kwargs):
        pass
    
    
    def setCached(*args, **kwargs):
        pass
    
    
    def setObjectPtr(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnDynSweptGeometryData(OpenMaya.MFnData):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def lineCount(*args, **kwargs):
        pass
    
    
    def sweptLine(*args, **kwargs):
        pass
    
    
    def sweptTriangle(*args, **kwargs):
        pass
    
    
    def triangleCount(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MDynSweptLine(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def length(*args, **kwargs):
        pass
    
    
    def normal(*args, **kwargs):
        pass
    
    
    def tangent(*args, **kwargs):
        pass
    
    
    def vertex(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MHairSystem(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def getCollisionObject(*args, **kwargs):
        pass
    
    
    def getFollicle(*args, **kwargs):
        pass
    
    
    def registerCollisionSolverCollide(*args, **kwargs):
        pass
    
    
    def registerCollisionSolverPreFrame(*args, **kwargs):
        pass
    
    
    def registeringCallableScript(*args, **kwargs):
        pass
    
    
    def setRegisteringCallableScript(*args, **kwargs):
        pass
    
    
    def unregisterCollisionSolverCollide(*args, **kwargs):
        pass
    
    
    def unregisterCollisionSolverPreFrame(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MDynSweptTriangle(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def area(*args, **kwargs):
        pass
    
    
    def normal(*args, **kwargs):
        pass
    
    
    def normalToPoint(*args, **kwargs):
        pass
    
    
    def uvPoint(*args, **kwargs):
        pass
    
    
    def vertex(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MFnInstancer(OpenMaya.MFnDagNode):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def allInstances(*args, **kwargs):
        pass
    
    
    def instancesForParticle(*args, **kwargs):
        pass
    
    
    def particleCount(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnNIdData(OpenMaya.MFnData):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def getObjectPtr(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MRenderLine(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def assign(*args, **kwargs):
        pass
    
    
    def getColor(*args, **kwargs):
        pass
    
    
    def getFlatness(*args, **kwargs):
        pass
    
    
    def getIncandescence(*args, **kwargs):
        pass
    
    
    def getLine(*args, **kwargs):
        pass
    
    
    def getParameter(*args, **kwargs):
        pass
    
    
    def getTransparency(*args, **kwargs):
        pass
    
    
    def getTwist(*args, **kwargs):
        pass
    
    
    def getWidth(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MRenderLineArray(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def assign(*args, **kwargs):
        pass
    
    
    def deleteArray(*args, **kwargs):
        pass
    
    
    def length(*args, **kwargs):
        pass
    
    
    def renderLine(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MnCloth(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def createNCloth(*args, **kwargs):
        pass
    
    
    def getBounce(*args, **kwargs):
        pass
    
    
    def getFriction(*args, **kwargs):
        pass
    
    
    def getInverseMass(*args, **kwargs):
        pass
    
    
    def getNumVertices(*args, **kwargs):
        pass
    
    
    def getPositions(*args, **kwargs):
        pass
    
    
    def getThickness(*args, **kwargs):
        pass
    
    
    def getVelocities(*args, **kwargs):
        pass
    
    
    def setAddCrossLinks(*args, **kwargs):
        pass
    
    
    def setAirTightness(*args, **kwargs):
        pass
    
    
    def setBendAngleDropoff(*args, **kwargs):
        pass
    
    
    def setBendAngleScale(*args, **kwargs):
        pass
    
    
    def setBendResistance(*args, **kwargs):
        pass
    
    
    def setBendRestAngleFromPositions(*args, **kwargs):
        pass
    
    
    def setBounce(*args, **kwargs):
        pass
    
    
    def setCollisionFlags(*args, **kwargs):
        pass
    
    
    def setComputeRestAngles(*args, **kwargs):
        pass
    
    
    def setComputeRestLength(*args, **kwargs):
        pass
    
    
    def setDamping(*args, **kwargs):
        pass
    
    
    def setDisableGravity(*args, **kwargs):
        pass
    
    
    def setDragAndLift(*args, **kwargs):
        pass
    
    
    def setFriction(*args, **kwargs):
        pass
    
    
    def setIncompressibility(*args, **kwargs):
        pass
    
    
    def setInputMeshAttractAndRigidStrength(*args, **kwargs):
        pass
    
    
    def setInputMeshAttractDamping(*args, **kwargs):
        pass
    
    
    def setInputMeshAttractPositions(*args, **kwargs):
        pass
    
    
    def setInverseMass(*args, **kwargs):
        pass
    
    
    def setLinksRestLengthFromPositions(*args, **kwargs):
        pass
    
    
    def setMaxIterations(*args, **kwargs):
        pass
    
    
    def setMaxSelfCollisionIterations(*args, **kwargs):
        pass
    
    
    def setPositions(*args, **kwargs):
        pass
    
    
    def setPressure(*args, **kwargs):
        pass
    
    
    def setPressureDamping(*args, **kwargs):
        pass
    
    
    def setPumpRate(*args, **kwargs):
        pass
    
    
    def setRestitutionAngle(*args, **kwargs):
        pass
    
    
    def setRestitutionTension(*args, **kwargs):
        pass
    
    
    def setSealHoles(*args, **kwargs):
        pass
    
    
    def setSelfCollideWidth(*args, **kwargs):
        pass
    
    
    def setSelfCollisionFlags(*args, **kwargs):
        pass
    
    
    def setSelfCollisionSoftness(*args, **kwargs):
        pass
    
    
    def setSelfCrossoverPush(*args, **kwargs):
        pass
    
    
    def setSelfTrappedCheck(*args, **kwargs):
        pass
    
    
    def setShearResistance(*args, **kwargs):
        pass
    
    
    def setStartPressure(*args, **kwargs):
        pass
    
    
    def setStretchAndCompressionResistance(*args, **kwargs):
        pass
    
    
    def setTangentialDrag(*args, **kwargs):
        pass
    
    
    def setThickness(*args, **kwargs):
        pass
    
    
    def setTopology(*args, **kwargs):
        pass
    
    
    def setTrackVolume(*args, **kwargs):
        pass
    
    
    def setVelocities(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MFnTurbulenceField(MFnField):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def frequency(*args, **kwargs):
        pass
    
    
    def phase(*args, **kwargs):
        pass
    
    
    def setFrequency(*args, **kwargs):
        pass
    
    
    def setPhase(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnVortexField(MFnField):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def axis(*args, **kwargs):
        pass
    
    
    def setAxis(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnDragField(MFnField):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def direction(*args, **kwargs):
        pass
    
    
    def setDirection(*args, **kwargs):
        pass
    
    
    def setUseDirection(*args, **kwargs):
        pass
    
    
    def useDirection(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MnParticle(MnObject):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def createNParticle(*args, **kwargs):
        pass
    
    
    def getBounce(*args, **kwargs):
        pass
    
    
    def getFriction(*args, **kwargs):
        pass
    
    
    def getInverseMass(*args, **kwargs):
        pass
    
    
    def getNumVertices(*args, **kwargs):
        pass
    
    
    def getPositions(*args, **kwargs):
        pass
    
    
    def getThickness(*args, **kwargs):
        pass
    
    
    def getVelocities(*args, **kwargs):
        pass
    
    
    def setBounce(*args, **kwargs):
        pass
    
    
    def setCollide(*args, **kwargs):
        pass
    
    
    def setDamping(*args, **kwargs):
        pass
    
    
    def setDisableGravity(*args, **kwargs):
        pass
    
    
    def setDragAndLift(*args, **kwargs):
        pass
    
    
    def setFriction(*args, **kwargs):
        pass
    
    
    def setIncompressibility(*args, **kwargs):
        pass
    
    
    def setInverseMass(*args, **kwargs):
        pass
    
    
    def setLiquidRadiusScale(*args, **kwargs):
        pass
    
    
    def setLiquidSimulation(*args, **kwargs):
        pass
    
    
    def setMaxIterations(*args, **kwargs):
        pass
    
    
    def setMaxSelfCollisionIterations(*args, **kwargs):
        pass
    
    
    def setPositions(*args, **kwargs):
        pass
    
    
    def setRestDensity(*args, **kwargs):
        pass
    
    
    def setSelfCollide(*args, **kwargs):
        pass
    
    
    def setSelfCollideWidth(*args, **kwargs):
        pass
    
    
    def setSelfCollisionSoftness(*args, **kwargs):
        pass
    
    
    def setSurfaceTension(*args, **kwargs):
        pass
    
    
    def setThickness(*args, **kwargs):
        pass
    
    
    def setTopology(*args, **kwargs):
        pass
    
    
    def setVelocities(*args, **kwargs):
        pass
    
    
    def setViscosity(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MnRigid(MnObject):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def createNRigid(*args, **kwargs):
        pass
    
    
    def getBounce(*args, **kwargs):
        pass
    
    
    def getFriction(*args, **kwargs):
        pass
    
    
    def getInverseMass(*args, **kwargs):
        pass
    
    
    def getNumVertices(*args, **kwargs):
        pass
    
    
    def getPositions(*args, **kwargs):
        pass
    
    
    def getThickness(*args, **kwargs):
        pass
    
    
    def getVelocities(*args, **kwargs):
        pass
    
    
    def setBounce(*args, **kwargs):
        pass
    
    
    def setCollisionFlags(*args, **kwargs):
        pass
    
    
    def setFriction(*args, **kwargs):
        pass
    
    
    def setPositions(*args, **kwargs):
        pass
    
    
    def setThickness(*args, **kwargs):
        pass
    
    
    def setTopology(*args, **kwargs):
        pass
    
    
    def setVelocities(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnUniformField(MFnField):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def direction(*args, **kwargs):
        pass
    
    
    def setDirection(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnRadialField(MFnField):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def radialType(*args, **kwargs):
        pass
    
    
    def setType(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnGravityField(MFnField):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def direction(*args, **kwargs):
        pass
    
    
    def setDirection(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnNewtonField(MFnField):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def minDistance(*args, **kwargs):
        pass
    
    
    def setMinDistance(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnAirField(MFnField):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def componentOnly(*args, **kwargs):
        pass
    
    
    def direction(*args, **kwargs):
        pass
    
    
    def enableSpread(*args, **kwargs):
        pass
    
    
    def inheritRotation(*args, **kwargs):
        pass
    
    
    def inheritVelocity(*args, **kwargs):
        pass
    
    
    def setComponentOnly(*args, **kwargs):
        pass
    
    
    def setDirection(*args, **kwargs):
        pass
    
    
    def setEnableSpread(*args, **kwargs):
        pass
    
    
    def setInheritRotation(*args, **kwargs):
        pass
    
    
    def setInheritVelocity(*args, **kwargs):
        pass
    
    
    def setSpeed(*args, **kwargs):
        pass
    
    
    def setSpread(*args, **kwargs):
        pass
    
    
    def speed(*args, **kwargs):
        pass
    
    
    def spread(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnVolumeAxisField(MFnField):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def detailTurbulence(*args, **kwargs):
        pass
    
    
    def direction(*args, **kwargs):
        pass
    
    
    def directionalSpeed(*args, **kwargs):
        pass
    
    
    def invertAttenuation(*args, **kwargs):
        pass
    
    
    def setDirection(*args, **kwargs):
        pass
    
    
    def setDirectionalSpeed(*args, **kwargs):
        pass
    
    
    def setInvertAttenuation(*args, **kwargs):
        pass
    
    
    def setSpeedAlongAxis(*args, **kwargs):
        pass
    
    
    def setSpeedAroundAxis(*args, **kwargs):
        pass
    
    
    def setSpeedAwayFromAxis(*args, **kwargs):
        pass
    
    
    def setSpeedAwayFromCenter(*args, **kwargs):
        pass
    
    
    def setTurbulence(*args, **kwargs):
        pass
    
    
    def setTurbulenceFrequency(*args, **kwargs):
        pass
    
    
    def setTurbulenceOffset(*args, **kwargs):
        pass
    
    
    def setTurbulenceSpeed(*args, **kwargs):
        pass
    
    
    def speedAlongAxis(*args, **kwargs):
        pass
    
    
    def speedAroundAxis(*args, **kwargs):
        pass
    
    
    def speedAwayFromAxis(*args, **kwargs):
        pass
    
    
    def speedAwayFromCenter(*args, **kwargs):
        pass
    
    
    def turbulence(*args, **kwargs):
        pass
    
    
    def turbulenceFrequency(*args, **kwargs):
        pass
    
    
    def turbulenceOffset(*args, **kwargs):
        pass
    
    
    def turbulenceSpeed(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None

def MDynSweptLine_className(*args, **kwargs):
    pass


def MDynSweptLine_swigregister(*args, **kwargs):
    pass


def MDynSweptTriangle_className(*args, **kwargs):
    pass


def MDynSweptTriangle_swigregister(*args, **kwargs):
    pass


def MDynamicsUtil_evalDynamics2dTexture(*args, **kwargs):
    pass


def MDynamicsUtil_hasValidDynamics2dTexture(*args, **kwargs):
    pass


def MDynamicsUtil_swigregister(*args, **kwargs):
    pass


def MFnAirField_className(*args, **kwargs):
    pass


def MFnAirField_swigregister(*args, **kwargs):
    pass


def MFnDragField_className(*args, **kwargs):
    pass


def MFnDragField_swigregister(*args, **kwargs):
    pass


def MFnDynSweptGeometryData_className(*args, **kwargs):
    pass


def MFnDynSweptGeometryData_swigregister(*args, **kwargs):
    pass


def MFnField_className(*args, **kwargs):
    pass


def MFnField_swigregister(*args, **kwargs):
    pass


def MFnFluid_className(*args, **kwargs):
    pass


def MFnFluid_swigregister(*args, **kwargs):
    pass


def MFnGravityField_className(*args, **kwargs):
    pass


def MFnGravityField_swigregister(*args, **kwargs):
    pass


def MFnInstancer_className(*args, **kwargs):
    pass


def MFnInstancer_swigregister(*args, **kwargs):
    pass


def MFnNIdData_className(*args, **kwargs):
    pass


def MFnNIdData_swigregister(*args, **kwargs):
    pass


def MFnNObjectData_className(*args, **kwargs):
    pass


def MFnNObjectData_swigregister(*args, **kwargs):
    pass


def MFnNewtonField_className(*args, **kwargs):
    pass


def MFnNewtonField_swigregister(*args, **kwargs):
    pass


def MFnParticleSystem_className(*args, **kwargs):
    pass


def MFnParticleSystem_swigregister(*args, **kwargs):
    pass


def MFnPfxGeometry_className(*args, **kwargs):
    pass


def MFnPfxGeometry_swigregister(*args, **kwargs):
    pass


def MFnRadialField_className(*args, **kwargs):
    pass


def MFnRadialField_swigregister(*args, **kwargs):
    pass


def MFnTurbulenceField_className(*args, **kwargs):
    pass


def MFnTurbulenceField_swigregister(*args, **kwargs):
    pass


def MFnUniformField_className(*args, **kwargs):
    pass


def MFnUniformField_swigregister(*args, **kwargs):
    pass


def MFnVolumeAxisField_className(*args, **kwargs):
    pass


def MFnVolumeAxisField_swigregister(*args, **kwargs):
    pass


def MFnVortexField_className(*args, **kwargs):
    pass


def MFnVortexField_swigregister(*args, **kwargs):
    pass


def MHairSystem_className(*args, **kwargs):
    pass


def MHairSystem_getCollisionObject(*args, **kwargs):
    pass


def MHairSystem_getFollicle(*args, **kwargs):
    pass


def MHairSystem_registerCollisionSolverCollide(*args, **kwargs):
    pass


def MHairSystem_registerCollisionSolverPreFrame(*args, **kwargs):
    pass


def MHairSystem_registeringCallableScript(*args, **kwargs):
    pass


def MHairSystem_setRegisteringCallableScript(*args, **kwargs):
    pass


def MHairSystem_swigregister(*args, **kwargs):
    pass


def MHairSystem_unregisterCollisionSolverCollide(*args, **kwargs):
    pass


def MHairSystem_unregisterCollisionSolverPreFrame(*args, **kwargs):
    pass


def MRenderLineArray_className(*args, **kwargs):
    pass


def MRenderLineArray_swigregister(*args, **kwargs):
    pass


def MRenderLine_className(*args, **kwargs):
    pass


def MRenderLine_swigregister(*args, **kwargs):
    pass


def MnCloth_swigregister(*args, **kwargs):
    pass


def MnObject_swigregister(*args, **kwargs):
    pass


def MnParticle_swigregister(*args, **kwargs):
    pass


def MnRigid_swigregister(*args, **kwargs):
    pass


def MnSolver_swigregister(*args, **kwargs):
    pass


def weakref_proxy(*args, **kwargs):
    """
    proxy(object[, callback]) -- create a proxy object that weakly
    references 'object'.  'callback', if given, is called with a
    reference to the proxy when 'object' is about to be finalized.
    """

    pass

