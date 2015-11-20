#!/usr/bin/env python
import os
import sys
import pdb
import string

menuStuff=""
footerStuff=""

def processHTM(file):
    print file
    #pdb.set_trace()
    (head,tail) = os.path.split(file)
    newfile='/work/html/dbn/eng/' + tail
    filein = open (file,'r')
    goodStuff = parseHtm( filein.read() )
    storeStuff(newfile,goodStuff)

def storeStuff(ofile,goodStuff):
    global menuStuff,footerStuff

    fileout = open (ofile,'w')
    goodStuff = addTemplate(goodStuff)
    fileout.write(goodStuff) 
    fileout.close()


# our globals for parse
findStart = '<!-- InstanceBeginEditable name="yaz" -->'
findEnd = '<!-- InstanceEndEditable -->'


def parseHtm(page):
    save = False
    keepit = ""
    #pdb.set_trace()
    for line in page.split("\n"):
        if findStart in line:
            save=True
        if findEnd in line:
            keepit= keepit + "\n" + findEnd + "\n"
            save=False
        if save:
            keepit= keepit + line + "\n"
    return keepit

def addTemplate(goodStuff):
    temp = open ('template.htm','r')
    page=temp.read()
    keepit = ""
    #pdb.set_trace()
    for line in page.split("\n"):
        keepit= keepit + line + "\n"
        if findStart in line:
            keepit = keepit + "\n" + goodStuff + "\n"

    return keepit



def main():
    '''Walk directory tree!'''
    rootDir = 'www.designbynur.com/eng'
    for dirName, subdirList, fileList in os.walk(rootDir):
        print('Found directory: %s' % dirName)
        print "menu level"
        for fname in fileList:
            if ".cooked" in fname:
                continue
            if ".htm" in fname:
                myfile=  os.path.join(dirName , fname)
                processHTM(myfile)


# Here's our payoff idiom!
if __name__ == '__main__':
    main()


