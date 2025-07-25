# Two programs to prints the numbers 1 to 10
print('Program to prints the numbers 1 to 10.\nPress 1 for the for loop and 2 for the while loop:')
userInput = int(input())
number = 0

if userInput == 1: # First program using a for loop
    print('for loop:')
    for num in range(11):
        print(num)
elif userInput == 2: # Second program using a while loop
    print('while loop')
    while number < 11:
        print(number)
        number = number + 1
else:
    print('Press 1 or 2.')
    