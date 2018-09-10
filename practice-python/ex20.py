#Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
#The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

#Extras:

#Use binary search.
import bisect
from datetime import datetime as dt

def check_num(lists, num):
    if num in lists:
        print('True')
        return True
    else:
        print('False')
        return False

def check_num_binary(lists,num):
    i = bisect.bisect_left(lists, num)
    if i != len(lists) and a[i] == num:
        print('True')
        return True
    else:
        print('False')
        return False

if __name__ == '__main__':
    lists = list(range(5))
    start_time = dt.now()
    check_num(lists, 6)
    end_time = dt.now()
    print('Duration {} of funciont check_num'.format(end_time - start_time))
    start_time = dt.now()
    check_num_binary(lists, 6)
    end_time = dt.now()
    print('Duration {} of funciont check_num_binary'.format(end_time - start_time))
