"""
This file outlines the basic functionality of defining and implementing functions in Python including decorators
Farhan Javed
farhan.javed47@gmail.com
12/2/2019
"""


def argumentList(*args):  # can be used to pass tuples/lists as arguments. args is convention
    if len(args):
        for arg in args:
            print(arg)


def keywordArguments(**kwargs):  # can be used to pass tuples/lists as arguments. kwargs is convention
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))


def passByValue(a):
    print(id(a))
    a = 4
    print(id(a))
    print(f'Passed by value a : {a}')


def passByReference(b):
    print(id(b))
    b[0] = 5
    print(id(b))
    #  However, if we were to assign the a new list to b, it would be a different object alltogether : b = [5]
    print(f'Passed by reference b: {b}')


def kitten():  # simple function without an argument
    print('Kitten is meowing')


def lion(name, age):  # function with parameters.
    print('Lion name : ' + name + ' aged : ' + str(age) + ' roars')


def lioness(name, age, partner='Simba'):  # functions with a default parameter.
    print('Lioness : ' + name + ' aged : ' + str(age) + ' is married to ' + partner)


#  Decorators
# since everything is a function in python, we can return functions as well from inside another function
def f1():
    def f2():
        print('this is f2')
    return f2

# with decorators I'm now calling func3 inside func1 because of the @func1 decorator keyword
def func1(f):
    def func2():
        print('this is before the function call')
        f()
        print('this is after the function call')
    return func2


@func1
def func3():
    print('this is func3')


def main():
    kitten()
    simba_age = 5
    nala_age = 4
    lion('Simba', simba_age)
    lioness('Nala', nala_age)
    simba_age = 8
    print('New simba age : ' + str(simba_age))

    # Mutable objects are passed by reference as they can be changed.
    # Immutable objects are passed by value as they cannot be changed.
    # The above is true for assignments and functions and generally anywhere in python.
    a = 10  # integers are immutable
    print('printing id of main a ' + str(id(a)))
    b = [2]  # lists are mutable
    print('printing id of main b ' + str(id(b)))
    passByValue(a)
    passByReference(b)
    print(f'Value of a after passed by value : {a}')
    print(f'Value of b after passed by reference : {b}')

    animals = ('Kitten', 'Lion', 'Tiger', 'Dog')
    argumentList(*animals)

    animalCalls = dict(Buffy='meow', Zilla='grr', Angel='rawr')
    keywordArguments(**animalCalls)

    x = f1()    # we can simply assign the return function to another variable and call the returned function from the
    # variable
    x()

    #  here is where it becomes a decorator
    func3()


if __name__ == '__main__': main()