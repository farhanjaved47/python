"""
Farhan Javed
farhan.javed47@gmail.com
12/15/2019
Basic Math functionality in python 3 - Part 2
https://docs.python.org/3/library/math.html
"""
import math


def main():
    factorial = 10
    square_root = 289
    print(math.factorial(factorial))  # prints the factorial of any given number
    print(math.sqrt(square_root))  # prints the square root of the given number

    # Math module also provide a built in function to calculate the GCD
    # GCD is the greatest common divisor for 2 number. Helps to reduce large fractions
    numerator = 2048
    denominator = 1024
    print(math.gcd(numerator, denominator))


if __name__ == '__main__': main()
