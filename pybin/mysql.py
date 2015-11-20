#!/usr/bin/env python
import os
import sys
import pdb
import mysql.connector

def connect(dbname):
    try:
        db = mysql.connector.connect(user='robroy',passwd='Nur4ever', db=dbname) 
    except mysql.connector.Error as err:
        print(err)
        sys.exit()
    return db 

def run_sql(dbh,sqlString):
    cursor = dbh.cursor()
    try:
        ret = cursor.execute(sqlString)
    except mysql.connector.Error as err:
        print(err)
    numrows = int(cursor.rowcount)

    # get and display one row at a time.
    for x in range(0,numrows):
        row = cursor.fetchone()
        print row[0], "-->", row[1:]
    return ret



def main():
    '''What wll we do!'''
#    setup()
    pdb.set_trace()
    print 'hello'
    db =connect('test')
    out=run_sql(db,"select * from ajax;")
    print out

# Here's our payoff idiom!
if __name__ == '__main__':
    main()


