#!/usr/bin/env python
import os
import sys
import pdb

def up(string,which):
    return string[:which] + string[which].upper() + string[(which+1):]


def main():
    '''What wll we do!'''
#    setup()
    pdb.set_trace()
    spam="hello"
    
    eggs=up(spam,1)

    print "spam "+spam 
    print "eggs "+eggs 
 

# Here's our payoff idiom!
if __name__ == '__main__':
    main()


