#!/usr/bin/env python
''' read html from file or url '''
import os
import re
import sys
import pdb
import urllib
from HTMLParser import HTMLParser


def getarg():
    if len(sys.argv) == 1:
        link = "http://www.robert-e-roy.com"
    else: 
        print sys.argv
        link = sys.argv[1]
    return link

def getit():
    thing = getarg()
    if  "http" in thing:
        myinfo = urllib.urlopen(thing)
        spam = myinfo.read()
    else:
        f = open (thing,'r')
        spam = f.read()
    return spam

def parseHtml(page):
    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            print "Start tag:", tag
            for attr in attrs:
                print "     attr:", attr
        def handle_endtag(self, tag):
            print "End tag  :", tag
        def handle_data(self, data):
            print "Data     :", data
        def handle_comment(self, data):
            print "Comment  :", data
        def handle_entityref(self, name):
            c = unichr(name2codepoint[name])
            print "Named ent:", c
        def handle_charref(self, name):
            if name.startswith('x'):
                c = unichr(int(name[1:], 16))
            else:
                c = unichr(int(name))
            print "Num ent  :", c
        def handle_decl(self, data):
            print "Decl     :", data

    parser = MyHTMLParser()
    parser.feed(page)
    return

def main():
    ''' read a web page '''
    pdb.set_trace()
#    setup()

    filecontent=getit()

    #print filecontent
    parseHtml(filecontent)


# Here's our idiom!
if __name__ == '__main__':
    main()


