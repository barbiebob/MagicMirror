#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding: utf8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib3
import soco
from soco import SoCo

# Sonos speakers
office = SoCo('192.168.1.71')
living_room = SoCo('192.168.1.72')

# Print function
def show_track(sonos):
  track = sonos.get_current_track_info()
  if "x-sonos-spotify" in track['uri']:
    print "Content-type: text/html\n\n<img src=img/spotify.jpg style=width:40px;height:34px;>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + track['artist'] + " - " + track['title']
  elif "p3-aac" in track['uri']:
    if not track['artist']:
      print "Content-type: text/html\n\n<img src=img/p3.jpg style=width:48px;height:34px;>&nbsp;&nbsp;&nbsp;"
    else:
      print "Content-type: text/html\n\n<img src=img/p3.jpg style=width:48px;height:34px;>&nbsp;&nbsp;&nbsp;" + track['artist'] + " <br /> " + track['title']
  elif "p3star" in track['uri']:
    if not track['artist']:
      print "Content-type: text/html\n\n<img src=img/p3star.png style=width:48px;height:34px;>&nbsp;&nbsp;&nbsp;"
    else:
      print "Content-type: text/html\n\n<img src=img/p3star.png style=width:48px;height:34px;>&nbsp;&nbsp;&nbsp;" + track['artist'] + " <br /> " + track['title']
  elif "p4" in track['uri']:
    if not track['artist']:
      print "Content-type: text/html\n\n<img src=img/p4.png style=width:48px;height:34px;>&nbsp;&nbsp;&nbsp;"
    else:
      print "Content-type: text/html\n\n<img src=img/p4.png style=width:48px;height:34px;>&nbsp;&nbsp;&nbsp;" + track['artist'] + " <br /> " + track['title']

# Get speaker status
office_state = office.get_current_transport_info()
office_track = office.get_current_track_info()
living_room_state = living_room.get_current_transport_info()
living_room_track = living_room.get_current_track_info()

# Check if and which speaker is playing
if office_state['current_transport_state'] == "PLAYING" and office_track['duration'] == "NOT_IMPLEMENTED":
  if not office_track['artist']:
    sonos = SoCo('192.168.1.72')
    state = sonos.get_current_transport_info()
    if state['current_transport_state'] == "PAUSED_PLAYBACK":
      print "Content-type: text/html\n\n" + "Not playing"
    elif state['current_transport_state'] == "STOPPED":
      print "Content-type: text/html\n\n" + "Not playing"
    else:
      show_track(sonos)
  else:
    sonos = SoCo('192.168.1.71')
    show_track(sonos)
elif living_room_state['current_transport_state'] == "PLAYING" and living_room_track['duration'] == "NOT_IMPLEMENTED":
  if not living_room_track['artist']:
    sonos = SoCo('192.168.1.71')
    state = sonos.get_current_transport_info()
    if state['current_transport_state'] == "PAUSED_PLAYBACK":
      print "Content-type: text/html\n\n" + "Not playing"
    elif state['current_transport_state'] == "STOPPED":
      print "Content-type: text/html\n\n" + "Not playing"
    else:
      show_track(sonos)
  else:
    sonos = SoCo('192.168.1.72')
    show_track(sonos)
elif office_state['current_transport_state'] == "PLAYING" and office_track['artist'] == "":
  sonos = SoCo('192.168.1.72')
  show_track(sonos)
else:
  print "Content-type: text/html\n\n" + "Not playing"
