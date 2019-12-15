"""
Farhan Javed
farhan.javed47@gmail.com
12/15/2019
Basic Math functionality in python 3 - Part 1
https://docs.python.org/3/library/math.html
"""
import math


def main():
    # constants in the math module
    print(math.pi)  # Pi constant
    print(math.e)  # The Euler's constant
    print(math.nan)  # Not a number
    print(math.inf)  # +ive infinity
    print(-math.inf)  # -ive infinity

    # basic trigonometry
    # trigonometric functions take angles in randians
    angle_in_degrees = 90
    angle_in_radians = math.radians(angle_in_degrees)
    print(math.sin(angle_in_radians))
    print(math.cos(angle_in_radians))
    print(math.tan(angle_in_radians))

    # Ceiling and floor functions work on the closest integer
    my_age = 24.6
    my_salary = 45.8
    print(f'My age is {math.floor(my_age)}')
    print(f'My salary is {math.ceil(my_salary)}')


if __name__ == '__main__': main()
