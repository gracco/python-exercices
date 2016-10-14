word = input("Please enter a word: ")

word_fowards = word[::-1]

if word == word_fowards:
    print("Yes, it's a palindrome")
else:
    print("No, it's not a palindome")
