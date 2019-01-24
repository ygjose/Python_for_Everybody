fname = input("Enter file name: ")
# This is line is unnecessary. It seems the file "mbox-short" removed blank lines so that the loop will not have the same problem as in the [clip](https://www.coursera.org/learn/python-data/lecture/n7ihY/worked-exercise-lists)
if len(fname) < 1 : continue

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
