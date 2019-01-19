# put the file in the same directory as the python working directory
rfile = open('mbox-short.txt')
for i in rfile:
    print(i.upper())
