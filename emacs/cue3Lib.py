import Cue3

import re
import StringIO
import sys
import os
import urllib

from datetime import datetime

Cue3.loadWrappers()

stateDict = {Cue3.JobState.Finished : 'Finished',
             Cue3.JobState.Pending : 'Pending',
             Cue3.JobState.Posted : 'Posted',
             Cue3.JobState.Shutdown : 'Shutdown',
             Cue3.JobState.Shutdown : 'Finished'}

def getFrameList(job):
    job = Cue3.findJob(job)
    buf = StringIO.StringIO()
    if not job:
        return
    for frame in job.getFrames():
        buf.write('  o %s\n' % frame.name())

    sys.stdout.write(buf.getvalue())
        
def getJobState(job):
    if job.data.state == Cue3.JobState.Finished:
        return "Finished"
    if job.data.isPaused:
        return "Paused"
    if job.stats.deadFrames > 0:
        return "Failing"
    return "Running"

def getJobList(expr, expand=None):
    buf = StringIO.StringIO()

    for job in Cue3.getJobs(regex=expr):
        if not re.search(expr, job.name()):
            continue

        status = getJobState(job)
        
        percent = float(job.percentCompleted())

        hasComment = " "
        if job.isCommented():
            hasComment = "C"

        if expand and re.match(expand, job.name()):
            buf.write('-%-10s %s %s %s\n' % (status, percentToString(percent), hasComment, job.name()))
            for frame in job.getFrames():
                rtime = '%s:%s' % (frame.runTime()/60, frame.runTime() % 60)
                mem = float(frame.memUsed()) / 1024.0
                memStr = '%.2f MB' % mem
                if mem > 1000:
                    mem = mem/1000.0
                    memStr = '%.2f GB' % mem
                try:
                    buf.write('-    %-50s    %-12s   %-16s  %8s   %s\n' % (frame.data.name, frame.data.state, frame.data.lastResource, rtime, memStr))
                except:
                    print(frame.data)
        else:            
            buf.write('+%-10s %s %s %s\n' % (status, percentToString(percent), hasComment, job.name()))
        
    sys.stdout.write(buf.getvalue())

def percentToString(percent):
    cap = int(float(percent)/10.0)
    return '[%s%s]' % ('*' * cap, '-' * (10 - cap))
    
def getJobListAsLISP(expr, expand=None):
    buf = StringIO.StringIO()
    buf.write("(")
    for job in Cue3.getJobs(regex=expr):
        if not re.search(expr, job.name()):
            continue

        status = getJobState(job)

        frData = []
        
        if expand and re.search(expand, job.name()):
            for fr in job.getFrames():
                frData.append('(%s "%s" "%s")' % (fr.data.number, fr.data.layerName, fr.data.state))

        percent = job.percentCompleted()
        comment = " "
        if job.isCommented():
            comment = "C"

        buf.write('("%s" "%s" %s %s' % (job.name(), status, comment, percent))
        for item in frData:
            buf.write('\n%s' % item)
        buf.write(')\n')
                
    buf.write(')')
    sys.stdout.write(buf.getvalue())

def pauseJobs(*args):
    for job in Cue3.getJobs(job=args):
        job.pause()        

def resumeJobs(*args):
    for job in Cue3.getJobs(job=args):
        job.resume()        

def killJob(job):
    jobs = Cue3.getJobs(job=job)
    if jobs:
        jobs[0].kill()
        
def killFrame(job, frame):
    jobs = Cue3.getJobs(job=job)
    if jobs:
        for fr in jobs[0].getFrames():
            if fr.data.name == frame:
                fr.kill()
                return

def eatFrame(job, frame):
    jobs = Cue3.getJobs(job=job)
    if jobs:
        lyr = [x for x in jobs[0].getFrames() if x.name() == frame]
        if lyr:
            # drop depends
            for dep in lyr[0].getWhatDependsOnThis():
                dep.satisfy()
            lyr[0].eat()
            
def retryFrame(job, frame):
    jobs = Cue3.getJobs(job=job)
    if jobs:
        for fr in jobs[0].getFrames():
            if fr.data.name == frame:
                fr.retry()
                return

def retryAllDeadFrames(job):
    jobs = Cue3.getJobs(job=job)
    if jobs:
        for fr in jobs[0].getFrames():
            if re.match('Dead', str(fr.data.state)):
                fr.retry()
            
def resumeJob(jobid, frame=None):
    jobs = Cue3.getJobs(job=jobid)

    if frame:
        fr = [x for x in jobs[0].getFrames() if x.data.name == frame]
        if fr:
            fr.retry()
    else:
        for job in jobs:
            job.resume()

