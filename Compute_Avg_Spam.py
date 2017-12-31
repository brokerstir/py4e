# 7.2
# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name

# Get file name from user and open file
fname = input("Enter file name: ")
fh = open(fname)

# Initialze variables
count = 0
total = 0

# Loop through each line in file
for line in fh:
    # Skip out of loop if line doesn't sart with X-DSPAM
    if not line.startswith("X-DSPAM-Confidence:") : continue

    # Strip whitespace and rename
    line = line.rstrip()
    text = line

    # Index positio where there is the first space
    index = text.find(' ')

    # Set as text the string staring with with the first space
    text = text[index:]

    # Strip whitespace
    text.strip()

    # Convert to floaing point number
    int = float(text)

    # Increment count as another for this loop iteration
    count += 1

    # Add corrent number to the total
    total += int

# We are now out of loop so compute average and print
avg_spam_conf = total / count
print("Average spam confidence:", avg_spam_conf)
