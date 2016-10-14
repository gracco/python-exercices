#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

#Extras:

#Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#Go back and do Exercise 5 using sets, and write the solution for that in a different function.

import random

a = random.sample(range(100), 40)
b = random.sample(range(100), 30)

def for_diff(a,b):
    l =[]
    if len(a) > len(b):
        [l.append(i) for i in a if i in b]
    else:
        [l.append(i) for i in b if i in a]
    return l

def set_diff(a,b):
    a = set(a)
    b = set(b)
    l = set()

    if len(a) > len(b):
         l = a.intersection(b)
    else:
        l = b.intersection(a)
    return l


print(sorted(for_diff(a,b)))
print(sorted(set_diff(a,b)))
