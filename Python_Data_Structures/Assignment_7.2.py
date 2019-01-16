# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count +1
        value_starts = line.find(':')
        values = line[value_starts+1: ]
        fvalues = float(values)
        total = total + fvalues
        average = total/count
   
print ('Average spam confidence:', average)


# Option 2
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
            continue
    count = count + 1
    value_starts = line.find(':')
    values = line[value_starts+1: ]
    fvalues = float(values)
    total = total + fvalues
    average = total/count
        
print ('Average spam confidence:', average)
