#function who creates and validates prime numbers
n = int(input("Please enter a number to check if it's prime or not: \n"))

not_prime = 0

for i in range(2, n - 1):
    if n % i  == 0:
        not_prime = 1

if not_prime == 0:
    print("It's prime")
else:
    print("It's NOT prime")
        
