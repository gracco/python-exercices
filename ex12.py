import random

a = list(random.sample(range(10),9))
n = []

def append_list(j,k):
    n.append(a[j])
    n.append(a[k])
    print(n)

append_list(0,-1)
