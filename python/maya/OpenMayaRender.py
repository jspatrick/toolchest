import OpenMaya
import _OpenMayaRender
import new
import weakref

from maya._OpenMayaRender import *

class MSwatchRenderBase(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def doIteration(*args, **kwargs):
        pass
    
    
    def image(*args, **kwargs):
        pass
    
    
    def node(*args, **kwargs):
        pass
    
    
    def resolution(*args, **kwargs):
        pass
    
    
    def swatchNode(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MShaderManager(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def addShaderIncludePath(*args, **kwargs):
        pass
    
    
    def addShaderPath(*args, **kwargs):
        pass
    
    
    def getEffectsFileShader(*args, **kwargs):
        pass
    
    
    def getStockShader(*args, **kwargs):
        pass
    
    
    def shaderIncludePaths(*args, **kwargs):
        pass
    
    
    def shaderPaths(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    k3dBlinnShader = None
    
    
    k3dSolidShader = None


class MDepthStencilState(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def desc(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kDecrementStencil = None
    
    
    kDecrementStencilSat = None
    
    
    kIncrementStencil = None
    
    
    kIncrementStencilSat = None
    
    
    kInvertStencil = None
    
    
    kKeepStencil = None
    
    
    kReplaceStencil = None
    
    
    kZeroStencil = None


class MGeometryRequirements(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def renderItemList(*args, **kwargs):
        pass
    
    
    def requirementDescriptors(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None


class MGeometryManager(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def dereferenceDefaultGeometry(*args, **kwargs):
        pass
    
    
    def getGeometry(*args, **kwargs):
        pass
    
    
    def referenceDefaultGeometry(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    kDefaultCube = None
    
    
    kDefaultPlane = None
    
    
    kDefaultSphere = None


class MRenderData(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def screenToWorld(*args, **kwargs):
        pass
    
    
    def worldToScreen(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    aspectRatio = None
    
    bottom = None
    
    bytesPerChannel = None
    
    depthArr = None
    
    eyePoint = None
    
    fieldOfView = None
    
    internalData = None
    
    left = None
    
    perspective = None
    
    resX = None
    
    resY = None
    
    rgbaArr = None
    
    right = None
    
    thisown = None
    
    top = None
    
    viewDirection = None
    
    worldToEyeMatrix = None
    
    xsize = None
    
    ysize = None
    
    __swig_destroy__ = None


class MSamplerState(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def desc(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kAnisotropic = None
    
    
    kMinLinear_MagMipPoint = None
    
    
    kMinLinear_MagPoint_MipLinear = None
    
    
    kMinMagLinear_MipPoint = None
    
    
    kMinMagMipLinear = None
    
    
    kMinMagMipPoint = None
    
    
    kMinMagPoint_MipLinear = None
    
    
    kMinPoint_MagLinear_MipPoint = None
    
    
    kMinPoint_MagMipLinear = None
    
    
    kTexBorder = None
    
    
    kTexClamp = None
    
    
    kTexMirror = None
    
    
    kTexWrap = None


class MRenderTargetManager(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def acquireRenderTarget(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None


class MHwTextureManager(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def deregisterTextureFile(*args, **kwargs):
        pass
    
    
    def glBind(*args, **kwargs):
        pass
    
    
    def registerTextureFile(*args, **kwargs):
        pass
    
    
    def textureFile(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None


class MTexture(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def name(*args, **kwargs):
        pass
    
    
    def resourceHandle(*args, **kwargs):
        pass
    
    
    def textureDescription(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MFnRenderPass(OpenMaya.MFnDependencyNode):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def customTokenString(*args, **kwargs):
        pass
    
    
    def frameBufferChannels(*args, **kwargs):
        pass
    
    
    def frameBufferType(*args, **kwargs):
        pass
    
    
    def getImplementation(*args, **kwargs):
        pass
    
    
    def passID(*args, **kwargs):
        pass
    
    
    def setImplementation(*args, **kwargs):
        pass
    
    
    def usesFiltering(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MVertexBufferDescriptor(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def dataType(*args, **kwargs):
        pass
    
    
    def dataTypeSize(*args, **kwargs):
        pass
    
    
    def dimension(*args, **kwargs):
        pass
    
    
    def name(*args, **kwargs):
        pass
    
    
    def offset(*args, **kwargs):
        pass
    
    
    def semantic(*args, **kwargs):
        pass
    
    
    def setDataType(*args, **kwargs):
        pass
    
    
    def setDimension(*args, **kwargs):
        pass
    
    
    def setName(*args, **kwargs):
        pass
    
    
    def setSemantic(*args, **kwargs):
        pass
    
    
    def stride(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MRasterizerState(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def desc(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kCullBack = None
    
    
    kCullFront = None
    
    
    kCullNone = None
    
    
    kFillSolid = None
    
    
    kFillWireFrame = None


class MD3D9Renderer(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def getD3D9Device(*args, **kwargs):
        pass
    
    
    def makeSwatchContextCurrent(*args, **kwargs):
        pass
    
    
    def readSwatchContextPixels(*args, **kwargs):
        pass
    
    
    def setBackgroundColor(*args, **kwargs):
        pass
    
    
    def theRenderer(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MBlendState(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def desc(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kAdd = None
    
    
    kAlphaChannel = None
    
    
    kBlendFactor = None
    
    
    kBlueChannel = None
    
    
    kBothInvSourceAlpha = None
    
    
    kBothSourceAlpha = None
    
    
    kDestinationAlpha = None
    
    
    kDestinationColor = None
    
    
    kGreenChannel = None
    
    
    kInvBlendFactor = None
    
    
    kInvDestinationAlpha = None
    
    
    kInvDestinationColor = None
    
    
    kInvSourceAlpha = None
    
    
    kInvSourceColor = None
    
    
    kMax = None
    
    
    kMaxTargets = None
    
    
    kMin = None
    
    
    kNoChannels = None
    
    
    kOne = None
    
    
    kRGBAChannels = None
    
    
    kRGBChannels = None
    
    
    kRedChannel = None
    
    
    kReverseSubtract = None
    
    
    kSourceAlpha = None
    
    
    kSourceAlphaSat = None
    
    
    kSourceColor = None
    
    
    kSubtract = None
    
    
    kZero = None


class MRenderCallback(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def postProcessCallback(*args, **kwargs):
        pass
    
    
    def renderCallback(*args, **kwargs):
        pass
    
    
    def shadowCastCallback(*args, **kwargs):
        pass
    
    
    def addCallback(*args, **kwargs):
        pass
    
    
    def removeCallback(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MRenderTarget(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def resourceHandle(*args, **kwargs):
        pass
    
    
    def updateDescription(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MViewportRenderer(object):
    def UIname(*args, **kwargs):
        pass
    
    
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def deregisterRenderer(*args, **kwargs):
        pass
    
    
    def initialize(*args, **kwargs):
        pass
    
    
    def name(*args, **kwargs):
        pass
    
    
    def nativelySupports(*args, **kwargs):
        pass
    
    
    def override(*args, **kwargs):
        pass
    
    
    def overrideThenStandardExclusion(*args, **kwargs):
        pass
    
    
    def registerRenderer(*args, **kwargs):
        pass
    
    
    def render(*args, **kwargs):
        pass
    
    
    def renderingOverride(*args, **kwargs):
        pass
    
    
    def setRenderingOverride(*args, **kwargs):
        pass
    
    
    def setUIName(*args, **kwargs):
        pass
    
    
    def uninitialize(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kDirect3D = None
    
    
    kExcludeAll = None
    
    
    kExcludeCVs = None
    
    
    kExcludeCameras = None
    
    
    kExcludeDeformers = None
    
    
    kExcludeDimensions = None
    
    
    kExcludeDynamicConstraints = None
    
    
    kExcludeDynamics = None
    
    
    kExcludeFluids = None
    
    
    kExcludeFollicles = None
    
    
    kExcludeGrid = None
    
    
    kExcludeHairSystems = None
    
    
    kExcludeHulls = None
    
    
    kExcludeIkHandles = None
    
    
    kExcludeImagePlane = None
    
    
    kExcludeJoints = None
    
    
    kExcludeLights = None
    
    
    kExcludeLocators = None
    
    
    kExcludeManipulators = None
    
    
    kExcludeMeshes = None
    
    
    kExcludeNCloths = None
    
    
    kExcludeNParticles = None
    
    
    kExcludeNRigids = None
    
    
    kExcludeNone = None
    
    
    kExcludeNurbsCurves = None
    
    
    kExcludeNurbsSurfaces = None
    
    
    kExcludePivots = None
    
    
    kExcludePlanes = None
    
    
    kExcludeSelectHandles = None
    
    
    kExcludeStrokes = None
    
    
    kExcludeSubdivSurfaces = None
    
    
    kExcludeTextures = None
    
    
    kNoOverride = None
    
    
    kOpenGL = None
    
    
    kOverrideAllDrawing = None
    
    
    kOverrideThenStandard = None
    
    
    kSoftware = None


class MRenderingInfo(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def cameraPath(*args, **kwargs):
        pass
    
    
    def height(*args, **kwargs):
        pass
    
    
    def originX(*args, **kwargs):
        pass
    
    
    def originY(*args, **kwargs):
        pass
    
    
    def projectionMatrix(*args, **kwargs):
        pass
    
    
    def renderTarget(*args, **kwargs):
        pass
    
    
    def renderingAPI(*args, **kwargs):
        pass
    
    
    def renderingVersion(*args, **kwargs):
        pass
    
    
    def viewMatrix(*args, **kwargs):
        pass
    
    
    def width(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None


class MFnImageSource(OpenMaya.MFnDependencyNode):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def getImageName(*args, **kwargs):
        pass
    
    
    def sourceCamera(*args, **kwargs):
        pass
    
    
    def sourceLayer(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MHardwareRenderer(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def addDrawProcedure(*args, **kwargs):
        pass
    
    
    def backEndString(*args, **kwargs):
        pass
    
    
    def dereferenceGeometry(*args, **kwargs):
        pass
    
    
    def drawSwatchBackGroundQuads(*args, **kwargs):
        pass
    
    
    def findDrawProcedure(*args, **kwargs):
        pass
    
    
    def getBufferSize(*args, **kwargs):
        pass
    
    
    def getColorBufferPixelFormat(*args, **kwargs):
        pass
    
    
    def getCurrentExposureNumber(*args, **kwargs):
        pass
    
    
    def getDepthBufferPixelFormat(*args, **kwargs):
        pass
    
    
    def getDrawProcedureCount(*args, **kwargs):
        pass
    
    
    def getDrawProcedureListNames(*args, **kwargs):
        pass
    
    
    def getSwatchLightDirection(*args, **kwargs):
        pass
    
    
    def getSwatchOrthoCameraSetting(*args, **kwargs):
        pass
    
    
    def getSwatchPerspectiveCameraSetting(*args, **kwargs):
        pass
    
    
    def getSwatchPerspectiveCameraTranslation(*args, **kwargs):
        pass
    
    
    def getTotalExposureCount(*args, **kwargs):
        pass
    
    
    def glFunctionTable(*args, **kwargs):
        pass
    
    
    def insertDrawProcedure(*args, **kwargs):
        pass
    
    
    def makeResourceContextCurrent(*args, **kwargs):
        pass
    
    
    def makeSwatchContextCurrent(*args, **kwargs):
        pass
    
    
    def readSwatchContextPixels(*args, **kwargs):
        pass
    
    
    def referenceDefaultGeometry(*args, **kwargs):
        pass
    
    
    def removeDrawProcedure(*args, **kwargs):
        pass
    
    
    def restoreCurrent(*args, **kwargs):
        pass
    
    
    def theRenderer(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    kDefaultCube = None
    
    
    kDefaultPlane = None
    
    
    kDefaultSphere = None
    
    
    kDepth_Float32 = None
    
    
    kFailure = None
    
    
    kItemExists = None
    
    
    kItemNotFound = None
    
    
    kLocationNotFound = None
    
    
    kPostExposure = None
    
    
    kPostRendering = None
    
    
    kPreExposure = None
    
    
    kPreRendering = None
    
    
    kRGBA_Fix8 = None
    
    
    kRGBA_Float16 = None
    
    
    kSuccess = None


class MRenderView(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def doesRenderEditorExist(*args, **kwargs):
        pass
    
    
    def endRender(*args, **kwargs):
        pass
    
    
    def getRenderRegion(*args, **kwargs):
        pass
    
    
    def refresh(*args, **kwargs):
        pass
    
    
    def setCurrentCamera(*args, **kwargs):
        pass
    
    
    def startRegionRender(*args, **kwargs):
        pass
    
    
    def startRender(*args, **kwargs):
        pass
    
    
    def updatePixels(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MRenderProfile(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def addRenderer(*args, **kwargs):
        pass
    
    
    def hasRenderer(*args, **kwargs):
        pass
    
    
    def numberOfRenderers(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kMayaD3D = None
    
    
    kMayaOpenGL = None
    
    
    kMayaSoftware = None


class MRenderOverride(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def cleanup(*args, **kwargs):
        pass
    
    
    def name(*args, **kwargs):
        pass
    
    
    def nextRenderOperation(*args, **kwargs):
        pass
    
    
    def renderOperation(*args, **kwargs):
        pass
    
    
    def setup(*args, **kwargs):
        pass
    
    
    def startOperationIterator(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    mName = None
    
    thisown = None
    
    __swig_destroy__ = None


class MBlendStateDesc(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def setDefaults(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    alphaToCoverageEnable = None
    
    blendFactor = None
    
    independentBlendEnable = None
    
    multiSampleMask = None
    
    targetBlends = None
    
    thisown = None
    
    __swig_destroy__ = None


class MSamplerStateDesc(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def setDefaults(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    addressU = None
    
    addressV = None
    
    addressW = None
    
    borderColor = None
    
    comparisonFn = None
    
    coordCount = None
    
    elementIndex = None
    
    filter = None
    
    maxAnisotropy = None
    
    maxLOD = None
    
    minLOD = None
    
    mipLODBias = None
    
    thisown = None
    
    __swig_destroy__ = None


class MTextureDescription(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def setToDefault2DTexture(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    fArraySlices = None
    
    fBytesPerRow = None
    
    fBytesPerSlice = None
    
    fDepth = None
    
    fEnvMapType = None
    
    fFormat = None
    
    fHeight = None
    
    fMipmaps = None
    
    fTextureType = None
    
    fWidth = None
    
    thisown = None
    
    __swig_destroy__ = None


class MFnRenderLayer(OpenMaya.MFnDependencyNode):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def adjustmentPlug(*args, **kwargs):
        pass
    
    
    def externalRenderPasses(*args, **kwargs):
        pass
    
    
    def inCurrentRenderLayer(*args, **kwargs):
        pass
    
    
    def inLayer(*args, **kwargs):
        pass
    
    
    def isPlugAdjusted(*args, **kwargs):
        pass
    
    
    def layerChildren(*args, **kwargs):
        pass
    
    
    def listMembers(*args, **kwargs):
        pass
    
    
    def passHasLight(*args, **kwargs):
        pass
    
    
    def passHasObject(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def currentLayer(*args, **kwargs):
        pass
    
    
    def defaultRenderLayer(*args, **kwargs):
        pass
    
    
    def findLayerByName(*args, **kwargs):
        pass
    
    
    def listAllRenderLayers(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MVertexBuffer(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def acquire(*args, **kwargs):
        pass
    
    
    def commit(*args, **kwargs):
        pass
    
    
    def descriptor(*args, **kwargs):
        pass
    
    
    def resourceHandle(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None


class MCameraOverride(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    mCameraPath = None
    
    mProjectionMatrix = None
    
    mUseProjectionMatrix = None
    
    mUseViewMatrix = None
    
    mViewMatrix = None
    
    thisown = None
    
    __swig_destroy__ = None


class MTextureManager(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def acquireTexture(*args, **kwargs):
        pass
    
    
    def addImagePath(*args, **kwargs):
        pass
    
    
    def imagePaths(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None


class MDrawRegistry(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def deregisterDrawOverrideCreator(*args, **kwargs):
        pass
    
    
    def deregisterGeometryOverrideCreator(*args, **kwargs):
        pass
    
    
    def deregisterShaderOverrideCreator(*args, **kwargs):
        pass
    
    
    def registerDrawOverrideCreator(*args, **kwargs):
        pass
    
    
    def registerGeometryOverrideCreator(*args, **kwargs):
        pass
    
    
    def registerShaderOverrideCreator(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None


class MDrawProcedureBase(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def enabled(*args, **kwargs):
        pass
    
    
    def execute(*args, **kwargs):
        pass
    
    
    def name(*args, **kwargs):
        pass
    
    
    def setEnabled(*args, **kwargs):
        pass
    
    
    def setName(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MUniformParameterList(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def append(*args, **kwargs):
        pass
    
    
    def assign(*args, **kwargs):
        pass
    
    
    def getElement(*args, **kwargs):
        pass
    
    
    def length(*args, **kwargs):
        pass
    
    
    def setElement(*args, **kwargs):
        pass
    
    
    def setLength(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MVaryingParameterList(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def append(*args, **kwargs):
        pass
    
    
    def assign(*args, **kwargs):
        pass
    
    
    def getElement(*args, **kwargs):
        pass
    
    
    def length(*args, **kwargs):
        pass
    
    
    def setElement(*args, **kwargs):
        pass
    
    
    def setLength(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class RV_PIXEL(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    a = None
    
    b = None
    
    g = None
    
    r = None
    
    thisown = None
    
    __swig_destroy__ = None


class MRenderItem(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def associateWithIndexBuffer(*args, **kwargs):
        pass
    
    
    def customData(*args, **kwargs):
        pass
    
    
    def drawMode(*args, **kwargs):
        pass
    
    
    def enable(*args, **kwargs):
        pass
    
    
    def geometry(*args, **kwargs):
        pass
    
    
    def isEnabled(*args, **kwargs):
        pass
    
    
    def name(*args, **kwargs):
        pass
    
    
    def primitive(*args, **kwargs):
        pass
    
    
    def requiredVertexBuffers(*args, **kwargs):
        pass
    
    
    def setCustomData(*args, **kwargs):
        pass
    
    
    def setShader(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MRenderOperation(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def name(*args, **kwargs):
        pass
    
    
    def operationType(*args, **kwargs):
        pass
    
    
    def targetOverrideList(*args, **kwargs):
        pass
    
    
    def viewportRectangleOverride(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kClear = None
    
    
    kHUDRender = None
    
    
    kPresentTarget = None
    
    
    kQuadRender = None
    
    
    kSceneRender = None
    
    
    kUserDefined = None


class MGLFunctionTable(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def extensionExists(*args, **kwargs):
        pass
    
    
    def glAccum(*args, **kwargs):
        pass
    
    
    def glActiveTexture(*args, **kwargs):
        pass
    
    
    def glAlphaFragmentOp1ATI(*args, **kwargs):
        pass
    
    
    def glAlphaFragmentOp2ATI(*args, **kwargs):
        pass
    
    
    def glAlphaFragmentOp3ATI(*args, **kwargs):
        pass
    
    
    def glAlphaFunc(*args, **kwargs):
        pass
    
    
    def glAreProgramsResidentNV(*args, **kwargs):
        pass
    
    
    def glAreTexturesResident(*args, **kwargs):
        pass
    
    
    def glArrayElement(*args, **kwargs):
        pass
    
    
    def glAttachObjectARB(*args, **kwargs):
        pass
    
    
    def glBegin(*args, **kwargs):
        pass
    
    
    def glBeginFragmentShaderATI(*args, **kwargs):
        pass
    
    
    def glBeginOcclusionQueryNV(*args, **kwargs):
        pass
    
    
    def glBeginQueryARB(*args, **kwargs):
        pass
    
    
    def glBeginVertexShaderEXT(*args, **kwargs):
        pass
    
    
    def glBindAttribLocationARB(*args, **kwargs):
        pass
    
    
    def glBindBufferARB(*args, **kwargs):
        pass
    
    
    def glBindFragmentShaderATI(*args, **kwargs):
        pass
    
    
    def glBindFramebufferEXT(*args, **kwargs):
        pass
    
    
    def glBindLightParameterEXT(*args, **kwargs):
        pass
    
    
    def glBindMaterialParameterEXT(*args, **kwargs):
        pass
    
    
    def glBindParameterEXT(*args, **kwargs):
        pass
    
    
    def glBindProgram(*args, **kwargs):
        pass
    
    
    def glBindProgramNV(*args, **kwargs):
        pass
    
    
    def glBindRenderbufferEXT(*args, **kwargs):
        pass
    
    
    def glBindTexGenParameterEXT(*args, **kwargs):
        pass
    
    
    def glBindTexture(*args, **kwargs):
        pass
    
    
    def glBindTextureUnitParameterEXT(*args, **kwargs):
        pass
    
    
    def glBindVertexShaderEXT(*args, **kwargs):
        pass
    
    
    def glBitmap(*args, **kwargs):
        pass
    
    
    def glBlendEquationEXT(*args, **kwargs):
        pass
    
    
    def glBlendFunc(*args, **kwargs):
        pass
    
    
    def glBufferDataARB(*args, **kwargs):
        pass
    
    
    def glBufferSubDataARB(*args, **kwargs):
        pass
    
    
    def glCallList(*args, **kwargs):
        pass
    
    
    def glCallLists(*args, **kwargs):
        pass
    
    
    def glCheckFramebufferStatusEXT(*args, **kwargs):
        pass
    
    
    def glClear(*args, **kwargs):
        pass
    
    
    def glClearAccum(*args, **kwargs):
        pass
    
    
    def glClearColor(*args, **kwargs):
        pass
    
    
    def glClearDepth(*args, **kwargs):
        pass
    
    
    def glClearIndex(*args, **kwargs):
        pass
    
    
    def glClearStencil(*args, **kwargs):
        pass
    
    
    def glClientActiveTexture(*args, **kwargs):
        pass
    
    
    def glClipPlane(*args, **kwargs):
        pass
    
    
    def glColor3b(*args, **kwargs):
        pass
    
    
    def glColor3bv(*args, **kwargs):
        pass
    
    
    def glColor3d(*args, **kwargs):
        pass
    
    
    def glColor3dv(*args, **kwargs):
        pass
    
    
    def glColor3f(*args, **kwargs):
        pass
    
    
    def glColor3fv(*args, **kwargs):
        pass
    
    
    def glColor3i(*args, **kwargs):
        pass
    
    
    def glColor3iv(*args, **kwargs):
        pass
    
    
    def glColor3s(*args, **kwargs):
        pass
    
    
    def glColor3sv(*args, **kwargs):
        pass
    
    
    def glColor3ub(*args, **kwargs):
        pass
    
    
    def glColor3ubv(*args, **kwargs):
        pass
    
    
    def glColor3ui(*args, **kwargs):
        pass
    
    
    def glColor3uiv(*args, **kwargs):
        pass
    
    
    def glColor3us(*args, **kwargs):
        pass
    
    
    def glColor3usv(*args, **kwargs):
        pass
    
    
    def glColor4b(*args, **kwargs):
        pass
    
    
    def glColor4bv(*args, **kwargs):
        pass
    
    
    def glColor4d(*args, **kwargs):
        pass
    
    
    def glColor4dv(*args, **kwargs):
        pass
    
    
    def glColor4f(*args, **kwargs):
        pass
    
    
    def glColor4fv(*args, **kwargs):
        pass
    
    
    def glColor4i(*args, **kwargs):
        pass
    
    
    def glColor4iv(*args, **kwargs):
        pass
    
    
    def glColor4s(*args, **kwargs):
        pass
    
    
    def glColor4sv(*args, **kwargs):
        pass
    
    
    def glColor4ub(*args, **kwargs):
        pass
    
    
    def glColor4ubv(*args, **kwargs):
        pass
    
    
    def glColor4ui(*args, **kwargs):
        pass
    
    
    def glColor4uiv(*args, **kwargs):
        pass
    
    
    def glColor4us(*args, **kwargs):
        pass
    
    
    def glColor4usv(*args, **kwargs):
        pass
    
    
    def glColorFragmentOp1ATI(*args, **kwargs):
        pass
    
    
    def glColorFragmentOp2ATI(*args, **kwargs):
        pass
    
    
    def glColorFragmentOp3ATI(*args, **kwargs):
        pass
    
    
    def glColorMask(*args, **kwargs):
        pass
    
    
    def glColorMaterial(*args, **kwargs):
        pass
    
    
    def glColorPointer(*args, **kwargs):
        pass
    
    
    def glCombinerInputNV(*args, **kwargs):
        pass
    
    
    def glCombinerOutputNV(*args, **kwargs):
        pass
    
    
    def glCombinerParameterfNV(*args, **kwargs):
        pass
    
    
    def glCombinerParameterfvNV(*args, **kwargs):
        pass
    
    
    def glCombinerParameteriNV(*args, **kwargs):
        pass
    
    
    def glCombinerParameterivNV(*args, **kwargs):
        pass
    
    
    def glCompileShaderARB(*args, **kwargs):
        pass
    
    
    def glCompressedTexImage1D(*args, **kwargs):
        pass
    
    
    def glCompressedTexImage2D(*args, **kwargs):
        pass
    
    
    def glCompressedTexImage3D(*args, **kwargs):
        pass
    
    
    def glCompressedTexSubImage1D(*args, **kwargs):
        pass
    
    
    def glCompressedTexSubImage2D(*args, **kwargs):
        pass
    
    
    def glCompressedTexSubImage3D(*args, **kwargs):
        pass
    
    
    def glCopyPixels(*args, **kwargs):
        pass
    
    
    def glCopyTexImage1D(*args, **kwargs):
        pass
    
    
    def glCopyTexImage2D(*args, **kwargs):
        pass
    
    
    def glCopyTexSubImage1D(*args, **kwargs):
        pass
    
    
    def glCopyTexSubImage2D(*args, **kwargs):
        pass
    
    
    def glCopyTexSubImage3D(*args, **kwargs):
        pass
    
    
    def glCreateProgramObjectARB(*args, **kwargs):
        pass
    
    
    def glCreateShaderObjectARB(*args, **kwargs):
        pass
    
    
    def glCullFace(*args, **kwargs):
        pass
    
    
    def glCullParameterdvEXT(*args, **kwargs):
        pass
    
    
    def glCullParameterfvEXT(*args, **kwargs):
        pass
    
    
    def glDeleteBuffersARB(*args, **kwargs):
        pass
    
    
    def glDeleteFencesNV(*args, **kwargs):
        pass
    
    
    def glDeleteFragmentShaderATI(*args, **kwargs):
        pass
    
    
    def glDeleteFramebuffersEXT(*args, **kwargs):
        pass
    
    
    def glDeleteLists(*args, **kwargs):
        pass
    
    
    def glDeleteObjectARB(*args, **kwargs):
        pass
    
    
    def glDeleteOcclusionQueriesNV(*args, **kwargs):
        pass
    
    
    def glDeletePrograms(*args, **kwargs):
        pass
    
    
    def glDeleteProgramsNV(*args, **kwargs):
        pass
    
    
    def glDeleteQueriesARB(*args, **kwargs):
        pass
    
    
    def glDeleteRenderbuffersEXT(*args, **kwargs):
        pass
    
    
    def glDeleteTextures(*args, **kwargs):
        pass
    
    
    def glDeleteVertexShaderEXT(*args, **kwargs):
        pass
    
    
    def glDepthFunc(*args, **kwargs):
        pass
    
    
    def glDepthMask(*args, **kwargs):
        pass
    
    
    def glDepthRange(*args, **kwargs):
        pass
    
    
    def glDetachObjectARB(*args, **kwargs):
        pass
    
    
    def glDisable(*args, **kwargs):
        pass
    
    
    def glDisableClientState(*args, **kwargs):
        pass
    
    
    def glDisableVariantClientStateEXT(*args, **kwargs):
        pass
    
    
    def glDisableVertexAttribArray(*args, **kwargs):
        pass
    
    
    def glDrawArrays(*args, **kwargs):
        pass
    
    
    def glDrawBuffer(*args, **kwargs):
        pass
    
    
    def glDrawElements(*args, **kwargs):
        pass
    
    
    def glDrawPixels(*args, **kwargs):
        pass
    
    
    def glDrawRangeElements(*args, **kwargs):
        pass
    
    
    def glEdgeFlag(*args, **kwargs):
        pass
    
    
    def glEdgeFlagPointer(*args, **kwargs):
        pass
    
    
    def glEdgeFlagv(*args, **kwargs):
        pass
    
    
    def glEnable(*args, **kwargs):
        pass
    
    
    def glEnableClientState(*args, **kwargs):
        pass
    
    
    def glEnableVariantClientStateEXT(*args, **kwargs):
        pass
    
    
    def glEnableVertexAttribArray(*args, **kwargs):
        pass
    
    
    def glEnd(*args, **kwargs):
        pass
    
    
    def glEndFragmentShaderATI(*args, **kwargs):
        pass
    
    
    def glEndList(*args, **kwargs):
        pass
    
    
    def glEndOcclusionQueryNV(*args, **kwargs):
        pass
    
    
    def glEndQueryARB(*args, **kwargs):
        pass
    
    
    def glEndVertexShaderEXT(*args, **kwargs):
        pass
    
    
    def glEvalCoord1d(*args, **kwargs):
        pass
    
    
    def glEvalCoord1dv(*args, **kwargs):
        pass
    
    
    def glEvalCoord1f(*args, **kwargs):
        pass
    
    
    def glEvalCoord1fv(*args, **kwargs):
        pass
    
    
    def glEvalCoord2d(*args, **kwargs):
        pass
    
    
    def glEvalCoord2dv(*args, **kwargs):
        pass
    
    
    def glEvalCoord2f(*args, **kwargs):
        pass
    
    
    def glEvalCoord2fv(*args, **kwargs):
        pass
    
    
    def glEvalMesh1(*args, **kwargs):
        pass
    
    
    def glEvalMesh2(*args, **kwargs):
        pass
    
    
    def glEvalPoint1(*args, **kwargs):
        pass
    
    
    def glEvalPoint2(*args, **kwargs):
        pass
    
    
    def glExecuteProgramNV(*args, **kwargs):
        pass
    
    
    def glExtractComponentEXT(*args, **kwargs):
        pass
    
    
    def glFeedbackBuffer(*args, **kwargs):
        pass
    
    
    def glFinalCombinerInputNV(*args, **kwargs):
        pass
    
    
    def glFinish(*args, **kwargs):
        pass
    
    
    def glFinishFenceNV(*args, **kwargs):
        pass
    
    
    def glFlush(*args, **kwargs):
        pass
    
    
    def glFlushVertexArrayRangeNV(*args, **kwargs):
        pass
    
    
    def glFogCoordPointerEXT(*args, **kwargs):
        pass
    
    
    def glFogCoorddEXT(*args, **kwargs):
        pass
    
    
    def glFogCoorddvEXT(*args, **kwargs):
        pass
    
    
    def glFogCoordfEXT(*args, **kwargs):
        pass
    
    
    def glFogCoordfvEXT(*args, **kwargs):
        pass
    
    
    def glFogf(*args, **kwargs):
        pass
    
    
    def glFogfv(*args, **kwargs):
        pass
    
    
    def glFogi(*args, **kwargs):
        pass
    
    
    def glFogiv(*args, **kwargs):
        pass
    
    
    def glFramebufferRenderbufferEXT(*args, **kwargs):
        pass
    
    
    def glFramebufferTexture1DEXT(*args, **kwargs):
        pass
    
    
    def glFramebufferTexture2DEXT(*args, **kwargs):
        pass
    
    
    def glFramebufferTexture3DEXT(*args, **kwargs):
        pass
    
    
    def glFrontFace(*args, **kwargs):
        pass
    
    
    def glFrustum(*args, **kwargs):
        pass
    
    
    def glGenBuffersARB(*args, **kwargs):
        pass
    
    
    def glGenFencesNV(*args, **kwargs):
        pass
    
    
    def glGenFragmentShadersATI(*args, **kwargs):
        pass
    
    
    def glGenFramebuffersEXT(*args, **kwargs):
        pass
    
    
    def glGenLists(*args, **kwargs):
        pass
    
    
    def glGenOcclusionQueriesNV(*args, **kwargs):
        pass
    
    
    def glGenPrograms(*args, **kwargs):
        pass
    
    
    def glGenProgramsNV(*args, **kwargs):
        pass
    
    
    def glGenQueriesARB(*args, **kwargs):
        pass
    
    
    def glGenRenderbuffersEXT(*args, **kwargs):
        pass
    
    
    def glGenSymbolsEXT(*args, **kwargs):
        pass
    
    
    def glGenTextures(*args, **kwargs):
        pass
    
    
    def glGenVertexShadersEXT(*args, **kwargs):
        pass
    
    
    def glGenerateMipmapEXT(*args, **kwargs):
        pass
    
    
    def glGetActiveAttribARB(*args, **kwargs):
        pass
    
    
    def glGetActiveUniformARB(*args, **kwargs):
        pass
    
    
    def glGetAttachedObjectsARB(*args, **kwargs):
        pass
    
    
    def glGetAttribLocationARB(*args, **kwargs):
        pass
    
    
    def glGetBooleanv(*args, **kwargs):
        pass
    
    
    def glGetBufferParameterivARB(*args, **kwargs):
        pass
    
    
    def glGetBufferPointervARB(*args, **kwargs):
        pass
    
    
    def glGetBufferSubDataARB(*args, **kwargs):
        pass
    
    
    def glGetClipPlane(*args, **kwargs):
        pass
    
    
    def glGetCombinerInputParameterfvNV(*args, **kwargs):
        pass
    
    
    def glGetCombinerInputParameterivNV(*args, **kwargs):
        pass
    
    
    def glGetCombinerOutputParameterfvNV(*args, **kwargs):
        pass
    
    
    def glGetCombinerOutputParameterivNV(*args, **kwargs):
        pass
    
    
    def glGetCompressedTexImage(*args, **kwargs):
        pass
    
    
    def glGetDoublev(*args, **kwargs):
        pass
    
    
    def glGetError(*args, **kwargs):
        pass
    
    
    def glGetFenceivNV(*args, **kwargs):
        pass
    
    
    def glGetFinalCombinerInputParameterfvNV(*args, **kwargs):
        pass
    
    
    def glGetFinalCombinerInputParameterivNV(*args, **kwargs):
        pass
    
    
    def glGetFloatv(*args, **kwargs):
        pass
    
    
    def glGetFramebufferAttachmentParameterivEXT(*args, **kwargs):
        pass
    
    
    def glGetHandleARB(*args, **kwargs):
        pass
    
    
    def glGetInfoLogARB(*args, **kwargs):
        pass
    
    
    def glGetIntegerv(*args, **kwargs):
        pass
    
    
    def glGetInvariantBooleanvEXT(*args, **kwargs):
        pass
    
    
    def glGetInvariantFloatvEXT(*args, **kwargs):
        pass
    
    
    def glGetInvariantIntegervEXT(*args, **kwargs):
        pass
    
    
    def glGetLightfv(*args, **kwargs):
        pass
    
    
    def glGetLightiv(*args, **kwargs):
        pass
    
    
    def glGetLocalConstantBooleanvEXT(*args, **kwargs):
        pass
    
    
    def glGetLocalConstantFloatvEXT(*args, **kwargs):
        pass
    
    
    def glGetLocalConstantIntegervEXT(*args, **kwargs):
        pass
    
    
    def glGetMapdv(*args, **kwargs):
        pass
    
    
    def glGetMapfv(*args, **kwargs):
        pass
    
    
    def glGetMapiv(*args, **kwargs):
        pass
    
    
    def glGetMaterialfv(*args, **kwargs):
        pass
    
    
    def glGetMaterialiv(*args, **kwargs):
        pass
    
    
    def glGetObjectParameterfvARB(*args, **kwargs):
        pass
    
    
    def glGetObjectParameterivARB(*args, **kwargs):
        pass
    
    
    def glGetOcclusionQueryivNV(*args, **kwargs):
        pass
    
    
    def glGetOcclusionQueryuivNV(*args, **kwargs):
        pass
    
    
    def glGetPixelMapfv(*args, **kwargs):
        pass
    
    
    def glGetPixelMapuiv(*args, **kwargs):
        pass
    
    
    def glGetPixelMapusv(*args, **kwargs):
        pass
    
    
    def glGetPointerv(*args, **kwargs):
        pass
    
    
    def glGetPolygonStipple(*args, **kwargs):
        pass
    
    
    def glGetProgramEnvParameterdv(*args, **kwargs):
        pass
    
    
    def glGetProgramEnvParameterfv(*args, **kwargs):
        pass
    
    
    def glGetProgramLocalParameterdv(*args, **kwargs):
        pass
    
    
    def glGetProgramLocalParameterfv(*args, **kwargs):
        pass
    
    
    def glGetProgramParameterdvNV(*args, **kwargs):
        pass
    
    
    def glGetProgramParameterfvNV(*args, **kwargs):
        pass
    
    
    def glGetProgramString(*args, **kwargs):
        pass
    
    
    def glGetProgramStringNV(*args, **kwargs):
        pass
    
    
    def glGetProgramiv(*args, **kwargs):
        pass
    
    
    def glGetProgramivNV(*args, **kwargs):
        pass
    
    
    def glGetQueryObjectivARB(*args, **kwargs):
        pass
    
    
    def glGetQueryObjectuivARB(*args, **kwargs):
        pass
    
    
    def glGetQueryivARB(*args, **kwargs):
        pass
    
    
    def glGetRenderbufferParameterivEXT(*args, **kwargs):
        pass
    
    
    def glGetShaderSourceARB(*args, **kwargs):
        pass
    
    
    def glGetString(*args, **kwargs):
        pass
    
    
    def glGetTexEnvfv(*args, **kwargs):
        pass
    
    
    def glGetTexEnviv(*args, **kwargs):
        pass
    
    
    def glGetTexGendv(*args, **kwargs):
        pass
    
    
    def glGetTexGenfv(*args, **kwargs):
        pass
    
    
    def glGetTexGeniv(*args, **kwargs):
        pass
    
    
    def glGetTexImage(*args, **kwargs):
        pass
    
    
    def glGetTexLevelParameterfv(*args, **kwargs):
        pass
    
    
    def glGetTexLevelParameteriv(*args, **kwargs):
        pass
    
    
    def glGetTexParameterfv(*args, **kwargs):
        pass
    
    
    def glGetTexParameteriv(*args, **kwargs):
        pass
    
    
    def glGetTrackMatrixivNV(*args, **kwargs):
        pass
    
    
    def glGetUniformLocationARB(*args, **kwargs):
        pass
    
    
    def glGetUniformfvARB(*args, **kwargs):
        pass
    
    
    def glGetUniformivARB(*args, **kwargs):
        pass
    
    
    def glGetVariantBooleanvEXT(*args, **kwargs):
        pass
    
    
    def glGetVariantFloatvEXT(*args, **kwargs):
        pass
    
    
    def glGetVariantIntegervEXT(*args, **kwargs):
        pass
    
    
    def glGetVariantPointervEXT(*args, **kwargs):
        pass
    
    
    def glGetVertexAttribPointerv(*args, **kwargs):
        pass
    
    
    def glGetVertexAttribPointervNV(*args, **kwargs):
        pass
    
    
    def glGetVertexAttribdv(*args, **kwargs):
        pass
    
    
    def glGetVertexAttribdvNV(*args, **kwargs):
        pass
    
    
    def glGetVertexAttribfv(*args, **kwargs):
        pass
    
    
    def glGetVertexAttribfvNV(*args, **kwargs):
        pass
    
    
    def glGetVertexAttribiv(*args, **kwargs):
        pass
    
    
    def glGetVertexAttribivNV(*args, **kwargs):
        pass
    
    
    def glHint(*args, **kwargs):
        pass
    
    
    def glIndexMask(*args, **kwargs):
        pass
    
    
    def glIndexPointer(*args, **kwargs):
        pass
    
    
    def glIndexd(*args, **kwargs):
        pass
    
    
    def glIndexdv(*args, **kwargs):
        pass
    
    
    def glIndexf(*args, **kwargs):
        pass
    
    
    def glIndexfv(*args, **kwargs):
        pass
    
    
    def glIndexi(*args, **kwargs):
        pass
    
    
    def glIndexiv(*args, **kwargs):
        pass
    
    
    def glIndexs(*args, **kwargs):
        pass
    
    
    def glIndexsv(*args, **kwargs):
        pass
    
    
    def glIndexub(*args, **kwargs):
        pass
    
    
    def glIndexubv(*args, **kwargs):
        pass
    
    
    def glInitNames(*args, **kwargs):
        pass
    
    
    def glInsertComponentEXT(*args, **kwargs):
        pass
    
    
    def glInterleavedArrays(*args, **kwargs):
        pass
    
    
    def glIsBufferARB(*args, **kwargs):
        pass
    
    
    def glIsEnabled(*args, **kwargs):
        pass
    
    
    def glIsFenceNV(*args, **kwargs):
        pass
    
    
    def glIsFramebufferEXT(*args, **kwargs):
        pass
    
    
    def glIsList(*args, **kwargs):
        pass
    
    
    def glIsOcclusionQueryNV(*args, **kwargs):
        pass
    
    
    def glIsProgram(*args, **kwargs):
        pass
    
    
    def glIsProgramNV(*args, **kwargs):
        pass
    
    
    def glIsQueryARB(*args, **kwargs):
        pass
    
    
    def glIsRenderbufferEXT(*args, **kwargs):
        pass
    
    
    def glIsTexture(*args, **kwargs):
        pass
    
    
    def glIsVariantEnabledEXT(*args, **kwargs):
        pass
    
    
    def glLightModelf(*args, **kwargs):
        pass
    
    
    def glLightModelfv(*args, **kwargs):
        pass
    
    
    def glLightModeli(*args, **kwargs):
        pass
    
    
    def glLightModeliv(*args, **kwargs):
        pass
    
    
    def glLightf(*args, **kwargs):
        pass
    
    
    def glLightfv(*args, **kwargs):
        pass
    
    
    def glLighti(*args, **kwargs):
        pass
    
    
    def glLightiv(*args, **kwargs):
        pass
    
    
    def glLineStipple(*args, **kwargs):
        pass
    
    
    def glLineWidth(*args, **kwargs):
        pass
    
    
    def glLinkProgramARB(*args, **kwargs):
        pass
    
    
    def glListBase(*args, **kwargs):
        pass
    
    
    def glLoadIdentity(*args, **kwargs):
        pass
    
    
    def glLoadMatrixd(*args, **kwargs):
        pass
    
    
    def glLoadMatrixf(*args, **kwargs):
        pass
    
    
    def glLoadName(*args, **kwargs):
        pass
    
    
    def glLoadProgramNV(*args, **kwargs):
        pass
    
    
    def glLoadTransposeMatrixd(*args, **kwargs):
        pass
    
    
    def glLoadTransposeMatrixdARB(*args, **kwargs):
        pass
    
    
    def glLoadTransposeMatrixf(*args, **kwargs):
        pass
    
    
    def glLoadTransposeMatrixfARB(*args, **kwargs):
        pass
    
    
    def glLockArraysEXT(*args, **kwargs):
        pass
    
    
    def glLogicOp(*args, **kwargs):
        pass
    
    
    def glMap1d(*args, **kwargs):
        pass
    
    
    def glMap1f(*args, **kwargs):
        pass
    
    
    def glMap2d(*args, **kwargs):
        pass
    
    
    def glMap2f(*args, **kwargs):
        pass
    
    
    def glMapBufferARB(*args, **kwargs):
        pass
    
    
    def glMapGrid1d(*args, **kwargs):
        pass
    
    
    def glMapGrid1f(*args, **kwargs):
        pass
    
    
    def glMapGrid2d(*args, **kwargs):
        pass
    
    
    def glMapGrid2f(*args, **kwargs):
        pass
    
    
    def glMaterialf(*args, **kwargs):
        pass
    
    
    def glMaterialfv(*args, **kwargs):
        pass
    
    
    def glMateriali(*args, **kwargs):
        pass
    
    
    def glMaterialiv(*args, **kwargs):
        pass
    
    
    def glMatrixMode(*args, **kwargs):
        pass
    
    
    def glMultMatrixd(*args, **kwargs):
        pass
    
    
    def glMultMatrixf(*args, **kwargs):
        pass
    
    
    def glMultTransposeMatrixd(*args, **kwargs):
        pass
    
    
    def glMultTransposeMatrixdARB(*args, **kwargs):
        pass
    
    
    def glMultTransposeMatrixf(*args, **kwargs):
        pass
    
    
    def glMultTransposeMatrixfARB(*args, **kwargs):
        pass
    
    
    def glMultiDrawArrays(*args, **kwargs):
        pass
    
    
    def glMultiDrawElements(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord1d(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord1dv(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord1f(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord1fv(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord1i(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord1iv(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord1s(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord1sv(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord2d(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord2dv(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord2f(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord2fv(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord2i(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord2iv(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord2s(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord2sv(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord3d(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord3dv(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord3f(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord3fv(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord3i(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord3iv(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord3s(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord3sv(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord4d(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord4dv(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord4f(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord4fv(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord4i(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord4iv(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord4s(*args, **kwargs):
        pass
    
    
    def glMultiTexCoord4sv(*args, **kwargs):
        pass
    
    
    def glNewList(*args, **kwargs):
        pass
    
    
    def glNormal3b(*args, **kwargs):
        pass
    
    
    def glNormal3bv(*args, **kwargs):
        pass
    
    
    def glNormal3d(*args, **kwargs):
        pass
    
    
    def glNormal3dv(*args, **kwargs):
        pass
    
    
    def glNormal3f(*args, **kwargs):
        pass
    
    
    def glNormal3fv(*args, **kwargs):
        pass
    
    
    def glNormal3i(*args, **kwargs):
        pass
    
    
    def glNormal3iv(*args, **kwargs):
        pass
    
    
    def glNormal3s(*args, **kwargs):
        pass
    
    
    def glNormal3sv(*args, **kwargs):
        pass
    
    
    def glNormalPointer(*args, **kwargs):
        pass
    
    
    def glOrtho(*args, **kwargs):
        pass
    
    
    def glPNTrianglesfATI(*args, **kwargs):
        pass
    
    
    def glPNTrianglesiATI(*args, **kwargs):
        pass
    
    
    def glPassTexCoordATI(*args, **kwargs):
        pass
    
    
    def glPassThrough(*args, **kwargs):
        pass
    
    
    def glPixelMapfv(*args, **kwargs):
        pass
    
    
    def glPixelMapuiv(*args, **kwargs):
        pass
    
    
    def glPixelMapusv(*args, **kwargs):
        pass
    
    
    def glPixelStoref(*args, **kwargs):
        pass
    
    
    def glPixelStorei(*args, **kwargs):
        pass
    
    
    def glPixelTransferf(*args, **kwargs):
        pass
    
    
    def glPixelTransferi(*args, **kwargs):
        pass
    
    
    def glPixelZoom(*args, **kwargs):
        pass
    
    
    def glPointParameterf(*args, **kwargs):
        pass
    
    
    def glPointParameterfv(*args, **kwargs):
        pass
    
    
    def glPointSize(*args, **kwargs):
        pass
    
    
    def glPolygonMode(*args, **kwargs):
        pass
    
    
    def glPolygonOffset(*args, **kwargs):
        pass
    
    
    def glPolygonStipple(*args, **kwargs):
        pass
    
    
    def glPopAttrib(*args, **kwargs):
        pass
    
    
    def glPopClientAttrib(*args, **kwargs):
        pass
    
    
    def glPopMatrix(*args, **kwargs):
        pass
    
    
    def glPopName(*args, **kwargs):
        pass
    
    
    def glPrimitiveRestartIndexNV(*args, **kwargs):
        pass
    
    
    def glPrimitiveRestartNV(*args, **kwargs):
        pass
    
    
    def glPrioritizeTextures(*args, **kwargs):
        pass
    
    
    def glProgramEnvParameter4d(*args, **kwargs):
        pass
    
    
    def glProgramEnvParameter4dv(*args, **kwargs):
        pass
    
    
    def glProgramEnvParameter4f(*args, **kwargs):
        pass
    
    
    def glProgramEnvParameter4fv(*args, **kwargs):
        pass
    
    
    def glProgramLocalParameter4d(*args, **kwargs):
        pass
    
    
    def glProgramLocalParameter4dv(*args, **kwargs):
        pass
    
    
    def glProgramLocalParameter4f(*args, **kwargs):
        pass
    
    
    def glProgramLocalParameter4fv(*args, **kwargs):
        pass
    
    
    def glProgramParameter4dNV(*args, **kwargs):
        pass
    
    
    def glProgramParameter4dvNV(*args, **kwargs):
        pass
    
    
    def glProgramParameter4fNV(*args, **kwargs):
        pass
    
    
    def glProgramParameter4fvNV(*args, **kwargs):
        pass
    
    
    def glProgramParameters4dvNV(*args, **kwargs):
        pass
    
    
    def glProgramParameters4fvNV(*args, **kwargs):
        pass
    
    
    def glProgramString(*args, **kwargs):
        pass
    
    
    def glPushAttrib(*args, **kwargs):
        pass
    
    
    def glPushClientAttrib(*args, **kwargs):
        pass
    
    
    def glPushMatrix(*args, **kwargs):
        pass
    
    
    def glPushName(*args, **kwargs):
        pass
    
    
    def glRasterPos2d(*args, **kwargs):
        pass
    
    
    def glRasterPos2dv(*args, **kwargs):
        pass
    
    
    def glRasterPos2f(*args, **kwargs):
        pass
    
    
    def glRasterPos2fv(*args, **kwargs):
        pass
    
    
    def glRasterPos2i(*args, **kwargs):
        pass
    
    
    def glRasterPos2iv(*args, **kwargs):
        pass
    
    
    def glRasterPos2s(*args, **kwargs):
        pass
    
    
    def glRasterPos2sv(*args, **kwargs):
        pass
    
    
    def glRasterPos3d(*args, **kwargs):
        pass
    
    
    def glRasterPos3dv(*args, **kwargs):
        pass
    
    
    def glRasterPos3f(*args, **kwargs):
        pass
    
    
    def glRasterPos3fv(*args, **kwargs):
        pass
    
    
    def glRasterPos3i(*args, **kwargs):
        pass
    
    
    def glRasterPos3iv(*args, **kwargs):
        pass
    
    
    def glRasterPos3s(*args, **kwargs):
        pass
    
    
    def glRasterPos3sv(*args, **kwargs):
        pass
    
    
    def glRasterPos4d(*args, **kwargs):
        pass
    
    
    def glRasterPos4dv(*args, **kwargs):
        pass
    
    
    def glRasterPos4f(*args, **kwargs):
        pass
    
    
    def glRasterPos4fv(*args, **kwargs):
        pass
    
    
    def glRasterPos4i(*args, **kwargs):
        pass
    
    
    def glRasterPos4iv(*args, **kwargs):
        pass
    
    
    def glRasterPos4s(*args, **kwargs):
        pass
    
    
    def glRasterPos4sv(*args, **kwargs):
        pass
    
    
    def glReadBuffer(*args, **kwargs):
        pass
    
    
    def glReadPixels(*args, **kwargs):
        pass
    
    
    def glRectd(*args, **kwargs):
        pass
    
    
    def glRectdv(*args, **kwargs):
        pass
    
    
    def glRectf(*args, **kwargs):
        pass
    
    
    def glRectfv(*args, **kwargs):
        pass
    
    
    def glRecti(*args, **kwargs):
        pass
    
    
    def glRectiv(*args, **kwargs):
        pass
    
    
    def glRects(*args, **kwargs):
        pass
    
    
    def glRectsv(*args, **kwargs):
        pass
    
    
    def glRenderMode(*args, **kwargs):
        pass
    
    
    def glRenderbufferStorageEXT(*args, **kwargs):
        pass
    
    
    def glRequestResidentProgramsNV(*args, **kwargs):
        pass
    
    
    def glRotated(*args, **kwargs):
        pass
    
    
    def glRotatef(*args, **kwargs):
        pass
    
    
    def glSampleCoverage(*args, **kwargs):
        pass
    
    
    def glSampleMapATI(*args, **kwargs):
        pass
    
    
    def glScaled(*args, **kwargs):
        pass
    
    
    def glScalef(*args, **kwargs):
        pass
    
    
    def glScissor(*args, **kwargs):
        pass
    
    
    def glSecondaryColor3bEXT(*args, **kwargs):
        pass
    
    
    def glSecondaryColor3bvEXT(*args, **kwargs):
        pass
    
    
    def glSecondaryColor3dEXT(*args, **kwargs):
        pass
    
    
    def glSecondaryColor3dvEXT(*args, **kwargs):
        pass
    
    
    def glSecondaryColor3fEXT(*args, **kwargs):
        pass
    
    
    def glSecondaryColor3fvEXT(*args, **kwargs):
        pass
    
    
    def glSecondaryColor3iEXT(*args, **kwargs):
        pass
    
    
    def glSecondaryColor3ivEXT(*args, **kwargs):
        pass
    
    
    def glSecondaryColor3sEXT(*args, **kwargs):
        pass
    
    
    def glSecondaryColor3svEXT(*args, **kwargs):
        pass
    
    
    def glSecondaryColor3ubEXT(*args, **kwargs):
        pass
    
    
    def glSecondaryColor3ubvEXT(*args, **kwargs):
        pass
    
    
    def glSecondaryColor3uiEXT(*args, **kwargs):
        pass
    
    
    def glSecondaryColor3uivEXT(*args, **kwargs):
        pass
    
    
    def glSecondaryColor3usEXT(*args, **kwargs):
        pass
    
    
    def glSecondaryColor3usvEXT(*args, **kwargs):
        pass
    
    
    def glSecondaryColorPointerEXT(*args, **kwargs):
        pass
    
    
    def glSelectBuffer(*args, **kwargs):
        pass
    
    
    def glSetFenceNV(*args, **kwargs):
        pass
    
    
    def glSetFragmentShaderConstantATI(*args, **kwargs):
        pass
    
    
    def glSetInvariantEXT(*args, **kwargs):
        pass
    
    
    def glSetLocalConstantEXT(*args, **kwargs):
        pass
    
    
    def glShadeModel(*args, **kwargs):
        pass
    
    
    def glShaderOp1EXT(*args, **kwargs):
        pass
    
    
    def glShaderOp2EXT(*args, **kwargs):
        pass
    
    
    def glShaderOp3EXT(*args, **kwargs):
        pass
    
    
    def glShaderSourceARB(*args, **kwargs):
        pass
    
    
    def glStencilFunc(*args, **kwargs):
        pass
    
    
    def glStencilMask(*args, **kwargs):
        pass
    
    
    def glStencilOp(*args, **kwargs):
        pass
    
    
    def glSwizzleEXT(*args, **kwargs):
        pass
    
    
    def glTestFenceNV(*args, **kwargs):
        pass
    
    
    def glTexCoord1d(*args, **kwargs):
        pass
    
    
    def glTexCoord1dv(*args, **kwargs):
        pass
    
    
    def glTexCoord1f(*args, **kwargs):
        pass
    
    
    def glTexCoord1fv(*args, **kwargs):
        pass
    
    
    def glTexCoord1i(*args, **kwargs):
        pass
    
    
    def glTexCoord1iv(*args, **kwargs):
        pass
    
    
    def glTexCoord1s(*args, **kwargs):
        pass
    
    
    def glTexCoord1sv(*args, **kwargs):
        pass
    
    
    def glTexCoord2d(*args, **kwargs):
        pass
    
    
    def glTexCoord2dv(*args, **kwargs):
        pass
    
    
    def glTexCoord2f(*args, **kwargs):
        pass
    
    
    def glTexCoord2fv(*args, **kwargs):
        pass
    
    
    def glTexCoord2i(*args, **kwargs):
        pass
    
    
    def glTexCoord2iv(*args, **kwargs):
        pass
    
    
    def glTexCoord2s(*args, **kwargs):
        pass
    
    
    def glTexCoord2sv(*args, **kwargs):
        pass
    
    
    def glTexCoord3d(*args, **kwargs):
        pass
    
    
    def glTexCoord3dv(*args, **kwargs):
        pass
    
    
    def glTexCoord3f(*args, **kwargs):
        pass
    
    
    def glTexCoord3fv(*args, **kwargs):
        pass
    
    
    def glTexCoord3i(*args, **kwargs):
        pass
    
    
    def glTexCoord3iv(*args, **kwargs):
        pass
    
    
    def glTexCoord3s(*args, **kwargs):
        pass
    
    
    def glTexCoord3sv(*args, **kwargs):
        pass
    
    
    def glTexCoord4d(*args, **kwargs):
        pass
    
    
    def glTexCoord4dv(*args, **kwargs):
        pass
    
    
    def glTexCoord4f(*args, **kwargs):
        pass
    
    
    def glTexCoord4fv(*args, **kwargs):
        pass
    
    
    def glTexCoord4i(*args, **kwargs):
        pass
    
    
    def glTexCoord4iv(*args, **kwargs):
        pass
    
    
    def glTexCoord4s(*args, **kwargs):
        pass
    
    
    def glTexCoord4sv(*args, **kwargs):
        pass
    
    
    def glTexCoordPointer(*args, **kwargs):
        pass
    
    
    def glTexEnvf(*args, **kwargs):
        pass
    
    
    def glTexEnvfv(*args, **kwargs):
        pass
    
    
    def glTexEnvi(*args, **kwargs):
        pass
    
    
    def glTexEnviv(*args, **kwargs):
        pass
    
    
    def glTexGend(*args, **kwargs):
        pass
    
    
    def glTexGendv(*args, **kwargs):
        pass
    
    
    def glTexGenf(*args, **kwargs):
        pass
    
    
    def glTexGenfv(*args, **kwargs):
        pass
    
    
    def glTexGeni(*args, **kwargs):
        pass
    
    
    def glTexGeniv(*args, **kwargs):
        pass
    
    
    def glTexImage1D(*args, **kwargs):
        pass
    
    
    def glTexImage2D(*args, **kwargs):
        pass
    
    
    def glTexImage3D(*args, **kwargs):
        pass
    
    
    def glTexParameterf(*args, **kwargs):
        pass
    
    
    def glTexParameterfv(*args, **kwargs):
        pass
    
    
    def glTexParameteri(*args, **kwargs):
        pass
    
    
    def glTexParameteriv(*args, **kwargs):
        pass
    
    
    def glTexSubImage1D(*args, **kwargs):
        pass
    
    
    def glTexSubImage2D(*args, **kwargs):
        pass
    
    
    def glTexSubImage3D(*args, **kwargs):
        pass
    
    
    def glTrackMatrixNV(*args, **kwargs):
        pass
    
    
    def glTranslated(*args, **kwargs):
        pass
    
    
    def glTranslatef(*args, **kwargs):
        pass
    
    
    def glUniform1fARB(*args, **kwargs):
        pass
    
    
    def glUniform1fvARB(*args, **kwargs):
        pass
    
    
    def glUniform1iARB(*args, **kwargs):
        pass
    
    
    def glUniform1ivARB(*args, **kwargs):
        pass
    
    
    def glUniform2fARB(*args, **kwargs):
        pass
    
    
    def glUniform2fvARB(*args, **kwargs):
        pass
    
    
    def glUniform2iARB(*args, **kwargs):
        pass
    
    
    def glUniform2ivARB(*args, **kwargs):
        pass
    
    
    def glUniform3fARB(*args, **kwargs):
        pass
    
    
    def glUniform3fvARB(*args, **kwargs):
        pass
    
    
    def glUniform3iARB(*args, **kwargs):
        pass
    
    
    def glUniform3ivARB(*args, **kwargs):
        pass
    
    
    def glUniform4fARB(*args, **kwargs):
        pass
    
    
    def glUniform4fvARB(*args, **kwargs):
        pass
    
    
    def glUniform4iARB(*args, **kwargs):
        pass
    
    
    def glUniform4ivARB(*args, **kwargs):
        pass
    
    
    def glUniformMatrix2fvARB(*args, **kwargs):
        pass
    
    
    def glUniformMatrix3fvARB(*args, **kwargs):
        pass
    
    
    def glUniformMatrix4fvARB(*args, **kwargs):
        pass
    
    
    def glUnlockArraysEXT(*args, **kwargs):
        pass
    
    
    def glUnmapBufferARB(*args, **kwargs):
        pass
    
    
    def glUseProgramObjectARB(*args, **kwargs):
        pass
    
    
    def glValidateProgramARB(*args, **kwargs):
        pass
    
    
    def glVariantPointerEXT(*args, **kwargs):
        pass
    
    
    def glVariantbvEXT(*args, **kwargs):
        pass
    
    
    def glVariantdvEXT(*args, **kwargs):
        pass
    
    
    def glVariantfvEXT(*args, **kwargs):
        pass
    
    
    def glVariantivEXT(*args, **kwargs):
        pass
    
    
    def glVariantsvEXT(*args, **kwargs):
        pass
    
    
    def glVariantubvEXT(*args, **kwargs):
        pass
    
    
    def glVariantuivEXT(*args, **kwargs):
        pass
    
    
    def glVariantusvEXT(*args, **kwargs):
        pass
    
    
    def glVertex2d(*args, **kwargs):
        pass
    
    
    def glVertex2dv(*args, **kwargs):
        pass
    
    
    def glVertex2f(*args, **kwargs):
        pass
    
    
    def glVertex2fv(*args, **kwargs):
        pass
    
    
    def glVertex2i(*args, **kwargs):
        pass
    
    
    def glVertex2iv(*args, **kwargs):
        pass
    
    
    def glVertex2s(*args, **kwargs):
        pass
    
    
    def glVertex2sv(*args, **kwargs):
        pass
    
    
    def glVertex3d(*args, **kwargs):
        pass
    
    
    def glVertex3dv(*args, **kwargs):
        pass
    
    
    def glVertex3f(*args, **kwargs):
        pass
    
    
    def glVertex3fv(*args, **kwargs):
        pass
    
    
    def glVertex3i(*args, **kwargs):
        pass
    
    
    def glVertex3iv(*args, **kwargs):
        pass
    
    
    def glVertex3s(*args, **kwargs):
        pass
    
    
    def glVertex3sv(*args, **kwargs):
        pass
    
    
    def glVertex4d(*args, **kwargs):
        pass
    
    
    def glVertex4dv(*args, **kwargs):
        pass
    
    
    def glVertex4f(*args, **kwargs):
        pass
    
    
    def glVertex4fv(*args, **kwargs):
        pass
    
    
    def glVertex4i(*args, **kwargs):
        pass
    
    
    def glVertex4iv(*args, **kwargs):
        pass
    
    
    def glVertex4s(*args, **kwargs):
        pass
    
    
    def glVertex4sv(*args, **kwargs):
        pass
    
    
    def glVertexArrayRangeNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib1d(*args, **kwargs):
        pass
    
    
    def glVertexAttrib1dNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib1dv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib1dvNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib1f(*args, **kwargs):
        pass
    
    
    def glVertexAttrib1fNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib1fv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib1fvNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib1s(*args, **kwargs):
        pass
    
    
    def glVertexAttrib1sNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib1sv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib1svNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib2d(*args, **kwargs):
        pass
    
    
    def glVertexAttrib2dNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib2dv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib2dvNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib2f(*args, **kwargs):
        pass
    
    
    def glVertexAttrib2fNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib2fv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib2fvNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib2s(*args, **kwargs):
        pass
    
    
    def glVertexAttrib2sNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib2sv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib2svNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib3d(*args, **kwargs):
        pass
    
    
    def glVertexAttrib3dNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib3dv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib3dvNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib3f(*args, **kwargs):
        pass
    
    
    def glVertexAttrib3fNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib3fv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib3fvNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib3s(*args, **kwargs):
        pass
    
    
    def glVertexAttrib3sNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib3sv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib3svNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4Nbv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4Niv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4Nsv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4Nub(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4Nubv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4Nuiv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4Nusv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4bv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4d(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4dNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4dv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4dvNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4f(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4fNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4fv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4fvNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4iv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4s(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4sNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4sv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4svNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4ubNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4ubv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4ubvNV(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4uiv(*args, **kwargs):
        pass
    
    
    def glVertexAttrib4usv(*args, **kwargs):
        pass
    
    
    def glVertexAttribPointer(*args, **kwargs):
        pass
    
    
    def glVertexAttribPointerNV(*args, **kwargs):
        pass
    
    
    def glVertexAttribs1dvNV(*args, **kwargs):
        pass
    
    
    def glVertexAttribs1fvNV(*args, **kwargs):
        pass
    
    
    def glVertexAttribs1svNV(*args, **kwargs):
        pass
    
    
    def glVertexAttribs2dvNV(*args, **kwargs):
        pass
    
    
    def glVertexAttribs2fvNV(*args, **kwargs):
        pass
    
    
    def glVertexAttribs2svNV(*args, **kwargs):
        pass
    
    
    def glVertexAttribs3dvNV(*args, **kwargs):
        pass
    
    
    def glVertexAttribs3fvNV(*args, **kwargs):
        pass
    
    
    def glVertexAttribs3svNV(*args, **kwargs):
        pass
    
    
    def glVertexAttribs4dvNV(*args, **kwargs):
        pass
    
    
    def glVertexAttribs4fvNV(*args, **kwargs):
        pass
    
    
    def glVertexAttribs4svNV(*args, **kwargs):
        pass
    
    
    def glVertexAttribs4ubvNV(*args, **kwargs):
        pass
    
    
    def glVertexPointer(*args, **kwargs):
        pass
    
    
    def glVertexWeightPointerEXT(*args, **kwargs):
        pass
    
    
    def glVertexWeightfEXT(*args, **kwargs):
        pass
    
    
    def glVertexWeightfvEXT(*args, **kwargs):
        pass
    
    
    def glViewport(*args, **kwargs):
        pass
    
    
    def glWriteMaskEXT(*args, **kwargs):
        pass
    
    
    def maxTextureSize(*args, **kwargs):
        pass
    
    
    def maxVertexAttributes(*args, **kwargs):
        pass
    
    
    def numTexImageUnits(*args, **kwargs):
        pass
    
    
    def numTexInterpolants(*args, **kwargs):
        pass
    
    
    def numTexUnits(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    kMGL_Version11 = None
    
    
    kMGL_Version12 = None
    
    
    kMGL_Version121 = None
    
    
    kMGL_Version13 = None
    
    
    kMGL_Version14 = None
    
    
    kMGL_Version15 = None
    
    
    kMGL_Version20 = None


class MSwatchRenderRegister(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def registerSwatchRender(*args, **kwargs):
        pass
    
    
    def unregisterSwatchRender(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MRenderUtil(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def convertPsdFile(*args, **kwargs):
        pass
    
    
    def diffuseReflectance(*args, **kwargs):
        pass
    
    
    def exactFileTextureName(*args, **kwargs):
        pass
    
    
    def exactImagePlaneFileName(*args, **kwargs):
        pass
    
    
    def generatingIprFile(*args, **kwargs):
        pass
    
    
    def getCommonRenderSettings(*args, **kwargs):
        pass
    
    
    def hemisphereCoverage(*args, **kwargs):
        pass
    
    
    def inCurrentRenderLayer(*args, **kwargs):
        pass
    
    
    def lightAttenuation(*args, **kwargs):
        pass
    
    
    def mainBeautyPassCustomTokenString(*args, **kwargs):
        pass
    
    
    def mainBeautyPassName(*args, **kwargs):
        pass
    
    
    def maximumSpecularReflection(*args, **kwargs):
        pass
    
    
    def mayaRenderState(*args, **kwargs):
        pass
    
    
    def raytrace(*args, **kwargs):
        pass
    
    
    def raytraceFirstGeometryIntersections(*args, **kwargs):
        pass
    
    
    def relativeFileName(*args, **kwargs):
        pass
    
    
    def renderObjectItem(*args, **kwargs):
        pass
    
    
    def renderPass(*args, **kwargs):
        pass
    
    
    def sampleShadingNetwork(*args, **kwargs):
        pass
    
    
    def sendRenderProgressInfo(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    kAll = None
    
    
    kAmbientOnly = None
    
    
    kBatchRender = None
    
    
    kColorOnly = None
    
    
    kDiffuseOnly = None
    
    
    kHardwareRender = None
    
    
    kInteractiveRender = None
    
    
    kIprRender = None
    
    
    kNotRendering = None
    
    
    kShadowOnly = None
    
    
    kSpecularOnly = None


class MHwrCallback(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def deviceDeleted(*args, **kwargs):
        pass
    
    
    def deviceLost(*args, **kwargs):
        pass
    
    
    def deviceNew(*args, **kwargs):
        pass
    
    
    def deviceReset(*args, **kwargs):
        pass
    
    
    def addCallback(*args, **kwargs):
        pass
    
    
    def removeCallback(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MVaryingParameter(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def addElement(*args, **kwargs):
        pass
    
    
    def assign(*args, **kwargs):
        pass
    
    
    def getBuffer(*args, **kwargs):
        pass
    
    
    def getElement(*args, **kwargs):
        pass
    
    
    def getElementSize(*args, **kwargs):
        pass
    
    
    def getMaximumStride(*args, **kwargs):
        pass
    
    
    def getSourceSetName(*args, **kwargs):
        pass
    
    
    def getSourceType(*args, **kwargs):
        pass
    
    
    def name(*args, **kwargs):
        pass
    
    
    def numElements(*args, **kwargs):
        pass
    
    
    def removeElements(*args, **kwargs):
        pass
    
    
    def semantic(*args, **kwargs):
        pass
    
    
    def setSource(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kBinormal = None
    
    
    kColor = None
    
    
    kFloat = None
    
    
    kInvalidParameter = None
    
    
    kNoSemantic = None
    
    
    kNormal = None
    
    
    kPosition = None
    
    
    kStructure = None
    
    
    kTangent = None
    
    
    kTexCoord = None
    
    
    kWeight = None


class MStencilOpDesc(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def setDefaults(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    stencilDepthFailOp = None
    
    stencilFailOp = None
    
    stencilFunc = None
    
    stencilPassOp = None
    
    thisown = None
    
    __swig_destroy__ = None


class MRasterizerStateDesc(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def setDefaults(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    antialiasedLineEnable = None
    
    cullMode = None
    
    depthBias = None
    
    depthBiasClamp = None
    
    depthBiasIsFloat = None
    
    depthClipEnable = None
    
    fillMode = None
    
    frontCounterClockwise = None
    
    multiSampleEnable = None
    
    scissorEnable = None
    
    slopeScaledDepthBias = None
    
    thisown = None
    
    __swig_destroy__ = None


class MRenderer(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def activeRenderOverride(*args, **kwargs):
        pass
    
    
    def deregisterOverride(*args, **kwargs):
        pass
    
    
    def drawAPIIsOpenGL(*args, **kwargs):
        pass
    
    
    def drawAPIVersion(*args, **kwargs):
        pass
    
    
    def findRenderOverride(*args, **kwargs):
        pass
    
    
    def getRenderTargetManager(*args, **kwargs):
        pass
    
    
    def getShaderManager(*args, **kwargs):
        pass
    
    
    def getTextureManager(*args, **kwargs):
        pass
    
    
    def outputTargetSize(*args, **kwargs):
        pass
    
    
    def registerOverride(*args, **kwargs):
        pass
    
    
    def renderOverrideCount(*args, **kwargs):
        pass
    
    
    def renderOverrideName(*args, **kwargs):
        pass
    
    
    def setRenderOverrideName(*args, **kwargs):
        pass
    
    
    def setGeometryDrawDirty(*args, **kwargs):
        pass
    
    
    def theRenderer(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None


class MTextureAssignment(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    texture = None
    
    thisown = None
    
    __swig_destroy__ = None


class MLightLinks(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def getIgnoredLights(*args, **kwargs):
        pass
    
    
    def getIgnoredObjects(*args, **kwargs):
        pass
    
    
    def getLinkedLights(*args, **kwargs):
        pass
    
    
    def getLinkedObjects(*args, **kwargs):
        pass
    
    
    def getShadowIgnoredLights(*args, **kwargs):
        pass
    
    
    def getShadowIgnoredObjects(*args, **kwargs):
        pass
    
    
    def getShadowLinkedLights(*args, **kwargs):
        pass
    
    
    def getShadowLinkedObjects(*args, **kwargs):
        pass
    
    
    def parseLinks(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MRenderTargetAssignment(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    target = None
    
    thisown = None
    
    __swig_destroy__ = None


class MGeometry(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def createIndexBuffer(*args, **kwargs):
        pass
    
    
    def createVertexBuffer(*args, **kwargs):
        pass
    
    
    def deleteIndexBuffer(*args, **kwargs):
        pass
    
    
    def deleteVertexBuffer(*args, **kwargs):
        pass
    
    
    def indexBuffer(*args, **kwargs):
        pass
    
    
    def indexBufferCount(*args, **kwargs):
        pass
    
    
    def vertexBuffer(*args, **kwargs):
        pass
    
    
    def vertexBufferCount(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    def dataTypeString(*args, **kwargs):
        pass
    
    
    def drawModeString(*args, **kwargs):
        pass
    
    
    def primitiveString(*args, **kwargs):
        pass
    
    
    def semanticString(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    kAll = None
    
    
    kBitangent = None
    
    
    kChar = None
    
    
    kColor = None
    
    
    kDouble = None
    
    
    kFloat = None
    
    
    kInt16 = None
    
    
    kInt32 = None
    
    
    kInvalidPrimitive = None
    
    
    kInvalidSemantic = None
    
    
    kInvalidType = None
    
    
    kLineStrip = None
    
    
    kLines = None
    
    
    kNormal = None
    
    
    kPoints = None
    
    
    kPosition = None
    
    
    kShaded = None
    
    
    kTangent = None
    
    
    kTexture = None
    
    
    kTriangleStrip = None
    
    
    kTriangles = None
    
    
    kUnsignedChar = None
    
    
    kUnsignedInt16 = None
    
    
    kUnsignedInt32 = None
    
    
    kWireframe = None


class MIndexBuffer(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def acquire(*args, **kwargs):
        pass
    
    
    def commit(*args, **kwargs):
        pass
    
    
    def dataType(*args, **kwargs):
        pass
    
    
    def resourceHandle(*args, **kwargs):
        pass
    
    
    def size(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None


class MShaderCompileMacro(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    mDefinition = None
    
    mName = None
    
    thisown = None
    
    __swig_destroy__ = None


class MShaderInstance(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def parameterList(*args, **kwargs):
        pass
    
    
    def parameterType(*args, **kwargs):
        pass
    
    
    def setParameter(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kBoolean = None
    
    
    kFloat = None
    
    
    kFloat2 = None
    
    
    kFloat3 = None
    
    
    kFloat4 = None
    
    
    kInteger = None
    
    
    kInvalid = None
    
    
    kTexture1 = None
    
    
    kTexture2 = None
    
    
    kTexture3 = None
    
    
    kTextureCube = None


class MTargetBlendDesc(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def setDefaults(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    alphaBlendOperation = None
    
    alphaDestinationBlend = None
    
    alphaSourceBlend = None
    
    blendEnable = None
    
    blendOperation = None
    
    destinationBlend = None
    
    sourceBlend = None
    
    targetWriteMask = None
    
    thisown = None
    
    __swig_destroy__ = None


class MVertexBufferDescriptorList(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def append(*args, **kwargs):
        pass
    
    
    def clear(*args, **kwargs):
        pass
    
    
    def getDescriptor(*args, **kwargs):
        pass
    
    
    def length(*args, **kwargs):
        pass
    
    
    def removeAt(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MRenderShadowData(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def worldToZbuffer(*args, **kwargs):
        pass
    
    
    def zbufferToWorld(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    depthMaps = None
    
    internalData = None
    
    lightPosition = None
    
    lightType = None
    
    midDistMaps = None
    
    perspective = None
    
    perspectiveMatrix = None
    
    projectionMatrix = None
    
    shadowResX = None
    
    shadowResY = None
    
    thisown = None
    
    useMidDistMap = None
    
    __swig_destroy__ = None
    
    
    kDirectional = None
    
    
    kInvalid = None
    
    
    kPoint = None
    
    
    kSpot = None


class MCommonRenderSettingsData(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def getBufferName(*args, **kwargs):
        pass
    
    
    def getImageName(*args, **kwargs):
        pass
    
    
    def isAnimated(*args, **kwargs):
        pass
    
    
    def isMovieFormat(*args, **kwargs):
        pass
    
    
    def setFieldName(*args, **kwargs):
        pass
    
    
    def setPassName(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    customExt = None
    
    customImageFormat = None
    
    deviceAspectRatio = None
    
    dotPerInch = None
    
    enableDefaultLight = None
    
    frameBy = None
    
    frameEnd = None
    
    framePadding = None
    
    frameStart = None
    
    height = None
    
    imageFormat = None
    
    name = None
    
    namePattern = None
    
    namingScheme = None
    
    pixelAspectRatio = None
    
    postMel = None
    
    postRenderLayerMel = None
    
    postRenderMel = None
    
    preMel = None
    
    preRenderLayerMel = None
    
    preRenderMel = None
    
    renderAll = None
    
    renumberBy = None
    
    renumberFrames = None
    
    renumberStart = None
    
    thisown = None
    
    useCustomExt = None
    
    width = None
    
    __swig_destroy__ = None
    
    
    kFullPathImage = None
    
    
    kFullPathTmp = None
    
    
    kRelativePath = None


class MDrawContext(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def getDepthRange(*args, **kwargs):
        pass
    
    
    def getDisplayStyle(*args, **kwargs):
        pass
    
    
    def getLightInformation(*args, **kwargs):
        pass
    
    
    def getMatrix(*args, **kwargs):
        pass
    
    
    def getRenderTargetSize(*args, **kwargs):
        pass
    
    
    def getSceneBox(*args, **kwargs):
        pass
    
    
    def getStateManager(*args, **kwargs):
        pass
    
    
    def getTuple(*args, **kwargs):
        pass
    
    
    def getViewportDimensions(*args, **kwargs):
        pass
    
    
    def numberOfActiveLights(*args, **kwargs):
        pass
    
    
    def viewDirectionAlongNegZ(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    kGouraudShaded = None
    
    
    kProjectionInverseMtx = None
    
    
    kProjectionMtx = None
    
    
    kProjectionTranposeMtx = None
    
    
    kProjectionTranspInverseMtx = None
    
    
    kViewDirection = None
    
    
    kViewInverseMtx = None
    
    
    kViewMtx = None
    
    
    kViewPosition = None
    
    
    kViewProjInverseMtx = None
    
    
    kViewProjMtx = None
    
    
    kViewProjTranposeMtx = None
    
    
    kViewProjTranspInverseMtx = None
    
    
    kViewRight = None
    
    
    kViewTranspInverseMtx = None
    
    
    kViewTransposeMtx = None
    
    
    kViewUp = None
    
    
    kWireFrame = None
    
    
    kWorldInverseMtx = None
    
    
    kWorldMtx = None
    
    
    kWorldTranspInverseMtx = None
    
    
    kWorldTransposeMtx = None
    
    
    kWorldViewInverseMtx = None
    
    
    kWorldViewMtx = None
    
    
    kWorldViewProjInverseMtx = None
    
    
    kWorldViewProjMtx = None
    
    
    kWorldViewProjTranspInverseMtx = None
    
    
    kWorldViewProjTransposeMtx = None
    
    
    kWorldViewTranspInverseMtx = None
    
    
    kWorldViewTransposeMtx = None


class MGeometryPrimitive(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def data(*args, **kwargs):
        pass
    
    
    def dataType(*args, **kwargs):
        pass
    
    
    def drawPrimitiveType(*args, **kwargs):
        pass
    
    
    def elementCount(*args, **kwargs):
        pass
    
    
    def uniqueID(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kInvalidIndexType = None
    
    
    kLineLoop = None
    
    
    kLineStrip = None
    
    
    kLines = None
    
    
    kMaxDrawPrimitiveTypeIndex = None
    
    
    kPoints = None
    
    
    kPolygon = None
    
    
    kQuadStrip = None
    
    
    kQuads = None
    
    
    kTriangleFan = None
    
    
    kTriangleStrip = None
    
    
    kTriangles = None


class MStateManager(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def acquireBlendState(*args, **kwargs):
        pass
    
    
    def acquireDepthStencilState(*args, **kwargs):
        pass
    
    
    def acquireRasterizerState(*args, **kwargs):
        pass
    
    
    def acquireSamplerState(*args, **kwargs):
        pass
    
    
    def getBlendState(*args, **kwargs):
        pass
    
    
    def getDepthStencilState(*args, **kwargs):
        pass
    
    
    def getMaxSamplerCount(*args, **kwargs):
        pass
    
    
    def getRasterizerState(*args, **kwargs):
        pass
    
    
    def getSamplerState(*args, **kwargs):
        pass
    
    
    def setBlendState(*args, **kwargs):
        pass
    
    
    def setDepthStencilState(*args, **kwargs):
        pass
    
    
    def setRasterizerState(*args, **kwargs):
        pass
    
    
    def setSamplerState(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    kCompareAlways = None
    
    
    kCompareEqual = None
    
    
    kCompareGreater = None
    
    
    kCompareGreaterEqual = None
    
    
    kCompareLess = None
    
    
    kCompareLessEqual = None
    
    
    kCompareNever = None
    
    
    kCompareNotEqual = None
    
    
    kDomainShader = None
    
    
    kGeometryShader = None
    
    
    kHullShader = None
    
    
    kNoShader = None
    
    
    kPixelShader = None
    
    
    kVertexShader = None


class MUniformParameter(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def assign(*args, **kwargs):
        pass
    
    
    def getAsBool(*args, **kwargs):
        pass
    
    
    def getAsFloat(*args, **kwargs):
        pass
    
    
    def getAsFloatArray(*args, **kwargs):
        pass
    
    
    def getAsInt(*args, **kwargs):
        pass
    
    
    def getAsString(*args, **kwargs):
        pass
    
    
    def getSource(*args, **kwargs):
        pass
    
    
    def hasChanged(*args, **kwargs):
        pass
    
    
    def isATexture(*args, **kwargs):
        pass
    
    
    def name(*args, **kwargs):
        pass
    
    
    def numColumns(*args, **kwargs):
        pass
    
    
    def numElements(*args, **kwargs):
        pass
    
    
    def numRows(*args, **kwargs):
        pass
    
    
    def semantic(*args, **kwargs):
        pass
    
    
    def setAsBool(*args, **kwargs):
        pass
    
    
    def setAsFloat(*args, **kwargs):
        pass
    
    
    def setAsFloatArray(*args, **kwargs):
        pass
    
    
    def setAsInt(*args, **kwargs):
        pass
    
    
    def setAsString(*args, **kwargs):
        pass
    
    
    def setDirty(*args, **kwargs):
        pass
    
    
    def type(*args, **kwargs):
        pass
    
    
    def userData(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kSemanticBump = None
    
    
    kSemanticBumpTexture = None
    
    
    kSemanticColor = None
    
    
    kSemanticColorTexture = None
    
    
    kSemanticEnvironment = None
    
    
    kSemanticNormal = None
    
    
    kSemanticNormalTexture = None
    
    
    kSemanticNormalizationTexture = None
    
    
    kSemanticObjectDir = None
    
    
    kSemanticObjectPos = None
    
    
    kSemanticProjectionDir = None
    
    
    kSemanticProjectionInverseMatrix = None
    
    
    kSemanticProjectionInverseTransposeMatrix = None
    
    
    kSemanticProjectionMatrix = None
    
    
    kSemanticProjectionPos = None
    
    
    kSemanticTime = None
    
    
    kSemanticUnknown = None
    
    
    kSemanticViewDir = None
    
    
    kSemanticViewInverseMatrix = None
    
    
    kSemanticViewInverseTransposeMatrix = None
    
    
    kSemanticViewMatrix = None
    
    
    kSemanticViewPos = None
    
    
    kSemanticWorldDir = None
    
    
    kSemanticWorldInverseMatrix = None
    
    
    kSemanticWorldInverseTransposeMatrix = None
    
    
    kSemanticWorldMatrix = None
    
    
    kSemanticWorldPos = None
    
    
    kSemanticWorldViewInverseMatrix = None
    
    
    kSemanticWorldViewInverseTransposeMatrix = None
    
    
    kSemanticWorldViewMatrix = None
    
    
    kSemanticWorldViewProjectionInverseMatrix = None
    
    
    kSemanticWorldViewProjectionInverseTransposeMatrix = None
    
    
    kSemanticWorldViewProjectionMatrix = None
    
    
    kType1DTexture = None
    
    
    kType2DTexture = None
    
    
    kType3DTexture = None
    
    
    kTypeBool = None
    
    
    kTypeCubeTexture = None
    
    
    kTypeEnvTexture = None
    
    
    kTypeFloat = None
    
    
    kTypeInt = None
    
    
    kTypeString = None
    
    
    kTypeUnknown = None


class MRenderItemList(object):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def append(*args, **kwargs):
        pass
    
    
    def clear(*args, **kwargs):
        pass
    
    
    def indexOf(*args, **kwargs):
        pass
    
    
    def itemAt(*args, **kwargs):
        pass
    
    
    def length(*args, **kwargs):
        pass
    
    
    def removeAt(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None


class MGeometryList(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def addLast(*args, **kwargs):
        pass
    
    
    def cullMode(*args, **kwargs):
        pass
    
    
    def geometry(*args, **kwargs):
        pass
    
    
    def isDone(*args, **kwargs):
        pass
    
    
    def length(*args, **kwargs):
        pass
    
    
    def next(*args, **kwargs):
        pass
    
    
    def objectToWorldMatrix(*args, **kwargs):
        pass
    
    
    def path(*args, **kwargs):
        pass
    
    
    def projectionMatrix(*args, **kwargs):
        pass
    
    
    def reset(*args, **kwargs):
        pass
    
    
    def setCurrentElement(*args, **kwargs):
        pass
    
    
    def viewMatrix(*args, **kwargs):
        pass
    
    
    MSetupFlags = None
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kAll = None
    
    
    kCullCCW = None
    
    
    kCullCW = None
    
    
    kCullNone = None
    
    
    kCulling = None
    
    
    kFixedFunctionLighting = None
    
    
    kMatrices = None
    
    
    kNone = None


class MRenderTargetDescription(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def arraySliceCount(*args, **kwargs):
        pass
    
    
    def height(*args, **kwargs):
        pass
    
    
    def isCubeMap(*args, **kwargs):
        pass
    
    
    def multiSampleCount(*args, **kwargs):
        pass
    
    
    def name(*args, **kwargs):
        pass
    
    
    def rasterFormat(*args, **kwargs):
        pass
    
    
    def setArraySliceCount(*args, **kwargs):
        pass
    
    
    def setHeight(*args, **kwargs):
        pass
    
    
    def setIsCubeMap(*args, **kwargs):
        pass
    
    
    def setMultiSampleCount(*args, **kwargs):
        pass
    
    
    def setRasterFormat(*args, **kwargs):
        pass
    
    
    def setWidth(*args, **kwargs):
        pass
    
    
    def width(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None


class MDepthStencilStateDesc(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def setDefaults(*args, **kwargs):
        pass
    
    
    def className(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    backFace = None
    
    depthEnable = None
    
    depthFunc = None
    
    depthWriteEnable = None
    
    frontFace = None
    
    stencilEnable = None
    
    stencilReadMask = None
    
    stencilReferenceVal = None
    
    stencilWriteMask = None
    
    thisown = None
    
    __swig_destroy__ = None


class MGeometryData(object):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def collectionNumber(*args, **kwargs):
        pass
    
    
    def data(*args, **kwargs):
        pass
    
    
    def dataType(*args, **kwargs):
        pass
    
    
    def elementCount(*args, **kwargs):
        pass
    
    
    def elementSize(*args, **kwargs):
        pass
    
    
    def elementType(*args, **kwargs):
        pass
    
    
    def elementTypeSize(*args, **kwargs):
        pass
    
    
    def objectName(*args, **kwargs):
        pass
    
    
    def objectOwnsData(*args, **kwargs):
        pass
    
    
    def setCollectionNumber(*args, **kwargs):
        pass
    
    
    def setObjectOwnsData(*args, **kwargs):
        pass
    
    
    def uniqueID(*args, **kwargs):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kAPISupported = None
    
    
    kBiNormal = None
    
    
    kChar = None
    
    
    kColor = None
    
    
    kColorMask = None
    
    
    kDouble = None
    
    
    kFloat = None
    
    
    kFour = None
    
    
    kInt16 = None
    
    
    kInt32 = None
    
    
    kInvalidDataType = None
    
    
    kInvalidElementSize = None
    
    
    kInvalidElementType = None
    
    
    kMaxDataTypeIndex = None
    
    
    kNormal = None
    
    
    kOne = None
    
    
    kPosition = None
    
    
    kPrimitiveCenter = None
    
    
    kTangent = None
    
    
    kTexCoord = None
    
    
    kThree = None
    
    
    kTwo = None
    
    
    kUnsignedChar = None
    
    
    kUnsignedInt16 = None
    
    
    kUnsignedInt32 = None
    
    
    kUserData = None
    
    
    kVelocity = None
    
    
    kWeight = None


class MQuadRender(MRenderOperation):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def clearOperation(*args, **kwargs):
        pass
    
    
    def shader(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MSceneRender(MRenderOperation):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def cameraOverride(*args, **kwargs):
        pass
    
    
    def clearOperation(*args, **kwargs):
        pass
    
    
    def cullingOverride(*args, **kwargs):
        pass
    
    
    def displayModeOverride(*args, **kwargs):
        pass
    
    
    def lightModeOverride(*args, **kwargs):
        pass
    
    
    def objectSetOverride(*args, **kwargs):
        pass
    
    
    def objectTypeExclusions(*args, **kwargs):
        pass
    
    
    def postRender(*args, **kwargs):
        pass
    
    
    def preRender(*args, **kwargs):
        pass
    
    
    def renderFilterOverride(*args, **kwargs):
        pass
    
    
    def shaderOverride(*args, **kwargs):
        pass
    
    
    def shadowEnableOverride(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None
    
    
    kAmbientLight = None
    
    
    kCullBackFaces = None
    
    
    kCullFrontFaces = None
    
    
    kCullNone = None
    
    
    kDefaultMaterial = None
    
    
    kExcludeAll = None
    
    
    kExcludeCVs = None
    
    
    kExcludeCameras = None
    
    
    kExcludeDeformers = None
    
    
    kExcludeDimensions = None
    
    
    kExcludeDynamicConstraints = None
    
    
    kExcludeDynamics = None
    
    
    kExcludeFluids = None
    
    
    kExcludeFollicles = None
    
    
    kExcludeGrid = None
    
    
    kExcludeHairSystems = None
    
    
    kExcludeHulls = None
    
    
    kExcludeIkHandles = None
    
    
    kExcludeImagePlane = None
    
    
    kExcludeJoints = None
    
    
    kExcludeLights = None
    
    
    kExcludeLocators = None
    
    
    kExcludeManipulators = None
    
    
    kExcludeMeshes = None
    
    
    kExcludeNCloths = None
    
    
    kExcludeNParticles = None
    
    
    kExcludeNRigids = None
    
    
    kExcludeNone = None
    
    
    kExcludeNurbsCurves = None
    
    
    kExcludeNurbsSurfaces = None
    
    
    kExcludePivots = None
    
    
    kExcludePlanes = None
    
    
    kExcludeSelectHandles = None
    
    
    kExcludeStrokes = None
    
    
    kExcludeSubdivSurfaces = None
    
    
    kExcludeTextures = None
    
    
    kLightDefault = None
    
    
    kNoCullingOverride = None
    
    
    kNoDisplayModeOverride = None
    
    
    kNoLightingModeOverride = None
    
    
    kNoSceneFilterOverride = None
    
    
    kRenderAllItems = None
    
    
    kRenderNonShadedItems = None
    
    
    kRenderShadedItems = None
    
    
    kSceneLights = None
    
    
    kShaded = None
    
    
    kWireFrame = None


class MHUDRender(MRenderOperation):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MPresentTarget(MRenderOperation):
    def __init__(self, *args):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def presentDepth(*args, **kwargs):
        pass
    
    
    def setPresentDepth(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MUserRenderOperation(MRenderOperation):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def cameraOverride(*args, **kwargs):
        pass
    
    
    def execute(*args, **kwargs):
        pass
    
    
    thisown = None
    
    __swig_destroy__ = None


class MClearOperation(MRenderOperation):
    def __init__(self):
        pass
    
    
    def __repr__(self):
        pass
    
    
    def clearColor(*args, **kwargs):
        pass
    
    
    def clearColor2(*args, **kwargs):
        pass
    
    
    def clearDepth(*args, **kwargs):
        pass
    
    
    def clearGradient(*args, **kwargs):
        pass
    
    
    def clearStencil(*args, **kwargs):
        pass
    
    
    def mask(*args, **kwargs):
        pass
    
    
    def setClearColor(*args, **kwargs):
        pass
    
    
    def setClearColor2(*args, **kwargs):
        pass
    
    
    def setClearDepth(*args, **kwargs):
        pass
    
    
    def setClearGradient(*args, **kwargs):
        pass
    
    
    def setClearStencil(*args, **kwargs):
        pass
    
    
    def setMask(*args, **kwargs):
        pass
    
    
    thisown = None
    
    kClearAll = None
    
    
    kClearColor = None
    
    
    kClearDepth = None
    
    
    kClearNone = None
    
    
    kClearStencil = None

def MBlendStateDesc_className(*args, **kwargs):
    pass


def MBlendStateDesc_swigregister(*args, **kwargs):
    pass


def MBlendState_className(*args, **kwargs):
    pass


def MBlendState_swigregister(*args, **kwargs):
    pass


def MCameraOverride_swigregister(*args, **kwargs):
    pass


def MClearOperation_swigregister(*args, **kwargs):
    pass


def MCommonRenderSettingsData_className(*args, **kwargs):
    pass


def MCommonRenderSettingsData_swigregister(*args, **kwargs):
    pass


def MD3D9Renderer_swigregister(*args, **kwargs):
    pass


def MD3D9Renderer_theRenderer(*args, **kwargs):
    pass


def MDepthStencilStateDesc_className(*args, **kwargs):
    pass


def MDepthStencilStateDesc_swigregister(*args, **kwargs):
    pass


def MDepthStencilState_className(*args, **kwargs):
    pass


def MDepthStencilState_swigregister(*args, **kwargs):
    pass


def MDrawContext_className(*args, **kwargs):
    pass


def MDrawContext_swigregister(*args, **kwargs):
    pass


def MDrawProcedureBase_swigregister(*args, **kwargs):
    pass


def MDrawRegistry_className(*args, **kwargs):
    pass


def MDrawRegistry_deregisterDrawOverrideCreator(*args, **kwargs):
    pass


def MDrawRegistry_deregisterGeometryOverrideCreator(*args, **kwargs):
    pass


def MDrawRegistry_deregisterShaderOverrideCreator(*args, **kwargs):
    pass


def MDrawRegistry_registerDrawOverrideCreator(*args, **kwargs):
    pass


def MDrawRegistry_registerGeometryOverrideCreator(*args, **kwargs):
    pass


def MDrawRegistry_registerShaderOverrideCreator(*args, **kwargs):
    pass


def MDrawRegistry_swigregister(*args, **kwargs):
    pass


def MFnImageSource_className(*args, **kwargs):
    pass


def MFnImageSource_swigregister(*args, **kwargs):
    pass


def MFnRenderLayer_className(*args, **kwargs):
    pass


def MFnRenderLayer_currentLayer(*args, **kwargs):
    pass


def MFnRenderLayer_defaultRenderLayer(*args, **kwargs):
    pass


def MFnRenderLayer_findLayerByName(*args, **kwargs):
    pass


def MFnRenderLayer_listAllRenderLayers(*args, **kwargs):
    pass


def MFnRenderLayer_swigregister(*args, **kwargs):
    pass


def MFnRenderPass_className(*args, **kwargs):
    pass


def MFnRenderPass_swigregister(*args, **kwargs):
    pass


def MGLFunctionTable_swigregister(*args, **kwargs):
    pass


def MGeometryData_swigregister(*args, **kwargs):
    pass


def MGeometryList_swigregister(*args, **kwargs):
    pass


def MGeometryManager_className(*args, **kwargs):
    pass


def MGeometryManager_dereferenceDefaultGeometry(*args, **kwargs):
    pass


def MGeometryManager_getGeometry(*args, **kwargs):
    pass


def MGeometryManager_referenceDefaultGeometry(*args, **kwargs):
    pass


def MGeometryManager_swigregister(*args, **kwargs):
    pass


def MGeometryPrimitive_swigregister(*args, **kwargs):
    pass


def MGeometryRequirements_className(*args, **kwargs):
    pass


def MGeometryRequirements_swigregister(*args, **kwargs):
    pass


def MGeometry_className(*args, **kwargs):
    pass


def MGeometry_dataTypeString(*args, **kwargs):
    pass


def MGeometry_drawModeString(*args, **kwargs):
    pass


def MGeometry_primitiveString(*args, **kwargs):
    pass


def MGeometry_semanticString(*args, **kwargs):
    pass


def MGeometry_swigregister(*args, **kwargs):
    pass


def MHUDRender_swigregister(*args, **kwargs):
    pass


def MHardwareRenderer_swigregister(*args, **kwargs):
    pass


def MHardwareRenderer_theRenderer(*args, **kwargs):
    pass


def MHwTextureManager_className(*args, **kwargs):
    pass


def MHwTextureManager_deregisterTextureFile(*args, **kwargs):
    pass


def MHwTextureManager_glBind(*args, **kwargs):
    pass


def MHwTextureManager_registerTextureFile(*args, **kwargs):
    pass


def MHwTextureManager_swigregister(*args, **kwargs):
    pass


def MHwTextureManager_textureFile(*args, **kwargs):
    pass


def MHwrCallback_addCallback(*args, **kwargs):
    pass


def MHwrCallback_removeCallback(*args, **kwargs):
    pass


def MHwrCallback_swigregister(*args, **kwargs):
    pass


def MIndexBuffer_className(*args, **kwargs):
    pass


def MIndexBuffer_swigregister(*args, **kwargs):
    pass


def MLightLinks_swigregister(*args, **kwargs):
    pass


def MPresentTarget_swigregister(*args, **kwargs):
    pass


def MQuadRender_swigregister(*args, **kwargs):
    pass


def MRasterizerStateDesc_className(*args, **kwargs):
    pass


def MRasterizerStateDesc_swigregister(*args, **kwargs):
    pass


def MRasterizerState_className(*args, **kwargs):
    pass


def MRasterizerState_swigregister(*args, **kwargs):
    pass


def MRenderCallback_addCallback(*args, **kwargs):
    pass


def MRenderCallback_removeCallback(*args, **kwargs):
    pass


def MRenderCallback_swigregister(*args, **kwargs):
    pass


def MRenderData_swigregister(*args, **kwargs):
    pass


def MRenderItemList_className(*args, **kwargs):
    pass


def MRenderItemList_swigregister(*args, **kwargs):
    pass


def MRenderItem_className(*args, **kwargs):
    pass


def MRenderItem_swigregister(*args, **kwargs):
    pass


def MRenderOperation_swigregister(*args, **kwargs):
    pass


def MRenderOverride_swigregister(*args, **kwargs):
    pass


def MRenderProfile_swigregister(*args, **kwargs):
    pass


def MRenderShadowData_swigregister(*args, **kwargs):
    pass


def MRenderTargetAssignment_swigregister(*args, **kwargs):
    pass


def MRenderTargetDescription_swigregister(*args, **kwargs):
    pass


def MRenderTargetManager_className(*args, **kwargs):
    pass


def MRenderTargetManager_swigregister(*args, **kwargs):
    pass


def MRenderTarget_className(*args, **kwargs):
    pass


def MRenderTarget_swigregister(*args, **kwargs):
    pass


def MRenderUtil_className(*args, **kwargs):
    pass


def MRenderUtil_convertPsdFile(*args, **kwargs):
    pass


def MRenderUtil_diffuseReflectance(*args, **kwargs):
    pass


def MRenderUtil_exactFileTextureName(*args, **kwargs):
    pass


def MRenderUtil_exactImagePlaneFileName(*args, **kwargs):
    pass


def MRenderUtil_generatingIprFile(*args, **kwargs):
    pass


def MRenderUtil_getCommonRenderSettings(*args, **kwargs):
    pass


def MRenderUtil_hemisphereCoverage(*args, **kwargs):
    pass


def MRenderUtil_inCurrentRenderLayer(*args, **kwargs):
    pass


def MRenderUtil_lightAttenuation(*args, **kwargs):
    pass


def MRenderUtil_mainBeautyPassCustomTokenString(*args, **kwargs):
    pass


def MRenderUtil_mainBeautyPassName(*args, **kwargs):
    pass


def MRenderUtil_maximumSpecularReflection(*args, **kwargs):
    pass


def MRenderUtil_mayaRenderState(*args, **kwargs):
    pass


def MRenderUtil_raytrace(*args, **kwargs):
    pass


def MRenderUtil_raytraceFirstGeometryIntersections(*args, **kwargs):
    pass


def MRenderUtil_relativeFileName(*args, **kwargs):
    pass


def MRenderUtil_renderObjectItem(*args, **kwargs):
    pass


def MRenderUtil_renderPass(*args, **kwargs):
    pass


def MRenderUtil_sampleShadingNetwork(*args, **kwargs):
    pass


def MRenderUtil_sendRenderProgressInfo(*args, **kwargs):
    pass


def MRenderUtil_swigregister(*args, **kwargs):
    pass


def MRenderView_className(*args, **kwargs):
    pass


def MRenderView_doesRenderEditorExist(*args, **kwargs):
    pass


def MRenderView_endRender(*args, **kwargs):
    pass


def MRenderView_getRenderRegion(*args, **kwargs):
    pass


def MRenderView_refresh(*args, **kwargs):
    pass


def MRenderView_setCurrentCamera(*args, **kwargs):
    pass


def MRenderView_startRegionRender(*args, **kwargs):
    pass


def MRenderView_startRender(*args, **kwargs):
    pass


def MRenderView_swigregister(*args, **kwargs):
    pass


def MRenderView_updatePixels(*args, **kwargs):
    pass


def MRenderer_setGeometryDrawDirty(*args, **kwargs):
    pass


def MRenderer_swigregister(*args, **kwargs):
    pass


def MRenderer_theRenderer(*args, **kwargs):
    pass


def MRenderingInfo_swigregister(*args, **kwargs):
    pass


def MSamplerStateDesc_className(*args, **kwargs):
    pass


def MSamplerStateDesc_swigregister(*args, **kwargs):
    pass


def MSamplerState_className(*args, **kwargs):
    pass


def MSamplerState_swigregister(*args, **kwargs):
    pass


def MSceneRender_swigregister(*args, **kwargs):
    pass


def MShaderCompileMacro_swigregister(*args, **kwargs):
    pass


def MShaderInstance_className(*args, **kwargs):
    pass


def MShaderInstance_swigregister(*args, **kwargs):
    pass


def MShaderManager_className(*args, **kwargs):
    pass


def MShaderManager_swigregister(*args, **kwargs):
    pass


def MStateManager_className(*args, **kwargs):
    pass


def MStateManager_swigregister(*args, **kwargs):
    pass


def MStencilOpDesc_className(*args, **kwargs):
    pass


def MStencilOpDesc_swigregister(*args, **kwargs):
    pass


def MSwatchRenderBase_swigregister(*args, **kwargs):
    pass


def MSwatchRenderRegister_registerSwatchRender(*args, **kwargs):
    pass


def MSwatchRenderRegister_swigregister(*args, **kwargs):
    pass


def MSwatchRenderRegister_unregisterSwatchRender(*args, **kwargs):
    pass


def MTargetBlendDesc_className(*args, **kwargs):
    pass


def MTargetBlendDesc_swigregister(*args, **kwargs):
    pass


def MTextureAssignment_swigregister(*args, **kwargs):
    pass


def MTextureDescription_swigregister(*args, **kwargs):
    pass


def MTextureManager_className(*args, **kwargs):
    pass


def MTextureManager_swigregister(*args, **kwargs):
    pass


def MTexture_className(*args, **kwargs):
    pass


def MTexture_swigregister(*args, **kwargs):
    pass


def MUniformParameterList_swigregister(*args, **kwargs):
    pass


def MUniformParameter_swigregister(*args, **kwargs):
    pass


def MUserRenderOperation_swigregister(*args, **kwargs):
    pass


def MVaryingParameterList_swigregister(*args, **kwargs):
    pass


def MVaryingParameter_swigregister(*args, **kwargs):
    pass


def MVertexBufferDescriptorList_className(*args, **kwargs):
    pass


def MVertexBufferDescriptorList_swigregister(*args, **kwargs):
    pass


def MVertexBufferDescriptor_className(*args, **kwargs):
    pass


def MVertexBufferDescriptor_swigregister(*args, **kwargs):
    pass


def MVertexBuffer_className(*args, **kwargs):
    pass


def MVertexBuffer_swigregister(*args, **kwargs):
    pass


def MViewportRenderer_swigregister(*args, **kwargs):
    pass


def RV_PIXEL_swigregister(*args, **kwargs):
    pass


def weakref_proxy(*args, **kwargs):
    """
    proxy(object[, callback]) -- create a proxy object that weakly
    references 'object'.  'callback', if given, is called with a
    reference to the proxy when 'object' is about to be finalized.
    """

    pass

MGL_2D = None

MGL_2X_BIT_ATI = None

MGL_2_BYTES = None

MGL_3D = None

MGL_3D_COLOR = None

MGL_3D_COLOR_TEXTURE = None

MGL_3_BYTES = None

MGL_4D_COLOR_TEXTURE = None

MGL_4X_BIT_ATI = None

MGL_4_BYTES = None

MGL_8X_BIT_ATI = None

MGL_ABGR_EXT = None

MGL_ACCUM = None

MGL_ACCUM_ALPHA_BITS = None

MGL_ACCUM_BLUE_BITS = None

MGL_ACCUM_BUFFER_BIT = None

MGL_ACCUM_CLEAR_VALUE = None

MGL_ACCUM_GREEN_BITS = None

MGL_ACCUM_RED_BITS = None

MGL_ACTIVE_TEXTURE = None

MGL_ACTIVE_TEXTURE_ARB = None

MGL_ADD = None

MGL_ADD_ATI = None

MGL_ADD_SIGNED = None

MGL_ADD_SIGNED_EXT = None

MGL_ALL_ATTRIB_BITS = None

MGL_ALL_COMPLETED_NV = None

MGL_ALPHA = None

MGL_ALPHA12 = None

MGL_ALPHA16 = None

MGL_ALPHA16F = None

MGL_ALPHA32F = None

MGL_ALPHA4 = None

MGL_ALPHA8 = None

MGL_ALPHA_BIAS = None

MGL_ALPHA_BITS = None

MGL_ALPHA_SCALE = None

MGL_ALPHA_TEST = None

MGL_ALPHA_TEST_FUNC = None

MGL_ALPHA_TEST_REF = None

MGL_ALWAYS = None

MGL_AMBIENT = None

MGL_AMBIENT_AND_DIFFUSE = None

MGL_AND = None

MGL_AND_INVERTED = None

MGL_AND_REVERSE = None

MGL_ARB_depth_texture = None

MGL_ARB_shadow = None

MGL_ARB_shadow_ambient = None

MGL_ARB_texture_env_dot3 = None

MGL_ARRAY_BUFFER_ARB = None

MGL_ARRAY_BUFFER_BINDING_ARB = None

MGL_ARRAY_ELEMENT_LOCK_COUNT_EXT = None

MGL_ARRAY_ELEMENT_LOCK_FIRST_EXT = None

MGL_ATTRIB_ARRAY_POINTER_NV = None

MGL_ATTRIB_ARRAY_SIZE_NV = None

MGL_ATTRIB_ARRAY_STRIDE_NV = None

MGL_ATTRIB_ARRAY_TYPE_NV = None

MGL_ATTRIB_STACK_DEPTH = None

MGL_AUTO_NORMAL = None

MGL_AUX0 = None

MGL_AUX1 = None

MGL_AUX2 = None

MGL_AUX3 = None

MGL_AUX_BUFFERS = None

MGL_BACK = None

MGL_BACK_LEFT = None

MGL_BACK_RIGHT = None

MGL_BGRA_EXT = None

MGL_BGR_EXT = None

MGL_BIAS_BIT_ATI = None

MGL_BIAS_BY_NEGATIVE_ONE_HALF_NV = None

MGL_BITMAP = None

MGL_BITMAP_TOKEN = None

MGL_BLEND = None

MGL_BLEND_COLOR = None

MGL_BLEND_COLOR_EXT = None

MGL_BLEND_DST = None

MGL_BLEND_EQUATION = None

MGL_BLEND_EQUATION_EXT = None

MGL_BLEND_SRC = None

MGL_BLUE = None

MGL_BLUE_BIAS = None

MGL_BLUE_BITS = None

MGL_BLUE_BIT_ATI = None

MGL_BLUE_SCALE = None

MGL_BOOL_ARB = None

MGL_BOOL_VEC2_ARB = None

MGL_BOOL_VEC3_ARB = None

MGL_BOOL_VEC4_ARB = None

MGL_BUFFER_ACCESS_ARB = None

MGL_BUFFER_MAPPED_ARB = None

MGL_BUFFER_MAP_POINTER_ARB = None

MGL_BUFFER_SIZE_ARB = None

MGL_BUFFER_USAGE_ARB = None

MGL_BYTE = None

MGL_C3F_V3F = None

MGL_C4F_N3F_V3F = None

MGL_C4UB_V2F = None

MGL_C4UB_V3F = None

MGL_CCW = None

MGL_CLAMP = None

MGL_CLAMP_FRAGMENT_COLOR = None

MGL_CLAMP_READ_COLOR = None

MGL_CLAMP_TO_BORDER = None

MGL_CLAMP_TO_BORDER_ARB = None

MGL_CLAMP_TO_BORDER_SGIS = None

MGL_CLAMP_TO_EDGE = None

MGL_CLAMP_VERTEX_COLOR = None

MGL_CLEAR = None

MGL_CLIENT_ACTIVE_TEXTURE = None

MGL_CLIENT_ACTIVE_TEXTURE_ARB = None

MGL_CLIENT_ALL_ATTRIB_BITS = None

MGL_CLIENT_ATTRIB_STACK_DEPTH = None

MGL_CLIENT_PIXEL_STORE_BIT = None

MGL_CLIENT_VERTEX_ARRAY_BIT = None

MGL_CLIP_PLANE0 = None

MGL_CLIP_PLANE1 = None

MGL_CLIP_PLANE2 = None

MGL_CLIP_PLANE3 = None

MGL_CLIP_PLANE4 = None

MGL_CLIP_PLANE5 = None

MGL_CLIP_VOLUME_CLIPPING_HINT_EXT = None

MGL_CND0_ATI = None

MGL_CND_ATI = None

MGL_COEFF = None

MGL_COLOR = None

MGL_COLOR_ALPHA_PAIRING_ATI = None

MGL_COLOR_ARRAY = None

MGL_COLOR_ARRAY_BUFFER_BINDING_ARB = None

MGL_COLOR_ARRAY_COUNT_EXT = None

MGL_COLOR_ARRAY_EXT = None

MGL_COLOR_ARRAY_POINTER = None

MGL_COLOR_ARRAY_POINTER_EXT = None

MGL_COLOR_ARRAY_SIZE = None

MGL_COLOR_ARRAY_SIZE_EXT = None

MGL_COLOR_ARRAY_STRIDE = None

MGL_COLOR_ARRAY_STRIDE_EXT = None

MGL_COLOR_ARRAY_TYPE = None

MGL_COLOR_ARRAY_TYPE_EXT = None

MGL_COLOR_BUFFER_BIT = None

MGL_COLOR_CLEAR_UNCLAMPED_VALUE_ATI = None

MGL_COLOR_CLEAR_VALUE = None

MGL_COLOR_INDEX = None

MGL_COLOR_INDEX12_EXT = None

MGL_COLOR_INDEX16_EXT = None

MGL_COLOR_INDEX1_EXT = None

MGL_COLOR_INDEX2_EXT = None

MGL_COLOR_INDEX4_EXT = None

MGL_COLOR_INDEX8_EXT = None

MGL_COLOR_INDEXES = None

MGL_COLOR_LOGIC_OP = None

MGL_COLOR_MATERIAL = None

MGL_COLOR_MATERIAL_FACE = None

MGL_COLOR_MATERIAL_PARAMETER = None

MGL_COLOR_SUM = None

MGL_COLOR_SUM_CLAMP_NV = None

MGL_COLOR_SUM_EXT = None

MGL_COLOR_TABLE_ALPHA_SIZE_EXT = None

MGL_COLOR_TABLE_BLUE_SIZE_EXT = None

MGL_COLOR_TABLE_FORMAT_EXT = None

MGL_COLOR_TABLE_GREEN_SIZE_EXT = None

MGL_COLOR_TABLE_INTENSITY_SIZE_EXT = None

MGL_COLOR_TABLE_LUMINANCE_SIZE_EXT = None

MGL_COLOR_TABLE_RED_SIZE_EXT = None

MGL_COLOR_TABLE_WIDTH_EXT = None

MGL_COLOR_WRITEMASK = None

MGL_COMBINE = None

MGL_COMBINE4_NV = None

MGL_COMBINER0_NV = None

MGL_COMBINER1_NV = None

MGL_COMBINER2_NV = None

MGL_COMBINER3_NV = None

MGL_COMBINER4_NV = None

MGL_COMBINER5_NV = None

MGL_COMBINER6_NV = None

MGL_COMBINER7_NV = None

MGL_COMBINER_AB_DOT_PRODUCT_NV = None

MGL_COMBINER_AB_OUTPUT_NV = None

MGL_COMBINER_BIAS_NV = None

MGL_COMBINER_CD_DOT_PRODUCT_NV = None

MGL_COMBINER_CD_OUTPUT_NV = None

MGL_COMBINER_COMPONENT_USAGE_NV = None

MGL_COMBINER_INPUT_NV = None

MGL_COMBINER_MAPPING_NV = None

MGL_COMBINER_MUX_SUM_NV = None

MGL_COMBINER_SCALE_NV = None

MGL_COMBINER_SUM_OUTPUT_NV = None

MGL_COMBINE_ALPHA = None

MGL_COMBINE_ALPHA_EXT = None

MGL_COMBINE_EXT = None

MGL_COMBINE_RGB = None

MGL_COMBINE_RGB_EXT = None

MGL_COMPARE_R_TO_TEXTURE_ARB = None

MGL_COMPILE = None

MGL_COMPILE_AND_EXECUTE = None

MGL_COMPRESSED_ALPHA = None

MGL_COMPRESSED_ALPHA_ARB = None

MGL_COMPRESSED_INTENSITY = None

MGL_COMPRESSED_INTENSITY_ARB = None

MGL_COMPRESSED_LUMINANCE = None

MGL_COMPRESSED_LUMINANCE_ALPHA = None

MGL_COMPRESSED_LUMINANCE_ALPHA_ARB = None

MGL_COMPRESSED_LUMINANCE_ARB = None

MGL_COMPRESSED_RGB = None

MGL_COMPRESSED_RGBA = None

MGL_COMPRESSED_RGBA_ARB = None

MGL_COMPRESSED_RGBA_S3TC_DXT1_EXT = None

MGL_COMPRESSED_RGBA_S3TC_DXT3_EXT = None

MGL_COMPRESSED_RGBA_S3TC_DXT5_EXT = None

MGL_COMPRESSED_RGB_ARB = None

MGL_COMPRESSED_RGB_S3TC_DXT1_EXT = None

MGL_COMPRESSED_TEXTURE_FORMATS = None

MGL_COMPRESSED_TEXTURE_FORMATS_ARB = None

MGL_COMP_BIT_ATI = None

MGL_CONSTANT = None

MGL_CONSTANT_ALPHA = None

MGL_CONSTANT_ALPHA_EXT = None

MGL_CONSTANT_ATTENUATION = None

MGL_CONSTANT_COLOR = None

MGL_CONSTANT_COLOR0_NV = None

MGL_CONSTANT_COLOR1_NV = None

MGL_CONSTANT_COLOR_EXT = None

MGL_CONSTANT_EXT = None

MGL_CONST_EYE_NV = None

MGL_CON_0_ATI = None

MGL_CON_10_ATI = None

MGL_CON_11_ATI = None

MGL_CON_12_ATI = None

MGL_CON_13_ATI = None

MGL_CON_14_ATI = None

MGL_CON_15_ATI = None

MGL_CON_16_ATI = None

MGL_CON_17_ATI = None

MGL_CON_18_ATI = None

MGL_CON_19_ATI = None

MGL_CON_1_ATI = None

MGL_CON_20_ATI = None

MGL_CON_21_ATI = None

MGL_CON_22_ATI = None

MGL_CON_23_ATI = None

MGL_CON_24_ATI = None

MGL_CON_25_ATI = None

MGL_CON_26_ATI = None

MGL_CON_27_ATI = None

MGL_CON_28_ATI = None

MGL_CON_29_ATI = None

MGL_CON_2_ATI = None

MGL_CON_30_ATI = None

MGL_CON_31_ATI = None

MGL_CON_3_ATI = None

MGL_CON_4_ATI = None

MGL_CON_5_ATI = None

MGL_CON_6_ATI = None

MGL_CON_7_ATI = None

MGL_CON_8_ATI = None

MGL_CON_9_ATI = None

MGL_COPY = None

MGL_COPY_INVERTED = None

MGL_COPY_PIXEL_TOKEN = None

MGL_CULL_FACE = None

MGL_CULL_FACE_MODE = None

MGL_CULL_FRAGMENT_NV = None

MGL_CULL_MODES_NV = None

MGL_CULL_VERTEX_EXT = None

MGL_CULL_VERTEX_EYE_POSITION_EXT = None

MGL_CULL_VERTEX_OBJECT_POSITION_EXT = None

MGL_CURRENT_ATTRIB_NV = None

MGL_CURRENT_BIT = None

MGL_CURRENT_COLOR = None

MGL_CURRENT_FOG_COORDINATE_EXT = None

MGL_CURRENT_INDEX = None

MGL_CURRENT_MATRIX = None

MGL_CURRENT_MATRIX_NV = None

MGL_CURRENT_MATRIX_STACK_DEPTH = None

MGL_CURRENT_MATRIX_STACK_DEPTH_NV = None

MGL_CURRENT_NORMAL = None

MGL_CURRENT_OCCLUSION_QUERY_ID_NV = None

MGL_CURRENT_QUERY_ARB = None

MGL_CURRENT_RASTER_COLOR = None

MGL_CURRENT_RASTER_DISTANCE = None

MGL_CURRENT_RASTER_INDEX = None

MGL_CURRENT_RASTER_POSITION = None

MGL_CURRENT_RASTER_POSITION_VALID = None

MGL_CURRENT_RASTER_TEXTURE_COORDS = None

MGL_CURRENT_SECONDARY_COLOR_EXT = None

MGL_CURRENT_TEXTURE_COORDS = None

MGL_CURRENT_VERTEX_ATTRIB = None

MGL_CURRENT_VERTEX_EXT = None

MGL_CURRENT_VERTEX_WEIGHT_EXT = None

MGL_CW = None

MGL_DECAL = None

MGL_DECR = None

MGL_DECR_WRAP_EXT = None

MGL_DEPENDENT_AR_TEXTURE_2D_NV = None

MGL_DEPENDENT_GB_TEXTURE_2D_NV = None

MGL_DEPTH = None

MGL_DEPTH_BIAS = None

MGL_DEPTH_BITS = None

MGL_DEPTH_BUFFER_BIT = None

MGL_DEPTH_CLEAR_VALUE = None

MGL_DEPTH_COMPONENT = None

MGL_DEPTH_COMPONENT16_ARB = None

MGL_DEPTH_COMPONENT24_ARB = None

MGL_DEPTH_COMPONENT32_ARB = None

MGL_DEPTH_FUNC = None

MGL_DEPTH_RANGE = None

MGL_DEPTH_SCALE = None

MGL_DEPTH_TEST = None

MGL_DEPTH_TEXTURE_MODE_ARB = None

MGL_DEPTH_WRITEMASK = None

MGL_DIFFUSE = None

MGL_DISCARD_NV = None

MGL_DITHER = None

MGL_DOMAIN = None

MGL_DONT_CARE = None

MGL_DOT2_ADD_ATI = None

MGL_DOT3_ATI = None

MGL_DOT3_RGB = None

MGL_DOT3_RGBA = None

MGL_DOT3_RGBA_ARB = None

MGL_DOT3_RGBA_EXT = None

MGL_DOT3_RGB_ARB = None

MGL_DOT3_RGB_EXT = None

MGL_DOT4_ATI = None

MGL_DOT_PRODUCT_CONST_EYE_REFLECT_CUBE_MAP_NV = None

MGL_DOT_PRODUCT_DEPTH_REPLACE_NV = None

MGL_DOT_PRODUCT_DIFFUSE_CUBE_MAP_NV = None

MGL_DOT_PRODUCT_NV = None

MGL_DOT_PRODUCT_REFLECT_CUBE_MAP_NV = None

MGL_DOT_PRODUCT_TEXTURE_2D_NV = None

MGL_DOT_PRODUCT_TEXTURE_3D_NV = None

MGL_DOT_PRODUCT_TEXTURE_CUBE_MAP_NV = None

MGL_DOUBLE = None

MGL_DOUBLEBUFFER = None

MGL_DRAW_BUFFER = None

MGL_DRAW_PIXEL_TOKEN = None

MGL_DSDT8_MAG8_INTENSITY8_NV = None

MGL_DSDT8_MAG8_NV = None

MGL_DSDT8_NV = None

MGL_DSDT_MAG_INTENSITY_NV = None

MGL_DSDT_MAG_NV = None

MGL_DSDT_MAG_VIB_NV = None

MGL_DSDT_NV = None

MGL_DST_ALPHA = None

MGL_DST_COLOR = None

MGL_DS_BIAS_NV = None

MGL_DS_SCALE_NV = None

MGL_DT_BIAS_NV = None

MGL_DT_SCALE_NV = None

MGL_DYNAMIC_COPY_ARB = None

MGL_DYNAMIC_DRAW_ARB = None

MGL_DYNAMIC_READ_ARB = None

MGL_EDGE_FLAG = None

MGL_EDGE_FLAG_ARRAY = None

MGL_EDGE_FLAG_ARRAY_BUFFER_BINDING_ARB = None

MGL_EDGE_FLAG_ARRAY_COUNT_EXT = None

MGL_EDGE_FLAG_ARRAY_EXT = None

MGL_EDGE_FLAG_ARRAY_POINTER = None

MGL_EDGE_FLAG_ARRAY_POINTER_EXT = None

MGL_EDGE_FLAG_ARRAY_STRIDE = None

MGL_EDGE_FLAG_ARRAY_STRIDE_EXT = None

MGL_EIGHTH_BIT_ATI = None

MGL_ELEMENT_ARRAY_BUFFER_ARB = None

MGL_ELEMENT_ARRAY_BUFFER_BINDING_ARB = None

MGL_EMBOSS_CONSTANT_NV = None

MGL_EMBOSS_LIGHT_NV = None

MGL_EMBOSS_MAP_NV = None

MGL_EMISSION = None

MGL_ENABLE_BIT = None

MGL_EQUAL = None

MGL_EQUIV = None

MGL_EVAL_BIT = None

MGL_EXP = None

MGL_EXP2 = None

MGL_EXPAND_NEGATE_NV = None

MGL_EXPAND_NORMAL_NV = None

MGL_EXTENSIONS = None

MGL_EXT_vertex_shader = None

MGL_EYE_LINEAR = None

MGL_EYE_PLANE = None

MGL_E_TIMES_F_NV = None

MGL_FALSE = None

MGL_FASTEST = None

MGL_FEEDBACK = None

MGL_FEEDBACK_BUFFER_POINTER = None

MGL_FEEDBACK_BUFFER_SIZE = None

MGL_FEEDBACK_BUFFER_TYPE = None

MGL_FENCE_CONDITION_NV = None

MGL_FENCE_STATUS_NV = None

MGL_FILL = None

MGL_FIXED_ONLY = None

MGL_FLAT = None

MGL_FLOAT = None

MGL_FLOAT_CLEAR_COLOR_VALUE_NV = None

MGL_FLOAT_MAT2_ARB = None

MGL_FLOAT_MAT3_ARB = None

MGL_FLOAT_MAT4_ARB = None

MGL_FLOAT_R16_NV = None

MGL_FLOAT_R32_NV = None

MGL_FLOAT_RG16_NV = None

MGL_FLOAT_RG32_NV = None

MGL_FLOAT_RGB16_NV = None

MGL_FLOAT_RGB32_NV = None

MGL_FLOAT_RGBA16_NV = None

MGL_FLOAT_RGBA32_NV = None

MGL_FLOAT_RGBA_MODE_NV = None

MGL_FLOAT_RGBA_NV = None

MGL_FLOAT_RGB_NV = None

MGL_FLOAT_RG_NV = None

MGL_FLOAT_R_NV = None

MGL_FLOAT_VEC2_ARB = None

MGL_FLOAT_VEC3_ARB = None

MGL_FLOAT_VEC4_ARB = None

MGL_FOG = None

MGL_FOG_BIT = None

MGL_FOG_COLOR = None

MGL_FOG_COORDINATE_ARRAY_BUFFER_BINDING_ARB = None

MGL_FOG_COORDINATE_ARRAY_EXT = None

MGL_FOG_COORDINATE_ARRAY_POINTER_EXT = None

MGL_FOG_COORDINATE_ARRAY_STRIDE_EXT = None

MGL_FOG_COORDINATE_ARRAY_TYPE_EXT = None

MGL_FOG_COORDINATE_EXT = None

MGL_FOG_COORDINATE_SOURCE_EXT = None

MGL_FOG_DENSITY = None

MGL_FOG_END = None

MGL_FOG_HINT = None

MGL_FOG_INDEX = None

MGL_FOG_MODE = None

MGL_FOG_SPECULAR_TEXTURE_WIN = None

MGL_FOG_START = None

MGL_FRAGMENT_DEPTH_EXT = None

MGL_FRAGMENT_PROGRAM_ARB = None

MGL_FRAGMENT_PROGRAM_BINDING_NV = None

MGL_FRAGMENT_PROGRAM_NV = None

MGL_FRAGMENT_SHADER_ARB = None

MGL_FRAGMENT_SHADER_ATI = None

MGL_FRONT = None

MGL_FRONT_AND_BACK = None

MGL_FRONT_FACE = None

MGL_FRONT_LEFT = None

MGL_FRONT_RIGHT = None

MGL_FULL_RANGE_EXT = None

MGL_FUNC_ADD = None

MGL_FUNC_ADD_EXT = None

MGL_FUNC_REVERSE_SUBTRACT = None

MGL_FUNC_REVERSE_SUBTRACT_EXT = None

MGL_FUNC_SUBTRACT = None

MGL_FUNC_SUBTRACT_EXT = None

MGL_GENERATE_MIPMAP_SGIS = None

MGL_GEQUAL = None

MGL_GREATER = None

MGL_GREEN = None

MGL_GREEN_BIAS = None

MGL_GREEN_BITS = None

MGL_GREEN_BIT_ATI = None

MGL_GREEN_SCALE = None

MGL_HALF_BIAS_NEGATE_NV = None

MGL_HALF_BIAS_NORMAL_NV = None

MGL_HALF_BIT_ATI = None

MGL_HALF_FLOAT = None

MGL_HILO16_NV = None

MGL_HILO_NV = None

MGL_HINT_BIT = None

MGL_HI_BIAS_NV = None

MGL_HI_SCALE_NV = None

MGL_IBM_TEXTURE_MIRRORED_REPEAT = None

MGL_IDENTITY_NV = None

MGL_INCR = None

MGL_INCR_WRAP_EXT = None

MGL_INDEX_ARRAY = None

MGL_INDEX_ARRAY_BUFFER_BINDING_ARB = None

MGL_INDEX_ARRAY_COUNT_EXT = None

MGL_INDEX_ARRAY_EXT = None

MGL_INDEX_ARRAY_POINTER = None

MGL_INDEX_ARRAY_POINTER_EXT = None

MGL_INDEX_ARRAY_STRIDE = None

MGL_INDEX_ARRAY_STRIDE_EXT = None

MGL_INDEX_ARRAY_TYPE = None

MGL_INDEX_ARRAY_TYPE_EXT = None

MGL_INDEX_BITS = None

MGL_INDEX_CLEAR_VALUE = None

MGL_INDEX_LOGIC_OP = None

MGL_INDEX_MODE = None

MGL_INDEX_OFFSET = None

MGL_INDEX_SHIFT = None

MGL_INDEX_WRITEMASK = None

MGL_INT = None

MGL_INTENSITY = None

MGL_INTENSITY12 = None

MGL_INTENSITY16 = None

MGL_INTENSITY16F = None

MGL_INTENSITY32F = None

MGL_INTENSITY4 = None

MGL_INTENSITY8 = None

MGL_INTERPOLATE = None

MGL_INTERPOLATE_EXT = None

MGL_INT_VEC2_ARB = None

MGL_INT_VEC3_ARB = None

MGL_INT_VEC4_ARB = None

MGL_INVALID_ENUM = None

MGL_INVALID_OPERATION = None

MGL_INVALID_VALUE = None

MGL_INVARIANT_DATATYPE_EXT = None

MGL_INVARIANT_EXT = None

MGL_INVARIANT_VALUE_EXT = None

MGL_INVERSE_NV = None

MGL_INVERSE_TRANSPOSE_NV = None

MGL_INVERT = None

MGL_ISOTROPIC_BRDF_NV = None

MGL_KEEP = None

MGL_LEFT = None

MGL_LEQUAL = None

MGL_LERP_ATI = None

MGL_LESS = None

MGL_LIGHT0 = None

MGL_LIGHT1 = None

MGL_LIGHT2 = None

MGL_LIGHT3 = None

MGL_LIGHT4 = None

MGL_LIGHT5 = None

MGL_LIGHT6 = None

MGL_LIGHT7 = None

MGL_LIGHTING = None

MGL_LIGHTING_BIT = None

MGL_LIGHT_MODEL_AMBIENT = None

MGL_LIGHT_MODEL_COLOR_CONTROL = None

MGL_LIGHT_MODEL_LOCAL_VIEWER = None

MGL_LIGHT_MODEL_TWO_SIDE = None

MGL_LINE = None

MGL_LINEAR = None

MGL_LINEAR_ATTENUATION = None

MGL_LINEAR_MIPMAP_LINEAR = None

MGL_LINEAR_MIPMAP_NEAREST = None

MGL_LINES = None

MGL_LINE_BIT = None

MGL_LINE_LOOP = None

MGL_LINE_RESET_TOKEN = None

MGL_LINE_SMOOTH = None

MGL_LINE_SMOOTH_HINT = None

MGL_LINE_STIPPLE = None

MGL_LINE_STIPPLE_PATTERN = None

MGL_LINE_STIPPLE_REPEAT = None

MGL_LINE_STRIP = None

MGL_LINE_TOKEN = None

MGL_LINE_WIDTH = None

MGL_LINE_WIDTH_GRANULARITY = None

MGL_LINE_WIDTH_RANGE = None

MGL_LIST_BASE = None

MGL_LIST_BIT = None

MGL_LIST_INDEX = None

MGL_LIST_MODE = None

MGL_LOAD = None

MGL_LOCAL_CONSTANT_DATATYPE_EXT = None

MGL_LOCAL_CONSTANT_EXT = None

MGL_LOCAL_CONSTANT_VALUE_EXT = None

MGL_LOCAL_EXT = None

MGL_LOGIC_OP = None

MGL_LOGIC_OP_MODE = None

MGL_LO_BIAS_NV = None

MGL_LO_SCALE_NV = None

MGL_LUMINANCE = None

MGL_LUMINANCE12 = None

MGL_LUMINANCE12_ALPHA12 = None

MGL_LUMINANCE12_ALPHA4 = None

MGL_LUMINANCE16 = None

MGL_LUMINANCE16F = None

MGL_LUMINANCE16_ALPHA16 = None

MGL_LUMINANCE32F = None

MGL_LUMINANCE4 = None

MGL_LUMINANCE4_ALPHA4 = None

MGL_LUMINANCE6_ALPHA2 = None

MGL_LUMINANCE8 = None

MGL_LUMINANCE8_ALPHA8 = None

MGL_LUMINANCE_ALPHA = None

MGL_LUMINANCE_ALPHA16F = None

MGL_LUMINANCE_ALPHA32F = None

MGL_MAD_ATI = None

MGL_MAGNITUDE_BIAS_NV = None

MGL_MAGNITUDE_SCALE_NV = None

MGL_MAP1_COLOR_4 = None

MGL_MAP1_GRID_DOMAIN = None

MGL_MAP1_GRID_SEGMENTS = None

MGL_MAP1_INDEX = None

MGL_MAP1_NORMAL = None

MGL_MAP1_TEXTURE_COORD_1 = None

MGL_MAP1_TEXTURE_COORD_2 = None

MGL_MAP1_TEXTURE_COORD_3 = None

MGL_MAP1_TEXTURE_COORD_4 = None

MGL_MAP1_VERTEX_3 = None

MGL_MAP1_VERTEX_4 = None

MGL_MAP1_VERTEX_ATTRIB0_4_NV = None

MGL_MAP1_VERTEX_ATTRIB10_4_NV = None

MGL_MAP1_VERTEX_ATTRIB11_4_NV = None

MGL_MAP1_VERTEX_ATTRIB12_4_NV = None

MGL_MAP1_VERTEX_ATTRIB13_4_NV = None

MGL_MAP1_VERTEX_ATTRIB14_4_NV = None

MGL_MAP1_VERTEX_ATTRIB15_4_NV = None

MGL_MAP1_VERTEX_ATTRIB1_4_NV = None

MGL_MAP1_VERTEX_ATTRIB2_4_NV = None

MGL_MAP1_VERTEX_ATTRIB3_4_NV = None

MGL_MAP1_VERTEX_ATTRIB4_4_NV = None

MGL_MAP1_VERTEX_ATTRIB5_4_NV = None

MGL_MAP1_VERTEX_ATTRIB6_4_NV = None

MGL_MAP1_VERTEX_ATTRIB7_4_NV = None

MGL_MAP1_VERTEX_ATTRIB8_4_NV = None

MGL_MAP1_VERTEX_ATTRIB9_4_NV = None

MGL_MAP2_COLOR_4 = None

MGL_MAP2_GRID_DOMAIN = None

MGL_MAP2_GRID_SEGMENTS = None

MGL_MAP2_INDEX = None

MGL_MAP2_NORMAL = None

MGL_MAP2_TEXTURE_COORD_1 = None

MGL_MAP2_TEXTURE_COORD_2 = None

MGL_MAP2_TEXTURE_COORD_3 = None

MGL_MAP2_TEXTURE_COORD_4 = None

MGL_MAP2_VERTEX_3 = None

MGL_MAP2_VERTEX_4 = None

MGL_MAP2_VERTEX_ATTRIB0_4_NV = None

MGL_MAP2_VERTEX_ATTRIB10_4_NV = None

MGL_MAP2_VERTEX_ATTRIB11_4_NV = None

MGL_MAP2_VERTEX_ATTRIB12_4_NV = None

MGL_MAP2_VERTEX_ATTRIB13_4_NV = None

MGL_MAP2_VERTEX_ATTRIB14_4_NV = None

MGL_MAP2_VERTEX_ATTRIB15_4_NV = None

MGL_MAP2_VERTEX_ATTRIB1_4_NV = None

MGL_MAP2_VERTEX_ATTRIB2_4_NV = None

MGL_MAP2_VERTEX_ATTRIB3_4_NV = None

MGL_MAP2_VERTEX_ATTRIB4_4_NV = None

MGL_MAP2_VERTEX_ATTRIB5_4_NV = None

MGL_MAP2_VERTEX_ATTRIB6_4_NV = None

MGL_MAP2_VERTEX_ATTRIB7_4_NV = None

MGL_MAP2_VERTEX_ATTRIB8_4_NV = None

MGL_MAP2_VERTEX_ATTRIB9_4_NV = None

MGL_MAP_COLOR = None

MGL_MAP_STENCIL = None

MGL_MATRIX0 = None

MGL_MATRIX0_NV = None

MGL_MATRIX1 = None

MGL_MATRIX10 = None

MGL_MATRIX11 = None

MGL_MATRIX12 = None

MGL_MATRIX13 = None

MGL_MATRIX14 = None

MGL_MATRIX15 = None

MGL_MATRIX16 = None

MGL_MATRIX17 = None

MGL_MATRIX18 = None

MGL_MATRIX19 = None

MGL_MATRIX1_NV = None

MGL_MATRIX2 = None

MGL_MATRIX20 = None

MGL_MATRIX21 = None

MGL_MATRIX22 = None

MGL_MATRIX23 = None

MGL_MATRIX24 = None

MGL_MATRIX25 = None

MGL_MATRIX26 = None

MGL_MATRIX27 = None

MGL_MATRIX28 = None

MGL_MATRIX29 = None

MGL_MATRIX2_NV = None

MGL_MATRIX3 = None

MGL_MATRIX30 = None

MGL_MATRIX31 = None

MGL_MATRIX3_NV = None

MGL_MATRIX4 = None

MGL_MATRIX4_NV = None

MGL_MATRIX5 = None

MGL_MATRIX5_NV = None

MGL_MATRIX6 = None

MGL_MATRIX6_NV = None

MGL_MATRIX7 = None

MGL_MATRIX7_NV = None

MGL_MATRIX8 = None

MGL_MATRIX9 = None

MGL_MATRIX_EXT = None

MGL_MATRIX_MODE = None

MGL_MAX = None

MGL_MAX_3D_TEXTURE_SIZE = None

MGL_MAX_3D_TEXTURE_SIZE_EXT = None

MGL_MAX_ATTRIB_STACK_DEPTH = None

MGL_MAX_CLIENT_ATTRIB_STACK_DEPTH = None

MGL_MAX_CLIP_PLANES = None

MGL_MAX_COMBINED_TEXTURE_IMAGE_UNITS_ARB = None

MGL_MAX_CUBE_MAP_TEXTURE_SIZE = None

MGL_MAX_CUBE_MAP_TEXTURE_SIZE_ARB = None

MGL_MAX_EVAL_ORDER = None

MGL_MAX_EXT = None

MGL_MAX_FRAGMENT_PROGRAM_LOCAL_PARAMETERS_NV = None

MGL_MAX_FRAGMENT_UNIFORM_COMPONENTS_ARB = None

MGL_MAX_GENERAL_COMBINERS_NV = None

MGL_MAX_LIGHTS = None

MGL_MAX_LIST_NESTING = None

MGL_MAX_MODELVIEW_STACK_DEPTH = None

MGL_MAX_NAME_STACK_DEPTH = None

MGL_MAX_OPTIMIZED_VERTEX_SHADER_INSTRUCTIONS_EXT = None

MGL_MAX_OPTIMIZED_VERTEX_SHADER_INVARIANTS_EXT = None

MGL_MAX_OPTIMIZED_VERTEX_SHADER_LOCALS_EXT = None

MGL_MAX_OPTIMIZED_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = None

MGL_MAX_OPTIMIZED_VERTEX_SHADER_VARIANTS_EXT = None

MGL_MAX_PIXEL_MAP_TABLE = None

MGL_MAX_PN_TRIANGLES_TESSELATION_LEVEL_ATI = None

MGL_MAX_PROGRAM_ADDRESS_REGISTERS = None

MGL_MAX_PROGRAM_ALU_INSTRUCTIONS_ARB = None

MGL_MAX_PROGRAM_ATTRIBS = None

MGL_MAX_PROGRAM_ENV_PARAMETERS = None

MGL_MAX_PROGRAM_INSTRUCTIONS = None

MGL_MAX_PROGRAM_LOCAL_PARAMETERS = None

MGL_MAX_PROGRAM_MATRICES = None

MGL_MAX_PROGRAM_MATRIX_STACK_DEPTH = None

MGL_MAX_PROGRAM_NATIVE_ADDRESS_REGISTERS = None

MGL_MAX_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB = None

MGL_MAX_PROGRAM_NATIVE_ATTRIBS = None

MGL_MAX_PROGRAM_NATIVE_INSTRUCTIONS = None

MGL_MAX_PROGRAM_NATIVE_PARAMETERS = None

MGL_MAX_PROGRAM_NATIVE_TEMPORARIES = None

MGL_MAX_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB = None

MGL_MAX_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB = None

MGL_MAX_PROGRAM_PARAMETERS = None

MGL_MAX_PROGRAM_TEMPORARIES = None

MGL_MAX_PROGRAM_TEX_INDIRECTIONS_ARB = None

MGL_MAX_PROGRAM_TEX_INSTRUCTIONS_ARB = None

MGL_MAX_PROJECTION_STACK_DEPTH = None

MGL_MAX_RECTANGLE_TEXTURE_SIZE = None

MGL_MAX_TEXTURE_COORDS_ARB = None

MGL_MAX_TEXTURE_COORDS_NV = None

MGL_MAX_TEXTURE_IMAGE_UNITS_ARB = None

MGL_MAX_TEXTURE_IMAGE_UNITS_NV = None

MGL_MAX_TEXTURE_MAX_ANISOTROPY_EXT = None

MGL_MAX_TEXTURE_SIZE = None

MGL_MAX_TEXTURE_STACK_DEPTH = None

MGL_MAX_TEXTURE_UNITS = None

MGL_MAX_TEXTURE_UNITS_ARB = None

MGL_MAX_TRACK_MATRICES_NV = None

MGL_MAX_TRACK_MATRIX_STACK_DEPTH_NV = None

MGL_MAX_VARYING_FLOATS_ARB = None

MGL_MAX_VERTEX_ARRAY_RANGE_ELEMENT_NV = None

MGL_MAX_VERTEX_ATTRIBS = None

MGL_MAX_VERTEX_SHADER_INSTRUCTIONS_EXT = None

MGL_MAX_VERTEX_SHADER_INVARIANTS_EXT = None

MGL_MAX_VERTEX_SHADER_LOCALS_EXT = None

MGL_MAX_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = None

MGL_MAX_VERTEX_SHADER_VARIANTS_EXT = None

MGL_MAX_VERTEX_TEXTURE_IMAGE_UNITS_ARB = None

MGL_MAX_VERTEX_UNIFORM_COMPONENTS_ARB = None

MGL_MAX_VIEWPORT_DIMS = None

MGL_MIN = None

MGL_MIN_EXT = None

MGL_MIRRORED_REPEAT_IBM = None

MGL_MIRROR_CLAMP_ATI = None

MGL_MIRROR_CLAMP_TO_EDGE_ATI = None

MGL_MODELVIEW = None

MGL_MODELVIEW0_EXT = None

MGL_MODELVIEW0_MATRIX_EXT = None

MGL_MODELVIEW0_STACK_DEPTH_EXT = None

MGL_MODELVIEW1_EXT = None

MGL_MODELVIEW1_STACK_DEPTH_EXT = None

MGL_MODELVIEW_MATRIX = None

MGL_MODELVIEW_MATRIX1_EXT = None

MGL_MODELVIEW_PROJECTION_NV = None

MGL_MODELVIEW_STACK_DEPTH = None

MGL_MODULATE = None

MGL_MOV_ATI = None

MGL_MULT = None

MGL_MULTISAMPLE = None

MGL_MULTISAMPLE_ARB = None

MGL_MULTISAMPLE_BIT = None

MGL_MULTISAMPLE_BIT_ARB = None

MGL_MUL_ATI = None

MGL_MVP_MATRIX_EXT = None

MGL_N3F_V3F = None

MGL_NAME_STACK_DEPTH = None

MGL_NAND = None

MGL_NEAREST = None

MGL_NEAREST_MIPMAP_LINEAR = None

MGL_NEAREST_MIPMAP_NEAREST = None

MGL_NEGATE_BIT_ATI = None

MGL_NEGATIVE_ONE_EXT = None

MGL_NEGATIVE_W_EXT = None

MGL_NEGATIVE_X_EXT = None

MGL_NEGATIVE_Y_EXT = None

MGL_NEGATIVE_Z_EXT = None

MGL_NEVER = None

MGL_NICEST = None

MGL_NONE = None

MGL_NOOP = None

MGL_NOR = None

MGL_NORMALIZE = None

MGL_NORMALIZED_RANGE_EXT = None

MGL_NORMAL_ARRAY = None

MGL_NORMAL_ARRAY_BUFFER_BINDING_ARB = None

MGL_NORMAL_ARRAY_COUNT_EXT = None

MGL_NORMAL_ARRAY_EXT = None

MGL_NORMAL_ARRAY_POINTER = None

MGL_NORMAL_ARRAY_POINTER_EXT = None

MGL_NORMAL_ARRAY_STRIDE = None

MGL_NORMAL_ARRAY_STRIDE_EXT = None

MGL_NORMAL_ARRAY_TYPE = None

MGL_NORMAL_ARRAY_TYPE_EXT = None

MGL_NORMAL_MAP = None

MGL_NORMAL_MAP_ARB = None

MGL_NOTEQUAL = None

MGL_NO_ERROR = None

MGL_NUM_COMPRESSED_TEXTURE_FORMATS = None

MGL_NUM_COMPRESSED_TEXTURE_FORMATS_ARB = None

MGL_NUM_FRAGMENT_CONSTANTS_ATI = None

MGL_NUM_FRAGMENT_REGISTERS_ATI = None

MGL_NUM_GENERAL_COMBINERS_NV = None

MGL_NUM_INPUT_INTERPOLATOR_COMPONENTS_ATI = None

MGL_NUM_INSTRUCTIONS_PER_PASS_ATI = None

MGL_NUM_INSTRUCTIONS_TOTAL_ATI = None

MGL_NUM_LOOPBACK_COMPONENTS_ATI = None

MGL_NUM_PASSES_ATI = None

MGL_OBJECT_ACTIVE_ATTRIBUTES_ARB = None

MGL_OBJECT_ACTIVE_ATTRIBUTE_MAX_LENGTH_ARB = None

MGL_OBJECT_ACTIVE_UNIFORMS_ARB = None

MGL_OBJECT_ACTIVE_UNIFORM_MAX_LENGTH_ARB = None

MGL_OBJECT_ATTACHED_OBJECTS_ARB = None

MGL_OBJECT_COMPILE_STATUS_ARB = None

MGL_OBJECT_DELETE_STATUS_ARB = None

MGL_OBJECT_INFO_LOG_LENGTH_ARB = None

MGL_OBJECT_LINEAR = None

MGL_OBJECT_LINK_STATUS_ARB = None

MGL_OBJECT_PLANE = None

MGL_OBJECT_SHADER_SOURCE_LENGTH_ARB = None

MGL_OBJECT_SUBTYPE_ARB = None

MGL_OBJECT_TYPE_ARB = None

MGL_OBJECT_VALIDATE_STATUS_ARB = None

MGL_OCCLUSION_TEST_HP = None

MGL_OCCLUSION_TEST_RESULT_HP = None

MGL_OFFSET_TEXTURE_2D_BIAS_NV = None

MGL_OFFSET_TEXTURE_2D_MATRIX_NV = None

MGL_OFFSET_TEXTURE_2D_NV = None

MGL_OFFSET_TEXTURE_2D_SCALE_NV = None

MGL_ONE = None

MGL_ONE_EXT = None

MGL_ONE_MINUS_CONSTANT_ALPHA = None

MGL_ONE_MINUS_CONSTANT_ALPHA_EXT = None

MGL_ONE_MINUS_CONSTANT_COLOR = None

MGL_ONE_MINUS_CONSTANT_COLOR_EXT = None

MGL_ONE_MINUS_DST_ALPHA = None

MGL_ONE_MINUS_DST_COLOR = None

MGL_ONE_MINUS_SRC_ALPHA = None

MGL_ONE_MINUS_SRC_COLOR = None

MGL_OPERAND0_ALPHA = None

MGL_OPERAND0_ALPHA_EXT = None

MGL_OPERAND0_RGB = None

MGL_OPERAND0_RGB_EXT = None

MGL_OPERAND1_ALPHA = None

MGL_OPERAND1_ALPHA_EXT = None

MGL_OPERAND1_RGB = None

MGL_OPERAND1_RGB_EXT = None

MGL_OPERAND2_ALPHA = None

MGL_OPERAND2_ALPHA_EXT = None

MGL_OPERAND2_RGB = None

MGL_OPERAND2_RGB_EXT = None

MGL_OPERAND3_ALPHA_NV = None

MGL_OPERAND3_RGB_NV = None

MGL_OP_ADD_EXT = None

MGL_OP_CLAMP_EXT = None

MGL_OP_CROSS_PRODUCT_EXT = None

MGL_OP_DOT3_EXT = None

MGL_OP_DOT4_EXT = None

MGL_OP_EXP_BASE_2_EXT = None

MGL_OP_FLOOR_EXT = None

MGL_OP_FRAC_EXT = None

MGL_OP_INDEX_EXT = None

MGL_OP_LOG_BASE_2_EXT = None

MGL_OP_MADD_EXT = None

MGL_OP_MAX_EXT = None

MGL_OP_MIN_EXT = None

MGL_OP_MOV_EXT = None

MGL_OP_MULTIPLY_MATRIX_EXT = None

MGL_OP_MUL_EXT = None

MGL_OP_NEGATE_EXT = None

MGL_OP_POWER_EXT = None

MGL_OP_RECIP_EXT = None

MGL_OP_RECIP_SQRT_EXT = None

MGL_OP_ROUND_EXT = None

MGL_OP_SET_GE_EXT = None

MGL_OP_SET_LT_EXT = None

MGL_OP_SUB_EXT = None

MGL_OR = None

MGL_ORDER = None

MGL_OR_INVERTED = None

MGL_OR_REVERSE = None

MGL_OUTPUT_COLOR0_EXT = None

MGL_OUTPUT_COLOR1_EXT = None

MGL_OUTPUT_FOG_EXT = None

MGL_OUTPUT_TEXTURE_COORD0_EXT = None

MGL_OUTPUT_TEXTURE_COORD10_EXT = None

MGL_OUTPUT_TEXTURE_COORD11_EXT = None

MGL_OUTPUT_TEXTURE_COORD12_EXT = None

MGL_OUTPUT_TEXTURE_COORD13_EXT = None

MGL_OUTPUT_TEXTURE_COORD14_EXT = None

MGL_OUTPUT_TEXTURE_COORD15_EXT = None

MGL_OUTPUT_TEXTURE_COORD16_EXT = None

MGL_OUTPUT_TEXTURE_COORD17_EXT = None

MGL_OUTPUT_TEXTURE_COORD18_EXT = None

MGL_OUTPUT_TEXTURE_COORD19_EXT = None

MGL_OUTPUT_TEXTURE_COORD1_EXT = None

MGL_OUTPUT_TEXTURE_COORD20_EXT = None

MGL_OUTPUT_TEXTURE_COORD21_EXT = None

MGL_OUTPUT_TEXTURE_COORD22_EXT = None

MGL_OUTPUT_TEXTURE_COORD23_EXT = None

MGL_OUTPUT_TEXTURE_COORD24_EXT = None

MGL_OUTPUT_TEXTURE_COORD25_EXT = None

MGL_OUTPUT_TEXTURE_COORD26_EXT = None

MGL_OUTPUT_TEXTURE_COORD27_EXT = None

MGL_OUTPUT_TEXTURE_COORD28_EXT = None

MGL_OUTPUT_TEXTURE_COORD29_EXT = None

MGL_OUTPUT_TEXTURE_COORD2_EXT = None

MGL_OUTPUT_TEXTURE_COORD30_EXT = None

MGL_OUTPUT_TEXTURE_COORD31_EXT = None

MGL_OUTPUT_TEXTURE_COORD3_EXT = None

MGL_OUTPUT_TEXTURE_COORD4_EXT = None

MGL_OUTPUT_TEXTURE_COORD5_EXT = None

MGL_OUTPUT_TEXTURE_COORD6_EXT = None

MGL_OUTPUT_TEXTURE_COORD7_EXT = None

MGL_OUTPUT_TEXTURE_COORD8_EXT = None

MGL_OUTPUT_TEXTURE_COORD9_EXT = None

MGL_OUTPUT_VERTEX_EXT = None

MGL_OUT_OF_MEMORY = None

MGL_PACK_ALIGNMENT = None

MGL_PACK_IMAGE_HEIGHT = None

MGL_PACK_IMAGE_HEIGHT_EXT = None

MGL_PACK_LSB_FIRST = None

MGL_PACK_ROW_LENGTH = None

MGL_PACK_SKIP_IMAGES = None

MGL_PACK_SKIP_IMAGES_EXT = None

MGL_PACK_SKIP_PIXELS = None

MGL_PACK_SKIP_ROWS = None

MGL_PACK_SWAP_BYTES = None

MGL_PASS_THROUGH_NV = None

MGL_PASS_THROUGH_TOKEN = None

MGL_PERSPECTIVE_CORRECTION_HINT = None

MGL_PHONG_HINT_WIN = None

MGL_PHONG_WIN = None

MGL_PIXEL_COUNTER_BITS_ARB = None

MGL_PIXEL_COUNTER_BITS_NV = None

MGL_PIXEL_COUNT_AVAILABLE_NV = None

MGL_PIXEL_COUNT_NV = None

MGL_PIXEL_MAP_A_TO_A = None

MGL_PIXEL_MAP_A_TO_A_SIZE = None

MGL_PIXEL_MAP_B_TO_B = None

MGL_PIXEL_MAP_B_TO_B_SIZE = None

MGL_PIXEL_MAP_G_TO_G = None

MGL_PIXEL_MAP_G_TO_G_SIZE = None

MGL_PIXEL_MAP_I_TO_A = None

MGL_PIXEL_MAP_I_TO_A_SIZE = None

MGL_PIXEL_MAP_I_TO_B = None

MGL_PIXEL_MAP_I_TO_B_SIZE = None

MGL_PIXEL_MAP_I_TO_G = None

MGL_PIXEL_MAP_I_TO_G_SIZE = None

MGL_PIXEL_MAP_I_TO_I = None

MGL_PIXEL_MAP_I_TO_I_SIZE = None

MGL_PIXEL_MAP_I_TO_R = None

MGL_PIXEL_MAP_I_TO_R_SIZE = None

MGL_PIXEL_MAP_R_TO_R = None

MGL_PIXEL_MAP_R_TO_R_SIZE = None

MGL_PIXEL_MAP_S_TO_S = None

MGL_PIXEL_MAP_S_TO_S_SIZE = None

MGL_PIXEL_MODE_BIT = None

MGL_PN_TRIANGLES_ATI = None

MGL_PN_TRIANGLES_NORMAL_MODE_ATI = None

MGL_PN_TRIANGLES_NORMAL_MODE_LINEAR_ATI = None

MGL_PN_TRIANGLES_NORMAL_MODE_QUADRATIC_ATI = None

MGL_PN_TRIANGLES_POINT_MODE_ATI = None

MGL_PN_TRIANGLES_POINT_MODE_CUBIC_ATI = None

MGL_PN_TRIANGLES_POINT_MODE_LINEAR_ATI = None

MGL_PN_TRIANGLES_TESSELATION_LEVEL_ATI = None

MGL_POINT = None

MGL_POINTS = None

MGL_POINT_BIT = None

MGL_POINT_DISTANCE_ATTENUATION_ARB = None

MGL_POINT_FADE_THRESHOLD_SIZE_ARB = None

MGL_POINT_SIZE = None

MGL_POINT_SIZE_GRANULARITY = None

MGL_POINT_SIZE_MAX_ARB = None

MGL_POINT_SIZE_MIN_ARB = None

MGL_POINT_SIZE_RANGE = None

MGL_POINT_SMOOTH = None

MGL_POINT_SMOOTH_HINT = None

MGL_POINT_TOKEN = None

MGL_POLYGON = None

MGL_POLYGON_BIT = None

MGL_POLYGON_MODE = None

MGL_POLYGON_OFFSET_FACTOR = None

MGL_POLYGON_OFFSET_FILL = None

MGL_POLYGON_OFFSET_LINE = None

MGL_POLYGON_OFFSET_POINT = None

MGL_POLYGON_OFFSET_UNITS = None

MGL_POLYGON_SMOOTH = None

MGL_POLYGON_SMOOTH_HINT = None

MGL_POLYGON_STIPPLE = None

MGL_POLYGON_STIPPLE_BIT = None

MGL_POLYGON_TOKEN = None

MGL_POSITION = None

MGL_PREVIOUS = None

MGL_PREVIOUS_EXT = None

MGL_PREVIOUS_TEXTURE_INPUT_NV = None

MGL_PRIMARY_COLOR = None

MGL_PRIMARY_COLOR_EXT = None

MGL_PRIMARY_COLOR_NV = None

MGL_PRIMITIVE_RESTART_INDEX_NV = None

MGL_PRIMITIVE_RESTART_NV = None

MGL_PROGRAM_ADDRESS_REGISTERS = None

MGL_PROGRAM_ALU_INSTRUCTIONS_ARB = None

MGL_PROGRAM_ATTRIBS = None

MGL_PROGRAM_BINDING = None

MGL_PROGRAM_ERROR_POSITION = None

MGL_PROGRAM_ERROR_POSITION_NV = None

MGL_PROGRAM_ERROR_STRING = None

MGL_PROGRAM_ERROR_STRING_NV = None

MGL_PROGRAM_FORMAT = None

MGL_PROGRAM_FORMAT_ASCII = None

MGL_PROGRAM_INSTRUCTIONS = None

MGL_PROGRAM_LENGTH = None

MGL_PROGRAM_LENGTH_NV = None

MGL_PROGRAM_NATIVE_ADDRESS_REGISTERS = None

MGL_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB = None

MGL_PROGRAM_NATIVE_ATTRIBS = None

MGL_PROGRAM_NATIVE_INSTRUCTIONS = None

MGL_PROGRAM_NATIVE_PARAMETERS = None

MGL_PROGRAM_NATIVE_TEMPORARIES = None

MGL_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB = None

MGL_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB = None

MGL_PROGRAM_OBJECT_ARB = None

MGL_PROGRAM_PARAMETERS = None

MGL_PROGRAM_PARAMETER_NV = None

MGL_PROGRAM_RESIDENT_NV = None

MGL_PROGRAM_STRING = None

MGL_PROGRAM_STRING_NV = None

MGL_PROGRAM_TARGET_NV = None

MGL_PROGRAM_TEMPORARIES = None

MGL_PROGRAM_TEX_INDIRECTIONS_ARB = None

MGL_PROGRAM_TEX_INSTRUCTIONS_ARB = None

MGL_PROGRAM_UNDER_NATIVE_LIMITS = None

MGL_PROJECTION = None

MGL_PROJECTION_MATRIX = None

MGL_PROJECTION_STACK_DEPTH = None

MGL_PROXY_TEXTURE_1D = None

MGL_PROXY_TEXTURE_2D = None

MGL_PROXY_TEXTURE_3D = None

MGL_PROXY_TEXTURE_3D_EXT = None

MGL_PROXY_TEXTURE_CUBE_MAP = None

MGL_PROXY_TEXTURE_CUBE_MAP_ARB = None

MGL_PROXY_TEXTURE_RECTANGLE = None

MGL_Q = None

MGL_QUADRATIC_ATTENUATION = None

MGL_QUADS = None

MGL_QUAD_STRIP = None

MGL_QUARTER_BIT_ATI = None

MGL_QUERY_RESULT_ARB = None

MGL_QUERY_RESULT_AVAILABLE_ARB = None

MGL_R = None

MGL_R3_G3_B2 = None

MGL_READ_BUFFER = None

MGL_READ_ONLY_ARB = None

MGL_READ_WRITE_ARB = None

MGL_RED = None

MGL_RED_BIAS = None

MGL_RED_BITS = None

MGL_RED_BIT_ATI = None

MGL_RED_SCALE = None

MGL_REFLECTION_MAP = None

MGL_REFLECTION_MAP_ARB = None

MGL_REGISTER_COMBINERS_NV = None

MGL_REG_0_ATI = None

MGL_REG_10_ATI = None

MGL_REG_11_ATI = None

MGL_REG_12_ATI = None

MGL_REG_13_ATI = None

MGL_REG_14_ATI = None

MGL_REG_15_ATI = None

MGL_REG_16_ATI = None

MGL_REG_17_ATI = None

MGL_REG_18_ATI = None

MGL_REG_19_ATI = None

MGL_REG_1_ATI = None

MGL_REG_20_ATI = None

MGL_REG_21_ATI = None

MGL_REG_22_ATI = None

MGL_REG_23_ATI = None

MGL_REG_24_ATI = None

MGL_REG_25_ATI = None

MGL_REG_26_ATI = None

MGL_REG_27_ATI = None

MGL_REG_28_ATI = None

MGL_REG_29_ATI = None

MGL_REG_2_ATI = None

MGL_REG_30_ATI = None

MGL_REG_31_ATI = None

MGL_REG_3_ATI = None

MGL_REG_4_ATI = None

MGL_REG_5_ATI = None

MGL_REG_6_ATI = None

MGL_REG_7_ATI = None

MGL_REG_8_ATI = None

MGL_REG_9_ATI = None

MGL_RENDER = None

MGL_RENDERER = None

MGL_RENDER_MODE = None

MGL_REPEAT = None

MGL_REPLACE = None

MGL_RESCALE_NORMAL_EXT = None

MGL_RETURN = None

MGL_RGB = None

MGL_RGB10 = None

MGL_RGB10_A2 = None

MGL_RGB12 = None

MGL_RGB16 = None

MGL_RGB16F = None

MGL_RGB32F = None

MGL_RGB4 = None

MGL_RGB5 = None

MGL_RGB5_A1 = None

MGL_RGB8 = None

MGL_RGBA = None

MGL_RGBA12 = None

MGL_RGBA16 = None

MGL_RGBA16F = None

MGL_RGBA2 = None

MGL_RGBA32F = None

MGL_RGBA4 = None

MGL_RGBA8 = None

MGL_RGBA_FLOAT_MODE = None

MGL_RGBA_FLOAT_MODE_ATI = None

MGL_RGBA_MODE = None

MGL_RGBA_UNSIGNED_DOT_PRODUCT_MAPPING_NV = None

MGL_RGB_SCALE = None

MGL_RGB_SCALE_EXT = None

MGL_RIGHT = None

MGL_S = None

MGL_SAMPLES = None

MGL_SAMPLES_ARB = None

MGL_SAMPLES_PASSED_ARB = None

MGL_SAMPLE_ALPHA_TO_COVERAGE = None

MGL_SAMPLE_ALPHA_TO_COVERAGE_ARB = None

MGL_SAMPLE_ALPHA_TO_ONE = None

MGL_SAMPLE_ALPHA_TO_ONE_ARB = None

MGL_SAMPLE_BUFFERS = None

MGL_SAMPLE_BUFFERS_ARB = None

MGL_SAMPLE_COVERAGE = None

MGL_SAMPLE_COVERAGE_ARB = None

MGL_SAMPLE_COVERAGE_INVERT = None

MGL_SAMPLE_COVERAGE_INVERT_ARB = None

MGL_SAMPLE_COVERAGE_VALUE = None

MGL_SAMPLE_COVERAGE_VALUE_ARB = None

MGL_SATURATE_BIT_ATI = None

MGL_SCALAR_EXT = None

MGL_SCALE_BY_FOUR_NV = None

MGL_SCALE_BY_ONE_HALF_NV = None

MGL_SCALE_BY_TWO_NV = None

MGL_SCISSOR_BIT = None

MGL_SCISSOR_BOX = None

MGL_SCISSOR_TEST = None

MGL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING_ARB = None

MGL_SECONDARY_COLOR_ARRAY_EXT = None

MGL_SECONDARY_COLOR_ARRAY_POINTER_EXT = None

MGL_SECONDARY_COLOR_ARRAY_SIZE_EXT = None

MGL_SECONDARY_COLOR_ARRAY_STRIDE_EXT = None

MGL_SECONDARY_COLOR_ARRAY_TYPE_EXT = None

MGL_SECONDARY_COLOR_NV = None

MGL_SECONDARY_INTERPOLATOR_ATI = None

MGL_SELECT = None

MGL_SELECTION_BUFFER_POINTER = None

MGL_SELECTION_BUFFER_SIZE = None

MGL_SEPARATE_SPECULAR_COLOR = None

MGL_SET = None

MGL_SHADER_CONSISTENT_NV = None

MGL_SHADER_OBJECT_ARB = None

MGL_SHADER_OPERATION_NV = None

MGL_SHADE_MODEL = None

MGL_SHININESS = None

MGL_SHORT = None

MGL_SIGNED_ALPHA8_NV = None

MGL_SIGNED_ALPHA_NV = None

MGL_SIGNED_HILO16_NV = None

MGL_SIGNED_HILO_NV = None

MGL_SIGNED_IDENTITY_NV = None

MGL_SIGNED_INTENSITY8_NV = None

MGL_SIGNED_INTENSITY_NV = None

MGL_SIGNED_LUMINANCE8_ALPHA8_NV = None

MGL_SIGNED_LUMINANCE8_NV = None

MGL_SIGNED_LUMINANCE_ALPHA_NV = None

MGL_SIGNED_LUMINANCE_NV = None

MGL_SIGNED_NEGATE_NV = None

MGL_SIGNED_RGB8_NV = None

MGL_SIGNED_RGB8_UNSIGNED_ALPHA8_NV = None

MGL_SIGNED_RGBA8_NV = None

MGL_SIGNED_RGBA_NV = None

MGL_SIGNED_RGB_NV = None

MGL_SIGNED_RGB_UNSIGNED_ALPHA_NV = None

MGL_SINGLE_COLOR = None

MGL_SMOOTH = None

MGL_SOURCE0_ALPHA = None

MGL_SOURCE0_ALPHA_EXT = None

MGL_SOURCE0_RGB = None

MGL_SOURCE0_RGB_EXT = None

MGL_SOURCE1_ALPHA = None

MGL_SOURCE1_ALPHA_EXT = None

MGL_SOURCE1_RGB = None

MGL_SOURCE1_RGB_EXT = None

MGL_SOURCE2_ALPHA = None

MGL_SOURCE2_ALPHA_EXT = None

MGL_SOURCE2_RGB = None

MGL_SOURCE2_RGB_EXT = None

MGL_SOURCE3_ALPHA_NV = None

MGL_SOURCE3_RGB_NV = None

MGL_SPARE0_NV = None

MGL_SPARE0_PLUS_SECONDARY_COLOR_NV = None

MGL_SPARE1_NV = None

MGL_SPECULAR = None

MGL_SPHERE_MAP = None

MGL_SPOT_CUTOFF = None

MGL_SPOT_DIRECTION = None

MGL_SPOT_EXPONENT = None

MGL_SRC_ALPHA = None

MGL_SRC_ALPHA_SATURATE = None

MGL_SRC_COLOR = None

MGL_STACK_OVERFLOW = None

MGL_STACK_UNDERFLOW = None

MGL_STATIC_COPY_ARB = None

MGL_STATIC_DRAW_ARB = None

MGL_STATIC_READ_ARB = None

MGL_STENCIL = None

MGL_STENCIL_BITS = None

MGL_STENCIL_BUFFER_BIT = None

MGL_STENCIL_CLEAR_VALUE = None

MGL_STENCIL_FAIL = None

MGL_STENCIL_FUNC = None

MGL_STENCIL_INDEX = None

MGL_STENCIL_PASS_DEPTH_FAIL = None

MGL_STENCIL_PASS_DEPTH_PASS = None

MGL_STENCIL_REF = None

MGL_STENCIL_TEST = None

MGL_STENCIL_VALUE_MASK = None

MGL_STENCIL_WRITEMASK = None

MGL_STEREO = None

MGL_STREAM_COPY_ARB = None

MGL_STREAM_DRAW_ARB = None

MGL_STREAM_READ_ARB = None

MGL_SUBPIXEL_BITS = None

MGL_SUBTRACT = None

MGL_SUB_ATI = None

MGL_SWIZZLE_STQ_ATI = None

MGL_SWIZZLE_STQ_DQ_ATI = None

MGL_SWIZZLE_STRQ_ATI = None

MGL_SWIZZLE_STRQ_DQ_ATI = None

MGL_SWIZZLE_STR_ATI = None

MGL_SWIZZLE_STR_DR_ATI = None

MGL_T = None

MGL_T2F_C3F_V3F = None

MGL_T2F_C4F_N3F_V3F = None

MGL_T2F_C4UB_V3F = None

MGL_T2F_N3F_V3F = None

MGL_T2F_V3F = None

MGL_T4F_C4F_N3F_V4F = None

MGL_T4F_V4F = None

MGL_TEXTURE = None

MGL_TEXTURE0 = None

MGL_TEXTURE0_ARB = None

MGL_TEXTURE1 = None

MGL_TEXTURE10 = None

MGL_TEXTURE10_ARB = None

MGL_TEXTURE11 = None

MGL_TEXTURE11_ARB = None

MGL_TEXTURE12 = None

MGL_TEXTURE12_ARB = None

MGL_TEXTURE13 = None

MGL_TEXTURE13_ARB = None

MGL_TEXTURE14 = None

MGL_TEXTURE14_ARB = None

MGL_TEXTURE15 = None

MGL_TEXTURE15_ARB = None

MGL_TEXTURE16 = None

MGL_TEXTURE16_ARB = None

MGL_TEXTURE17 = None

MGL_TEXTURE17_ARB = None

MGL_TEXTURE18 = None

MGL_TEXTURE18_ARB = None

MGL_TEXTURE19 = None

MGL_TEXTURE19_ARB = None

MGL_TEXTURE1_ARB = None

MGL_TEXTURE2 = None

MGL_TEXTURE20 = None

MGL_TEXTURE20_ARB = None

MGL_TEXTURE21 = None

MGL_TEXTURE21_ARB = None

MGL_TEXTURE22 = None

MGL_TEXTURE22_ARB = None

MGL_TEXTURE23 = None

MGL_TEXTURE23_ARB = None

MGL_TEXTURE24 = None

MGL_TEXTURE24_ARB = None

MGL_TEXTURE25 = None

MGL_TEXTURE25_ARB = None

MGL_TEXTURE26 = None

MGL_TEXTURE26_ARB = None

MGL_TEXTURE27 = None

MGL_TEXTURE27_ARB = None

MGL_TEXTURE28 = None

MGL_TEXTURE28_ARB = None

MGL_TEXTURE29 = None

MGL_TEXTURE29_ARB = None

MGL_TEXTURE2_ARB = None

MGL_TEXTURE3 = None

MGL_TEXTURE30 = None

MGL_TEXTURE30_ARB = None

MGL_TEXTURE31 = None

MGL_TEXTURE31_ARB = None

MGL_TEXTURE3_ARB = None

MGL_TEXTURE4 = None

MGL_TEXTURE4_ARB = None

MGL_TEXTURE5 = None

MGL_TEXTURE5_ARB = None

MGL_TEXTURE6 = None

MGL_TEXTURE6_ARB = None

MGL_TEXTURE7 = None

MGL_TEXTURE7_ARB = None

MGL_TEXTURE8 = None

MGL_TEXTURE8_ARB = None

MGL_TEXTURE9 = None

MGL_TEXTURE9_ARB = None

MGL_TEXTURE_1D = None

MGL_TEXTURE_1D_BINDING = None

MGL_TEXTURE_2D = None

MGL_TEXTURE_2D_BINDING = None

MGL_TEXTURE_3D = None

MGL_TEXTURE_3D_EXT = None

MGL_TEXTURE_ALPHA_SIZE = None

MGL_TEXTURE_ALPHA_TYPE = None

MGL_TEXTURE_BINDING_1D = None

MGL_TEXTURE_BINDING_2D = None

MGL_TEXTURE_BINDING_CUBE_MAP = None

MGL_TEXTURE_BINDING_CUBE_MAP_ARB = None

MGL_TEXTURE_BINDING_RECTANGLE = None

MGL_TEXTURE_BIT = None

MGL_TEXTURE_BLUE_SIZE = None

MGL_TEXTURE_BLUE_TYPE = None

MGL_TEXTURE_BORDER = None

MGL_TEXTURE_BORDER_COLOR = None

MGL_TEXTURE_BORDER_VALUES_NV = None

MGL_TEXTURE_COMPARE_FAIL_VALUE_ARB = None

MGL_TEXTURE_COMPARE_FUNC_ARB = None

MGL_TEXTURE_COMPARE_MODE_ARB = None

MGL_TEXTURE_COMPARE_OPERATOR_SGIX = None

MGL_TEXTURE_COMPARE_SGIX = None

MGL_TEXTURE_COMPONENTS = None

MGL_TEXTURE_COMPRESSED = None

MGL_TEXTURE_COMPRESSED_ARB = None

MGL_TEXTURE_COMPRESSED_IMAGE_SIZE = None

MGL_TEXTURE_COMPRESSION_HINT = None

MGL_TEXTURE_COMPRESSION_HINT_ARB = None

MGL_TEXTURE_COORD_ARRAY = None

MGL_TEXTURE_COORD_ARRAY_COUNT_EXT = None

MGL_TEXTURE_COORD_ARRAY_EXT = None

MGL_TEXTURE_COORD_ARRAY_POINTER = None

MGL_TEXTURE_COORD_ARRAY_POINTER_EXT = None

MGL_TEXTURE_COORD_ARRAY_SIZE = None

MGL_TEXTURE_COORD_ARRAY_SIZE_EXT = None

MGL_TEXTURE_COORD_ARRAY_STRIDE = None

MGL_TEXTURE_COORD_ARRAY_STRIDE_EXT = None

MGL_TEXTURE_COORD_ARRAY_TYPE = None

MGL_TEXTURE_COORD_ARRAY_TYPE_EXT = None

MGL_TEXTURE_CUBE_MAP = None

MGL_TEXTURE_CUBE_MAP_ARB = None

MGL_TEXTURE_CUBE_MAP_NEGATIVE_X = None

MGL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB = None

MGL_TEXTURE_CUBE_MAP_NEGATIVE_Y = None

MGL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB = None

MGL_TEXTURE_CUBE_MAP_NEGATIVE_Z = None

MGL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB = None

MGL_TEXTURE_CUBE_MAP_POSITIVE_X = None

MGL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB = None

MGL_TEXTURE_CUBE_MAP_POSITIVE_Y = None

MGL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB = None

MGL_TEXTURE_CUBE_MAP_POSITIVE_Z = None

MGL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB = None

MGL_TEXTURE_DEPTH = None

MGL_TEXTURE_DEPTH_EXT = None

MGL_TEXTURE_DEPTH_SIZE_ARB = None

MGL_TEXTURE_DEPTH_TYPE = None

MGL_TEXTURE_DS_SIZE_NV = None

MGL_TEXTURE_DT_SIZE_NV = None

MGL_TEXTURE_ENV = None

MGL_TEXTURE_ENV_COLOR = None

MGL_TEXTURE_ENV_MODE = None

MGL_TEXTURE_FLOAT_COMPONENTS_NV = None

MGL_TEXTURE_GEN_MODE = None

MGL_TEXTURE_GEN_Q = None

MGL_TEXTURE_GEN_R = None

MGL_TEXTURE_GEN_S = None

MGL_TEXTURE_GEN_T = None

MGL_TEXTURE_GEQUAL_R_SGIX = None

MGL_TEXTURE_GREEN_SIZE = None

MGL_TEXTURE_GREEN_TYPE = None

MGL_TEXTURE_HEIGHT = None

MGL_TEXTURE_HI_SIZE_NV = None

MGL_TEXTURE_IMAGE_SIZE_ARB = None

MGL_TEXTURE_INTENSITY_SIZE = None

MGL_TEXTURE_INTENSITY_TYPE = None

MGL_TEXTURE_INTERNAL_FORMAT = None

MGL_TEXTURE_LEQUAL_R_SGIX = None

MGL_TEXTURE_LO_SIZE_NV = None

MGL_TEXTURE_LUMINANCE_SIZE = None

MGL_TEXTURE_LUMINANCE_TYPE = None

MGL_TEXTURE_MAG_FILTER = None

MGL_TEXTURE_MAG_SIZE_NV = None

MGL_TEXTURE_MATRIX = None

MGL_TEXTURE_MAX_ANISOTROPY_EXT = None

MGL_TEXTURE_MIN_FILTER = None

MGL_TEXTURE_PRIORITY = None

MGL_TEXTURE_RECTANGLE = None

MGL_TEXTURE_RED_SIZE = None

MGL_TEXTURE_RED_TYPE = None

MGL_TEXTURE_RESIDENT = None

MGL_TEXTURE_SHADER_NV = None

MGL_TEXTURE_STACK_DEPTH = None

MGL_TEXTURE_WIDTH = None

MGL_TEXTURE_WRAP_R = None

MGL_TEXTURE_WRAP_R_EXT = None

MGL_TEXTURE_WRAP_S = None

MGL_TEXTURE_WRAP_T = None

MGL_TRACK_MATRIX_NV = None

MGL_TRACK_MATRIX_TRANSFORM_NV = None

MGL_TRANSFORM_BIT = None

MGL_TRANSPOSE_COLOR_MATRIX = None

MGL_TRANSPOSE_COLOR_MATRIX_ARB = None

MGL_TRANSPOSE_CURRENT_MATRIX = None

MGL_TRANSPOSE_MODELVIEW_MATRIX = None

MGL_TRANSPOSE_MODELVIEW_MATRIX_ARB = None

MGL_TRANSPOSE_NV = None

MGL_TRANSPOSE_PROJECTION_MATRIX = None

MGL_TRANSPOSE_PROJECTION_MATRIX_ARB = None

MGL_TRANSPOSE_TEXTURE_MATRIX = None

MGL_TRANSPOSE_TEXTURE_MATRIX_ARB = None

MGL_TRIANGLES = None

MGL_TRIANGLE_FAN = None

MGL_TRIANGLE_STRIP = None

MGL_TRUE = None

MGL_UNPACK_ALIGNMENT = None

MGL_UNPACK_IMAGE_HEIGHT = None

MGL_UNPACK_IMAGE_HEIGHT_EXT = None

MGL_UNPACK_LSB_FIRST = None

MGL_UNPACK_ROW_LENGTH = None

MGL_UNPACK_SKIP_IMAGES = None

MGL_UNPACK_SKIP_IMAGES_EXT = None

MGL_UNPACK_SKIP_PIXELS = None

MGL_UNPACK_SKIP_ROWS = None

MGL_UNPACK_SWAP_BYTES = None

MGL_UNSIGNED_BYTE = None

MGL_UNSIGNED_BYTE_3_3_2_EXT = None

MGL_UNSIGNED_IDENTITY_NV = None

MGL_UNSIGNED_INT = None

MGL_UNSIGNED_INT_10_10_10_2_EXT = None

MGL_UNSIGNED_INT_8_8_8_8_EXT = None

MGL_UNSIGNED_INT_S8_S8_8_8_NV = None

MGL_UNSIGNED_INT_S8_S8_8_8_REV_NV = None

MGL_UNSIGNED_INVERT_NV = None

MGL_UNSIGNED_NORMALIZED = None

MGL_UNSIGNED_SHORT = None

MGL_UNSIGNED_SHORT_4_4_4_4_EXT = None

MGL_UNSIGNED_SHORT_5_5_5_1_EXT = None

MGL_V2F = None

MGL_V3F = None

MGL_VARIABLE_A_NV = None

MGL_VARIABLE_B_NV = None

MGL_VARIABLE_C_NV = None

MGL_VARIABLE_D_NV = None

MGL_VARIABLE_E_NV = None

MGL_VARIABLE_F_NV = None

MGL_VARIABLE_G_NV = None

MGL_VARIANT_ARRAY_EXT = None

MGL_VARIANT_ARRAY_POINTER_EXT = None

MGL_VARIANT_ARRAY_STRIDE_EXT = None

MGL_VARIANT_ARRAY_TYPE_EXT = None

MGL_VARIANT_DATATYPE_EXT = None

MGL_VARIANT_EXT = None

MGL_VARIANT_VALUE_EXT = None

MGL_VECTOR_EXT = None

MGL_VENDOR = None

MGL_VERSION = None

MGL_VERTEX_ARRAY = None

MGL_VERTEX_ARRAY_BUFFER_BINDING_ARB = None

MGL_VERTEX_ARRAY_COUNT_EXT = None

MGL_VERTEX_ARRAY_EXT = None

MGL_VERTEX_ARRAY_POINTER = None

MGL_VERTEX_ARRAY_POINTER_EXT = None

MGL_VERTEX_ARRAY_RANGE_LENGTH_NV = None

MGL_VERTEX_ARRAY_RANGE_NV = None

MGL_VERTEX_ARRAY_RANGE_POINTER_NV = None

MGL_VERTEX_ARRAY_RANGE_VALID_NV = None

MGL_VERTEX_ARRAY_RANGE_WITHOUT_FLUSH_NV = None

MGL_VERTEX_ARRAY_SIZE = None

MGL_VERTEX_ARRAY_SIZE_EXT = None

MGL_VERTEX_ARRAY_STRIDE = None

MGL_VERTEX_ARRAY_STRIDE_EXT = None

MGL_VERTEX_ARRAY_TYPE = None

MGL_VERTEX_ARRAY_TYPE_EXT = None

MGL_VERTEX_ATTRIB_ARRAY0_NV = None

MGL_VERTEX_ATTRIB_ARRAY10_NV = None

MGL_VERTEX_ATTRIB_ARRAY11_NV = None

MGL_VERTEX_ATTRIB_ARRAY12_NV = None

MGL_VERTEX_ATTRIB_ARRAY13_NV = None

MGL_VERTEX_ATTRIB_ARRAY14_NV = None

MGL_VERTEX_ATTRIB_ARRAY15_NV = None

MGL_VERTEX_ATTRIB_ARRAY1_NV = None

MGL_VERTEX_ATTRIB_ARRAY2_NV = None

MGL_VERTEX_ATTRIB_ARRAY3_NV = None

MGL_VERTEX_ATTRIB_ARRAY4_NV = None

MGL_VERTEX_ATTRIB_ARRAY5_NV = None

MGL_VERTEX_ATTRIB_ARRAY6_NV = None

MGL_VERTEX_ATTRIB_ARRAY7_NV = None

MGL_VERTEX_ATTRIB_ARRAY8_NV = None

MGL_VERTEX_ATTRIB_ARRAY9_NV = None

MGL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING_ARB = None

MGL_VERTEX_ATTRIB_ARRAY_ENABLED = None

MGL_VERTEX_ATTRIB_ARRAY_NORMALIZED = None

MGL_VERTEX_ATTRIB_ARRAY_POINTER = None

MGL_VERTEX_ATTRIB_ARRAY_SIZE = None

MGL_VERTEX_ATTRIB_ARRAY_STRIDE = None

MGL_VERTEX_ATTRIB_ARRAY_TYPE = None

MGL_VERTEX_PROGRAM = None

MGL_VERTEX_PROGRAM_BINDING_NV = None

MGL_VERTEX_PROGRAM_NV = None

MGL_VERTEX_PROGRAM_POINT_SIZE = None

MGL_VERTEX_PROGRAM_POINT_SIZE_NV = None

MGL_VERTEX_PROGRAM_TWO_SIDE = None

MGL_VERTEX_PROGRAM_TWO_SIDE_NV = None

MGL_VERTEX_SHADER_ARB = None

MGL_VERTEX_SHADER_BINDING_EXT = None

MGL_VERTEX_SHADER_EXT = None

MGL_VERTEX_SHADER_INSTRUCTIONS_EXT = None

MGL_VERTEX_SHADER_INVARIANTS_EXT = None

MGL_VERTEX_SHADER_LOCALS_EXT = None

MGL_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = None

MGL_VERTEX_SHADER_OPTIMIZED_EXT = None

MGL_VERTEX_SHADER_VARIANTS_EXT = None

MGL_VERTEX_STATE_PROGRAM_NV = None

MGL_VERTEX_WEIGHTING_EXT = None

MGL_VERTEX_WEIGHT_ARRAY_EXT = None

MGL_VERTEX_WEIGHT_ARRAY_POINTER_EXT = None

MGL_VERTEX_WEIGHT_ARRAY_SIZE_EXT = None

MGL_VERTEX_WEIGHT_ARRAY_STRIDE_EXT = None

MGL_VERTEX_WEIGHT_ARRAY_TYPE_EXT = None

MGL_VIBRANCE_BIAS_NV = None

MGL_VIBRANCE_SCALE_NV = None

MGL_VIEWPORT = None

MGL_VIEWPORT_BIT = None

MGL_WEIGHT_ARRAY_BUFFER_BINDING_ARB = None

MGL_WRITE_ONLY_ARB = None

MGL_W_EXT = None

MGL_XOR = None

MGL_X_EXT = None

MGL_Y_EXT = None

MGL_ZERO = None

MGL_ZERO_EXT = None

MGL_ZOOM_X = None

MGL_ZOOM_Y = None

MGL_Z_EXT = None

TEXTURE_COORD_ARRAY_BUFFER_BINDING_ARB = None

kA8 = None

kA8B8G8R8 = None

kB5G5R5A1 = None

kB5G6R5 = None

kB8G8R8A8 = None

kB8G8R8X8 = None

kCubeMap = None

kD24S8 = None

kD24X8 = None

kD32_FLOAT = None

kDXT1_UNORM = None

kDXT1_UNORM_SRGB = None

kDXT2_UNORM = None

kDXT2_UNORM_PREALPHA = None

kDXT2_UNORM_SRGB = None

kDXT3_UNORM = None

kDXT3_UNORM_PREALPHA = None

kDXT3_UNORM_SRGB = None

kDXT4_SNORM = None

kDXT4_UNORM = None

kDXT5_SNORM = None

kDXT5_UNORM = None

kDepthTexture = None

kEnvCrossHoriz = None

kEnvCrossVert = None

kEnvCubemap = None

kEnvHemiSphere = None

kEnvLatLong = None

kEnvNone = None

kEnvSphere = None

kImage1D = None

kImage1DArray = None

kImage2D = None

kImage2DArray = None

kL16 = None

kL8 = None

kMGLext_ARB_OpenMGL20 = None

kMGLext_ARB_color_buffer_float = None

kMGLext_ARB_depth_texture = None

kMGLext_ARB_fragment_program = None

kMGLext_ARB_fragment_program_shadow = None

kMGLext_ARB_half_float_pixel = None

kMGLext_ARB_matrix_palette = None

kMGLext_ARB_occlusion_query = None

kMGLext_ARB_point_parameters = None

kMGLext_ARB_shadow = None

kMGLext_ARB_shadow_ambient = None

kMGLext_ARB_texgen_reflection = None

kMGLext_ARB_texture_env_crossbar = None

kMGLext_ARB_texture_float = None

kMGLext_ARB_texture_non_power_of_two = None

kMGLext_ARB_texture_rectangle = None

kMGLext_ARB_vertex_blend = None

kMGLext_ARB_vertex_buffer_object = None

kMGLext_ARB_vertex_program = None

kMGLext_ATI_fragment_shader = None

kMGLext_ATI_pixel_format_float = None

kMGLext_EXT_compiled_vertex_array = None

kMGLext_EXT_cull_vertex = None

kMGLext_EXT_fog_coord = None

kMGLext_EXT_secondary_color = None

kMGLext_EXT_texture_filter_anisotropic = None

kMGLext_EXT_vertex_shader = None

kMGLext_EXT_vertex_weighting = None

kMGLext_MGLX_choose_fbconfig = None

kMGLext_MGLX_choose_fbconfig_sgix = None

kMGLext_MGLX_create_context_with_config_sgix = None

kMGLext_MGLX_create_new_context = None

kMGLext_MGLX_create_pbuffer = None

kMGLext_MGLX_create_pbuffer_sgix = None

kMGLext_MGLX_destroy_pbuffer = None

kMGLext_MGLX_destroy_window = None

kMGLext_MGLX_get_visual_from_fbconfig_sgix = None

kMGLext_NUMBER_OF_EXTENSIONS = None

kMGLext_NV_fence = None

kMGLext_NV_float_buffer = None

kMGLext_NV_fragment_program = None

kMGLext_NV_occlusion_query = None

kMGLext_NV_primitive_restart = None

kMGLext_NV_register_combiners = None

kMGLext_NV_texture_shader = None

kMGLext_NV_vertex_array_range = None

kMGLext_NV_vertex_program = None

kMGLext_SGIS_generate_mipmap = None

kMGLext_SGIX_depth_texture = None

kMGLext_SGIX_shadow = None

kMGLext_WMGL_ARB_buffer_region = None

kMGLext_WMGL_ARB_extensions_string = None

kMGLext_WMGL_ARB_make_current_read = None

kMGLext_WMGL_ARB_pbuffer = None

kMGLext_WMGL_ARB_pixel_format = None

kMGLext_WMGL_ARB_render_texture = None

kMGLext_WMGL_NV_allocate_memory = None

kMGLext_bgra = None

kMGLext_blend_color = None

kMGLext_blend_minmax = None

kMGLext_blend_subtract = None

kMGLext_color_matrix = None

kMGLext_color_table = None

kMGLext_convolution = None

kMGLext_draw_range_elements = None

kMGLext_frame_buffer_object = None

kMGLext_histogram = None

kMGLext_imaging_subset = None

kMGLext_multi_draw_arrays = None

kMGLext_multisample = None

kMGLext_multitexture = None

kMGLext_packed_pixels = None

kMGLext_rescale_normal = None

kMGLext_separate_specular_color = None

kMGLext_texture3D = None

kMGLext_texture_border_clamp = None

kMGLext_texture_compression = None

kMGLext_texture_compression_s3tc = None

kMGLext_texture_cube_map = None

kMGLext_texture_edge_clamp = None

kMGLext_texture_env_add = None

kMGLext_texture_env_combine = None

kMGLext_texture_env_dot3 = None

kMGLext_texture_lod = None

kMGLext_transpose_matrix = None

kNumberOfEnvMapTypes = None

kNumberOfRasterFormats = None

kNumberOfTextureTypes = None

kR10G10B10A2_UINT = None

kR10G10B10A2_UNORM = None

kR16G16B16A16_FLOAT = None

kR16G16B16A16_SINT = None

kR16G16B16A16_SNORM = None

kR16G16B16A16_UINT = None

kR16G16B16A16_UNORM = None

kR16G16_FLOAT = None

kR16G16_SINT = None

kR16G16_SNORM = None

kR16G16_UINT = None

kR16G16_UNORM = None

kR16_FLOAT = None

kR16_SINT = None

kR16_SNORM = None

kR16_UINT = None

kR16_UNORM = None

kR1_UNORM = None

kR24G8 = None

kR24X8 = None

kR32G32B32A32_FLOAT = None

kR32G32B32A32_SINT = None

kR32G32B32A32_UINT = None

kR32G32B32_FLOAT = None

kR32G32B32_SINT = None

kR32G32B32_UINT = None

kR32G32_FLOAT = None

kR32G32_SINT = None

kR32G32_UINT = None

kR32_FLOAT = None

kR32_SINT = None

kR32_UINT = None

kR8G8B8A8_SINT = None

kR8G8B8A8_SNORM = None

kR8G8B8A8_UINT = None

kR8G8B8A8_UNORM = None

kR8G8B8X8 = None

kR8G8_SINT = None

kR8G8_SNORM = None

kR8G8_UINT = None

kR8G8_UNORM = None

kR8_SINT = None

kR8_SNORM = None

kR8_UINT = None

kR8_UNORM = None

kR9G9B9E5_FLOAT = None

kVolumeTexture = None
