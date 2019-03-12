name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        senders = words[1]
        counts[senders] = counts.get(senders,0)+1

msender = None
nmail = None
for sender,count in counts.items():
    if nmail is None or count > nmail:
        msender = sender
        nmail = count
print(msender, nmail)
