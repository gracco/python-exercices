number = int(input("Please enter a number: "))

a = list(range(1,number+1))

for i in a:
    if number % i == 0:
        print(i)
