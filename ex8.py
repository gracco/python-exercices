import random

actions = ['rock', 'paper', 'scisors']
random_actions = random.choice(actions)



while True:
    player_actions = input("Please enter rock paper or scisors: ")
    if player_actions == 'rock' and random_actions == 'paper':
        print('{} wraps {} so you LOSE'.format(random_actions, player_actions))
        break
    elif player_actions == 'rock' and random_actions == 'scisors':
        print('{} is broken by {} so you WIN'.format(random_actions, player_actions))
        break
    elif player_actions == 'rock' and random_actions == 'rock':
        print('{} equal to {} so DRAW'.format(random_actions, player_actions))
        continue
    elif player_actions == 'paper' and random_actions == 'scisors':
        print('{} cut {} so you LOSE'.format(random_actions, player_actions))
        break
    elif player_actions == 'paper' and random_actions == 'rock':
        print('{} is wrapped by {} so you WIN'.format(random_actions, player_actions))
        break
    elif player_actions == 'paper' and random_actions == 'paper':
        print('{} equal to {} so DRAW'.format(random_actions, player_actions))
        continue
    if player_actions == 'scisors' and random_actions == 'paper':
        print('{} is cut by {} so you WIN'.format(random_actions, player_actions))
        break
    elif player_actions == 'scisors' and random_actions == 'scisors':
        print('{} equal to {} so DRAW'.format(random_actions, player_actions))
        continue
    elif player_actions == 'scisors' and random_actions == 'rock':
        print('{} brokes {} so you LOSE'.format(random_actions, player_actions))
        break
