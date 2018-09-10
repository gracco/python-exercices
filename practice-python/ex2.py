#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

def main():
    askNumber()

def askNumber():
    number = int(input("Please type a number: "))
    evenOrOdd(number)

def evenOrOdd(number):
    if number % 2 == 0 :
        print('The number {} is even'.format(number))
    else:
        print('The number {} is odd'.format(number))

if __name__ == "__main__":
    main()