#!/net/apps/spinux1/aw/maya2012-5.0SPI/bin/mayapy
from __future__ import with_statement
import re, os, logging
import maya.standalone
maya.standalone.initialize()

import maya.cmds as MC
import maya.mel as MM


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def funcString(func):
    '''
    Make a string version of a function that can be written to disk
    @param func = 'bindSkin' or similar
    '''    
    cmdsFunc  = getattr(MC, func)
    try:
        helpDoc = MM.eval('help %s' % func)        
        if not re.search('Command Type: Command', helpDoc):
            return ""
    except RuntimeError:
        return ''
    except TypeError:
        logger.warning("helpDoc = %r" % helpDoc)
        return ''
    
    result = '''
def %s(*args, **kwargs):
    """
    %s
    """
''' % (func, helpDoc.strip())

    return result

def makeStubFile(dirname):
    '''
    Generate stub files in a directory, directory
    '''
    #get a set of directories
    if not os.path.isdir(dirname):
        raise Exception ("provide a directory")
    cmdsFile = os.path.join(dirname, 'maya')
    if not os.path.exists(cmdsFile):
        os.mkdir(cmdsFile)
    cmdsFile = os.path.join(cmdsFile, 'cmds')
    if not os.path.exists(cmdsFile):
        os.mkdir(cmdsFile)
    cmdsFile = os.path.join(cmdsFile, '__init__.py')
    
    funcs = dir(MC)
    with open(cmdsFile, 'w') as cmdsFile:
        cmdsFile.seek(0)
        cmdsFile.truncate()
        for func in funcs:
            cmdStr = funcString(func)
            if cmdStr:
                logger.info('writing %s' % func)
                cmdsFile.write(cmdStr)


if __name__ == '__main__':
    try:
        dirname = sys.argv[1]
    except:
        dirname = os.environ.get('HOME')
        logger.warning("No directory provided.  Making files in %s" % dirname)
    makeStubFile(dirname)
