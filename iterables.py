# iterables -  an object/collection that can return its elements one at a time,
#               allowing it to be iterated over in a loop

# array
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number, end='-')
print()

# tuple
numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print(number, end='-')
print()
print()

# set - can't reverse
fruits = {"orange", "apple", "banana", "coconut"}
for fruit in fruits:
    print(fruit, end='-')
print()

#string
name = "my name is Min Choi"
for character in name:
    print(character, end=" ")
print()


# dictionary
dictionary = {"a":1, "b":2, "c":3, "d":4}
for val in dictionary:
    print(f"{val} ")
for key, val in dictionary.items():
    print(f"{key} {val} ")
for key in dictionary.keys():
    print(f"{key}")
