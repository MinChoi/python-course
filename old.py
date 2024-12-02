"""

# keyword arguments

def say_hello(first, second, third):
    return f'first: {first}, second: {second}, third: {third}'

print(say_hello(third=3, second=2, first=1))
print(say_hello(1, third=3, second=2))

print('1', '2', '3', sep='-')



####
import random

# random number
randomInt = random.randint(1,10)
print(randomInt)

# random, no argumenets
rand_no = random.random()
print(rand_no)

# choice
options = ('Rock', 'Scissors', 'Paper')
print(random.choice(options))

# cards
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
print(cards)
random.shuffle(cards)
print(cards)


#  collection type: dictionary

menu = {
    "food1": 1,
    "food2": 2.5,
    "food3": 3,
    "food4": 4.5,
    "food5": 5.55
}
cart = []
total = 0

while True:
    print('--------------- MENU --------------')
    for food, price in menu.items():
        print(f"{food:15}: ${price:.2f}")
    print('-----------------------------------')
    select = input('Insert food (q to quit):')

    if select.lower() == 'q':
        break
    elif menu.get(select) is not None:
        cart.append(select)
        total += menu.get(select)

print(cart)
print(f'Total: ${total:.2f}')




#  collection type: dictionary

capitals = {
    "USA": "Washington",
    "Korea": "Seoul",
    "Australia": "Camberwell"
}

print(capitals.get('Korea'))
print(capitals.get('Russia'))

if capitals.get('Russia'):
    russia_capital = capitals.get('Russia')
    print(f'russia is capital is {russia_capital}')
else:
    print(f'russia capital is not set')

capitals.update({'Russia': 'Moscow'})

# print(capitals.get('Korea'))
# print(capitals.get('Russia'))
#
# if capitals.get('Russia'):
#     russia_capital = capitals.get('Russia')
#     print(f'russia is capital is {russia_capital}')
# else:
#     print(f'russia capital is not set')
#
# for key in capitals.keys():
#     print(key)
# for value in capitals.values():
#     print(value)

# print(capitals.items())

for key, item in capitals.items():
    print(key)
    print(item)



# quiz

questions = (
    "Answer 1",
    "Answer 12",
    "Answer 7",
    "Answer 66",
    "Answer 22 again"
)

options = (
    (1, 2, 3, 4),
    (11, 12, 13, 14),
    (5, 6, 7, 8),
    (55, 66, 77, 88),
    (21, 22, 23, 24),
)

answers = (
    '1', '12', '7', '66', '22'
)

guesses = []
score = 0
question_num = 0

for question in questions:
    print('---------')
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input('Enter guess: ')
    guesses.append(guess)

    # print('guess == answers[question_num]')
    # print(guess, answers[question_num])

    if guess == answers[question_num]:
        score += 1
        print('CORRECT!')
    else:
        print('INCORRECT!')

    question_num += 1

print('---------------------')
print('--     Result      --')
print('---------------------')
print(f'Answer {answers}')
print(f'Guess  {guesses}')
print(f'Total score: {int(score / len(questions) * 100)}')




# calculator
num_pad = (
    (1,2,3),
    (4,5,6),
    (7,8,9),
    ("*", 0, "#"),
)

for row in num_pad:
    for button in row:
        print(button, end=' ')
    print()

# shopping cart

foods = []
prices = []

while True:
    food = input('Enter food name, q to quit:')

    if food.lower() == 'q':
        break
    else:
        price = input(f'Enter the price of {food}: $')
        foods.append(food)
        prices.append(price)

# print(foods)
# print(prices)

total = 0
for x in prices:
    total += float(x)

print()
print('------- TOTAL -------')
print(f'total price is {total}')




# collections
## list [] ordered and changeable. duplicate is ok
## set {} unordered and immutable (변경할수없는), no duplicate
## tuple () ordered and unchangeable, faster


# set

alphabets = {'a', 'b', 'c', 'd', 'f'}

print(alphabets)
print(alphabets)
print(alphabets)
print(alphabets)
print(alphabets)


# print(dir(alphabets))
# print(help(alphabets))

alphabets = ['a', 'b', 'c', 'd', 'f']

print(alphabets)
print(alphabets[2])
print(alphabets[:2])
print(alphabets[::2])
print(alphabets[::-1])

alphabets.append('g')

for x in alphabets:
    print(x)


# print(dir(alphabets))
# print(help(alphabets))


# nested loop

rows = int(input('enter rows:'))
column = int(input('enter columns:'))
symbol = input('enter symbol:')


for y in range(rows):
    for x in range (0, column):
        print(symbol, end='')
    print()





# countdown

import time

countdown = int(input('How many seconds?'))

for countdown in range(countdown, 0, -1):
    seconds = countdown % 60
    minutes = int(countdown / 60) % 60
    hours = int(countdown / 3600)
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(1)

print('Done..')



## for loop

for x in reversed(range(0, 10, 2)):
    print(f'x = {x}')


credit_card = '1234-5678-9012-3456'
for y in credit_card:
    if y=='-':
        continue
    else:
        print(y)





# calculate amount

principle = 0
interest = 0
time = 0

# while principle <= 0:
#     principle = float(input('Enter principle:'))
#     if principle <= 0:
#         print('Principle can\'t be less than 0')

while True:
    principle = float(input('Enter principle:'))
    if principle < 0:
        print('Principle can\'t be less than 0')
    else:
        break


while interest <= 0:
    interest = float(input('Enter interest:'))
    if interest <= 0:
        print('interest can\'t be less than 0')

while time <= 0:
    time = int(input('Enter time:'))
    if time <= 0:
        print('time can\'t be less than 0')

total = principle * pow((1 + interest / 100), time)

print(f'total: {total}')



# while loop

num = int(input('Enter number 1-10:'))

while num < 1 or num > 10:
    print('num is not between')
    num = int(input('Enter number 1-10 again:'))

print(f'num is {num}')



##
price1 = 13212.3
price2 = -1.234
price3 = 4321.1

print(f'p1: ${price1:.2f}')
print(f'p1: ${price1:6}')
print(f'p1: ${price1:,}')

##
credit_number = "1234-5678-9012-3456"

print('line1')
print(credit_number[4])
print('line2')
print(credit_number[4:6])
print(credit_number[:6])
print(credit_number[6:])
print(credit_number[-1])
print(credit_number[::2])

last_digit = credit_number[-4:]
print(last_digit)
print(f'xxxx-xxxx-xxxx-{last_digit}')

neg_digit = credit_number[::-1]
print(neg_digit)

##
name = input('Enter your full name')
length = len(name)

print(f'length = {length}')

# find
# rfind

print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count('c'))
print(name.replace('c', 'M'))

if not name == 'min':
    print('it is not min')
else:
    print('it is min')

# if

num1 = float(input('num1?'))

if 0 <= num1 < 10:
    print('num is 1 digit')
else:
    print('num is NOT 1 digit')

print('Second..')
print('num1 is 1 digit' if (0 <= num1 < 10) else 'num is NOT 1 digit')

print('EVEN' if num1 % 2 == 0 else 'ODD')



operator = input('operator?')
num1 = float(input('num1?'))
num2 = float(input('num2?'))


if operator == '+':
    result = num1 + num2
    pass
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    result = num1 + num2

result = round(result, 2)

print(f'result: {result}')

# /if


#math
a = -3.15
b = 2
c = 8
print(round(a ))
print(abs(a ))
print(pow(b, 4))
print(max(a,b,c))
print(min(a,b,c))

import math

print(math.pi)
print(math.sqrt(25))
print(math.ceil(9.1))
print(math.floor(9.1))
import math
radius = float(input('radius?'))
area = round(math.pi * pow(radius, 2), 2)2
print(f'area is {area}')

#/math

# input
width = float(input('width?'))
height = float(input('height?'))
area = width * height
print(f'area is {area}')
# //input

# typecasting
print(str('1'))
print(int('1'))
print(float('1'))
print(bool('1'))
print(type(str('1')))
print(type(int('1')))
print(type(float('1')))
print(type(bool('1')))

# test concat
test_concat = "1" + str(2)
print(test_concat)

# string returns true or false
print(bool('test')) # True
print(bool('')) # Frue
# // typecasting


# variables
#string
my_name = 'Min Choi'
print('testing')
print(f'test {my_name}')

#integer
age = 25
print(f'{age}')

# float
price = 10.5
print(f'price is  {price}')

# boolean
is_true = True
is_false = False

print(f'true is {is_true}')
"""