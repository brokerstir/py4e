# 10.2 Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time
#  and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour

# Get file from user and open file
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

# Start a dictionary
counts = dict()

# Loop through each line in file, skip line if not start with "From"
for line in handle:
    if not line.startswith("From ") : continue
    # Split the line delimited by space
    line =  line.split()
    # Get the string of time in sixth position
    time = line[5]
    # Split this tring delimited by :
    time = time.split(':')
    # First position is the hour
    hour = time[0]
    # Add this hour to dictionar or increment the count if already exists
    counts[hour] = counts.get(hour, 0 ) + 1

# Start a list
lst = list()
# Loop through key, value pairs in dictionsary
for key, val in counts.items():
    # Set each pair as a tuple
    newtup = (key, val)
    # Append tuple to the list
    lst.append(newtup)

# Sort the list
lst = sorted(lst)

# Loop through list of tubles and print each one
for key, val in lst:
    print(key, val)
