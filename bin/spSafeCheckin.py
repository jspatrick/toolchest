#!/usr/bin/python
import sys, subprocess

#https://www.siafoo.net/snippet/88
COLORS = {'grey': 30,
          'red': 31,
          'green': 32,
          'yellow': 33,
          'blue': 34,
          'magenta': 35}


def getFormattedString(string, color):    
    if not sys.stdout.isatty():
        return string
    #
    base =  '\033[%sm%s\033[0m'    
    code = COLORS[color]
    return base % (code, string)
          
def isPylintSuccessful(fpath):
    args = ['pylint', '-E']
    args.append(fpath)
    process = subprocess.Popen(args, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
    result = process.communicate()        
    returnCode = process.returncode
    
    if returnCode != 0:        
        sys.stderr.write(getFormattedString(result[0], 'red'))
        sys.stderr.write(getFormattedString(result[1], 'red'))
        return False
    
    return True
    
        
                     

if __name__ == '__main__':
    failed = []
    
    for arg in sys.argv[1:]:
        if arg.endswith('.py'):
           if not isPylintSuccessful(arg):
               failed.append(arg)

    if failed:
        sys.stderr.write("\n%s failed pylint check\n" % ', '.join(failed))        
        sys.exit(2)
    else:
        args = ['vcci']
        args.extend(sys.argv[1:])
        subprocess.call(args)
        
    sys.exit(0)
    
