#!/usr/bin/env python
import os
import sys
import pdb
import MySQLdb


def connect(dbname):
    try:
        db = MySQLdb.connect(db=dbname, read_default_file='~/.my.cnf') 
    except MySQLdb.Error as err:
        print(err)
        sys.exit()
    return db 

def run_sql(dbh,sqlString):
    cursor = dbh.cursor()
    try:
        ret = cursor.execute(sqlString)
    except MySQLdb.Error as err:
        print(err)
    else:
        retList=[] 
    numrows = int(cursor.rowcount)

    # get and display one row at a time.
    for x in range(0,numrows):
        row = cursor.fetchone()
        #print row[0], "-->", row[1:]
        retList.append(row)
    return retList



def main():
    '''What wll we do!'''
#    setup()
    pdb.set_trace()
    print 'hello'
    db =connect('test')
    out=run_sql(db,"show tables in test;")
    print out[1]
    print  "==="


    print out

# Here's our payoff idiom!
if __name__ == '__main__':
    main()

