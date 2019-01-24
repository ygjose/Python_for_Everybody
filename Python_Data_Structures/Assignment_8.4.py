fname = input("Enter file name: ")
fh = open(fname)
lst = list()
# Open the file romeo.txt and read it line by line.
for line in fh:
    # For each line, split the line into a list of words using the split() method
    sfile = line.split()
    for words in sfile:
        # For each word on each line check to see if the word is already in the list
        if words not in lst:
            # if not append it to the list
            lst.append(words)
# sort and print the resulting words in alphabetical order
lst.sort()   
print(lst)
