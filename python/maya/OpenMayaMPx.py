import OpenMaya
import OpenMayaAnim
import OpenMayaRender
import OpenMayaUI
import _OpenMayaMPx
import new
import weakref

from maya._OpenMayaMPx import *

class MPxUIControl(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MPxGeometryOverride(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def cleanUp(*args, **kwargs):
        pass
    
    
    def populateGeometry(*args, **kwargs):
        pass
    
    
    def updateDG(*args, **kwargs):
        pass
    
    
    def updateRenderItems(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MPxControlCommand(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def appendSyntax(*args, **kwargs):
        pass
    
    
    def clearResult(*args, **kwargs):
        pass
    
    
    def doEditFlags(*args, **kwargs):
        pass
    
    
    def doQueryFlags(*args, **kwargs):
        pass
    
    
    def makeControl(*args, **kwargs):
        pass
    
    
    def setResult(*args, **kwargs):
        pass
    
    
    def skipFlagForCreate(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MPxDrawOverride(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def boundingBox(*args, **kwargs):
        pass
    
    
    def prepareForDraw(*args, **kwargs):
        pass
    
    
    def transform(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MPxMidiInputDevice(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def closeDevice(*args, **kwargs):
        pass
    
    
    def deviceState(*args, **kwargs):
        pass
    
    
    def doButtonEvents(*args, **kwargs):
        pass
    
    
    def doMovementEvents(*args, **kwargs):
        pass
    
    
    def getMessage(*args, **kwargs):
        pass
    
    
    def nameAxes(*args, **kwargs):
        pass
    
    
    def nameButtons(*args, **kwargs):
        pass
    
    
    def openDevice(*args, **kwargs):
        pass
    
    
    def sendMessage(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MPxContext(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def abortAction(*args, **kwargs):
        pass
    
    
    def addManipulator(*args, **kwargs):
        pass
    
    
    def argTypeNumericalInput(*args, **kwargs):
        pass
    
    
    def completeAction(*args, **kwargs):
        pass
    
    
    def deleteAction(*args, **kwargs):
        pass
    
    
    def deleteManipulators(*args, **kwargs):
        pass
    
    
    def doDrag(*args, **kwargs):
        pass
    
    
    def doEnterRegion(*args, **kwargs):
        pass
    
    
    def doHold(*args, **kwargs):
        pass
    
    
    def doPress(*args, **kwargs):
        pass
    
    
    def doRelease(*args, **kwargs):
        pass
    
    
    def feedbackNumericalInput(*args, **kwargs):
        pass
    
    
    def helpStateHasChanged(*args, **kwargs):
        pass
    
    
    def image(*args, **kwargs):
        pass
    
    
    def newToolCommand(*args, **kwargs):
        pass
    
    
    def processNumericalInput(*args, **kwargs):
        pass
    
    
    def setImage(*args, **kwargs):
        pass
    
    
    def stringClassName(*args, **kwargs):
        pass
    
    
    def toolOffCleanup(*args, **kwargs):
        pass
    
    
    def toolOnSetup(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kImage1 = None
    
    
    kImage2 = None
    
    
    kImage3 = None


class MPxContextCommand(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def appendSyntax(*args, **kwargs):
        pass
    
    
    def doEditFlags(*args, **kwargs):
        pass
    
    
    def doQueryFlags(*args, **kwargs):
        pass
    
    
    def makeObj(*args, **kwargs):
        pass
    
    
    def setResult(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MPxBakeEngine(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def bake(*args, **kwargs):
        pass
    
    
    def getUVRange(*args, **kwargs):
        pass
    
    
    def setNeedTransparency(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    fInstance = None
    
    thisown = None
    
    __swig_destroy__ = None


class MPxShaderOverride(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def activateKey(*args, **kwargs):
        pass
    
    
    def draw(*args, **kwargs):
        pass
    
    
    def endUpdate(*args, **kwargs):
        pass
    
    
    def initialize(*args, **kwargs):
        pass
    
    
    def isTransparent(*args, **kwargs):
        pass
    
    
    def rebuildAlways(*args, **kwargs):
        pass
    
    
    def terminateKey(*args, **kwargs):
        pass
    
    
    def updateDG(*args, **kwargs):
        pass
    
    
    def updateDevice(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MPxCommand(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def commandString(*args, **kwargs):
        pass
    
    
    def doIt(*args, **kwargs):
        pass
    
    
    def hasSyntax(*args, **kwargs):
        pass
    
    
    def isHistoryOn(*args, **kwargs):
        pass
    
    
    def isUndoable(*args, **kwargs):
        pass
    
    
    def redoIt(*args, **kwargs):
        pass
    
    
    def setCommandString(*args, **kwargs):
        pass
    
    
    def setHistoryOn(*args, **kwargs):
        pass
    
    
    def setUndoable(*args, **kwargs):
        pass
    
    
    def syntax(*args, **kwargs):
        pass
    
    
    def undoIt(*args, **kwargs):
        pass
    
    
    def appendToResult(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def clearResult(*args, **kwargs):
        pass
    
    
    def currentDoubleResult(*args, **kwargs):
        pass
    
    
    def currentIntResult(*args, **kwargs):
        pass
    
    
    def currentResultType(*args, **kwargs):
        pass
    
    
    def currentStringResult(*args, **kwargs):
        pass
    
    
    def displayError(*args, **kwargs):
        pass
    
    
    def displayInfo(*args, **kwargs):
        pass
    
    
    def displayWarning(*args, **kwargs):
        pass
    
    
    def getCurrentResult(*args, **kwargs):
        pass
    
    
    def isCurrentResultArray(*args, **kwargs):
        pass
    
    
    def setResult(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kDouble = None
    
    
    kLong = None
    
    
    kNoArg = None
    
    
    kString = None


class MPxTransformationMatrix(object):
    def __disown__(self):
        pass
    
    
    def __eq__(*args, **kwargs):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __ne__(*args, **kwargs):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def asInterpolationMatrix(*args, **kwargs):
        pass
    
    
    def asMatrix(*args, **kwargs):
        pass
    
    
    def asMatrixInverse(*args, **kwargs):
        pass
    
    
    def asRotateMatrix(*args, **kwargs):
        pass
    
    
    def asRotateMatrixInverse(*args, **kwargs):
        pass
    
    
    def asScaleMatrix(*args, **kwargs):
        pass
    
    
    def asScaleMatrixInverse(*args, **kwargs):
        pass
    
    
    def asTransformationMatrix(*args, **kwargs):
        pass
    
    
    def assign(*args, **kwargs):
        pass
    
    
    def copyValues(*args, **kwargs):
        pass
    
    
    def decomposeMatrix(*args, **kwargs):
        pass
    
    
    def eulerRotateOrientation(*args, **kwargs):
        pass
    
    
    def eulerRotation(*args, **kwargs):
        pass
    
    
    def isEquivalent(*args, **kwargs):
        pass
    
    
    def reverse(*args, **kwargs):
        pass
    
    
    def rotateBy(*args, **kwargs):
        pass
    
    
    def rotateOrientation(*args, **kwargs):
        pass
    
    
    def rotatePivot(*args, **kwargs):
        pass
    
    
    def rotatePivotTranslation(*args, **kwargs):
        pass
    
    
    def rotateTo(*args, **kwargs):
        pass
    
    
    def rotation(*args, **kwargs):
        pass
    
    
    def rotationOrder(*args, **kwargs):
        pass
    
    
    def scale(*args, **kwargs):
        pass
    
    
    def scaleBy(*args, **kwargs):
        pass
    
    
    def scalePivot(*args, **kwargs):
        pass
    
    
    def scalePivotTranslation(*args, **kwargs):
        pass
    
    
    def scaleTo(*args, **kwargs):
        pass
    
    
    def setRotateOrientation(*args, **kwargs):
        pass
    
    
    def setRotatePivot(*args, **kwargs):
        pass
    
    
    def setRotatePivotTranslation(*args, **kwargs):
        pass
    
    
    def setRotationOrder(*args, **kwargs):
        pass
    
    
    def setScalePivot(*args, **kwargs):
        pass
    
    
    def setScalePivotTranslation(*args, **kwargs):
        pass
    
    
    def shear(*args, **kwargs):
        pass
    
    
    def shearBy(*args, **kwargs):
        pass
    
    
    def shearTo(*args, **kwargs):
        pass
    
    
    def transformBy(*args, **kwargs):
        pass
    
    
    def translateBy(*args, **kwargs):
        pass
    
    
    def translateTo(*args, **kwargs):
        pass
    
    
    def translation(*args, **kwargs):
        pass
    
    
    def typeId(*args, **kwargs):
        pass
    
    
    def unSquishIt(*args, **kwargs):
        pass
    
    
    def unSquishMatrix(*args, **kwargs):
        pass
    
    
    def convertEulerRotationOrder(*args, **kwargs):
        pass
    
    
    def convertTransformationRotationOrder(*args, **kwargs):
        pass
    
    
    def creator(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    baseTransformationMatrixId = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    identity = None


class MPxFileTranslator(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def allowMultipleFileOptimization(*args, **kwargs):
        pass
    
    
    def canBeOpened(*args, **kwargs):
        pass
    
    
    def defaultExtension(*args, **kwargs):
        pass
    
    
    def filter(*args, **kwargs):
        pass
    
    
    def haveNamespaceSupport(*args, **kwargs):
        pass
    
    
    def haveReadMethod(*args, **kwargs):
        pass
    
    
    def haveReferenceMethod(*args, **kwargs):
        pass
    
    
    def haveWriteMethod(*args, **kwargs):
        pass
    
    
    def identifyFile(*args, **kwargs):
        pass
    
    
    def reader(*args, **kwargs):
        pass
    
    
    def writer(*args, **kwargs):
        pass
    
    
    def fileAccessMode(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kCouldBeMyFileType = None
    
    
    kExportAccessMode = None
    
    
    kExportActiveAccessMode = None
    
    
    kImportAccessMode = None
    
    
    kIsMyFileType = None
    
    
    kNotMyFileType = None
    
    
    kOpenAccessMode = None
    
    
    kReferenceAccessMode = None
    
    
    kSaveAccessMode = None
    
    
    kUnknownAccessMode = None


class MPxModelEditorCommand(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def appendSyntax(*args, **kwargs):
        pass
    
    
    def doEditFlags(*args, **kwargs):
        pass
    
    
    def doQueryFlags(*args, **kwargs):
        pass
    
    
    def editorCommandName(*args, **kwargs):
        pass
    
    
    def editorMenuScriptName(*args, **kwargs):
        pass
    
    
    def makeModelView(*args, **kwargs):
        pass
    
    
    def modelView(*args, **kwargs):
        pass
    
    
    def setResult(*args, **kwargs):
        pass
    
    
    def skipFlagForCreate(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MFnPlugin(OpenMaya.MFnBase):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def addMenuItem(*args, **kwargs):
        pass
    
    
    def apiVersion(*args, **kwargs):
        pass
    
    
    def deregisterCacheFormat(*args, **kwargs):
        pass
    
    
    def deregisterCommand(*args, **kwargs):
        pass
    
    
    def deregisterConstraintCommand(*args, **kwargs):
        pass
    
    
    def deregisterContextCommand(*args, **kwargs):
        pass
    
    
    def deregisterControlCommand(*args, **kwargs):
        pass
    
    
    def deregisterData(*args, **kwargs):
        pass
    
    
    def deregisterDevice(*args, **kwargs):
        pass
    
    
    def deregisterDragAndDropBehavior(*args, **kwargs):
        pass
    
    
    def deregisterFileTranslator(*args, **kwargs):
        pass
    
    
    def deregisterIkSolver(*args, **kwargs):
        pass
    
    
    def deregisterImageFile(*args, **kwargs):
        pass
    
    
    def deregisterModelEditorCommand(*args, **kwargs):
        pass
    
    
    def deregisterNode(*args, **kwargs):
        pass
    
    
    def deregisterRenderPassImpl(*args, **kwargs):
        pass
    
    
    def loadPath(*args, **kwargs):
        pass
    
    
    def matrixTypeIdFromXformId(*args, **kwargs):
        pass
    
    
    def name(*args, **kwargs):
        pass
    
    
    def registerBakeEngine(*args, **kwargs):
        pass
    
    
    def registerCacheFormat(*args, **kwargs):
        pass
    
    
    def registerCommand(*args, **kwargs):
        pass
    
    
    def registerConstraintCommand(*args, **kwargs):
        pass
    
    
    def registerContextCommand(*args, **kwargs):
        pass
    
    
    def registerControlCommand(*args, **kwargs):
        pass
    
    
    def registerData(*args, **kwargs):
        pass
    
    
    def registerDevice(*args, **kwargs):
        pass
    
    
    def registerDragAndDropBehavior(*args, **kwargs):
        pass
    
    
    def registerFileTranslator(*args, **kwargs):
        pass
    
    
    def registerIkSolver(*args, **kwargs):
        pass
    
    
    def registerImageFile(*args, **kwargs):
        pass
    
    
    def registerMaterialInfo(*args, **kwargs):
        pass
    
    
    def registerModelEditorCommand(*args, **kwargs):
        pass
    
    
    def registerNode(*args, **kwargs):
        pass
    
    
    def registerRenderPassImpl(*args, **kwargs):
        pass
    
    
    def registerShape(*args, **kwargs):
        pass
    
    
    def registerTransform(*args, **kwargs):
        pass
    
    
    def registerUI(*args, **kwargs):
        pass
    
    
    def registerUIStrings(*args, **kwargs):
        pass
    
    
    def removeMenuItem(*args, **kwargs):
        pass
    
    
    def setName(*args, **kwargs):
        pass
    
    
    def setVersion(*args, **kwargs):
        pass
    
    
    def unregisterBakeEngine(*args, **kwargs):
        pass
    
    
    def unregisterMaterialInfo(*args, **kwargs):
        pass
    
    
    def vendor(*args, **kwargs):
        pass
    
    
    def version(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def findPlugin(*args, **kwargs):
        pass
    
    
    def isNodeRegistered(*args, **kwargs):
        pass
    
    
    def registeringCallableScript(*args, **kwargs):
        pass
    
    
    def setRegisteringCallableScript(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kDefaultDataLocation = None


class MPxSurfaceShapeUI(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def canDrawUV(*args, **kwargs):
        pass
    
    
    def draw(*args, **kwargs):
        pass
    
    
    def drawUV(*args, **kwargs):
        pass
    
    
    def getDrawData(*args, **kwargs):
        pass
    
    
    def getDrawRequests(*args, **kwargs):
        pass
    
    
    def material(*args, **kwargs):
        pass
    
    
    def select(*args, **kwargs):
        pass
    
    
    def selectUV(*args, **kwargs):
        pass
    
    
    def surfaceShape(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def surfaceShapeUI(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kSelectMeshEdges = None
    
    
    kSelectMeshFaces = None
    
    
    kSelectMeshUVs = None
    
    
    kSelectMeshVerts = None


class MPxRenderPassImpl(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def frameBufferSemantic(*args, **kwargs):
        pass
    
    
    def getDefaultType(*args, **kwargs):
        pass
    
    
    def getNumChannels(*args, **kwargs):
        pass
    
    
    def isCompatible(*args, **kwargs):
        pass
    
    
    def perLightPassContributionSupported(*args, **kwargs):
        pass
    
    
    def typesSupported(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kBit = None
    
    
    kColorSemantic = None
    
    
    kDepthSemantic = None
    
    
    kDirectionVectorSemantic = None
    
    
    kFloat16 = None
    
    
    kFloat32 = None
    
    
    kFloat64 = None
    
    
    kInt16 = None
    
    
    kInt32 = None
    
    
    kInt64 = None
    
    
    kInt8 = None
    
    
    kInvalidSemantic = None
    
    
    kLabelSemantic = None
    
    
    kMaskSemantic = None
    
    
    kOther = None
    
    
    kOtherSemantic = None
    
    
    kUInt16 = None
    
    
    kUInt32 = None
    
    
    kUInt64 = None
    
    
    kUInt8 = None
    
    
    kVectorSemantic = None


class MPxGlBuffer(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def attributeList(*args, **kwargs):
        pass
    
    
    def beginBufferNotify(*args, **kwargs):
        pass
    
    
    def close(*args, **kwargs):
        pass
    
    
    def context(*args, **kwargs):
        pass
    
    
    def display(*args, **kwargs):
        pass
    
    
    def drawable(*args, **kwargs):
        pass
    
    
    def endBufferNotify(*args, **kwargs):
        pass
    
    
    def open(*args, **kwargs):
        pass
    
    
    def setDisplay(*args, **kwargs):
        pass
    
    
    def setDoubleBuffer(*args, **kwargs):
        pass
    
    
    def setDrawable(*args, **kwargs):
        pass
    
    
    def setUseExternalDrawable(*args, **kwargs):
        pass
    
    
    def setVisual(*args, **kwargs):
        pass
    
    
    def visual(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MPx3dModelView(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def backgroundColor(*args, **kwargs):
        pass
    
    
    def beginGL(*args, **kwargs):
        pass
    
    
    def beginXorDrawing(*args, **kwargs):
        pass
    
    
    def colorAtIndex(*args, **kwargs):
        pass
    
    
    def customDraw(*args, **kwargs):
        pass
    
    
    def customDrawEnabled(*args, **kwargs):
        pass
    
    
    def destroyOnPanelDestruction(*args, **kwargs):
        pass
    
    
    def displayAxisAtOriginOn(*args, **kwargs):
        pass
    
    
    def displayAxisOn(*args, **kwargs):
        pass
    
    
    def displayCameraAnnotationOn(*args, **kwargs):
        pass
    
    
    def displayHUD(*args, **kwargs):
        pass
    
    
    def displayStyle(*args, **kwargs):
        pass
    
    
    def doUpdateOnMove(*args, **kwargs):
        pass
    
    
    def drawAdornments(*args, **kwargs):
        pass
    
    
    def drawAdornmentsNow(*args, **kwargs):
        pass
    
    
    def drawHUDNow(*args, **kwargs):
        pass
    
    
    def drawOnePass(*args, **kwargs):
        pass
    
    
    def drawText(*args, **kwargs):
        pass
    
    
    def endGL(*args, **kwargs):
        pass
    
    
    def endXorDrawing(*args, **kwargs):
        pass
    
    
    def fogColor(*args, **kwargs):
        pass
    
    
    def fogDensity(*args, **kwargs):
        pass
    
    
    def fogEnd(*args, **kwargs):
        pass
    
    
    def fogMode(*args, **kwargs):
        pass
    
    
    def fogSource(*args, **kwargs):
        pass
    
    
    def fogStart(*args, **kwargs):
        pass
    
    
    def getAsM3dView(*args, **kwargs):
        pass
    
    
    def getCamera(*args, **kwargs):
        pass
    
    
    def getCameraHUDName(*args, **kwargs):
        pass
    
    
    def getCameraSet(*args, **kwargs):
        pass
    
    
    def getColorIndexAndTable(*args, **kwargs):
        pass
    
    
    def getCurrentCameraSetCamera(*args, **kwargs):
        pass
    
    
    def getObjectsToView(*args, **kwargs):
        pass
    
    
    def hasStereoBufferSupport(*args, **kwargs):
        pass
    
    
    def isBackfaceCulling(*args, **kwargs):
        pass
    
    
    def isBackgroundFogEnabled(*args, **kwargs):
        pass
    
    
    def isFogEnabled(*args, **kwargs):
        pass
    
    
    def isShadeActiveOnly(*args, **kwargs):
        pass
    
    
    def isTextureDisplayEnabled(*args, **kwargs):
        pass
    
    
    def isTwoSidedLighting(*args, **kwargs):
        pass
    
    
    def isVisible(*args, **kwargs):
        pass
    
    
    def isWireframeOnShaded(*args, **kwargs):
        pass
    
    
    def isXrayEnabled(*args, **kwargs):
        pass
    
    
    def lightingMode(*args, **kwargs):
        pass
    
    
    def multipleDrawEnabled(*args, **kwargs):
        pass
    
    
    def multipleDrawPassCount(*args, **kwargs):
        pass
    
    
    def name(*args, **kwargs):
        pass
    
    
    def numActiveColors(*args, **kwargs):
        pass
    
    
    def numDormantColors(*args, **kwargs):
        pass
    
    
    def numUserDefinedColors(*args, **kwargs):
        pass
    
    
    def objectDisplay(*args, **kwargs):
        pass
    
    
    def okForMultipleDraw(*args, **kwargs):
        pass
    
    
    def portHeight(*args, **kwargs):
        pass
    
    
    def portWidth(*args, **kwargs):
        pass
    
    
    def postMultipleDraw(*args, **kwargs):
        pass
    
    
    def postMultipleDrawPass(*args, **kwargs):
        pass
    
    
    def preMultipleDraw(*args, **kwargs):
        pass
    
    
    def preMultipleDrawPass(*args, **kwargs):
        pass
    
    
    def refresh(*args, **kwargs):
        pass
    
    
    def removingCamera(*args, **kwargs):
        pass
    
    
    def setBackfaceCulling(*args, **kwargs):
        pass
    
    
    def setBackgroundFogEnabled(*args, **kwargs):
        pass
    
    
    def setCamera(*args, **kwargs):
        pass
    
    
    def setCameraInDraw(*args, **kwargs):
        pass
    
    
    def setCameraSet(*args, **kwargs):
        pass
    
    
    def setCurrentCameraSetCamera(*args, **kwargs):
        pass
    
    
    def setCustomDrawEnable(*args, **kwargs):
        pass
    
    
    def setDestroyOnPanelDestruction(*args, **kwargs):
        pass
    
    
    def setDisplayAxis(*args, **kwargs):
        pass
    
    
    def setDisplayAxisAtOrigin(*args, **kwargs):
        pass
    
    
    def setDisplayCameraAnnotation(*args, **kwargs):
        pass
    
    
    def setDisplayHUD(*args, **kwargs):
        pass
    
    
    def setDisplayStyle(*args, **kwargs):
        pass
    
    
    def setDoUpdateOnMove(*args, **kwargs):
        pass
    
    
    def setDrawAdornments(*args, **kwargs):
        pass
    
    
    def setDrawColor(*args, **kwargs):
        pass
    
    
    def setFogColor(*args, **kwargs):
        pass
    
    
    def setFogDensity(*args, **kwargs):
        pass
    
    
    def setFogEnabled(*args, **kwargs):
        pass
    
    
    def setFogEnd(*args, **kwargs):
        pass
    
    
    def setFogMode(*args, **kwargs):
        pass
    
    
    def setFogSource(*args, **kwargs):
        pass
    
    
    def setFogStart(*args, **kwargs):
        pass
    
    
    def setInStereoDrawMode(*args, **kwargs):
        pass
    
    
    def setLightingMode(*args, **kwargs):
        pass
    
    
    def setMultipleDrawEnable(*args, **kwargs):
        pass
    
    
    def setObjectDisplay(*args, **kwargs):
        pass
    
    
    def setObjectsToView(*args, **kwargs):
        pass
    
    
    def setTextureDisplayEnabled(*args, **kwargs):
        pass
    
    
    def setTwoSidedLighting(*args, **kwargs):
        pass
    
    
    def setUserDefinedColor(*args, **kwargs):
        pass
    
    
    def setViewSelected(*args, **kwargs):
        pass
    
    
    def setViewSelectedPrefix(*args, **kwargs):
        pass
    
    
    def setViewSelectedSet(*args, **kwargs):
        pass
    
    
    def setWireframeOnShaded(*args, **kwargs):
        pass
    
    
    def setXrayEnabled(*args, **kwargs):
        pass
    
    
    def templateColor(*args, **kwargs):
        pass
    
    
    def updateViewingParameters(*args, **kwargs):
        pass
    
    
    def userDefinedColorIndex(*args, **kwargs):
        pass
    
    
    def viewSelected(*args, **kwargs):
        pass
    
    
    def viewSelectedPrefix(*args, **kwargs):
        pass
    
    
    def viewSelectedSet(*args, **kwargs):
        pass
    
    
    def viewToObjectSpace(*args, **kwargs):
        pass
    
    
    def viewToWorld(*args, **kwargs):
        pass
    
    
    def viewType(*args, **kwargs):
        pass
    
    
    def wantStereoGLBuffer(*args, **kwargs):
        pass
    
    
    def worldToView(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def getModelView(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kFogCoordinate = None
    
    
    kFogExponential = None
    
    
    kFogExponentialSquared = None
    
    
    kFogFragment = None
    
    
    kFogLinear = None
    
    
    kLightActive = None
    
    
    kLightAll = None
    
    
    kLightDefault = None
    
    
    kLightNone = None
    
    
    kLightQuality = None
    
    
    kLightSelected = None


class MPxImageFile(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def close(*args, **kwargs):
        pass
    
    
    def glLoad(*args, **kwargs):
        pass
    
    
    def load(*args, **kwargs):
        pass
    
    
    def open(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MPxGeometryIterator(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def component(*args, **kwargs):
        pass
    
    
    def currentPoint(*args, **kwargs):
        pass
    
    
    def geometry(*args, **kwargs):
        pass
    
    
    def hasNormals(*args, **kwargs):
        pass
    
    
    def hasPoints(*args, **kwargs):
        pass
    
    
    def index(*args, **kwargs):
        pass
    
    
    def indexUnsimplified(*args, **kwargs):
        pass
    
    
    def isDone(*args, **kwargs):
        pass
    
    
    def iteratorCount(*args, **kwargs):
        pass
    
    
    def maxPoints(*args, **kwargs):
        pass
    
    
    def next(*args, **kwargs):
        pass
    
    
    def point(*args, **kwargs):
        pass
    
    
    def reset(*args, **kwargs):
        pass
    
    
    def setCurrentPoint(*args, **kwargs):
        pass
    
    
    def setMaxPoints(*args, **kwargs):
        pass
    
    
    def setObject(*args, **kwargs):
        pass
    
    
    def setPoint(*args, **kwargs):
        pass
    
    
    def setPointGetNext(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MPxNode(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def compute(*args, **kwargs):
        pass
    
    
    def connectionBroken(*args, **kwargs):
        pass
    
    
    def connectionMade(*args, **kwargs):
        pass
    
    
    def copyInternalData(*args, **kwargs):
        pass
    
    
    def existWithoutInConnections(*args, **kwargs):
        pass
    
    
    def existWithoutOutConnections(*args, **kwargs):
        pass
    
    
    def getFilesToArchive(*args, **kwargs):
        pass
    
    
    def getInternalValue(*args, **kwargs):
        pass
    
    
    def getInternalValueInContext(*args, **kwargs):
        pass
    
    
    def internalArrayCount(*args, **kwargs):
        pass
    
    
    def isAbstractClass(*args, **kwargs):
        pass
    
    
    def isPassiveOutput(*args, **kwargs):
        pass
    
    
    def legalConnection(*args, **kwargs):
        pass
    
    
    def legalDisconnection(*args, **kwargs):
        pass
    
    
    def name(*args, **kwargs):
        pass
    
    
    def passThroughToMany(*args, **kwargs):
        pass
    
    
    def passThroughToOne(*args, **kwargs):
        pass
    
    
    def postConstructor(*args, **kwargs):
        pass
    
    
    def setDependentsDirty(*args, **kwargs):
        pass
    
    
    def setExistWithoutInConnections(*args, **kwargs):
        pass
    
    
    def setExistWithoutOutConnections(*args, **kwargs):
        pass
    
    
    def setInternalValue(*args, **kwargs):
        pass
    
    
    def setInternalValueInContext(*args, **kwargs):
        pass
    
    
    def shouldSave(*args, **kwargs):
        pass
    
    
    def thisMObject(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    def typeId(*args, **kwargs):
        pass
    
    
    def typeName(*args, **kwargs):
        pass
    
    
    def addAttribute(*args, **kwargs):
        pass
    
    
    def attributeAffects(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def inheritAttributesFrom(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    caching = None
    
    isHistoricallyInteresting = None
    
    message = None
    
    state = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kCameraSetNode = None
    
    
    kConstraintNode = None
    
    
    kDeformerNode = None
    
    
    kDependNode = None
    
    
    kEmitterNode = None
    
    
    kFieldNode = None
    
    
    kFluidEmitterNode = None
    
    
    kHardwareShader = None
    
    
    kHwShaderNode = None
    
    
    kIkSolverNode = None
    
    
    kImagePlaneNode = None
    
    
    kLast = None
    
    
    kLocatorNode = None
    
    
    kManipContainer = None
    
    
    kManipulatorNode = None
    
    
    kObjectSet = None
    
    
    kParticleAttributeMapperNode = None
    
    
    kSpringNode = None
    
    
    kSurfaceShape = None
    
    
    kTransformNode = None


class MPxMaterialInformation(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def computeMaterial(*args, **kwargs):
        pass
    
    
    def connectAsTexture(*args, **kwargs):
        pass
    
    
    def materialInfoIsDirty(*args, **kwargs):
        pass
    
    
    def textureDisconnected(*args, **kwargs):
        pass
    
    
    def useMaterialAsTexture(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    fInstance = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kOverrideDraw = None
    
    
    kSimpleMaterial = None
    
    
    kTexture = None


class MaterialInputData(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    ambient = None
    
    diffuse = None
    
    emission = None
    
    hasTransparency = None
    
    shininess = None
    
    specular = None
    
    thisown = None
    
    __swig_destroy__ = None


class MPxCacheFormat(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def beginReadChunk(*args, **kwargs):
        pass
    
    
    def beginWriteChunk(*args, **kwargs):
        pass
    
    
    def close(*args, **kwargs):
        pass
    
    
    def endReadChunk(*args, **kwargs):
        pass
    
    
    def endWriteChunk(*args, **kwargs):
        pass
    
    
    def extension(*args, **kwargs):
        pass
    
    
    def findChannelName(*args, **kwargs):
        pass
    
    
    def findTime(*args, **kwargs):
        pass
    
    
    def handlesDescription(*args, **kwargs):
        pass
    
    
    def isValid(*args, **kwargs):
        pass
    
    
    def open(*args, **kwargs):
        pass
    
    
    def readArraySize(*args, **kwargs):
        pass
    
    
    def readChannelName(*args, **kwargs):
        pass
    
    
    def readDescription(*args, **kwargs):
        pass
    
    
    def readDoubleArray(*args, **kwargs):
        pass
    
    
    def readDoubleVectorArray(*args, **kwargs):
        pass
    
    
    def readFloatArray(*args, **kwargs):
        pass
    
    
    def readFloatVectorArray(*args, **kwargs):
        pass
    
    
    def readHeader(*args, **kwargs):
        pass
    
    
    def readInt32(*args, **kwargs):
        pass
    
    
    def readIntArray(*args, **kwargs):
        pass
    
    
    def readNextTime(*args, **kwargs):
        pass
    
    
    def readTime(*args, **kwargs):
        pass
    
    
    def rewind(*args, **kwargs):
        pass
    
    
    def writeChannelName(*args, **kwargs):
        pass
    
    
    def writeDescription(*args, **kwargs):
        pass
    
    
    def writeDoubleArray(*args, **kwargs):
        pass
    
    
    def writeDoubleVectorArray(*args, **kwargs):
        pass
    
    
    def writeFloatArray(*args, **kwargs):
        pass
    
    
    def writeFloatVectorArray(*args, **kwargs):
        pass
    
    
    def writeHeader(*args, **kwargs):
        pass
    
    
    def writeInt32(*args, **kwargs):
        pass
    
    
    def writeIntArray(*args, **kwargs):
        pass
    
    
    def writeTime(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kRead = None
    
    
    kReadWrite = None
    
    
    kWrite = None


class MPxDragAndDropBehavior(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def connectAttrToAttr(*args, **kwargs):
        pass
    
    
    def connectAttrToNode(*args, **kwargs):
        pass
    
    
    def connectNodeToAttr(*args, **kwargs):
        pass
    
    
    def connectNodeToNode(*args, **kwargs):
        pass
    
    
    def shouldBeUsedFor(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MPxMayaAsciiFilterOutput(object):
    def __init__(self, *args):
        pass
    
    
    def __lshift__(*args, **kwargs):
        pass
    
    
    def __repr__(self):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MPxData(object):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def copy(*args, **kwargs):
        pass
    
    
    def name(*args, **kwargs):
        pass
    
    
    def readASCII(*args, **kwargs):
        pass
    
    
    def readBinary(*args, **kwargs):
        pass
    
    
    def typeId(*args, **kwargs):
        pass
    
    
    def writeASCII(*args, **kwargs):
        pass
    
    
    def writeBinary(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kData = None
    
    
    kGeometryData = None
    
    
    kLast = None


class MPxEmitterNode(MPxNode):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def compute(*args, **kwargs):
        pass
    
    
    def draw(*args, **kwargs):
        pass
    
    
    def evalEmission2dTexture(*args, **kwargs):
        pass
    
    
    def getCurrentTime(*args, **kwargs):
        pass
    
    
    def getDeltaTime(*args, **kwargs):
        pass
    
    
    def getEmitterType(*args, **kwargs):
        pass
    
    
    def getMaxDistance(*args, **kwargs):
        pass
    
    
    def getMinDistance(*args, **kwargs):
        pass
    
    
    def getOwnerShape(*args, **kwargs):
        pass
    
    
    def getRandomSeed(*args, **kwargs):
        pass
    
    
    def getRandomState(*args, **kwargs):
        pass
    
    
    def getRate(*args, **kwargs):
        pass
    
    
    def getStartTime(*args, **kwargs):
        pass
    
    
    def getWorldMatrix(*args, **kwargs):
        pass
    
    
    def getWorldPosition(*args, **kwargs):
        pass
    
    
    def hasValidEmission2dTexture(*args, **kwargs):
        pass
    
    
    def randgen(*args, **kwargs):
        pass
    
    
    def resetRandomState(*args, **kwargs):
        pass
    
    
    def setRandomState(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    def volumePrimitiveBoundingBox(*args, **kwargs):
        pass
    
    
    def volumePrimitiveDistanceFromAxis(*args, **kwargs):
        pass
    
    
    def volumePrimitivePointInside(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    mCurrentTime = None
    
    mDeltaTime = None
    
    mDirection = None
    
    mDirectionX = None
    
    mDirectionY = None
    
    mDirectionZ = None
    
    mEmitterType = None
    
    mInheritFactor = None
    
    mIsFull = None
    
    mMaxDistance = None
    
    mMinDistance = None
    
    mOutput = None
    
    mOwnerCentroid = None
    
    mOwnerCentroidX = None
    
    mOwnerCentroidY = None
    
    mOwnerCentroidZ = None
    
    mOwnerPosData = None
    
    mOwnerVelData = None
    
    mRandState = None
    
    mRandStateX = None
    
    mRandStateY = None
    
    mRandStateZ = None
    
    mRate = None
    
    mSeed = None
    
    mSpeed = None
    
    mStartTime = None
    
    mSweptGeometry = None
    
    mWorldMatrix = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kCurve = None
    
    
    kDirectional = None
    
    
    kOmni = None
    
    
    kSurface = None
    
    
    kVolume = None


class MPxIkSolverNode(MPxNode):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def create(*args, **kwargs):
        pass
    
    
    def doSolve(*args, **kwargs):
        pass
    
    
    def funcValueTolerance(*args, **kwargs):
        pass
    
    
    def groupHandlesByTopology(*args, **kwargs):
        pass
    
    
    def handleGroup(*args, **kwargs):
        pass
    
    
    def hasJointLimitSupport(*args, **kwargs):
        pass
    
    
    def hasUniqueSolution(*args, **kwargs):
        pass
    
    
    def isPositionOnly(*args, **kwargs):
        pass
    
    
    def isSingleChainOnly(*args, **kwargs):
        pass
    
    
    def maxIterations(*args, **kwargs):
        pass
    
    
    def positionOnly(*args, **kwargs):
        pass
    
    
    def postSolve(*args, **kwargs):
        pass
    
    
    def preSolve(*args, **kwargs):
        pass
    
    
    def rotatePlane(*args, **kwargs):
        pass
    
    
    def setFuncValueTolerance(*args, **kwargs):
        pass
    
    
    def setHandleGroup(*args, **kwargs):
        pass
    
    
    def setMaxIterations(*args, **kwargs):
        pass
    
    
    def setPositionOnly(*args, **kwargs):
        pass
    
    
    def setRotatePlane(*args, **kwargs):
        pass
    
    
    def setSingleChainOnly(*args, **kwargs):
        pass
    
    
    def setSupportJointLimits(*args, **kwargs):
        pass
    
    
    def setUniqueSolution(*args, **kwargs):
        pass
    
    
    def singleChainOnly(*args, **kwargs):
        pass
    
    
    def snapHandle(*args, **kwargs):
        pass
    
    
    def solverTypeName(*args, **kwargs):
        pass
    
    
    def supportJointLimits(*args, **kwargs):
        pass
    
    
    def toSolverSpace(*args, **kwargs):
        pass
    
    
    def toWorldSpace(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    def uniqueSolution(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MPxPolyTrg(MPxNode):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def compute(*args, **kwargs):
        pass
    
    
    def isAbstractClass(*args, **kwargs):
        pass
    
    
    def postConstructor(*args, **kwargs):
        pass
    
    
    def registerTrgFunction(*args, **kwargs):
        pass
    
    
    def unregisterTrgFunction(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MPxLocatorNode(MPxNode):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def boundingBox(*args, **kwargs):
        pass
    
    
    def color(*args, **kwargs):
        pass
    
    
    def colorRGB(*args, **kwargs):
        pass
    
    
    def draw(*args, **kwargs):
        pass
    
    
    def drawLast(*args, **kwargs):
        pass
    
    
    def excludeAsLocator(*args, **kwargs):
        pass
    
    
    def isBounded(*args, **kwargs):
        pass
    
    
    def isTransparent(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    boundingBoxCenterX = None
    
    boundingBoxCenterY = None
    
    boundingBoxCenterZ = None
    
    center = None
    
    instObjGroups = None
    
    intermediateObject = None
    
    inverseMatrix = None
    
    isTemplated = None
    
    localPosition = None
    
    localPositionX = None
    
    localPositionY = None
    
    localPositionZ = None
    
    localScale = None
    
    localScaleX = None
    
    localScaleY = None
    
    localScaleZ = None
    
    matrix = None
    
    nodeBoundingBox = None
    
    nodeBoundingBoxMax = None
    
    nodeBoundingBoxMaxX = None
    
    nodeBoundingBoxMaxY = None
    
    nodeBoundingBoxMaxZ = None
    
    nodeBoundingBoxMin = None
    
    nodeBoundingBoxMinX = None
    
    nodeBoundingBoxMinY = None
    
    nodeBoundingBoxMinZ = None
    
    nodeBoundingBoxSize = None
    
    nodeBoundingBoxSizeX = None
    
    nodeBoundingBoxSizeY = None
    
    nodeBoundingBoxSizeZ = None
    
    objectColor = None
    
    objectGroupColor = None
    
    objectGroupId = None
    
    objectGroups = None
    
    objectGrpCompList = None
    
    parentInverseMatrix = None
    
    parentMatrix = None
    
    thisown = None
    
    underWorldObject = None
    
    useObjectColor = None
    
    visibility = None
    
    worldInverseMatrix = None
    
    worldMatrix = None
    
    worldPosition = None
    
    worldPositionX = None
    
    worldPositionY = None
    
    worldPositionZ = None
    
    __swig_destroy__ = None


class MPxMayaAsciiFilter(MPxFileTranslator):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def haveReadMethod(*args, **kwargs):
        pass
    
    
    def haveWriteMethod(*args, **kwargs):
        pass
    
    
    def processReadOptions(*args, **kwargs):
        pass
    
    
    def processWriteOptions(*args, **kwargs):
        pass
    
    
    def reader(*args, **kwargs):
        pass
    
    
    def writePostConnectAttrsBlock(*args, **kwargs):
        pass
    
    
    def writePostCreateNodesBlock(*args, **kwargs):
        pass
    
    
    def writePostHeader(*args, **kwargs):
        pass
    
    
    def writePostRequires(*args, **kwargs):
        pass
    
    
    def writePreConnectAttrsBlock(*args, **kwargs):
        pass
    
    
    def writePreCreateNodesBlock(*args, **kwargs):
        pass
    
    
    def writePreTrailer(*args, **kwargs):
        pass
    
    
    def writer(*args, **kwargs):
        pass
    
    
    def writesConnectAttr(*args, **kwargs):
        pass
    
    
    def writesCreateNode(*args, **kwargs):
        pass
    
    
    def writesDisconnectAttr(*args, **kwargs):
        pass
    
    
    def writesFileReference(*args, **kwargs):
        pass
    
    
    def writesParentNode(*args, **kwargs):
        pass
    
    
    def writesRequirements(*args, **kwargs):
        pass
    
    
    def writesSelectNode(*args, **kwargs):
        pass
    
    
    def writesSetAttr(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MPxSpringNode(MPxNode):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def applySpringLaw(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    mDeltaTime = None
    
    mEnd1Weight = None
    
    mEnd2Weight = None
    
    thisown = None
    
    __swig_destroy__ = None


class MPxFieldNode(MPxNode):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def compute(*args, **kwargs):
        pass
    
    
    def draw(*args, **kwargs):
        pass
    
    
    def falloffCurve(*args, **kwargs):
        pass
    
    
    def getForceAtPoint(*args, **kwargs):
        pass
    
    
    def iconBitmap(*args, **kwargs):
        pass
    
    
    def iconSizeAndOrigin(*args, **kwargs):
        pass
    
    
    def isFalloffCurveConstantOne(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    mApplyPerVertex = None
    
    mAttenuation = None
    
    mDeltaTime = None
    
    mInputData = None
    
    mInputForce = None
    
    mInputMass = None
    
    mInputPPData = None
    
    mInputPositions = None
    
    mInputVelocities = None
    
    mMagnitude = None
    
    mMaxDistance = None
    
    mOutputForce = None
    
    mOwnerCentroid = None
    
    mOwnerCentroidX = None
    
    mOwnerCentroidY = None
    
    mOwnerCentroidZ = None
    
    mOwnerPPData = None
    
    mOwnerPosData = None
    
    mOwnerVelData = None
    
    mUseMaxDistance = None
    
    mWorldMatrix = None
    
    thisown = None
    
    __swig_destroy__ = None


class MPxConstraintCommand(MPxCommand):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def aimVectorAttribute(*args, **kwargs):
        pass
    
    
    def appendSyntax(*args, **kwargs):
        pass
    
    
    def connectObjectAndConstraint(*args, **kwargs):
        pass
    
    
    def connectTarget(*args, **kwargs):
        pass
    
    
    def constraintEnableRestAttribute(*args, **kwargs):
        pass
    
    
    def constraintInstancedAttribute(*args, **kwargs):
        pass
    
    
    def constraintNode(*args, **kwargs):
        pass
    
    
    def constraintOutputAttribute(*args, **kwargs):
        pass
    
    
    def constraintRestAttribute(*args, **kwargs):
        pass
    
    
    def constraintTargetAttribute(*args, **kwargs):
        pass
    
    
    def constraintTargetInstancedAttribute(*args, **kwargs):
        pass
    
    
    def constraintTargetWeightAttribute(*args, **kwargs):
        pass
    
    
    def constraintTypeId(*args, **kwargs):
        pass
    
    
    def createdConstraint(*args, **kwargs):
        pass
    
    
    def doCreate(*args, **kwargs):
        pass
    
    
    def doEdit(*args, **kwargs):
        pass
    
    
    def doIt(*args, **kwargs):
        pass
    
    
    def doQuery(*args, **kwargs):
        pass
    
    
    def getObjectAttributesArray(*args, **kwargs):
        pass
    
    
    def handleNewTargets(*args, **kwargs):
        pass
    
    
    def hasVectorFlags(*args, **kwargs):
        pass
    
    
    def objectAttribute(*args, **kwargs):
        pass
    
    
    def offsetAttribute(*args, **kwargs):
        pass
    
    
    def parseArgs(*args, **kwargs):
        pass
    
    
    def redoIt(*args, **kwargs):
        pass
    
    
    def supportsOffset(*args, **kwargs):
        pass
    
    
    def targetType(*args, **kwargs):
        pass
    
    
    def undoIt(*args, **kwargs):
        pass
    
    
    def upVectorAttribute(*args, **kwargs):
        pass
    
    
    def worldUpMatrixAttribute(*args, **kwargs):
        pass
    
    
    def worldUpTypeAttribute(*args, **kwargs):
        pass
    
    
    def worldUpVectorAttribute(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kGeometryShape = None
    
    
    kLast = None
    
    
    kTransform = None


class MPxPolyTweakUVCommand(MPxCommand):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def getTweakedUVs(*args, **kwargs):
        pass
    
    
    def parseSyntax(*args, **kwargs):
        pass
    
    
    def newSyntax(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MPxConstraint(MPxNode):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def constraintRotateOrderAttribute(*args, **kwargs):
        pass
    
    
    def getOutputAttributes(*args, **kwargs):
        pass
    
    
    def passiveOutputAttribute(*args, **kwargs):
        pass
    
    
    def targetAttribute(*args, **kwargs):
        pass
    
    
    def weightAttribute(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    enableRestPosition = None
    
    lockOutput = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kLast = None
    
    
    kObject = None
    
    
    kObjectRotation = None
    
    
    kScene = None
    
    
    kVector = None


class MPxObjectSet(MPxNode):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def canBeDeleted(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    DNSetMembers = None
    
    annotation = None
    
    dagSetMembers = None
    
    edgesOnlySet = None
    
    editPointsOnlySet = None
    
    facetsOnlySet = None
    
    groupNodes = None
    
    isLayer = None
    
    memberWireframeColor = None
    
    partition = None
    
    renderableOnlySet = None
    
    thisown = None
    
    usedByNodes = None
    
    verticesOnlySet = None
    
    __swig_destroy__ = None


class MPxManipulatorNode(MPxNode):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def addDoubleValue(*args, **kwargs):
        pass
    
    
    def addPointValue(*args, **kwargs):
        pass
    
    
    def addVectorValue(*args, **kwargs):
        pass
    
    
    def colorAndName(*args, **kwargs):
        pass
    
    
    def connectPlugToValue(*args, **kwargs):
        pass
    
    
    def connectToDependNode(*args, **kwargs):
        pass
    
    
    def dimmedColor(*args, **kwargs):
        pass
    
    
    def doDrag(*args, **kwargs):
        pass
    
    
    def doPress(*args, **kwargs):
        pass
    
    
    def doRelease(*args, **kwargs):
        pass
    
    
    def draw(*args, **kwargs):
        pass
    
    
    def finishAddingManips(*args, **kwargs):
        pass
    
    
    def getDoubleValue(*args, **kwargs):
        pass
    
    
    def getInstancePtr(*args, **kwargs):
        pass
    
    
    def getPointValue(*args, **kwargs):
        pass
    
    
    def getVectorValue(*args, **kwargs):
        pass
    
    
    def glActiveName(*args, **kwargs):
        pass
    
    
    def glFirstHandle(*args, **kwargs):
        pass
    
    
    def labelBackgroundColor(*args, **kwargs):
        pass
    
    
    def labelColor(*args, **kwargs):
        pass
    
    
    def lineColor(*args, **kwargs):
        pass
    
    
    def mainColor(*args, **kwargs):
        pass
    
    
    def mouseDown(*args, **kwargs):
        pass
    
    
    def mousePosition(*args, **kwargs):
        pass
    
    
    def mouseRay(*args, **kwargs):
        pass
    
    
    def mouseRayWorld(*args, **kwargs):
        pass
    
    
    def mouseUp(*args, **kwargs):
        pass
    
    
    def prevColor(*args, **kwargs):
        pass
    
    
    def selectedColor(*args, **kwargs):
        pass
    
    
    def setDoubleValue(*args, **kwargs):
        pass
    
    
    def setInstancePtr(*args, **kwargs):
        pass
    
    
    def setPointValue(*args, **kwargs):
        pass
    
    
    def setVectorValue(*args, **kwargs):
        pass
    
    
    def xColor(*args, **kwargs):
        pass
    
    
    def yColor(*args, **kwargs):
        pass
    
    
    def zColor(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def newManipulator(*args, **kwargs):
        pass
    
    
    connectedNodes = None
    
    thisown = None
    
    __swig_destroy__ = None


class MPxSurfaceShape(MPxNode):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def acceptsGeometryIterator(*args, **kwargs):
        pass
    
    
    def activeComponents(*args, **kwargs):
        pass
    
    
    def boundingBox(*args, **kwargs):
        pass
    
    
    def cachedShapeAttr(*args, **kwargs):
        pass
    
    
    def childChanged(*args, **kwargs):
        pass
    
    
    def closestPoint(*args, **kwargs):
        pass
    
    
    def componentToPlugs(*args, **kwargs):
        pass
    
    
    def convertToTweakNodePlug(*args, **kwargs):
        pass
    
    
    def createFullVertexGroup(*args, **kwargs):
        pass
    
    
    def deleteComponents(*args, **kwargs):
        pass
    
    
    def geometryData(*args, **kwargs):
        pass
    
    
    def geometryIteratorSetup(*args, **kwargs):
        pass
    
    
    def getWorldMatrix(*args, **kwargs):
        pass
    
    
    def hasActiveComponents(*args, **kwargs):
        pass
    
    
    def isBounded(*args, **kwargs):
        pass
    
    
    def isRenderable(*args, **kwargs):
        pass
    
    
    def localShapeInAttr(*args, **kwargs):
        pass
    
    
    def localShapeOutAttr(*args, **kwargs):
        pass
    
    
    def match(*args, **kwargs):
        pass
    
    
    def matchComponent(*args, **kwargs):
        pass
    
    
    def newControlPointComponent(*args, **kwargs):
        pass
    
    
    def pointAtParm(*args, **kwargs):
        pass
    
    
    def setRenderable(*args, **kwargs):
        pass
    
    
    def transformUsing(*args, **kwargs):
        pass
    
    
    def tweakUsing(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    def undeleteComponents(*args, **kwargs):
        pass
    
    
    def vertexOffsetDirection(*args, **kwargs):
        pass
    
    
    def worldShapeOutAttr(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    boundingBoxCenterX = None
    
    boundingBoxCenterY = None
    
    boundingBoxCenterZ = None
    
    center = None
    
    instObjGroups = None
    
    intermediateObject = None
    
    inverseMatrix = None
    
    isTemplated = None
    
    mControlPoints = None
    
    mControlValueX = None
    
    mControlValueY = None
    
    mControlValueZ = None
    
    mHasHistoryOnCreate = None
    
    matrix = None
    
    nodeBoundingBox = None
    
    nodeBoundingBoxMax = None
    
    nodeBoundingBoxMaxX = None
    
    nodeBoundingBoxMaxY = None
    
    nodeBoundingBoxMaxZ = None
    
    nodeBoundingBoxMin = None
    
    nodeBoundingBoxMinX = None
    
    nodeBoundingBoxMinY = None
    
    nodeBoundingBoxMinZ = None
    
    nodeBoundingBoxSize = None
    
    nodeBoundingBoxSizeX = None
    
    nodeBoundingBoxSizeY = None
    
    nodeBoundingBoxSizeZ = None
    
    objectColor = None
    
    objectGroupColor = None
    
    objectGroupId = None
    
    objectGroups = None
    
    objectGrpCompList = None
    
    parentInverseMatrix = None
    
    parentMatrix = None
    
    thisown = None
    
    useObjectColor = None
    
    visibility = None
    
    worldInverseMatrix = None
    
    worldMatrix = None
    
    __swig_destroy__ = None
    
    
    kBoundingBoxChanged = None
    
    
    kMatchInvalidAttribute = None
    
    
    kMatchInvalidAttributeDim = None
    
    
    kMatchInvalidAttributeIndex = None
    
    
    kMatchInvalidAttributeRange = None
    
    
    kMatchInvalidName = None
    
    
    kMatchNone = None
    
    
    kMatchOk = None
    
    
    kMatchTooMany = None
    
    
    kNoPointCaching = None
    
    
    kNormal = None
    
    
    kObjectChanged = None
    
    
    kRestorePoints = None
    
    
    kSavePoints = None
    
    
    kUTangent = None
    
    
    kUVNTriad = None
    
    
    kUpdatePoints = None
    
    
    kVTangent = None


class MPxParticleAttributeMapperNode(MPxNode):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    computeNode = None
    
    computeNodeColor = None
    
    computeNodeColorB = None
    
    computeNodeColorG = None
    
    computeNodeColorR = None
    
    outColorPP = None
    
    outMaxValue = None
    
    outMinValue = None
    
    outValuePP = None
    
    thisown = None
    
    time = None
    
    uCoordPP = None
    
    vCoordPP = None
    
    __swig_destroy__ = None


class MPxManipContainer(MPxNode):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def addCircleSweepManip(*args, **kwargs):
        pass
    
    
    def addCurveSegmentManip(*args, **kwargs):
        pass
    
    
    def addDirectionManip(*args, **kwargs):
        pass
    
    
    def addDiscManip(*args, **kwargs):
        pass
    
    
    def addDistanceManip(*args, **kwargs):
        pass
    
    
    def addFreePointTriadManip(*args, **kwargs):
        pass
    
    
    def addMPxManipulatorNode(*args, **kwargs):
        pass
    
    
    def addManipToPlugConversion(*args, **kwargs):
        pass
    
    
    def addPlugToManipConversion(*args, **kwargs):
        pass
    
    
    def addPointOnCurveManip(*args, **kwargs):
        pass
    
    
    def addPointOnSurfaceManip(*args, **kwargs):
        pass
    
    
    def addRotateManip(*args, **kwargs):
        pass
    
    
    def addScaleManip(*args, **kwargs):
        pass
    
    
    def addStateManip(*args, **kwargs):
        pass
    
    
    def addToggleManip(*args, **kwargs):
        pass
    
    
    def connectToDependNode(*args, **kwargs):
        pass
    
    
    def createChildren(*args, **kwargs):
        pass
    
    
    def doDrag(*args, **kwargs):
        pass
    
    
    def doPress(*args, **kwargs):
        pass
    
    
    def doRelease(*args, **kwargs):
        pass
    
    
    def draw(*args, **kwargs):
        pass
    
    
    def finishAddingManips(*args, **kwargs):
        pass
    
    
    def getConverterManipValue(*args, **kwargs):
        pass
    
    
    def getConverterPlugValue(*args, **kwargs):
        pass
    
    
    def isManipActive(*args, **kwargs):
        pass
    
    
    def manipToPlugConversion(*args, **kwargs):
        pass
    
    
    def plugToManipConversion(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    def addToManipConnectTable(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def initialize(*args, **kwargs):
        pass
    
    
    def newManipulator(*args, **kwargs):
        pass
    
    
    def removeFromManipConnectTable(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kCircleSweepManip = None
    
    
    kCurveSegmentManip = None
    
    
    kCustomManip = None
    
    
    kDirectionManip = None
    
    
    kDiscManip = None
    
    
    kDistanceManip = None
    
    
    kFreePointTriadManip = None
    
    
    kPointOnCurveManip = None
    
    
    kPointOnSurfaceManip = None
    
    
    kStateManip = None
    
    
    kToggleManip = None


class MPxGeometryData(MPxData):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def copy(*args, **kwargs):
        pass
    
    
    def deleteComponent(*args, **kwargs):
        pass
    
    
    def deleteComponentsFromGroups(*args, **kwargs):
        pass
    
    
    def iterator(*args, **kwargs):
        pass
    
    
    def matrix(*args, **kwargs):
        pass
    
    
    def name(*args, **kwargs):
        pass
    
    
    def setMatrix(*args, **kwargs):
        pass
    
    
    def smartCopy(*args, **kwargs):
        pass
    
    
    def typeId(*args, **kwargs):
        pass
    
    
    def updateCompleteVertexGroup(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MPxToolCommand(MPxCommand):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def cancel(*args, **kwargs):
        pass
    
    
    def doIt(*args, **kwargs):
        pass
    
    
    def finalize(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MPxSelectionContext(MPxContext):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def abortAction(*args, **kwargs):
        pass
    
    
    def addManipulator(*args, **kwargs):
        pass
    
    
    def argTypeNumericalInput(*args, **kwargs):
        pass
    
    
    def deleteManipulators(*args, **kwargs):
        pass
    
    
    def doDrag(*args, **kwargs):
        pass
    
    
    def doHold(*args, **kwargs):
        pass
    
    
    def doPress(*args, **kwargs):
        pass
    
    
    def doRelease(*args, **kwargs):
        pass
    
    
    def feedbackNumericalInput(*args, **kwargs):
        pass
    
    
    def helpStateHasChanged(*args, **kwargs):
        pass
    
    
    def image(*args, **kwargs):
        pass
    
    
    def newToolCommand(*args, **kwargs):
        pass
    
    
    def processNumericalInput(*args, **kwargs):
        pass
    
    
    def setImage(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MPxHwShaderNode(MPxNode):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def bind(*args, **kwargs):
        pass
    
    
    def colorsPerVertex(*args, **kwargs):
        pass
    
    
    def currentPath(*args, **kwargs):
        pass
    
    
    def currentShadingEngine(*args, **kwargs):
        pass
    
    
    def dirtyMask(*args, **kwargs):
        pass
    
    
    def geometry(*args, **kwargs):
        pass
    
    
    def glBind(*args, **kwargs):
        pass
    
    
    def glGeometry(*args, **kwargs):
        pass
    
    
    def glUnbind(*args, **kwargs):
        pass
    
    
    def hasTransparency(*args, **kwargs):
        pass
    
    
    def invertTexCoords(*args, **kwargs):
        pass
    
    
    def normalsPerVertex(*args, **kwargs):
        pass
    
    
    def provideVertexIDs(*args, **kwargs):
        pass
    
    
    def renderSwatchImage(*args, **kwargs):
        pass
    
    
    def supportsBatching(*args, **kwargs):
        pass
    
    
    def texCoordsPerVertex(*args, **kwargs):
        pass
    
    
    def transparencyOptions(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    def unbind(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def getHwShaderNodePtr(*args, **kwargs):
        pass
    
    
    outColor = None
    
    outColorB = None
    
    outColorG = None
    
    outColorR = None
    
    outGlowColor = None
    
    outGlowColorB = None
    
    outGlowColorG = None
    
    outGlowColorR = None
    
    outMatteOpacity = None
    
    outMatteOpacityB = None
    
    outMatteOpacityG = None
    
    outMatteOpacityR = None
    
    outTransparency = None
    
    outTransparencyB = None
    
    outTransparencyG = None
    
    outTransparencyR = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kDirtyAll = None
    
    
    kDirtyColorArrays = None
    
    
    kDirtyNone = None
    
    
    kDirtyNormalArray = None
    
    
    kDirtyTexCoordArrays = None
    
    
    kDirtyVertexArray = None
    
    
    kIsTransparent = None
    
    
    kNoTransparencyFrontBackCull = None
    
    
    kNoTransparencyPolygonSort = None
    
    
    kWriteAll = None
    
    
    kWriteColorArrays = None
    
    
    kWriteNone = None
    
    
    kWriteNormalArray = None
    
    
    kWriteTexCoordArrays = None
    
    
    kWriteVertexArray = None


class MPxImagePlane(MPxNode):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def exactImageFile(*args, **kwargs):
        pass
    
    
    def loadImageMap(*args, **kwargs):
        pass
    
    
    def refreshImage(*args, **kwargs):
        pass
    
    
    def setImageDirty(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    alphaGain = None
    
    alreadyPremult = None
    
    center = None
    
    centerX = None
    
    centerY = None
    
    centerZ = None
    
    colorGain = None
    
    colorGainB = None
    
    colorGainG = None
    
    colorGainR = None
    
    colorOffset = None
    
    colorOffsetB = None
    
    colorOffsetG = None
    
    colorOffsetR = None
    
    composite = None
    
    coverage = None
    
    coverageOrigin = None
    
    coverageOriginX = None
    
    coverageOriginY = None
    
    coverageX = None
    
    coverageY = None
    
    depth = None
    
    depthBias = None
    
    depthFile = None
    
    depthOversample = None
    
    depthScale = None
    
    displayMode = None
    
    displayOnlyIfCurrent = None
    
    fit = None
    
    frameExtension = None
    
    frameOffset = None
    
    height = None
    
    imageName = None
    
    imageType = None
    
    lockedToCamera = None
    
    maxShadingSamples = None
    
    offset = None
    
    offsetX = None
    
    offsetY = None
    
    rotate = None
    
    separateDepth = None
    
    shadingSamples = None
    
    shadingSamplesOverride = None
    
    size = None
    
    sizeX = None
    
    sizeY = None
    
    sourceTexture = None
    
    squeezeCorrection = None
    
    thisown = None
    
    useDepthMap = None
    
    useFrameExtension = None
    
    visibleInReflections = None
    
    visibleInRefractions = None
    
    width = None
    
    __swig_destroy__ = None


class MPxUITableControl(MPxUIControl):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def addToSelection(*args, **kwargs):
        pass
    
    
    def allowEdit(*args, **kwargs):
        pass
    
    
    def allowSelection(*args, **kwargs):
        pass
    
    
    def cellString(*args, **kwargs):
        pass
    
    
    def clearSelection(*args, **kwargs):
        pass
    
    
    def collapseOrExpandRow(*args, **kwargs):
        pass
    
    
    def isSelected(*args, **kwargs):
        pass
    
    
    def labelString(*args, **kwargs):
        pass
    
    
    def numberOfColumns(*args, **kwargs):
        pass
    
    
    def numberOfRows(*args, **kwargs):
        pass
    
    
    def redrawCells(*args, **kwargs):
        pass
    
    
    def redrawLabels(*args, **kwargs):
        pass
    
    
    def removeFromSelection(*args, **kwargs):
        pass
    
    
    def setNumberOfColumns(*args, **kwargs):
        pass
    
    
    def setNumberOfRows(*args, **kwargs):
        pass
    
    
    def setSelection(*args, **kwargs):
        pass
    
    
    def suspendUpdates(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kAllLabels = None
    
    
    kColumnLabel = None
    
    
    kNoLabel = None
    
    
    kRowLabel = None


class MPxHardwareShader(MPxNode):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def populateRequirements(*args, **kwargs):
        pass
    
    
    def profile(*args, **kwargs):
        pass
    
    
    def render(*args, **kwargs):
        pass
    
    
    def renderSwatchImage(*args, **kwargs):
        pass
    
    
    def setUniformParameters(*args, **kwargs):
        pass
    
    
    def setVaryingParameters(*args, **kwargs):
        pass
    
    
    def transparencyOptions(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def findResource(*args, **kwargs):
        pass
    
    
    def getHardwareShaderPtr(*args, **kwargs):
        pass
    
    
    outColor = None
    
    outColorB = None
    
    outColorG = None
    
    outColorR = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kIsTransparent = None
    
    
    kNoTransparencyFrontBackCull = None
    
    
    kNoTransparencyPolygonSort = None


class MPxDeformerNode(MPxNode):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def accessoryAttribute(*args, **kwargs):
        pass
    
    
    def accessoryNodeSetup(*args, **kwargs):
        pass
    
    
    def deform(*args, **kwargs):
        pass
    
    
    def getDeformationDetails(*args, **kwargs):
        pass
    
    
    def setDeformationDetails(*args, **kwargs):
        pass
    
    
    def setModifiedCallback(*args, **kwargs):
        pass
    
    
    def setUseExistingConnectionWhenSetEditing(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    def weightValue(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    envelope = None
    
    groupId = None
    
    input = None
    
    inputGeom = None
    
    outputGeom = None
    
    thisown = None
    
    weightList = None
    
    weights = None
    
    __swig_destroy__ = None
    
    
    kDeformsAll = None
    
    
    kDeformsColors = None
    
    
    kDeformsUVs = None


class MPxTransform(MPxNode):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def applyRotateOrientationLocks(*args, **kwargs):
        pass
    
    
    def applyRotatePivotLocks(*args, **kwargs):
        pass
    
    
    def applyRotatePivotLocksTranslate(*args, **kwargs):
        pass
    
    
    def applyRotationLimits(*args, **kwargs):
        pass
    
    
    def applyRotationLocks(*args, **kwargs):
        pass
    
    
    def applyScaleLimits(*args, **kwargs):
        pass
    
    
    def applyScaleLocks(*args, **kwargs):
        pass
    
    
    def applyScaleLocksPivot(*args, **kwargs):
        pass
    
    
    def applyScaleLocksPivotTranslate(*args, **kwargs):
        pass
    
    
    def applyShearLocks(*args, **kwargs):
        pass
    
    
    def applyTranslationLimits(*args, **kwargs):
        pass
    
    
    def applyTranslationLocks(*args, **kwargs):
        pass
    
    
    def boundingBox(*args, **kwargs):
        pass
    
    
    def checkAndSetRotateOrientation(*args, **kwargs):
        pass
    
    
    def checkAndSetRotatePivot(*args, **kwargs):
        pass
    
    
    def checkAndSetRotatePivotTranslation(*args, **kwargs):
        pass
    
    
    def checkAndSetRotation(*args, **kwargs):
        pass
    
    
    def checkAndSetScale(*args, **kwargs):
        pass
    
    
    def checkAndSetScalePivot(*args, **kwargs):
        pass
    
    
    def checkAndSetScalePivotTranslation(*args, **kwargs):
        pass
    
    
    def checkAndSetShear(*args, **kwargs):
        pass
    
    
    def checkAndSetTranslation(*args, **kwargs):
        pass
    
    
    def clearLimits(*args, **kwargs):
        pass
    
    
    def compute(*args, **kwargs):
        pass
    
    
    def computeLocalTransformation(*args, **kwargs):
        pass
    
    
    def copyInternalData(*args, **kwargs):
        pass
    
    
    def createTransformationMatrix(*args, **kwargs):
        pass
    
    
    def enableLimit(*args, **kwargs):
        pass
    
    
    def getEulerRotation(*args, **kwargs):
        pass
    
    
    def getMatrix(*args, **kwargs):
        pass
    
    
    def getMatrixInverse(*args, **kwargs):
        pass
    
    
    def getRotateOrientation(*args, **kwargs):
        pass
    
    
    def getRotatePivot(*args, **kwargs):
        pass
    
    
    def getRotatePivotTranslation(*args, **kwargs):
        pass
    
    
    def getRotation(*args, **kwargs):
        pass
    
    
    def getRotationOrder(*args, **kwargs):
        pass
    
    
    def getScale(*args, **kwargs):
        pass
    
    
    def getScalePivot(*args, **kwargs):
        pass
    
    
    def getScalePivotTranslation(*args, **kwargs):
        pass
    
    
    def getShear(*args, **kwargs):
        pass
    
    
    def getTranslation(*args, **kwargs):
        pass
    
    
    def isBounded(*args, **kwargs):
        pass
    
    
    def isLimited(*args, **kwargs):
        pass
    
    
    def limitValue(*args, **kwargs):
        pass
    
    
    def postConstructor(*args, **kwargs):
        pass
    
    
    def resetTransformation(*args, **kwargs):
        pass
    
    
    def rotateBy(*args, **kwargs):
        pass
    
    
    def rotateTo(*args, **kwargs):
        pass
    
    
    def scaleBy(*args, **kwargs):
        pass
    
    
    def scaleTo(*args, **kwargs):
        pass
    
    
    def setLimit(*args, **kwargs):
        pass
    
    
    def setRotateOrientation(*args, **kwargs):
        pass
    
    
    def setRotatePivot(*args, **kwargs):
        pass
    
    
    def setRotatePivotTranslation(*args, **kwargs):
        pass
    
    
    def setRotationOrder(*args, **kwargs):
        pass
    
    
    def setScalePivot(*args, **kwargs):
        pass
    
    
    def setScalePivotTranslation(*args, **kwargs):
        pass
    
    
    def shearBy(*args, **kwargs):
        pass
    
    
    def shearTo(*args, **kwargs):
        pass
    
    
    def transformationMatrix(*args, **kwargs):
        pass
    
    
    def transformationMatrixPtr(*args, **kwargs):
        pass
    
    
    def translateBy(*args, **kwargs):
        pass
    
    
    def translateTo(*args, **kwargs):
        pass
    
    
    def treatAsTransform(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    def updateMatrixAttrs(*args, **kwargs):
        pass
    
    
    def validateAndSetValue(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def isNonAffineMatricesEnabled(*args, **kwargs):
        pass
    
    
    def mustCallValidateAndSet(*args, **kwargs):
        pass
    
    
    def setNonAffineMatricesEnabled(*args, **kwargs):
        pass
    
    
    boundingBoxCenterX = None
    
    boundingBoxCenterY = None
    
    boundingBoxCenterZ = None
    
    center = None
    
    displayHandle = None
    
    displayLocalAxis = None
    
    displayRotatePivot = None
    
    displayScalePivot = None
    
    drawOverride = None
    
    dynamics = None
    
    geometry = None
    
    ghosting = None
    
    identification = None
    
    inheritsTransform = None
    
    instObjGroups = None
    
    intermediateObject = None
    
    inverseMatrix = None
    
    isTemplated = None
    
    layerOverrideColor = None
    
    layerRenderable = None
    
    lodVisibility = None
    
    matrix = None
    
    maxRotLimit = None
    
    maxRotLimitEnable = None
    
    maxRotXLimit = None
    
    maxRotXLimitEnable = None
    
    maxRotYLimit = None
    
    maxRotYLimitEnable = None
    
    maxRotZLimit = None
    
    maxRotZLimitEnable = None
    
    maxScaleLimit = None
    
    maxScaleLimitEnable = None
    
    maxScaleXLimit = None
    
    maxScaleXLimitEnable = None
    
    maxScaleYLimit = None
    
    maxScaleYLimitEnable = None
    
    maxScaleZLimit = None
    
    maxScaleZLimitEnable = None
    
    maxTransLimit = None
    
    maxTransLimitEnable = None
    
    maxTransXLimit = None
    
    maxTransXLimitEnable = None
    
    maxTransYLimit = None
    
    maxTransYLimitEnable = None
    
    maxTransZLimit = None
    
    maxTransZLimitEnable = None
    
    minRotLimit = None
    
    minRotLimitEnable = None
    
    minRotXLimit = None
    
    minRotXLimitEnable = None
    
    minRotYLimit = None
    
    minRotYLimitEnable = None
    
    minRotZLimit = None
    
    minRotZLimitEnable = None
    
    minScaleLimit = None
    
    minScaleLimitEnable = None
    
    minScaleXLimit = None
    
    minScaleXLimitEnable = None
    
    minScaleYLimit = None
    
    minScaleYLimitEnable = None
    
    minScaleZLimit = None
    
    minScaleZLimitEnable = None
    
    minTransLimit = None
    
    minTransLimitEnable = None
    
    minTransXLimit = None
    
    minTransXLimitEnable = None
    
    minTransYLimit = None
    
    minTransYLimitEnable = None
    
    minTransZLimit = None
    
    minTransZLimitEnable = None
    
    nodeBoundingBox = None
    
    nodeBoundingBoxMax = None
    
    nodeBoundingBoxMaxX = None
    
    nodeBoundingBoxMaxY = None
    
    nodeBoundingBoxMaxZ = None
    
    nodeBoundingBoxMin = None
    
    nodeBoundingBoxMinX = None
    
    nodeBoundingBoxMinY = None
    
    nodeBoundingBoxMinZ = None
    
    nodeBoundingBoxSize = None
    
    nodeBoundingBoxSizeX = None
    
    nodeBoundingBoxSizeY = None
    
    nodeBoundingBoxSizeZ = None
    
    objectColor = None
    
    objectGroupColor = None
    
    objectGroupId = None
    
    objectGroups = None
    
    objectGrpCompList = None
    
    overrideColor = None
    
    overrideDisplayType = None
    
    overrideEnabled = None
    
    overrideLevelOfDetail = None
    
    overridePlayback = None
    
    overrideShading = None
    
    overrideTexturing = None
    
    overrideVisibility = None
    
    parentInverseMatrix = None
    
    parentMatrix = None
    
    renderInfo = None
    
    renderLayerColor = None
    
    renderLayerId = None
    
    renderLayerInfo = None
    
    renderLayerRenderable = None
    
    rotate = None
    
    rotateAxis = None
    
    rotateAxisX = None
    
    rotateAxisY = None
    
    rotateAxisZ = None
    
    rotateOrder = None
    
    rotatePivot = None
    
    rotatePivotTranslate = None
    
    rotatePivotTranslateX = None
    
    rotatePivotTranslateY = None
    
    rotatePivotTranslateZ = None
    
    rotatePivotX = None
    
    rotatePivotY = None
    
    rotatePivotZ = None
    
    rotateQuaternion = None
    
    rotateQuaternionW = None
    
    rotateQuaternionX = None
    
    rotateQuaternionY = None
    
    rotateQuaternionZ = None
    
    rotateX = None
    
    rotateY = None
    
    rotateZ = None
    
    rotationInterpolation = None
    
    scale = None
    
    scalePivot = None
    
    scalePivotTranslate = None
    
    scalePivotTranslateX = None
    
    scalePivotTranslateY = None
    
    scalePivotTranslateZ = None
    
    scalePivotX = None
    
    scalePivotY = None
    
    scalePivotZ = None
    
    scaleX = None
    
    scaleY = None
    
    scaleZ = None
    
    selectHandle = None
    
    selectHandleX = None
    
    selectHandleY = None
    
    selectHandleZ = None
    
    shear = None
    
    shearXY = None
    
    shearXZ = None
    
    shearYZ = None
    
    showManipDefault = None
    
    specifiedManipLocation = None
    
    thisown = None
    
    transMinusRotatePivot = None
    
    transMinusRotatePivotX = None
    
    transMinusRotatePivotY = None
    
    transMinusRotatePivotZ = None
    
    translate = None
    
    translateX = None
    
    translateY = None
    
    translateZ = None
    
    useObjectColor = None
    
    visibility = None
    
    worldInverseMatrix = None
    
    worldMatrix = None
    
    xformMatrix = None
    
    __swig_destroy__ = None


class MPxCameraSet(MPxNode):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    active = None
    
    camera = None
    
    cameraLayer = None
    
    order = None
    
    sceneData = None
    
    thisown = None
    
    __swig_destroy__ = None


class MPxFluidEmitterNode(MPxEmitterNode):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def compute(*args, **kwargs):
        pass
    
    
    def fluidColor(*args, **kwargs):
        pass
    
    
    def fluidDensityEmission(*args, **kwargs):
        pass
    
    
    def fluidDropoff(*args, **kwargs):
        pass
    
    
    def fluidEmitColor(*args, **kwargs):
        pass
    
    
    def fluidEmitter(*args, **kwargs):
        pass
    
    
    def fluidFuelEmission(*args, **kwargs):
        pass
    
    
    def fluidHeatEmission(*args, **kwargs):
        pass
    
    
    def fluidJitter(*args, **kwargs):
        pass
    
    
    def turbulence(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    mEmissionFunction = None
    
    mEmitFluidColor = None
    
    mFluidColor = None
    
    mFluidColorB = None
    
    mFluidColorG = None
    
    mFluidColorR = None
    
    mFluidDensityEmission = None
    
    mFluidDropoff = None
    
    mFluidFuelEmission = None
    
    mFluidHeatEmission = None
    
    mFluidJitter = None
    
    mTurbulence = None
    
    thisown = None
    
    __swig_destroy__ = None


class MPxComponentShape(MPxSurfaceShape):
    def __disown__(self):
        pass
    
    
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def componentToPlugs(*args, **kwargs):
        pass
    
    
    def createFullVertexGroup(*args, **kwargs):
        pass
    
    
    def getControlPoints(*args, **kwargs):
        pass
    
    
    def localShapeInAttr(*args, **kwargs):
        pass
    
    
    def match(*args, **kwargs):
        pass
    
    
    def setControlPoints(*args, **kwargs):
        pass
    
    
    def transformUsing(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None

def MFnPlugin_className(*args, **kwargs):
    pass


def MFnPlugin_findPlugin(*args, **kwargs):
    pass


def MFnPlugin_isNodeRegistered(*args, **kwargs):
    pass


def MFnPlugin_registeringCallableScript(*args, **kwargs):
    pass


def MFnPlugin_setRegisteringCallableScript(*args, **kwargs):
    pass


def MFnPlugin_swigregister(*args, **kwargs):
    pass


def MPx3dModelView_className(*args, **kwargs):
    pass


def MPx3dModelView_getModelView(*args, **kwargs):
    pass


def MPx3dModelView_swigregister(*args, **kwargs):
    pass


def MPxBakeEngine_swigregister(*args, **kwargs):
    pass


def MPxCacheFormat_className(*args, **kwargs):
    pass


def MPxCacheFormat_swigregister(*args, **kwargs):
    pass


def MPxCameraSet_className(*args, **kwargs):
    pass


def MPxCameraSet_swigregister(*args, **kwargs):
    pass


def MPxCommand_appendToResult(*args, **kwargs):
    pass


def MPxCommand_className(*args, **kwargs):
    pass


def MPxCommand_clearResult(*args, **kwargs):
    pass


def MPxCommand_currentDoubleResult(*args, **kwargs):
    pass


def MPxCommand_currentIntResult(*args, **kwargs):
    pass


def MPxCommand_currentResultType(*args, **kwargs):
    pass


def MPxCommand_currentStringResult(*args, **kwargs):
    pass


def MPxCommand_displayError(*args, **kwargs):
    pass


def MPxCommand_displayInfo(*args, **kwargs):
    pass


def MPxCommand_displayWarning(*args, **kwargs):
    pass


def MPxCommand_getCurrentResult(*args, **kwargs):
    pass


def MPxCommand_isCurrentResultArray(*args, **kwargs):
    pass


def MPxCommand_setResult(*args, **kwargs):
    pass


def MPxCommand_swigregister(*args, **kwargs):
    pass


def MPxComponentShape_swigregister(*args, **kwargs):
    pass


def MPxConstraintCommand_swigregister(*args, **kwargs):
    pass


def MPxConstraint_className(*args, **kwargs):
    pass


def MPxConstraint_swigregister(*args, **kwargs):
    pass


def MPxContextCommand_className(*args, **kwargs):
    pass


def MPxContextCommand_swigregister(*args, **kwargs):
    pass


def MPxContext__ignoreEntry(*args, **kwargs):
    pass


def MPxContext_className(*args, **kwargs):
    pass


def MPxContext_swigregister(*args, **kwargs):
    pass


def MPxControlCommand_className(*args, **kwargs):
    pass


def MPxControlCommand_swigregister(*args, **kwargs):
    pass


def MPxData_swigregister(*args, **kwargs):
    pass


def MPxDeformerNode_className(*args, **kwargs):
    pass


def MPxDeformerNode_swigregister(*args, **kwargs):
    pass


def MPxDragAndDropBehavior_className(*args, **kwargs):
    pass


def MPxDragAndDropBehavior_swigregister(*args, **kwargs):
    pass


def MPxDrawOverride_className(*args, **kwargs):
    pass


def MPxDrawOverride_swigregister(*args, **kwargs):
    pass


def MPxEmitterNode_className(*args, **kwargs):
    pass


def MPxEmitterNode_swigregister(*args, **kwargs):
    pass


def MPxFieldNode_className(*args, **kwargs):
    pass


def MPxFieldNode_swigregister(*args, **kwargs):
    pass


def MPxFileTranslator_fileAccessMode(*args, **kwargs):
    pass


def MPxFileTranslator_swigregister(*args, **kwargs):
    pass


def MPxFluidEmitterNode_className(*args, **kwargs):
    pass


def MPxFluidEmitterNode_swigregister(*args, **kwargs):
    pass


def MPxGeometryData_swigregister(*args, **kwargs):
    pass


def MPxGeometryIterator_className(*args, **kwargs):
    pass


def MPxGeometryIterator_swigregister(*args, **kwargs):
    pass


def MPxGeometryOverride_className(*args, **kwargs):
    pass


def MPxGeometryOverride_swigregister(*args, **kwargs):
    pass


def MPxGlBuffer_className(*args, **kwargs):
    pass


def MPxGlBuffer_swigregister(*args, **kwargs):
    pass


def MPxHardwareShader_className(*args, **kwargs):
    pass


def MPxHardwareShader_findResource(*args, **kwargs):
    pass


def MPxHardwareShader_getHardwareShaderPtr(*args, **kwargs):
    pass


def MPxHardwareShader_swigregister(*args, **kwargs):
    pass


def MPxHwShaderNode_className(*args, **kwargs):
    pass


def MPxHwShaderNode_getHwShaderNodePtr(*args, **kwargs):
    pass


def MPxHwShaderNode_swigregister(*args, **kwargs):
    pass


def MPxIkSolverNode_className(*args, **kwargs):
    pass


def MPxIkSolverNode_swigregister(*args, **kwargs):
    pass


def MPxImageFile_swigregister(*args, **kwargs):
    pass


def MPxImagePlane_className(*args, **kwargs):
    pass


def MPxImagePlane_swigregister(*args, **kwargs):
    pass


def MPxLocatorNode_className(*args, **kwargs):
    pass


def MPxLocatorNode_swigregister(*args, **kwargs):
    pass


def MPxManipContainer_addToManipConnectTable(*args, **kwargs):
    pass


def MPxManipContainer_className(*args, **kwargs):
    pass


def MPxManipContainer_initialize(*args, **kwargs):
    pass


def MPxManipContainer_newManipulator(*args, **kwargs):
    pass


def MPxManipContainer_removeFromManipConnectTable(*args, **kwargs):
    pass


def MPxManipContainer_swigregister(*args, **kwargs):
    pass


def MPxManipulatorNode_className(*args, **kwargs):
    pass


def MPxManipulatorNode_newManipulator(*args, **kwargs):
    pass


def MPxManipulatorNode_swigregister(*args, **kwargs):
    pass


def MPxMaterialInformation_swigregister(*args, **kwargs):
    pass


def MPxMayaAsciiFilterOutput_swigregister(*args, **kwargs):
    pass


def MPxMayaAsciiFilter_swigregister(*args, **kwargs):
    pass


def MPxMidiInputDevice_className(*args, **kwargs):
    pass


def MPxMidiInputDevice_swigregister(*args, **kwargs):
    pass


def MPxModelEditorCommand_className(*args, **kwargs):
    pass


def MPxModelEditorCommand_swigregister(*args, **kwargs):
    pass


def MPxNode_addAttribute(*args, **kwargs):
    pass


def MPxNode_attributeAffects(*args, **kwargs):
    pass


def MPxNode_className(*args, **kwargs):
    pass


def MPxNode_inheritAttributesFrom(*args, **kwargs):
    pass


def MPxNode_swigregister(*args, **kwargs):
    pass


def MPxObjectSet_className(*args, **kwargs):
    pass


def MPxObjectSet_swigregister(*args, **kwargs):
    pass


def MPxParticleAttributeMapperNode_className(*args, **kwargs):
    pass


def MPxParticleAttributeMapperNode_swigregister(*args, **kwargs):
    pass


def MPxPolyTrg_swigregister(*args, **kwargs):
    pass


def MPxPolyTweakUVCommand_newSyntax(*args, **kwargs):
    pass


def MPxPolyTweakUVCommand_swigregister(*args, **kwargs):
    pass


def MPxRenderPassImpl_swigregister(*args, **kwargs):
    pass


def MPxSelectionContext_className(*args, **kwargs):
    pass


def MPxSelectionContext_swigregister(*args, **kwargs):
    pass


def MPxShaderOverride_className(*args, **kwargs):
    pass


def MPxShaderOverride_swigregister(*args, **kwargs):
    pass


def MPxSpringNode_className(*args, **kwargs):
    pass


def MPxSpringNode_swigregister(*args, **kwargs):
    pass


def MPxSurfaceShapeUI_className(*args, **kwargs):
    pass


def MPxSurfaceShapeUI_surfaceShapeUI(*args, **kwargs):
    pass


def MPxSurfaceShapeUI_swigregister(*args, **kwargs):
    pass


def MPxSurfaceShape_className(*args, **kwargs):
    pass


def MPxSurfaceShape_swigregister(*args, **kwargs):
    pass


def MPxToolCommand_className(*args, **kwargs):
    pass


def MPxToolCommand_swigregister(*args, **kwargs):
    pass


def MPxTransform_className(*args, **kwargs):
    pass


def MPxTransform_isNonAffineMatricesEnabled(*args, **kwargs):
    pass


def MPxTransform_mustCallValidateAndSet(*args, **kwargs):
    pass


def MPxTransform_setNonAffineMatricesEnabled(*args, **kwargs):
    pass


def MPxTransform_swigregister(*args, **kwargs):
    pass


def MPxTransformationMatrix_convertEulerRotationOrder(*args, **kwargs):
    pass


def MPxTransformationMatrix_convertTransformationRotationOrder(*args, **kwargs):
    pass


def MPxTransformationMatrix_creator(*args, **kwargs):
    pass


def MPxTransformationMatrix_swigregister(*args, **kwargs):
    pass


def MPxUIControl_className(*args, **kwargs):
    pass


def MPxUIControl_swigregister(*args, **kwargs):
    pass


def MPxUITableControl_className(*args, **kwargs):
    pass


def MPxUITableControl_swigregister(*args, **kwargs):
    pass


def MaterialInputData_swigregister(*args, **kwargs):
    pass


def asHashable(mpxObj):
    pass


def asMPxPtr(mpxObj):
    pass


def getLockCaptureCount(*args, **kwargs):
    pass


def weakref_proxy(*args, **kwargs):
    """
    proxy(object[, callback]) -- create a proxy object that weakly
    references 'object'.  'callback', if given, is called with a
    reference to the proxy when 'object' is about to be finalized.
    """

    pass

PLUGIN_COMPANY = None

cvar = None
