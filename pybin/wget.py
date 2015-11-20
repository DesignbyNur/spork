#!/usr/bin/env python
import os
import sys
import pdb
import urllib


def getarg():
    if len(sys.argv) == 0:
        link = "http://www.robert-e-roy.com"
    else: 
        print sys.argv
        link = sys.argv[1]
    return link

def from_url( url, filename = None ):
    '''Store the url content to filename'''
    if not filename:
        filename = os.path.basename( os.path.realpath(url) )

    req = urllib.request.Request( url )
    try:
        response = urllib.request.urlopen( req )
    except urllib.error.URLError as e:
        if hasattr( e, 'reason' ):
            print( 'Fail in reaching the server -> ', e.reason )
            return False
        elif hasattr( e, 'code' ):
            print( 'The server couldn\'t fulfill the request -> ', e.code )
            return False
    else:
        with open( filename, 'wb' ) as fo:
            fo.write( response.read() )
            print( 'Url saved as %s' % filename )
        return True

 

def main():
    ''' read a web page '''
    pdb.set_trace()
#    setup()
    link = getarg()
    spam = from_url(link)
    print spam
    print "bye" 

# Here's our payoff idiom!
if __name__ == '__main__':
    main()


