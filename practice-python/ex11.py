def insert_num():
    return int(input("Please insert a number:"))

number = insert_num()
a = list(range(1,number+1))

print([i for i in a if number % i == 0 ])
