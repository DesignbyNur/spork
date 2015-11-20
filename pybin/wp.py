#!/usr/bin/env python
import os
import sys
import pdb
import subprocess


def runWP(command):
    print "command ",command, "\n"
    status = subprocess.Popen("wp %s"%command , shell=True)
    print "status ",status, "\n"
    return status



def main():
    '''Run a wp command  !'''
#    setup()
    pdb.set_trace()
    print 'hello'


    try: 
        runWP("core version")
    except SystemExit:
        sys.exit()




# Here's our payoff idiom!
if __name__ == '__main__':
    main()


