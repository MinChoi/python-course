# rock, paper, scissors

import random

options = ('rock', 'paper', 'scissors')

computer = random.choice(options)
player = None

while True:
    player = input('Select your choice Rock, Paper or Scissors: ')
    if player not in options:
        print('Please select correctly')
    else:
        break


print(f'Player: {player}')
print(f'Computer: {computer}')

if computer == player:
    print('TIE!')
elif player == 'rock' and computer == 'scissors':
    print('Player win!')
elif player == 'scissors' and computer == 'paper':
    print('Player win!')
elif player == 'paper' and computer == 'rock':
    print('Player win!')
else:
    print('Player lose!')
