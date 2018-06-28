# print the last fibonacci sequence

quant_fibo = 10

first_n = 0
second_n = 1
count = 0
final_list = []

if quant_fibo == 1:
    print(first_n)
else:
    while count < quant_fibo:
        final_list.append(first_n)
        last = first_n + second_n
        first_n = second_n
        second_n = last
        count += 1

print(final_list)