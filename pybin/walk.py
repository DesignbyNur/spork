#!/usr/bin/env python
import os
import sys
import pdb
import string
from HTMLParser import HTMLParser
from myWP import postStuff

def processHTML(file):
    print file
    ofile=file +".cooked"
    filein = open (file,'r')
    goodStuff = parseHtml( filein.read() )
    storeStuff(ofile,goodStuff)
    postStuff(file,goodStuff)

def storeStuff(ofile,goodStuff):
    fileout = open (ofile,'w')
    fileout.write(goodStuff) 
    fileout.close()


# our globals for parse
find ="equalsFeatureContent"
find ="component-content"
nest=0
save = False
guts =""


def parseHtml(page):
    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            #print "Start tag:", tag
            global save,guts,nest
            if save :
                nest+=1
            for attr in attrs:
                #print "     attr:", attr
                if find in attr :
                    save = True
                    print "found it"
                    #now many more starts

        def handle_endtag(self, tag):
            #print "End tag  :", tag
            global save,guts,nest
            if save :
                nest-=1
                if nest == 0:
                    save=False
        def handle_data(self, data):
            #print "Data     :", data
            global save,guts
            if save :
                lines= data.strip(string.whitespace)
                if lines:   
                    guts += lines

        def handle_comment(self, data):
            #print "Comment  :", data
            pass
        def handle_entityref(self, name):
            #c = unichr(name2codepoint[name])
            pass
            #print "Named ent:", name
        def handle_charref(self, name):
            if name.startswith('x'):
                c = unichr(int(name[1:], 16))
            else:
                c = unichr(int(name))
            print "Num ent  :", c
        def handle_decl(self, data):
            pass
            #print "Decl     :", data
    global guts
    parser = MyHTMLParser()
    parser.feed(page)
    keepit=guts
    guts=""
    return keepit

def main():
    '''Walk directory tree!'''
    pdb.set_trace()
    rootDir = 'acrdentalartworksinc.com'
    for dirName, subdirList, fileList in os.walk(rootDir):
        print('Found directory: %s' % dirName)
        print "menu level"
        for fname in fileList:
            if ".cooked" in fname:
                continue
            if ".html" in fname:
                myfile=  os.path.join(dirName , fname)
                processHTML(myfile)


# Here's our payoff idiom!
if __name__ == '__main__':
    main()


