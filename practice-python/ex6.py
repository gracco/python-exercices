# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

def main():
    word, word_fowards = askWord()
    compareWords(word, word_fowards)

def askWord():
    word = input("Please enter a word: ")
    word_fowards = word[::-1]
    return word, word_fowards

def compareWords(word, word_forwards):
    if word == word_forwards:
        print("Yes, it's a palindrome")
    else:
        print("No, it's not a palindome")

if __name__ == "__main__":
    main()