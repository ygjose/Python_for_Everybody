import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

xmldata = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_160202.xml').read()
print('Retrieved', len(xmldata), 'characters')

tree = ET.fromstring(xmldata)
counts = tree.findall('comments/comment') # I found 'counts = tree.findall('.//count')' is not working

lst = list()
for item in counts:
    number = item.find('count').text
    integer = int(number)
    lst.append(integer)

print(sum(lst))
