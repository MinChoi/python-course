# list comprehensions
# [expression for value in iterable if condition]

##
doubles = []
for x in range(1,11):
    doubles.append(x*2)
print(doubles)

##
new_doubles = [x*2 for x in range(1,11)]
print(new_doubles)

##
names = ['michael', 'john', 'jane']
print(names)
names = [name.capitalize() for name in names]
print(names)


##
numbers = [-3, -2, -1, 0, 1, 2, 3]
positive_numbers = [num for num in numbers if num >= 0]
print(positive_numbers)
negative_numbers = [num for num in numbers if num < 0]
print(negative_numbers)
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)

##
grades = [86, 43, 56, 99, 75, 82]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)