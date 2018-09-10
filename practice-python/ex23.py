#/usr/bin/env python3

#Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
#One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

import requests

link_prime_numbers = 'http://www.practicepython.org/assets/primenumbers.txt'
link_happy_numbers = 'http://www.practicepython.org/assets/happynumbers.txt'

req_prime = requests.get(link_prime_numbers)
req_happy = requests.get(link_happy_numbers)

prime_numbers = list(req_prime.text)
happy_numbers = list(req_happy.text)

def intersect(a,b):
    return(list(set(a) & set(b)))

print(sorted(intersect(prime_numbers,happy_numbers)))
