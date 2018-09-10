# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example,
# 13 is a divisor of 26 because 26 / 13 has no remainder.)

def main():
    number = askNumber()
    numberList = createNumberList(number)
    checkPrintDivisors(numberList, number)

def askNumber():
    number = int(input("Please enter a number: "))
    return number

def createNumberList(number):
    numberList = list(range(1,number+1))
    return numberList

def checkPrintDivisors(numberList, number):
    for i in numberList:
        if number % i == 0:
            print(i, end=' ')

if __name__ == "__main__":
    main()