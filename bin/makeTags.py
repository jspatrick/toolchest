#!/usr/local/bin/python
'''
Create tag files
'''
from __future__ import with_statement
import subprocess, os, string, logging, optparse, re
if not logging.getLogger().handlers:
    logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("makeTags")
logger.setLevel(logging.INFO)


MEL_REGEX = r'/^(global)*[ \t]*(proc)([ \t]+(int|float|string|matrix|vector))?([ \t]*\[[ \t]*\][ \t]*)?([ \t])+([a-zA-Z0-9_]+).*/\7/f,definition/'

def execCmd(args, shell=False):
    '''
    Convenience wrapper
    '''
    p = subprocess.Popen(args, shell=shell, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = p.communicate()
    if err:
        raise RuntimeError("command error: %s" % err)
    else:
        return out

def appendFile(f1, f2):
    '''
    Append f2 to f1
    '''
    with open(f1, 'a') as f1:
        f1.seek(0, os.SEEK_END)
        with open(f2, 'r') as f2:
            f1.write(f2.read())

class TagMaker(object):
    def __init__(self, mayaver = None, tagsDir = None, show=None, emacs=True):
        self.emacsFlag = 'e' if emacs else ''
        
        #make different tag files for
        if not mayaver:
            mayaver = 'maya%s' % os.environ.get('MAYA_SHOW_VERSION', None)
        else:
            if not mayaver.startswith('maya'):
                mayaver = 'maya%s' % mayaver
        if not re.match('maya20[0-9]{2}', mayaver):
            raise RuntimeError("Bad maya verion name '%s'" % mayaver)
        if not mayaver:
            raise RuntimeError("Cannot get maya version.  Setshot or pass in manually")

        if not tagsDir:
            tagsDir = os.environ['HOME']

        self.tagFiles = {'live': 'TAGS_live',
                         'dev': 'TAGS_dev'}

        for k, tag in self.tagFiles.items():
            self.tagFiles[k] = os.path.join(tagsDir, tag)
        self.tagsDir = tagsDir

        #get the shows - always spi
        self.shows = ['spi']
        if not show:
            show = os.getenv('SHOW', None)
        if not show or show == 'spi':
            logger.warning("Not set to a show - tags will only be generated for SPI!")
        else:
            self.shows.insert(0, show)

        #ignore chars for now or we'll end up parsing tons of clipboard .ma files, etc
        liveDirs = ['/shots/$show/home/%s_prod/scripts/tools' % mayaver,
        #'/shots/$show/home/%s_prod/scripts/chars' % mayaver,
                    '/shots/$show/home/%s_prod/scripts/other' % mayaver,
                   '/shots/$show/home/%s_sw/scripts/tools' % mayaver,
                   '/shots/$show/home/%s_sw/scripts/chars' % mayaver,
                   '/shots/$show/home/%s_sw/scripts/other' % mayaver]
        #'/shots/$show/home/%s_prod/python/common' % mayaver,
        #'/shots/$show/home/%s_sw/python/common' % mayaver]

        u = os.environ['USER']
        devDirs = ['/shots/$show/home/dev/%s/%s_prod/scripts/tools' % (u,mayaver),
                   '/shots/$show/home/dev/%s/%s_prod/scripts/others' % (u,mayaver),
        #'/shots/$show/home/dev/%s/%s_prod/scripts/chars' % (u,mayaver),
                   '/shots/$show/home/dev/%s/%s_sw/scripts/tools' % (u,mayaver),
                   '/shots/$show/home/dev/%s/%s_sw/scripts/others' % (u,mayaver),
                   '/shots/$show/home/dev/%s/%s_sw/scripts/chars' % (u,mayaver)]
        #'/shots/$show/home/dev/%s/%s_prod/python' % (u,mayaver)]

        self.live_templates = [string.Template(x) for x in liveDirs]
        self.dev_templates = [string.Template(x) for x in devDirs]


        self.tagsCmdTemplate = string.Template( """
ctags -a%sf $tagsFile --langdef=mel \
--regex-mel='%s' --langmap=mel:.mel \
--languages=mel --links=yes -R $searchDir
""" % (self.emacsFlag, MEL_REGEX))

    def rmTags(self, tagTypes=['dev', 'live']):
        for tagType in tagTypes:
            tPath = self.tagFiles[tagType]
            if os.path.exists(tPath):
                logger.info('deleting %s' % tPath)
                os.remove(tPath)

    def mkTags(self, tagType='live'):
        ''' make tag files '''


        if tagType not in self.tagFiles:
            raise RuntimeError("invalid type '%s' % tagType")
        self.rmTags(tagTypes=[tagType])

        dirList = []
        for show in self.shows:
            templates = getattr(self, "%s_templates" % tagType)
            for template in templates:

                #skip chars that aren't dev or spi
                if template.template.endswith('/chars') and not (show ==  'spi' or tagType == 'dev'):
                    logger.info("Skipping %s" % template.template)
                    continue

                dir_ = template.substitute(show=show)

                if not os.path.exists(dir_):
                    logger.debug("Skipping non-existant %s" % dir_)
                    continue

                tagFile = self.tagFiles[tagType]
                created = False
                if not os.path.exists(tagFile):
                    created=True

                strCmd = self.tagsCmdTemplate.substitute(tagsFile=tagFile, searchDir=dir_)

                logger.debug("Executing: %s" % strCmd)
                result = execCmd(strCmd, shell=True)
                if result:
                    logger.info(result)
                logger.info("%s Tags Index: %s" % \
                            (created and "Created" or "Appended to", tagFile))


    def combineFiles(self, typeList=["dev","live"], newFile='TAGS'):
        '''
        Combine the tag files in order listed
        '''
        newPath = os.path.join(self.tagsDir, newFile)
        if os.path.exists(newPath):
            os.remove(newPath)
        for tagType in typeList:
            if os.path.exists(self.tagFiles[tagType]):
                appendFile(newPath, self.tagFiles[tagType])
            else:
                logger.warning('Skipping non-existent file: %s' % self.tagFiles[tagType])

if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option('-s', '--show', dest='show',
                      default=os.environ.get('SHOW', None),
                      help='make tags for SHOW')
    parser.add_option('-o', '--outdir', dest='outdir',
                      default=os.environ['HOME'],
                      help='create tag files in DIR')
                      
    parser.add_option('-t', '--standardTags', dest='emacs',
                      default=True, action='store_false',
                      help='create "standard" tag files for non-emacs editors')
                      
    parser.add_option('-m', '--mayaver', dest='mayaver',
                      default='maya2013')

    parser.add_option('-v', '--verbose', dest='verbose', action='store_true',
                      default=False, help='print tags commands')

    opts, args = parser.parse_args()

    if opts.verbose:
        logger.setLevel(logging.DEBUG)

    tagMaker = TagMaker(show=opts.show, mayaver=opts.mayaver, tagsDir = opts.outdir, emacs=opts.emacs)

    tagMaker.rmTags()
    tagMaker.mkTags(tagType='live')
    tagMaker.mkTags(tagType='dev')
    tagMaker.combineFiles(['dev', 'live'])

