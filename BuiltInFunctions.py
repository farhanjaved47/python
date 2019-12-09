"""
Farhan Javed
farhan.javed47@gmail.com
12/9/2019
Built In Functions for Python
https://www.w3schools.com/python/python_ref_functions.asp
"""


class Bunny:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return f'repr : the number of bunnies is {self._n}'

    def __str__(self):
        return f'str : the number of bunnies is {self._n}'


def main():
    x = '47'
    y = int(x)  # the int() is a constructor for the int class.

    print(f'x is {x} and of the type {type(x)}')
    print(f'y is {y} and of the type {type(y)}')

    s = 'Hello World'
    print(repr(s))
    bunnies = Bunny(21)
    print(repr(bunnies))
    print(bunnies)  # prints the __str__. if not found then __repr__ else the object's memory value

    x = (1, 2, 3, 4, 5)
    y = list(reversed(x))  # reverses the list x
    print(x)
    print(y)
    print(max(x))  # prints the max from x
    print(min(x))  # prints the min from x
    print(sum(x))  # sum of all the elements in x
    print(sum(x, 10))  # sum of all the elements in x plus 10
    z = (0, 0, 0, 0, 0, 0)
    print(any(z))  # False if all 0
    print(any(x))  # true if any digit is not zero
    f = (6, 7, 8, 9, 10)
    z = zip(x, f)
    for a, b in z:
        print(f'{a} - {b}')

    animals = {'cat', 'dog', 'rabbit', 'pig'}
    for i, v in enumerate(animals):
        print(f'{i}: {v}')

    print(type(bunnies))  # prints the type of the object
    print(isinstance(bunnies, Bunny))  # checks if an object is of a specific class or not
    print(id(bunnies))  # prints the id of an object


if __name__ == '__main__': main()