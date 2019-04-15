import re
ihand=input('Enter your text: ')
fhand=open(ihand)
numlist=list()
for line in fhand:
    line=line.rstrip()
    numbers=re.findall('[0-9]+', line)
    if len(numbers) > 0:
        numlist.extend(numbers)
newlist =list()
for number in numlist:
    num = int(number)
    newlist.append(num)
print('Sum: ', sum(newlist))
