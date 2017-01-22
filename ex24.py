#Time for some fake graphics! Let’s say we want to draw game boards that look like this:

# --- --- ---
#|   |   |   |
# --- --- ---
#|   |   |   |
# --- --- ---
#|   |   |   |
# --- --- ---
#This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

# size = input("Please enter the size of the board, ex 3x3, 4x4, 16x7: \n")
# size_numbers = size.split('x')
# horizontal_number = size_numbers[0]
# vertical_number = size_numbers[1]
#
# #print(size_numbers)
#
# lines = '--- '
# columns = '|   ' + "|"
#
# while n <= size_numbers:
#     print(lines*horizontal_number)
#     print()


n = int(input("enter the board size "))
print(" ---" * n)
for r in range(1,n+1):
  print ("|   "*(n+1))
  print (" ---"*n)
