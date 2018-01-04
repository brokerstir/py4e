# 9.4 Write a program to read through the mbox-short.txt
# and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most prolific committer.

# Get file from user and open file
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

# Define dictionary
counts = dict()

# Loop through each line in file
for line in handle:
    # Skip out of loop if line not start with From
    if not line.startswith("From ") : continue
    # Split line at each space
    words = line.split()
    # Define second sring in line as word
    word = (words[1])
    # Increment the nunber of times that word appers
    counts[word] = counts.get(word,0) + 1
#print(counts)

# Define variables
bigcount = None
bigword = None
# Loop through dictionary
for word,count in counts.items():
    # Find the word that with highest count
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
