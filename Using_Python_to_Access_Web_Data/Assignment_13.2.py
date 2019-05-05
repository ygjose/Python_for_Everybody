import urllib.request, urllib.parse, urllib.error
import json

url = inpt('Enter location: ')
if len(url) < 1: break

jsondata = urllib.request.urlopen(url).read()
print('Retrieved', len(jsondata), 'characters')

info = json.loads(jsondata)
comments = info['comments']
print('Count:', len(comments))

lst = list()
for item in comments:
    count = int(item['count'])
    lst.append(count)

print('Sum: ', sum(lst))
