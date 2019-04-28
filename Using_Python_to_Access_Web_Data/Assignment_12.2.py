# Do not write this code in an editor and read it via Termianl/Command, because it always shows you ImportError: cannot import name 'BeautifulSoup' from 'bs4'
# My gut feeling is that Python will search all files which contain the word 'bs4' when importing BeatifulSoup (be careful with capital letters!). Since this script (you wrote in an editor) also contains 'bs4' (in line 5 in my case), you cannot import BeautifulSoup from this script apparently. Thus, it will give you error traceback.
# My solution is that just type this code in Terminal/Commander. It will not show any error ;-)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# This lines, which are from Chapter 13, are more straightforward 
html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_160200.html').read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the 'span' tags
tags = soup('span')

# loop through the tags and extract contents (i.e., numbers)
sum = 0
for tag in tags:
    sum = sum + int(tag.contents[0])
print(sum)
