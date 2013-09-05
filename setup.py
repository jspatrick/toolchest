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

def setupJedi():    
    path = os.environ.get('PATH', '').split(':')
    if toolchest_dir not in path:
        path.insert(0, toolchest_dir)
        os.environ['PATH'] = ':'.join(path)
 
    jedi_path = os.path.join(toolchest_dir, 'emacs/elpa/jedi-20130714.1415/')
    os.chdir(jedi_path)
    p = subprocess.Popen('make requirements', stdout=subprocess.PIPE, shell=True)
    print "seting up jedi - this requires an internet connection..."
    print p.communicate()


def main():
    makeLinks()
    setupJedi()

main()
    
        
