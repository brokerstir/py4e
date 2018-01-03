# 8.5 Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line
# (i.e. the entire address of the person who sent the message). Then print out a count at the end.

# Get file name from user
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

# Open file and set count to zero
fh = open(fname)
count = 0

# Loop through each line in file
for line in fh:
    # Skip out of loop if line doesn't start with From
    if not line.startswith("From ") : continue
    # Split the line
    line =  line.split()
    # Print second string in line
    print(line[1])
    # Increment count
    count += 1

# After loop, print count
print("There were", count, "lines in the file with From as the first word")
