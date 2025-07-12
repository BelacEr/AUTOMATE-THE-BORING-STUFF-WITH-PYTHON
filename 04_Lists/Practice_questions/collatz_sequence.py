# Program to do the Collatz sequences, sometimes called "the simplest impossible math problem."

def collatz(number):
    try:
        while True:
            if number == 1:
                print(number)
                break
            elif number % 2 == 0:   # This means the number is an even
                print(number)
                number = number // 2
            elif number % 2 == 1:
                print(number)
                number = 3 * number + 1
    except ValueError:
        print('You must enter a number.')

collatz(int(input('Enter a number: \n')))
    