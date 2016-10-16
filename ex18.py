#Create a program that will play the “cows and bulls” game with the user. The game works like this:

#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
#For every digit that the user guessed correctly in the correct place, they have a “cow”.
#For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
#Once the user guesses the correct number, the game is over.
#Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

import random

def cow_game():
    number = list(str((random.randint(1000,9998))))
    retries = 0
    bulls = 0
    cows =  0
    print(number)

    while True:
        user_number = list((input('Please enter a number: \n >>>:')))
        retries += 1
        for i in user_number:
            if i in user_number and i in number:
                cows +=1
                if number.index(i) == user_number.index(i):
                    bulls += 1

        print("Cows: {} \n Bulls: {} \n You tried {} times".format(cows,bulls,retries))
        bulls = 0
        cows = 0
        if user_number == number:
            print("You won!")
            break

if __name__ == "__main__":
    cow_game()
