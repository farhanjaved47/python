"""
Farhan Javed
fahran.javed47@gmail.com
12/30/2019
DocStrings
"""
import collections


def myFunction(arg1, arg2):
    """
    myFunction(arg1, args2) --> Simply prints out the two argument given
    :param arg1: first argument
    :param arg2: second argument
    :return: None
    """

    print(arg1, arg2)


def main():
    print(map.__doc__)  # Can view the doc strings by using this method
    print(collections.__doc__)  # Can see documentation of an entire module
    print(myFunction.__doc__)


if __name__ == '__main__':
    main()