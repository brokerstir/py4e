# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
# Use the file romeo.txt

# Get file name from user and open file handle
fname = input("Enter file name: ")
fh = open(fname)

# Define a new list
lst = list()

# Loop through each line in file
for line in fh:

    # Split the words in each line
    line = line.split()

    # Loop through each word in current line
    for word in line:
        # Skip out of loop if word exists in list
        if word in lst : continue
        # Add word to list if not exist
        lst.append(word)

# Sort the list and print
lst.sort()
print(lst)
