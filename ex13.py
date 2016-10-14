fibo_l = [1,1]

number = int(input("Please enter a number:"))

def fibbo():
    fibo_l.append(fibo_l[len(fibo_l) - 1] + fibo_l[len(fibo_l) - 2])
    return

while len(fibo_l) < number:
    fibbo()

print(fibo_l)
