import OpenMaya
import OpenMayaRender
import _OpenMayaUI
import new
import weakref

from maya._OpenMayaUI import *

class MObjectListFilter(object):
    def UIname(*args, **kwargs):
        pass
    
    
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def filterType(*args, **kwargs):
        pass
    
    
    def getList(*args, **kwargs):
        pass
    
    
    def name(*args, **kwargs):
        pass
    
    
    def requireListUpdate(*args, **kwargs):
        pass
    
    
    def setFilterType(*args, **kwargs):
        pass
    
    
    def setUIName(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def deregisterFilter(*args, **kwargs):
        pass
    
    
    def registerFilter(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kExclusionList = None
    
    
    kInclusionList = None
    
    
    kNumberOfFilterTypes = None


class MToolsInfo(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def isDirty(*args, **kwargs):
        pass
    
    
    def resetDirtyFlag(*args, **kwargs):
        pass
    
    
    def setDirtyFlag(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MDrawRequest(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def assign(*args, **kwargs):
        pass
    
    
    def color(*args, **kwargs):
        pass
    
    
    def component(*args, **kwargs):
        pass
    
    
    def displayCullOpposite(*args, **kwargs):
        pass
    
    
    def displayCulling(*args, **kwargs):
        pass
    
    
    def displayStatus(*args, **kwargs):
        pass
    
    
    def displayStyle(*args, **kwargs):
        pass
    
    
    def drawData(*args, **kwargs):
        pass
    
    
    def drawLast(*args, **kwargs):
        pass
    
    
    def isTransparent(*args, **kwargs):
        pass
    
    
    def material(*args, **kwargs):
        pass
    
    
    def matrix(*args, **kwargs):
        pass
    
    
    def multiPath(*args, **kwargs):
        pass
    
    
    def setColor(*args, **kwargs):
        pass
    
    
    def setComponent(*args, **kwargs):
        pass
    
    
    def setDisplayCullOpposite(*args, **kwargs):
        pass
    
    
    def setDisplayCulling(*args, **kwargs):
        pass
    
    
    def setDisplayStatus(*args, **kwargs):
        pass
    
    
    def setDisplayStyle(*args, **kwargs):
        pass
    
    
    def setDrawData(*args, **kwargs):
        pass
    
    
    def setDrawLast(*args, **kwargs):
        pass
    
    
    def setIsTransparent(*args, **kwargs):
        pass
    
    
    def setMaterial(*args, **kwargs):
        pass
    
    
    def setMatrix(*args, **kwargs):
        pass
    
    
    def setMultiPath(*args, **kwargs):
        pass
    
    
    def setToken(*args, **kwargs):
        pass
    
    
    def setView(*args, **kwargs):
        pass
    
    
    def token(*args, **kwargs):
        pass
    
    
    def view(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MEvent(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def getPosition(*args, **kwargs):
        pass
    
    
    def getWindowPosition(*args, **kwargs):
        pass
    
    
    def isModifierControl(*args, **kwargs):
        pass
    
    
    def isModifierKeyRelease(*args, **kwargs):
        pass
    
    
    def isModifierLeftMouseButton(*args, **kwargs):
        pass
    
    
    def isModifierMiddleMouseButton(*args, **kwargs):
        pass
    
    
    def isModifierNone(*args, **kwargs):
        pass
    
    
    def isModifierShift(*args, **kwargs):
        pass
    
    
    def modifiers(*args, **kwargs):
        pass
    
    
    def mouseButton(*args, **kwargs):
        pass
    
    
    def setModifiers(*args, **kwargs):
        pass
    
    
    def setPosition(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    controlKey = None
    
    
    kLeftMouse = None
    
    
    kMiddleMouse = None
    
    
    shiftKey = None


class MDeviceChannel(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def axisIndex(*args, **kwargs):
        pass
    
    
    def childByIndex(*args, **kwargs):
        pass
    
    
    def hasChildren(*args, **kwargs):
        pass
    
    
    def longName(*args, **kwargs):
        pass
    
    
    def name(*args, **kwargs):
        pass
    
    
    def numChildren(*args, **kwargs):
        pass
    
    
    def parent(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MDrawTraversal(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def enableFiltering(*args, **kwargs):
        pass
    
    
    def filterNode(*args, **kwargs):
        pass
    
    
    def filteringEnabled(*args, **kwargs):
        pass
    
    
    def frustumValid(*args, **kwargs):
        pass
    
    
    def itemHasStatus(*args, **kwargs):
        pass
    
    
    def itemPath(*args, **kwargs):
        pass
    
    
    def leafLevelCulling(*args, **kwargs):
        pass
    
    
    def numberOfItems(*args, **kwargs):
        pass
    
    
    def setFrustum(*args, **kwargs):
        pass
    
    
    def setLeafLevelCulling(*args, **kwargs):
        pass
    
    
    def setOrthoFrustum(*args, **kwargs):
        pass
    
    
    def setPerspFrustum(*args, **kwargs):
        pass
    
    
    def traverse(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kActiveItem = None
    
    
    kTemplateItem = None


class MFeedbackLine(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def clear(*args, **kwargs):
        pass
    
    
    def setFormat(*args, **kwargs):
        pass
    
    
    def setShowFeedback(*args, **kwargs):
        pass
    
    
    def setTitle(*args, **kwargs):
        pass
    
    
    def setValue(*args, **kwargs):
        pass
    
    
    def showFeedback(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MMaterial(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def applyTexture(*args, **kwargs):
        pass
    
    
    def evaluateDiffuse(*args, **kwargs):
        pass
    
    
    def evaluateEmission(*args, **kwargs):
        pass
    
    
    def evaluateMaterial(*args, **kwargs):
        pass
    
    
    def evaluateShininess(*args, **kwargs):
        pass
    
    
    def evaluateSpecular(*args, **kwargs):
        pass
    
    
    def evaluateTexture(*args, **kwargs):
        pass
    
    
    def evaluateTextureTransformation(*args, **kwargs):
        pass
    
    
    def getDiffuse(*args, **kwargs):
        pass
    
    
    def getEmission(*args, **kwargs):
        pass
    
    
    def getHasTransparency(*args, **kwargs):
        pass
    
    
    def getHwShaderNode(*args, **kwargs):
        pass
    
    
    def getShininess(*args, **kwargs):
        pass
    
    
    def getSpecular(*args, **kwargs):
        pass
    
    
    def getTextureTransformation(*args, **kwargs):
        pass
    
    
    def materialIsTextured(*args, **kwargs):
        pass
    
    
    def setMaterial(*args, **kwargs):
        pass
    
    
    def textureImage(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def defaultMaterial(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kAmbientColor = None
    
    
    kBumpMap = None
    
    
    kColor = None
    
    
    kCosinePower = None
    
    
    kDiffuse = None
    
    
    kEccentricity = None
    
    
    kHighlightSize = None
    
    
    kIncandescence = None
    
    
    kReflectedColor = None
    
    
    kReflectivity = None
    
    
    kRoughness = None
    
    
    kSpecularColor = None
    
    
    kSpecularRollOff = None
    
    
    kTransluscence = None
    
    
    kTransparency = None
    
    
    kWhiteness = None


class MDrawRequestQueue(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def add(*args, **kwargs):
        pass
    
    
    def assign(*args, **kwargs):
        pass
    
    
    def isEmpty(*args, **kwargs):
        pass
    
    
    def remove(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MUiMessage(OpenMaya.MMessage):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def add3dViewDestroyMsgCallback(*args, **kwargs):
        pass
    
    
    def add3dViewPostMultipleDrawPassMsgCallback(*args, **kwargs):
        pass
    
    
    def add3dViewPostRenderMsgCallback(*args, **kwargs):
        pass
    
    
    def add3dViewPreMultipleDrawPassMsgCallback(*args, **kwargs):
        pass
    
    
    def add3dViewPreRenderMsgCallback(*args, **kwargs):
        pass
    
    
    def addCameraChangedCallback(*args, **kwargs):
        pass
    
    
    def addUiDeletedCallback(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MDeviceState(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def buttonState(*args, **kwargs):
        pass
    
    
    def devicePosition(*args, **kwargs):
        pass
    
    
    def isNull(*args, **kwargs):
        pass
    
    
    def maxAxis(*args, **kwargs):
        pass
    
    
    def setButtonState(*args, **kwargs):
        pass
    
    
    def setDevicePosition(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MDrawInfo(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def canDrawComponent(*args, **kwargs):
        pass
    
    
    def completelyInside(*args, **kwargs):
        pass
    
    
    def displayStatus(*args, **kwargs):
        pass
    
    
    def displayStyle(*args, **kwargs):
        pass
    
    
    def getPrototype(*args, **kwargs):
        pass
    
    
    def inSelect(*args, **kwargs):
        pass
    
    
    def inUserInteraction(*args, **kwargs):
        pass
    
    
    def inclusiveMatrix(*args, **kwargs):
        pass
    
    
    def multiPath(*args, **kwargs):
        pass
    
    
    def objectDisplayStatus(*args, **kwargs):
        pass
    
    
    def projectionMatrix(*args, **kwargs):
        pass
    
    
    def setMultiPath(*args, **kwargs):
        pass
    
    
    def userChangingViewContext(*args, **kwargs):
        pass
    
    
    def view(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MProgressWindow(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def advanceProgress(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def endProgress(*args, **kwargs):
        pass
    
    
    def isCancelled(*args, **kwargs):
        pass
    
    
    def isInterruptable(*args, **kwargs):
        pass
    
    
    def progress(*args, **kwargs):
        pass
    
    
    def progressMax(*args, **kwargs):
        pass
    
    
    def progressMin(*args, **kwargs):
        pass
    
    
    def progressStatus(*args, **kwargs):
        pass
    
    
    def reserve(*args, **kwargs):
        pass
    
    
    def setInterruptable(*args, **kwargs):
        pass
    
    
    def setProgress(*args, **kwargs):
        pass
    
    
    def setProgressMax(*args, **kwargs):
        pass
    
    
    def setProgressMin(*args, **kwargs):
        pass
    
    
    def setProgressRange(*args, **kwargs):
        pass
    
    
    def setProgressStatus(*args, **kwargs):
        pass
    
    
    def setTitle(*args, **kwargs):
        pass
    
    
    def startProgress(*args, **kwargs):
        pass
    
    
    def title(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MManipData(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def asBool(*args, **kwargs):
        pass
    
    
    def asDouble(*args, **kwargs):
        pass
    
    
    def asFloat(*args, **kwargs):
        pass
    
    
    def asLong(*args, **kwargs):
        pass
    
    
    def asMObject(*args, **kwargs):
        pass
    
    
    def asShort(*args, **kwargs):
        pass
    
    
    def asUnsigned(*args, **kwargs):
        pass
    
    
    def assign(*args, **kwargs):
        pass
    
    
    def isSimple(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MHWShaderSwatchGenerator(OpenMayaRender.MSwatchRenderBase):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def createObj(*args, **kwargs):
        pass
    
    
    def getSwatchBackgroundColor(*args, **kwargs):
        pass
    
    
    def initialize(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MTextureEditorDrawInfo(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def drawingFunction(*args, **kwargs):
        pass
    
    
    def setDrawingFunction(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kDrawEdgeForSelect = None
    
    
    kDrawEverything = None
    
    
    kDrawFacetForSelect = None
    
    
    kDrawFunctionFirst = None
    
    
    kDrawFunctionLast = None
    
    
    kDrawUVForSelect = None
    
    
    kDrawVertexForSelect = None
    
    
    kDrawWireframe = None


class MCursor(object):
    def __eq__(*args, **kwargs):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __ne__(*args, **kwargs):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def assign(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    crossHairCursor = None
    
    
    defaultCursor = None
    
    
    doubleCrossHairCursor = None
    
    
    editCursor = None
    
    
    handCursor = None
    
    
    pencilCursor = None


class MFnManip3D(OpenMaya.MFnTransform):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def isOptimizePlaybackOn(*args, **kwargs):
        pass
    
    
    def isVisible(*args, **kwargs):
        pass
    
    
    def manipScale(*args, **kwargs):
        pass
    
    
    def rotateXYZValue(*args, **kwargs):
        pass
    
    
    def setManipScale(*args, **kwargs):
        pass
    
    
    def setOptimizePlayback(*args, **kwargs):
        pass
    
    
    def setVisible(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def deleteManipulator(*args, **kwargs):
        pass
    
    
    def globalSize(*args, **kwargs):
        pass
    
    
    def handleSize(*args, **kwargs):
        pass
    
    
    def lineSize(*args, **kwargs):
        pass
    
    
    def setGlobalSize(*args, **kwargs):
        pass
    
    
    def setHandleSize(*args, **kwargs):
        pass
    
    
    def setLineSize(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MQtUtil(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def addWidgetToMayaLayout(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def deregisterUIType(*args, **kwargs):
        pass
    
    
    def findControl(*args, **kwargs):
        pass
    
    
    def findLayout(*args, **kwargs):
        pass
    
    
    def findMenuItem(*args, **kwargs):
        pass
    
    
    def findWindow(*args, **kwargs):
        pass
    
    
    def fullName(*args, **kwargs):
        pass
    
    
    def getCurrentParent(*args, **kwargs):
        pass
    
    
    def getLayoutChildren(*args, **kwargs):
        pass
    
    
    def getParent(*args, **kwargs):
        pass
    
    
    def mainWindow(*args, **kwargs):
        pass
    
    
    def nativeWindow(*args, **kwargs):
        pass
    
    
    def registerUIType(*args, **kwargs):
        pass
    
    
    def toMString(*args, **kwargs):
        pass
    
    
    def toQString(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MDrawData(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def geometry(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class M3dView(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def backgroundColor(*args, **kwargs):
        pass
    
    
    def beginGL(*args, **kwargs):
        pass
    
    
    def beginProjMatrixOverride(*args, **kwargs):
        pass
    
    
    def beginSelect(*args, **kwargs):
        pass
    
    
    def beginXorDrawing(*args, **kwargs):
        pass
    
    
    def colorAtIndex(*args, **kwargs):
        pass
    
    
    def colorMask(*args, **kwargs):
        pass
    
    
    def display(*args, **kwargs):
        pass
    
    
    def displayStyle(*args, **kwargs):
        pass
    
    
    def drawText(*args, **kwargs):
        pass
    
    
    def endGL(*args, **kwargs):
        pass
    
    
    def endProjMatrixOverride(*args, **kwargs):
        pass
    
    
    def endSelect(*args, **kwargs):
        pass
    
    
    def endXorDrawing(*args, **kwargs):
        pass
    
    
    def getCamera(*args, **kwargs):
        pass
    
    
    def getColorIndexAndTable(*args, **kwargs):
        pass
    
    
    def getLightCount(*args, **kwargs):
        pass
    
    
    def getLightIndex(*args, **kwargs):
        pass
    
    
    def getLightPath(*args, **kwargs):
        pass
    
    
    def getLightingMode(*args, **kwargs):
        pass
    
    
    def getRendererName(*args, **kwargs):
        pass
    
    
    def getScreenPosition(*args, **kwargs):
        pass
    
    
    def glxContext(*args, **kwargs):
        pass
    
    
    def initNames(*args, **kwargs):
        pass
    
    
    def isLightVisible(*args, **kwargs):
        pass
    
    
    def isShadeActiveOnly(*args, **kwargs):
        pass
    
    
    def loadName(*args, **kwargs):
        pass
    
    
    def modelViewMatrix(*args, **kwargs):
        pass
    
    
    def multipleDrawEnabled(*args, **kwargs):
        pass
    
    
    def multipleDrawPassCount(*args, **kwargs):
        pass
    
    
    def numActiveColors(*args, **kwargs):
        pass
    
    
    def numDormantColors(*args, **kwargs):
        pass
    
    
    def numUserDefinedColors(*args, **kwargs):
        pass
    
    
    def objectDisplay(*args, **kwargs):
        pass
    
    
    def objectListFilterName(*args, **kwargs):
        pass
    
    
    def popName(*args, **kwargs):
        pass
    
    
    def popViewport(*args, **kwargs):
        pass
    
    
    def portHeight(*args, **kwargs):
        pass
    
    
    def portWidth(*args, **kwargs):
        pass
    
    
    def projectionMatrix(*args, **kwargs):
        pass
    
    
    def pushName(*args, **kwargs):
        pass
    
    
    def pushViewport(*args, **kwargs):
        pass
    
    
    def readBufferTo2dTexture(*args, **kwargs):
        pass
    
    
    def readColorBuffer(*args, **kwargs):
        pass
    
    
    def readDepthMap(*args, **kwargs):
        pass
    
    
    def refresh(*args, **kwargs):
        pass
    
    
    def renderOverrideName(*args, **kwargs):
        pass
    
    
    def rendererString(*args, **kwargs):
        pass
    
    
    def selectMode(*args, **kwargs):
        pass
    
    
    def setCamera(*args, **kwargs):
        pass
    
    
    def setColorMask(*args, **kwargs):
        pass
    
    
    def setDisplayStyle(*args, **kwargs):
        pass
    
    
    def setDrawColor(*args, **kwargs):
        pass
    
    
    def setMultipleDrawEnable(*args, **kwargs):
        pass
    
    
    def setMultipleDrawPassCount(*args, **kwargs):
        pass
    
    
    def setObjectDisplay(*args, **kwargs):
        pass
    
    
    def setObjectListFilterName(*args, **kwargs):
        pass
    
    
    def setRenderOverrideName(*args, **kwargs):
        pass
    
    
    def setShowViewSelectedChildren(*args, **kwargs):
        pass
    
    
    def setUserDefinedColor(*args, **kwargs):
        pass
    
    
    def setViewSelectedPrefix(*args, **kwargs):
        pass
    
    
    def showViewSelectedChildren(*args, **kwargs):
        pass
    
    
    def templateColor(*args, **kwargs):
        pass
    
    
    def textureMode(*args, **kwargs):
        pass
    
    
    def updateViewingParameters(*args, **kwargs):
        pass
    
    
    def userDefinedColorIndex(*args, **kwargs):
        pass
    
    
    def usingDefaultMaterial(*args, **kwargs):
        pass
    
    
    def usingMipmappedTextures(*args, **kwargs):
        pass
    
    
    def viewSelectedPrefix(*args, **kwargs):
        pass
    
    
    def viewToObjectSpace(*args, **kwargs):
        pass
    
    
    def viewToWorld(*args, **kwargs):
        pass
    
    
    def viewport(*args, **kwargs):
        pass
    
    
    def widget(*args, **kwargs):
        pass
    
    
    def window(*args, **kwargs):
        pass
    
    
    def wireframeOnlyInShadedMode(*args, **kwargs):
        pass
    
    
    def worldToView(*args, **kwargs):
        pass
    
    
    def writeColorBuffer(*args, **kwargs):
        pass
    
    
    def active3dView(*args, **kwargs):
        pass
    
    
    def applicationShell(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def get3dView(*args, **kwargs):
        pass
    
    
    def getM3dViewFromModelEditor(*args, **kwargs):
        pass
    
    
    def getM3dViewFromModelPanel(*args, **kwargs):
        pass
    
    
    def numberOf3dViews(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kActive = None
    
    
    kActiveAffected = None
    
    
    kActiveColors = None
    
    
    kActiveComponent = None
    
    
    kActiveTemplate = None
    
    
    kBackgroundColor = None
    
    
    kBoundingBox = None
    
    
    kCenter = None
    
    
    kDefaultQualityRenderer = None
    
    
    kDepth_8 = None
    
    
    kDepth_Float = None
    
    
    kDisplayCVs = None
    
    
    kDisplayCameras = None
    
    
    kDisplayDeformers = None
    
    
    kDisplayDimensions = None
    
    
    kDisplayDynamicConstraints = None
    
    
    kDisplayDynamics = None
    
    
    kDisplayEverything = None
    
    
    kDisplayFluids = None
    
    
    kDisplayFollicles = None
    
    
    kDisplayGrid = None
    
    
    kDisplayHairSystems = None
    
    
    kDisplayHulls = None
    
    
    kDisplayIkHandles = None
    
    
    kDisplayImagePlane = None
    
    
    kDisplayJoints = None
    
    
    kDisplayLights = None
    
    
    kDisplayLocators = None
    
    
    kDisplayManipulators = None
    
    
    kDisplayMeshes = None
    
    
    kDisplayNCloths = None
    
    
    kDisplayNParticles = None
    
    
    kDisplayNRigids = None
    
    
    kDisplayNurbsCurves = None
    
    
    kDisplayNurbsSurfaces = None
    
    
    kDisplayPivots = None
    
    
    kDisplayPlanes = None
    
    
    kDisplaySelectHandles = None
    
    
    kDisplayStrokes = None
    
    
    kDisplaySubdivSurfaces = None
    
    
    kDisplayTextures = None
    
    
    kDormant = None
    
    
    kDormantColors = None
    
    
    kExternalRenderer = None
    
    
    kFlatShaded = None
    
    
    kGouraudShaded = None
    
    
    kHighQualityRenderer = None
    
    
    kHilite = None
    
    
    kIntermediateObject = None
    
    
    kInvisible = None
    
    
    kLead = None
    
    
    kLeft = None
    
    
    kLightActive = None
    
    
    kLightAll = None
    
    
    kLightDefault = None
    
    
    kLightSelected = None
    
    
    kLive = None
    
    
    kNoStatus = None
    
    
    kPoints = None
    
    
    kRight = None
    
    
    kStippleDashed = None
    
    
    kStippleNone = None
    
    
    kTemplate = None
    
    
    kTemplateColor = None
    
    
    kWireFrame = None


class MFnDiscManip(MFnManip3D):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def angleIndex(*args, **kwargs):
        pass
    
    
    def axisIndex(*args, **kwargs):
        pass
    
    
    def centerIndex(*args, **kwargs):
        pass
    
    
    def connectToAnglePlug(*args, **kwargs):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def setAngle(*args, **kwargs):
        pass
    
    
    def setCenterPoint(*args, **kwargs):
        pass
    
    
    def setNormal(*args, **kwargs):
        pass
    
    
    def setRadius(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MSelectInfo(MDrawInfo):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def addSelection(*args, **kwargs):
        pass
    
    
    def getAlignmentMatrix(*args, **kwargs):
        pass
    
    
    def getLocalRay(*args, **kwargs):
        pass
    
    
    def highestPriority(*args, **kwargs):
        pass
    
    
    def isRay(*args, **kwargs):
        pass
    
    
    def selectClosest(*args, **kwargs):
        pass
    
    
    def selectForHilite(*args, **kwargs):
        pass
    
    
    def selectOnHilitedOnly(*args, **kwargs):
        pass
    
    
    def selectPath(*args, **kwargs):
        pass
    
    
    def selectable(*args, **kwargs):
        pass
    
    
    def selectableComponent(*args, **kwargs):
        pass
    
    
    def setHighestPriority(*args, **kwargs):
        pass
    
    
    def singleSelection(*args, **kwargs):
        pass
    
    
    def view(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnPointOnSurfaceManip(MFnManip3D):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def connectToParamPlug(*args, **kwargs):
        pass
    
    
    def connectToSurfacePlug(*args, **kwargs):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def getParameters(*args, **kwargs):
        pass
    
    
    def isDrawSurfaceOn(*args, **kwargs):
        pass
    
    
    def paramIndex(*args, **kwargs):
        pass
    
    
    def setDrawArrows(*args, **kwargs):
        pass
    
    
    def setDrawSurface(*args, **kwargs):
        pass
    
    
    def setParameters(*args, **kwargs):
        pass
    
    
    def surfaceIndex(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnStateManip(MFnManip3D):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def connectToStatePlug(*args, **kwargs):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def maxStates(*args, **kwargs):
        pass
    
    
    def positionIndex(*args, **kwargs):
        pass
    
    
    def setInitialState(*args, **kwargs):
        pass
    
    
    def setMaxStates(*args, **kwargs):
        pass
    
    
    def state(*args, **kwargs):
        pass
    
    
    def stateIndex(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnDistanceManip(MFnManip3D):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def connectToDistancePlug(*args, **kwargs):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def currentPointIndex(*args, **kwargs):
        pass
    
    
    def directionIndex(*args, **kwargs):
        pass
    
    
    def distanceIndex(*args, **kwargs):
        pass
    
    
    def isDrawLineOn(*args, **kwargs):
        pass
    
    
    def isDrawStartOn(*args, **kwargs):
        pass
    
    
    def scalingFactor(*args, **kwargs):
        pass
    
    
    def setDirection(*args, **kwargs):
        pass
    
    
    def setDrawLine(*args, **kwargs):
        pass
    
    
    def setDrawStart(*args, **kwargs):
        pass
    
    
    def setScalingFactor(*args, **kwargs):
        pass
    
    
    def setStartPoint(*args, **kwargs):
        pass
    
    
    def startPointIndex(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnRotateManip(MFnManip3D):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def connectToRotationCenterPlug(*args, **kwargs):
        pass
    
    
    def connectToRotationPlug(*args, **kwargs):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def displayWithNode(*args, **kwargs):
        pass
    
    
    def isSnapModeOn(*args, **kwargs):
        pass
    
    
    def rotateMode(*args, **kwargs):
        pass
    
    
    def rotationCenterIndex(*args, **kwargs):
        pass
    
    
    def rotationIndex(*args, **kwargs):
        pass
    
    
    def setInitialRotation(*args, **kwargs):
        pass
    
    
    def setRotateMode(*args, **kwargs):
        pass
    
    
    def setSnapIncrement(*args, **kwargs):
        pass
    
    
    def setSnapMode(*args, **kwargs):
        pass
    
    
    def snapIncrement(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kGimbal = None
    
    
    kObjectSpace = None
    
    
    kWorldSpace = None


class MFnCircleSweepManip(MFnManip3D):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def angleIndex(*args, **kwargs):
        pass
    
    
    def axisIndex(*args, **kwargs):
        pass
    
    
    def centerIndex(*args, **kwargs):
        pass
    
    
    def connectToAnglePlug(*args, **kwargs):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def endCircleIndex(*args, **kwargs):
        pass
    
    
    def endPoint(*args, **kwargs):
        pass
    
    
    def setAngle(*args, **kwargs):
        pass
    
    
    def setCenterPoint(*args, **kwargs):
        pass
    
    
    def setDrawAsArc(*args, **kwargs):
        pass
    
    
    def setEndPoint(*args, **kwargs):
        pass
    
    
    def setNormal(*args, **kwargs):
        pass
    
    
    def setRadius(*args, **kwargs):
        pass
    
    
    def setStartPoint(*args, **kwargs):
        pass
    
    
    def startCircleIndex(*args, **kwargs):
        pass
    
    
    def startPoint(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnPointOnCurveManip(MFnManip3D):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def connectToCurvePlug(*args, **kwargs):
        pass
    
    
    def connectToParamPlug(*args, **kwargs):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def curveIndex(*args, **kwargs):
        pass
    
    
    def curvePoint(*args, **kwargs):
        pass
    
    
    def isDrawCurveOn(*args, **kwargs):
        pass
    
    
    def paramIndex(*args, **kwargs):
        pass
    
    
    def parameter(*args, **kwargs):
        pass
    
    
    def setDrawCurve(*args, **kwargs):
        pass
    
    
    def setParameter(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnToggleManip(MFnManip3D):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def connectToTogglePlug(*args, **kwargs):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def direction(*args, **kwargs):
        pass
    
    
    def directionIndex(*args, **kwargs):
        pass
    
    
    def length(*args, **kwargs):
        pass
    
    
    def lengthIndex(*args, **kwargs):
        pass
    
    
    def setDirection(*args, **kwargs):
        pass
    
    
    def setLength(*args, **kwargs):
        pass
    
    
    def setStartPoint(*args, **kwargs):
        pass
    
    
    def setToggle(*args, **kwargs):
        pass
    
    
    def startPoint(*args, **kwargs):
        pass
    
    
    def startPointIndex(*args, **kwargs):
        pass
    
    
    def toggle(*args, **kwargs):
        pass
    
    
    def toggleIndex(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnCurveSegmentManip(MFnManip3D):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def connectToCurvePlug(*args, **kwargs):
        pass
    
    
    def connectToEndParamPlug(*args, **kwargs):
        pass
    
    
    def connectToStartParamPlug(*args, **kwargs):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def curveIndex(*args, **kwargs):
        pass
    
    
    def endParamIndex(*args, **kwargs):
        pass
    
    
    def endParameter(*args, **kwargs):
        pass
    
    
    def setEndParameter(*args, **kwargs):
        pass
    
    
    def setStartParameter(*args, **kwargs):
        pass
    
    
    def startParamIndex(*args, **kwargs):
        pass
    
    
    def startParameter(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnScaleManip(MFnManip3D):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def connectToScaleCenterPlug(*args, **kwargs):
        pass
    
    
    def connectToScalePlug(*args, **kwargs):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def displayWithNode(*args, **kwargs):
        pass
    
    
    def isSnapModeOn(*args, **kwargs):
        pass
    
    
    def scaleCenterIndex(*args, **kwargs):
        pass
    
    
    def scaleIndex(*args, **kwargs):
        pass
    
    
    def setInitialScale(*args, **kwargs):
        pass
    
    
    def setSnapIncrement(*args, **kwargs):
        pass
    
    
    def setSnapMode(*args, **kwargs):
        pass
    
    
    def snapIncrement(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnDirectionManip(MFnManip3D):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def connectToDirectionPlug(*args, **kwargs):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def directionIndex(*args, **kwargs):
        pass
    
    
    def endPointIndex(*args, **kwargs):
        pass
    
    
    def setDirection(*args, **kwargs):
        pass
    
    
    def setDrawStart(*args, **kwargs):
        pass
    
    
    def setNormalizeDirection(*args, **kwargs):
        pass
    
    
    def setStartPoint(*args, **kwargs):
        pass
    
    
    def startPointIndex(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MFnFreePointTriadManip(MFnManip3D):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def connectToPointPlug(*args, **kwargs):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def isDrawAxesOn(*args, **kwargs):
        pass
    
    
    def isKeyframeAllOn(*args, **kwargs):
        pass
    
    
    def isSnapModeOn(*args, **kwargs):
        pass
    
    
    def pointIndex(*args, **kwargs):
        pass
    
    
    def setDirection(*args, **kwargs):
        pass
    
    
    def setDrawArrowHead(*args, **kwargs):
        pass
    
    
    def setDrawAxes(*args, **kwargs):
        pass
    
    
    def setGlobalTriadPlane(*args, **kwargs):
        pass
    
    
    def setKeyframeAll(*args, **kwargs):
        pass
    
    
    def setPoint(*args, **kwargs):
        pass
    
    
    def setSnapMode(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kViewPlane = None
    
    
    kXYPlane = None
    
    
    kXZPlane = None
    
    
    kYZPlane = None

def M3dView_active3dView(*args, **kwargs):
    pass


def M3dView_applicationShell(*args, **kwargs):
    pass


def M3dView_className(*args, **kwargs):
    pass


def M3dView_get3dView(*args, **kwargs):
    pass


def M3dView_getM3dViewFromModelEditor(*args, **kwargs):
    pass


def M3dView_getM3dViewFromModelPanel(*args, **kwargs):
    pass


def M3dView_numberOf3dViews(*args, **kwargs):
    pass


def M3dView_swigregister(*args, **kwargs):
    pass


def MCursor_swigregister(*args, **kwargs):
    pass


def MDeviceChannel_swigregister(*args, **kwargs):
    pass


def MDeviceState_swigregister(*args, **kwargs):
    pass


def MDrawData_className(*args, **kwargs):
    pass


def MDrawData_swigregister(*args, **kwargs):
    pass


def MDrawInfo_className(*args, **kwargs):
    pass


def MDrawInfo_swigregister(*args, **kwargs):
    pass


def MDrawRequestQueue_className(*args, **kwargs):
    pass


def MDrawRequestQueue_swigregister(*args, **kwargs):
    pass


def MDrawRequest_className(*args, **kwargs):
    pass


def MDrawRequest_swigregister(*args, **kwargs):
    pass


def MDrawTraversal_swigregister(*args, **kwargs):
    pass


def MEvent_className(*args, **kwargs):
    pass


def MEvent_swigregister(*args, **kwargs):
    pass


def MFeedbackLine_className(*args, **kwargs):
    pass


def MFeedbackLine_clear(*args, **kwargs):
    pass


def MFeedbackLine_setFormat(*args, **kwargs):
    pass


def MFeedbackLine_setShowFeedback(*args, **kwargs):
    pass


def MFeedbackLine_setTitle(*args, **kwargs):
    pass


def MFeedbackLine_setValue(*args, **kwargs):
    pass


def MFeedbackLine_showFeedback(*args, **kwargs):
    pass


def MFeedbackLine_swigregister(*args, **kwargs):
    pass


def MFnCircleSweepManip_className(*args, **kwargs):
    pass


def MFnCircleSweepManip_swigregister(*args, **kwargs):
    pass


def MFnCurveSegmentManip_className(*args, **kwargs):
    pass


def MFnCurveSegmentManip_swigregister(*args, **kwargs):
    pass


def MFnDirectionManip_className(*args, **kwargs):
    pass


def MFnDirectionManip_swigregister(*args, **kwargs):
    pass


def MFnDiscManip_className(*args, **kwargs):
    pass


def MFnDiscManip_swigregister(*args, **kwargs):
    pass


def MFnDistanceManip_className(*args, **kwargs):
    pass


def MFnDistanceManip_swigregister(*args, **kwargs):
    pass


def MFnFreePointTriadManip_className(*args, **kwargs):
    pass


def MFnFreePointTriadManip_swigregister(*args, **kwargs):
    pass


def MFnManip3D_className(*args, **kwargs):
    pass


def MFnManip3D_deleteManipulator(*args, **kwargs):
    pass


def MFnManip3D_globalSize(*args, **kwargs):
    pass


def MFnManip3D_handleSize(*args, **kwargs):
    pass


def MFnManip3D_lineSize(*args, **kwargs):
    pass


def MFnManip3D_setGlobalSize(*args, **kwargs):
    pass


def MFnManip3D_setHandleSize(*args, **kwargs):
    pass


def MFnManip3D_setLineSize(*args, **kwargs):
    pass


def MFnManip3D_swigregister(*args, **kwargs):
    pass


def MFnPointOnCurveManip_className(*args, **kwargs):
    pass


def MFnPointOnCurveManip_swigregister(*args, **kwargs):
    pass


def MFnPointOnSurfaceManip_className(*args, **kwargs):
    pass


def MFnPointOnSurfaceManip_swigregister(*args, **kwargs):
    pass


def MFnRotateManip_className(*args, **kwargs):
    pass


def MFnRotateManip_swigregister(*args, **kwargs):
    pass


def MFnScaleManip_className(*args, **kwargs):
    pass


def MFnScaleManip_swigregister(*args, **kwargs):
    pass


def MFnStateManip_className(*args, **kwargs):
    pass


def MFnStateManip_swigregister(*args, **kwargs):
    pass


def MFnToggleManip_className(*args, **kwargs):
    pass


def MFnToggleManip_swigregister(*args, **kwargs):
    pass


def MHWShaderSwatchGenerator_createObj(*args, **kwargs):
    pass


def MHWShaderSwatchGenerator_getSwatchBackgroundColor(*args, **kwargs):
    pass


def MHWShaderSwatchGenerator_initialize(*args, **kwargs):
    pass


def MHWShaderSwatchGenerator_swigregister(*args, **kwargs):
    pass


def MManipData_className(*args, **kwargs):
    pass


def MManipData_swigregister(*args, **kwargs):
    pass


def MMaterial_className(*args, **kwargs):
    pass


def MMaterial_defaultMaterial(*args, **kwargs):
    pass


def MMaterial_swigregister(*args, **kwargs):
    pass


def MObjectListFilter_className(*args, **kwargs):
    pass


def MObjectListFilter_deregisterFilter(*args, **kwargs):
    pass


def MObjectListFilter_registerFilter(*args, **kwargs):
    pass


def MObjectListFilter_swigregister(*args, **kwargs):
    pass


def MProgressWindow_advanceProgress(*args, **kwargs):
    pass


def MProgressWindow_className(*args, **kwargs):
    pass


def MProgressWindow_endProgress(*args, **kwargs):
    pass


def MProgressWindow_isCancelled(*args, **kwargs):
    pass


def MProgressWindow_isInterruptable(*args, **kwargs):
    pass


def MProgressWindow_progress(*args, **kwargs):
    pass


def MProgressWindow_progressMax(*args, **kwargs):
    pass


def MProgressWindow_progressMin(*args, **kwargs):
    pass


def MProgressWindow_progressStatus(*args, **kwargs):
    pass


def MProgressWindow_reserve(*args, **kwargs):
    pass


def MProgressWindow_setInterruptable(*args, **kwargs):
    pass


def MProgressWindow_setProgress(*args, **kwargs):
    pass


def MProgressWindow_setProgressMax(*args, **kwargs):
    pass


def MProgressWindow_setProgressMin(*args, **kwargs):
    pass


def MProgressWindow_setProgressRange(*args, **kwargs):
    pass


def MProgressWindow_setProgressStatus(*args, **kwargs):
    pass


def MProgressWindow_setTitle(*args, **kwargs):
    pass


def MProgressWindow_startProgress(*args, **kwargs):
    pass


def MProgressWindow_swigregister(*args, **kwargs):
    pass


def MProgressWindow_title(*args, **kwargs):
    pass


def MQtUtil_addWidgetToMayaLayout(*args, **kwargs):
    pass


def MQtUtil_className(*args, **kwargs):
    pass


def MQtUtil_deregisterUIType(*args, **kwargs):
    pass


def MQtUtil_findControl(*args, **kwargs):
    pass


def MQtUtil_findLayout(*args, **kwargs):
    pass


def MQtUtil_findMenuItem(*args, **kwargs):
    pass


def MQtUtil_findWindow(*args, **kwargs):
    pass


def MQtUtil_fullName(*args, **kwargs):
    pass


def MQtUtil_getCurrentParent(*args, **kwargs):
    pass


def MQtUtil_getLayoutChildren(*args, **kwargs):
    pass


def MQtUtil_getParent(*args, **kwargs):
    pass


def MQtUtil_mainWindow(*args, **kwargs):
    pass


def MQtUtil_nativeWindow(*args, **kwargs):
    pass


def MQtUtil_registerUIType(*args, **kwargs):
    pass


def MQtUtil_swigregister(*args, **kwargs):
    pass


def MQtUtil_toMString(*args, **kwargs):
    pass


def MQtUtil_toQString(*args, **kwargs):
    pass


def MSelectInfo_className(*args, **kwargs):
    pass


def MSelectInfo_swigregister(*args, **kwargs):
    pass


def MTextureEditorDrawInfo_className(*args, **kwargs):
    pass


def MTextureEditorDrawInfo_swigregister(*args, **kwargs):
    pass


def MToolsInfo_className(*args, **kwargs):
    pass


def MToolsInfo_isDirty(*args, **kwargs):
    pass


def MToolsInfo_resetDirtyFlag(*args, **kwargs):
    pass


def MToolsInfo_setDirtyFlag(*args, **kwargs):
    pass


def MToolsInfo_swigregister(*args, **kwargs):
    pass


def MUiMessage_add3dViewDestroyMsgCallback(*args, **kwargs):
    pass


def MUiMessage_add3dViewPostMultipleDrawPassMsgCallback(*args, **kwargs):
    pass


def MUiMessage_add3dViewPostRenderMsgCallback(*args, **kwargs):
    pass


def MUiMessage_add3dViewPreMultipleDrawPassMsgCallback(*args, **kwargs):
    pass


def MUiMessage_add3dViewPreRenderMsgCallback(*args, **kwargs):
    pass


def MUiMessage_addCameraChangedCallback(*args, **kwargs):
    pass


def MUiMessage_addUiDeletedCallback(*args, **kwargs):
    pass


def MUiMessage_className(*args, **kwargs):
    pass


def MUiMessage_swigregister(*args, **kwargs):
    pass


def weakref_proxy(*args, **kwargs):
    """
    proxy(object[, callback]) -- create a proxy object that weakly
    references 'object'.  'callback', if given, is called with a
    reference to the proxy when 'object' is about to be finalized.
    """

    pass

cvar = None
