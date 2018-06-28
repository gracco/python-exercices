#A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....

#The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms. 
#This means to say the nth term is the sum of (n-1)th and (n-2)th term.

size_seq = 100
first_num = 0
sec_num = 1

fibo_list = []
count = 0

while count < size_seq:
  fibo_list.append(first_num)
  next_num = first_num + sec_num
  first_num = sec_num
  sec_num = next_num
  count += 1

print(fibo_list)