def getLogFilePath(jobName, frame):
    jobs = Cue3.getJobs(job=jobName)
    for fr in jobs[0].getFrames():
        if fr.data.name == frame:
            #print (os.path.join(jobs[0].logDir(), '%s.%s.rqlog' % (jobs[0].name(), fr.data.name)))
            url = 'http://cue3stat.spimageworks.com/?mode=log&path=%s' % (os.path.join(jobs[0].logDir(), '%s.%s.rqlog' % (jobs[0].name(), fr.data.name)))
            fh = urllib.urlopen(url)
            data = fh.read()
            fh.close()
            print data

                    
def satisfyDepends(jobName, frame):
    jobs = Cue3.getJobs(job=jobName)
    for fr in jobs[0].getFrames():
        if fr.data.name == frame:
            for dep in fr.getWhatThisDependsOn():
                dep.satisfy()


def addComment(jobName, subject, comment): 
    jobs = Cue3.getJobs(job=jobName)
    job = jobs[0]

    if subject is None:
        subject = ''
    if comment is None:
        comment = ''

    job.addComment(subject,comment)

def getComments(jobName) :
    cstr = ""
    try:
        jobs = Cue3.getJobs(job=jobName)
        job = jobs[0]
        comments = job.getComments()
        for c in comments:
            ts = datetime.fromtimestamp(c.timestamp()).strftime('%Y-%m-%d %H:%M:%S')            
            cstr +=  '  [%s]\n' % (c.user() +' : ' + ts + ' : ' + c.subject() +' : ' + c.message())
    except Exception, e:
        print e.__str__()
    print cstr
    


def getOutputs(jobName, frame=None):
    try:
        jobs = Cue3.getJobs(job=jobName)
        if jobs:
            layers = jobs[0].getLayers()
            #print(layers)
            if frame:
                frame = re.sub(r'[\d]+-', '', frame)
                layers = [x for x in jobs[0].getLayers() if x.data.name == frame]
            else:
                layers = jobs[0].getLayers()
            
            if layers:
                outputs = layers[0].proxy.getOutputPaths()
                print(' '.join([x for x in outputs]))
    except:
        pass
        
if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser()

    parser.add_option('-j', '--job', dest='job')
    parser.add_option('-p', '--pause', dest='pause', default=False, action='store_true')
    parser.add_option('-r', '--resume', dest='resume', default=False, action='store_true')
    parser.add_option('-k', '--kill', dest='kill', default=False, action='store_true')
    parser.add_option('-l', '--list', dest='list', default=False, action='store_true')
    parser.add_option('',   '--lisp', dest='lisp', default=False, action='store_true')
    parser.add_option('-e', '--expandFrames', dest='expandFrames')
    parser.add_option('-f', '--frame', dest='frame')
    parser.add_option('-g', '--getLogFile', dest='logFile', default=False, action='store_true')
    parser.add_option('-a', '--allFrames', dest='allFrames', default=False, action='store_true')
    parser.add_option('-x', '--eatFrame', dest='eatFrame', default=False, action='store_true')
    parser.add_option('-d', '--depends', dest='depends', default=False, action='store_true')
    parser.add_option('-o', '--outputs', dest='outputs', default=False, action='store_true')
    parser.add_option('-c', '--comment', dest='comment', default=None)
    parser.add_option(      '--subject', dest='subject', default=None)
    parser.add_option('--getComments', dest='getComment',default=False,action='store_true')
    
    (options, args) = parser.parse_args()
    
    # args are jobnames
    if options.pause:
        pauseJobs(*args)

    if options.eatFrame:
        eatFrame(args[0], options.frame)
        
    if options.kill:
        if options.frame:
            killFrame(args[0], options.frame)
        else:
            killJob(args[0])
        
    if options.resume:
        if options.allFrames:
            retryAllDeadFrames(args[0])
        elif options.frame:
            retryFrame(args[0], options.frame)
        else:
            resumeJobs(*args)

    if options.logFile:
        getLogFilePath(args[0], options.frame)

    if options.list:
        getJobList(args[0], options.expandFrames)

    if options.lisp:
        getJobListAsLISP(args[0], options.expandFrames)

    if options.depends:
        satisfyDepends(args[0], options.frame)
        
    if options.outputs:
        getOutputs(args[0], options.frame)

    if (options.comment is not None) or (options.subject is not None):
        addComment(args[0], options.subject, options.comment)

    if options.getComment:
        getComments(args[0])
