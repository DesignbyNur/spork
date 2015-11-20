#!/usr/bin/env python
import os
import sys
import pdb
import datetime, xmlrpclib


wp_url = "http://justrob.local/demo1/xmlrpc.php"
server = xmlrpclib.ServerProxy(wp_url)




def postStuff(title, content):
    global server
    print content
    categories = ["somecategory"]
    tags = ["sometag", "othertag"]
    wp_blogid = ""
    date_created = xmlrpclib.DateTime(datetime.datetime.strptime("2015-10-20 21:08", "%Y-%m-%d %H:%M"))
    data = {'title': title, 'description': content, 'dateCreated': date_created, 'categories': categories, 'mt_keywords': tags}
    wp_username = "DBNAdmin"
    wp_password = "Nur4ever"
    status_published = 1
    post_id = server.metaWeblog.newPost(wp_blogid, wp_username, wp_password, data, status_published)
    return post_id

def main():
    '''What wll we do!'''
#    setup()
    pdb.set_trace()
    answer = postStuff("my Title","some stuff")
    print "answer was",answer
 

# Here's our payoff idiom!
if __name__ == '__main__':
    main()


