import random

rounds = 0

def randomize_number():
    r = str(random.randint(0,9))
    return r

random_number = randomize_number()

while True:
    number = input("Please enter a number: or exit ")
    if number == 'exit':
        print('\nBye')
        break
    elif number == random_number:
        rounds += 1
        print('You win! with {} rounds'.format(rounds))
        print('I am randonmizing another number!')
        randomize_number
        continue

    elif number > random_number:
        rounds += 1
        print('The number is lower than this, try again!')
        continue
    elif number < random_number:
        rounds += 1
        print('The number is higher than this, try again!')
        continue
