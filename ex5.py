import random

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = random.sample(range(100), 40)
b = random.sample(range(100), 30)

a.sort()
b.sort()

new_list = []
if len(a) > len(b):
    for i in a:
        if i in b:
            new_list.append(i)
else:
    for i in a:
        if i in b:
            new_list.append(i)


print(new_list)
