# variable scope = where a variable is visiable
# scope resolution = (LEGB) local - enclosed - global - built-in

# local
def func1():
    x = 1
    print(x)
func1()


# enclosed
def func2():
    x = 2
    def func3():
        print(x)
    func3()
func2()

# global
y = 4
def func4():
    print(y)
func4()

# built-in
from math import pi
#pi = 'xxx'
print(pi)
