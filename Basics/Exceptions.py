"""
Farhan Javed
farhan.javed47@gmail.com
12/07/2019
Basic exception raising and handling
"""
import sys  # sys library contain useful constants which can help with the error messages


def div(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    elif num1 == 0:
        raise TypeError('Do not divide zero by anything please')
    else:
        return num1 / num2


def main():
    try:  # put this around the statement which might throw an exception
        answer = div(2, 1)
    except ZeroDivisionError as z:  # can catch well defined exception
        print(f'Exception Caught: {z}')
    except:
        print(f'Unknown exception caught: {sys.exc_info()[1]} ')  # can use sys for info about unknown exceptions
        # however using a bare exception is never recommended. This is just for example purposes.
    else:
        print(f'Answer of division is : {answer}')


if __name__ == '__main__': main()