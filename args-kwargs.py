# *args = multiple non-key arguments
# **kwargs - multiple keyword arguments

# args become tuple
def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(add(2,3,4,5))


def display_name(*names):
    for name in names:
        print(name, end=' ')
display_name('Min', 'Kwang', 'Choi')
print()
print()

###############

# kwargs become dictionary
def display_address(**kwargs):
    print('Value name: ', end='')
    for value_name in kwargs:
        print(value_name, end=', ')
    print()

    for val in kwargs.values():
        print(val)


display_address(street='5 Andrew',
                suburb='Seabrook',
                postcode='3028',
                state='VIC')


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')

    for key, value in kwargs.items():
        print(f'{key}: {value}')


shipping_label('Min', 'Choi',
               address='4 Buller Ct',
               suburb='Hoppers Crossing')