#!/usr/bin/env python
import os
import sys
import pdb


def fib(n):
        a, b =0 , 1
        while a < n:
                print a,
                a,b = b, a+b


def main():
    '''What wll we do!'''
#    setup()
    pdb.set_trace()
    n=input("Enter fib n: ")
    fib(n) 

# Here's our payoff idiom!
if __name__ == '__main__':
    main()


