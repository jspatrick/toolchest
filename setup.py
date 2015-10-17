#!/usr/bin/python
"""
Install my dev setup
 - emacs config
 - virtual_env for emacs
 - jedi setup for emacs
 - tools/binaries
 - shell scripts
 - aliases
"""

import os, logging, shutil, sys
import subprocess

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger("ToolchestSetup")

def thisDir():
    module = sys.modules.get(__name__, None)
    if hasattr(module, '__file__'):
        return os.path.dirname(os.path.abspath(__file__))

    cwd = os.getcwd()
    if not cwd.endswith('toolchest'):
        raise RuntimeError("Cannot determine current directory")
        
    return cwd


toolchest_dir = thisDir()

def getShell():
    return os.environ.get('SHELL', 'bash').split('/')[-1]

symlinks = {os.path.join(toolchest_dir, 'emacs'): '~/.emacs.d',
            os.path.join(toolchest_dir, 'shell', 'aliases.csh'): '~/.aliases',
            os.path.join(toolchest_dir, 'shell', 'aliases.bash'): '~/.aliases',
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
        
        
link_predicates = {os.path.join(toolchest_dir, 'shell', 'spi_aliases.csh'): 
                       EnvironmentPredicate('HOST', expectedValue='shark257.spimageworks.com'),
                   os.path.join(toolchest_dir, 'shell', 'aliases.csh'):
                       EnvironmentPredicate('SHELL', expectedValue='/bin/csh'),
                   os.path.join(toolchest_dir, 'shell', 'aliases.bash'):
                       EnvironmentPredicate('SHELL', expectedValue='/bin/bash')}
    

def full_path(path):
    p = os.path.expanduser(os.path.expandvars(path))
    p = os.path.abspath(p)
    return p

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

        target = full_path(target)
        link = full_path(link)
        if not os.path.exists(target):
            raise RuntimeError("target %s does not exist" % target)
        _logger.info("Processing %s -> %s" % (link, target))        
        
        #check existing predicates

        pred = link_predicates.get(target, None)
        if pred is not None:
            if not pred():
                _logger.info("Skipping %s" % target)
                continue
        else:
            print "No predicate for %s" % link

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


main()
    
        
