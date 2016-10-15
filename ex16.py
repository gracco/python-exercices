#Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

#Extra:

#Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
import random

def password(quant):
    options = ['numbers', 'letters', 'symbols','letters_upper']
    numbers = list(str(range(10)))
    letters = list('abcdefghijklmnopqrstuvwxyz')
    letters_upper = list('abcdefghijklmnopqrstuvwxyz'.upper())
    symbols = list("[]\{\}!@#$%&*<>")
    password = []
    i = random.randint(10,20)

    while i != 0:
        j = random.choice(options)
        if j == 'numbers':
            sorted_numbers = random.sample(numbers, random.randrange(10))
            sorted_numbers = ''.join(sorted_numbers)
            password.append(sorted_numbers)
        elif j == 'letters':
            sorted_letters = random.sample(letters, random.randrange(26))
            sorted_letters = ''.join(sorted_letters)
            password.append(sorted_letters)
        elif j == 'letters_upper':
            sorted_letters = random.sample(letters_upper, random.randrange(26))
            sorted_letters = ''.join(sorted_letters)
            password.append(sorted_letters)
        elif j == 'symbols':
            sorted_symbols = random.sample(symbols, random.randrange(11))
            sorted_symbols = ''.join(sorted_symbols)
            password.append(sorted_symbols)
        i -= 1

    list_password = list(''.join(password))
    random.shuffle(list_password)
    string_password = ''.join(list_password)


    if quant <= len(string_password):
        print(''.join(random.sample(string_password,quant)))
    elif quant == 0:
        print(string_password)



if __name__ == '__main__':
    quant = int(input("Type the number of characters for you password:\n"))
    password(quant)
