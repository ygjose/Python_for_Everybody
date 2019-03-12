fname = input('Enter file name: ')
fopen = open(fname)
counts = dict()
for line in fopen:
    if line.startswith('From '):
        words = line.split()
        weekdays = words[2]
        counts[weekdays] = counts.get(weekdays,0) + 1
print(counts)
