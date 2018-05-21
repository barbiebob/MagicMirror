#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding: utf8
import requests
import sys
#import urllib3
#import ssl
reload(sys)
sys.setdefaultencoding('utf-8')

key = '7382522b-e09f-4317-9888-9276e6e37165'

url = 'https://api.resrobot.se/departureBoard?key=%s&id=740000868&format=json&maxJourneys=6&products=16&passlist=0' % key
request = requests.get(url, verify=False)

data = request.json()

print("Content-type: text/html\n\n")
print("<p class=bigger>Avgångar Vikingstad</p>")
for train in data['Departure']:
  time = train['time']
  time = time[:-3]
  print "<p class=smaller>" + time + " " + train['direction'] + "</p>"
