#!/usr/bin/env python
import os
import sys
import pdb
import time
import array


def main():
    '''What wll we do!'''
    tsize=10000000
    print "cpu speed test\n"
#    pdb.set_trace()
    myArray=[0]

    start=time.time()
    msize=0
    while (msize < tsize):
        msize += 1

	myArray.append(1)

    now=time.time()
    print now
    print start
    diff= now-start
    print 'total time to count', tsize, 'took',  diff 
    print 'total time to count {} took {} seconds '.format(tsize,diff)
     

# Here's our payoff idiom!
if __name__ == '__main__':
    main()


