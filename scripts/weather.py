#!/usr/bin/env python
#coding: utf8
# -*- coding: utf-8 -*-

import commands
import datetime
from datetime import timedelta

# Get temperature in Celsius
request = "curl -s 'http://api.openweathermap.org/data/2.5/weather?q=Vikingstad,SE&appid=570785fa1a36740b5641d949cac44d59&units=metric' | jq . | grep -w temp | sed 's/[^[:digit:].-]//g'"
temp = commands.getoutput(request)

# Get feelslike temperature in Celcius
request = "curl -s 'http://api.apixu.com/v1/current.json?key=1b79be9f124044288b685052170805&q=Stockholm' | jq . | grep -w feelslike_c | sed 's/[^[:digit:].-]//g'"
feelslike = commands.getoutput(request)

# Get wind speed in m/s
request = "curl -s 'http://api.openweathermap.org/data/2.5/weather?q=Vikingstad,SE&appid=570785fa1a36740b5641d949cac44d59&units=metric' | jq . | grep -w speed |  sed 's/[^[:digit:].-]//g'"
wind = commands.getoutput(request)

# Get sunset time
request = "curl -s 'http://api.openweathermap.org/data/2.5/weather?q=Vikingstad,SE&appid=570785fa1a36740b5641d949cac44d59&units=metric' | jq . | grep -w sunset | sed 's/[^0-9]//g'"
sunset = commands.getoutput(request)
sunset = float(sunset)
sunset = datetime.datetime.fromtimestamp(sunset).strftime('%H:%M')

# Print the output
print("Content-type: text/html\n\n" "&ensp;&ensp;&ensp;" "Temperatur: &nbsp;&ensp;" + temp + " ºC")
print("&ensp;&ensp;&ensp;" "Känns som: &nbsp;&nbsp;&ensp;" + feelslike + " ºC" + "<br />")
print("&ensp;&ensp;&ensp;" "Vind: &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;" + wind + " m/s" + "<br />")
print("&ensp;&ensp;&ensp;" "Solnedgång:  &nbsp;&ensp;" + sunset)
