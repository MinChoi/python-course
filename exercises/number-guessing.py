# number guessing
import random

number = random.randint(0, 100)
is_running = True
guesses = 0

while is_running:
    guess = input('Please enter number: ')

    if not guess.isdigit():
        print('No number')
        continue

    guess = int(guess)
    guesses += 1
    if guesses == 5:
        print(f'Too many guesses! The answer is {number}')
        break

    if number == guess:
        print(f'Correct! The number is {number}')
        print(f'Guesses: {guesses}')
        break


    if number > guess:
        print('Number is bigger')
    elif number < guess:
        print('Number is smaller')


