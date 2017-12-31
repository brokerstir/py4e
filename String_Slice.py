# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475";

# index the position where there is the first space
index = text.find(' ')

# define the string after index position as text
text = text[index:]

# strip whiespace of text
text.strip()

#convert text to floating point number and print
int = float(text)
print(int)
