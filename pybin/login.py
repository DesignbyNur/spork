#!/usr/bin/env python

import pdb

import urllib2
import urllib

pdb.set_trace()

url="http://s92500497.onlinehome.us/wp-login.php"

headers = [
  ("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5")]

data = [
    ("log","DBNadmin"), 
    ("pwd","Nur4ever"), 
    ("testcookie",1), 
    ("submit","Log In"), 
    ("redirect_to","http://wordpress.com/"), 
    ("rememberme","forewer")]

req = urllib2.Request(url, urllib.urlencode(dict(data)), dict(headers))
response = urllib2.urlopen(req)

the_page=response.read()
print the_page
