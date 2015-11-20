#!/usr/bin/env python
import os
import sys
import pdb
import re


def translate(myString):
    #m = re.search(r"(&#8211;)",myString)
    #m = re.findall(r"(&#82..);",myString,re.MULTILINE)
    #m = re.sub(r'(&#8\d\d\d.)','XYZ',myString,re.MULTILINE)
    m = re.sub('(&#8243;)','"',myString,re.MULTILINE)
    mm = re.sub('(&#8211;)','-',m,re.MULTILINE)
    pdb.set_trace()
   
    print mm
    return mm


def process(file):
    filein = open (file,'r')
    goodStuff = translate( filein.read() )
    ofile=file +".cooked"
    fileout = open (ofile,'w')
    fileout.write(goodStuff)
    fileout.close()

def main():
    '''translate chars!'''
#    setup()
    print 'hello'
    rootDir="."
    for dirName, subdirList, fileList in os.walk(rootDir):
         for fname in fileList:
            if ".csv" in fname:
                 myfile=  os.path.join(dirName , fname)
                 process(myfile)


# Here's our payoff idiom!
if __name__ == '__main__':
    main()


