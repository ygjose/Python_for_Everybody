name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        hms = time.split(':')
        hour = hms[0]
        if hour not in counts:
            counts[hour] = 1
        else:
            counts[hour] +=1

lst = list(counts.items())
lst.sort()

for key, val in lst:
    print(key,val)
