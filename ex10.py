import random

a = random.sample(range(100), 40)
b = random.sample(range(100), 30)
new = []
if len(a) > len(b):
    [new.append(i) for i in a if i in b]
else:
    [new.append(i) for i in b if i in a]

print(new)
