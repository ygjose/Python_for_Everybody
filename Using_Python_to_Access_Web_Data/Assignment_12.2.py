import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_160200.html').read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the 'span' tags
tags = soup('span')

# loop through the tags and extract contents (i.e., numbers)
sum = 0
for tag in tags:
    sum = sum + int(tag.contents[0])
print(sum)
