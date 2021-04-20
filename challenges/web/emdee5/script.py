#!/bin/usr/python

import hashlib
import sys
import requests
import urllib
import re

##GET URL FROM COMMANDLINE
url=sys.argv[1]
##__________________________________________

##INITIALIZE REQUEST
req = requests.session()
##__________________________________________

##SEND GET REQUEST FROM URL
rget = req.get(url)
##__________________________________________

##GET THE HTML CONTENT FROM THE RESPONSE OF GET REQUEST
html = rget.content
##__________________________________________

##CLEAN THE HTML TO REMOVE HTML TAGS. FUNCTION COPIED FROM INTERNET
def cleanHTML(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr,'',raw_html)
    return cleantext
##___________________________________________

clean = cleanHTML(html)

##EXTRACT THE RANDOM WORD FROM THE WEBSITE CONTENT
clean = clean.split("string")[1]
##___________________________________________

##MD5 THE RANDOM STRING
result = hashlib.md5(clean).hexdigest()
##___________________________________________

##CREATE A POST REQUEST AND SEND IT BACK TO THE URL
data = {'hash': result}
x = req.post(url = url,data = data)
##___________________________________________

##PRINT THE RESPONSE
print(x.text)
##___________________________________________
