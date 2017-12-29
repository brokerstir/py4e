# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except
# and put out an appropriate message and ignore the number.

# Initialize varibles
largest = None
smallest = None

# Loop until user enters done
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num =  int(num)
        if largest is None:
            largest = num
        if smallest is None:
            smallest = num
        if num > largest:
            largest = num
        if num < smallest:
            smallest =  num
    except:
        print('Invalid input')
    
# print results
print("Maximum is", largest)
print("Minimum is", smallest)
