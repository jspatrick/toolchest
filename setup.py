#!/usr/bin/python
import os, logging, shutil, sys
import subprocess

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger("ToolchestSetup")

def thisDir():
    if not __file__:
        cwd = os.getcwd()
        testval = lambda x: x
        thisFile = sys.modules[test.__module__].__file__        
    else:
        thisFile = os.path.abspath(__file__)
        
    return os.path.dirname(thisFile)

    
toolchest_dir = thisDir()

symlinks = {os.path.join(toolchest_dir, 'emacs'): '~/.emacs.d',
            os.path.join(toolchest_dir, 'shell', 'aliases.csh'): '~/.aliases',
            os.path.join(toolchest_dir, 'shell', 'spi_aliases.csh'): '~/.spi_aliases',
            os.path.join(toolchest_dir, 'shell', 'spi_jump.csh'): '~/spi_jump.csh',
            os.path.join(toolchest_dir, 'shell', 'set_python_path.csh'): '~/set_python_path.csh'
            }


class EnvironmentPredicate(object):
    def __init__(self, var, expectedValue=None):
        self.var = var
        self.expectedValue = expectedValue
        
    def __call__(self):
        
        val =  os.environ.get(self.var, None)
        if self.expectedValue is not None:
            if val != self.expectedValue:
                return False
        if val is None:
            return False
        return True
        
        
link_predicates = {'~/.spAliases': EnvironmentPredicate('HOST', expectedValue='shark257.spimageworks.com')}
    
def expandedPath(path):
    return os.path.expanduser(os.path.expandvars(path))


def moveToBackup(filepath, backupToken = 'bak'):
    """
    Move filepath to a backup location
    @return: the new file path     
    """
    i = 1
    basePath = '%s.%s' % (filepath, backupToken)
    newPath = basePath
    while os.path.exists(newPath):
        newPath = '%s.%i' % (basePath, i)
        i += 1
        if i >= 10:
            raise RuntimeError("Cannot get backup path for %s" % filepath)

    shutil.move(filepath, newPath)
    return newPath

    
def makeLinks():    
    for target, link in symlinks.iteritems():

        target = expandedPath(target)
        link = expandedPath(link)
        if not os.path.exists(target):
            raise RuntimeError("target %s does not exist" % target)
        _logger.info("Processing %s -> %s" % (link, target))        
        
        #check existing predicates
        pred = link_predicates.get(target, None)
        if pred and not pred():
            _logger.info("Skipping %s" % target)
            continue
        
        #if the link exists but is not pointing to target...        
        #os.path.exists is false for bad simlinks, so also check if it's a link
        if os.path.exists(link) or os.path.islink(link):
            
            if os.path.islink(link):            
                _logger.warning("Deleting existing link %s to create new one" % (link))
                os.unlink(link)
            else:
                backedup = moveToBackup(link)
                _logger.warning("Moved existing file %s to %s" % (link, backedup))

            
        os.symlink(target, link)

        
def main():
    makeLinks()

if __name__ == '__main__':
    main()
