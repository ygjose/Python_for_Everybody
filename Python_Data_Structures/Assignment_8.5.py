fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
# Read the file line by line
for line in fh:
    # Remove possisble blanks in each line
    line = line.strip()
    # Find a line that starts with 'From ', instead of 'From' (in this case, it will include 'From:')
    if not line.startswith('From '):
        continue
    # Parse the 'From...' line using split() method
    info = line.split()
    # Print out the second word in the line
    print(info[1])
    # Don't forget to trace the iteration times
    count = count + 1
# Print out the final result for the counts
print("There were", count, "lines in the file with From as the first word")
