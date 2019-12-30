"""
Farhan Javed
farhan.javed47@gmail.com
12/30/2019
Part 2 of built in functions in the Python standard library
"""


def filterFunc(x):
    if x % 2:
        return True
    return False


def filterFunc2(x):
    if x.isupper():
        return False
    return True


def squareFunc(x):
    return pow(x, 2)


def toGrade(x):
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    elif x >= 50:
        return 'E'
    return 'F'


def main():
    nums = (1, 8, 45, 11, 221, 57, 72, 89, 92)
    chars = 'abCDEFghIJKlMNopQRstuvWXyz'
    grades = (81, 89, 52, 12, 65, 99, 72, 25, 44, 33)

    # TODO : use filter to remove even numbers from a list
    odds = list(filter(filterFunc, nums))
    print(sorted(odds))
    odds_alt = [filterFunc(x) for x in nums]
    print(sorted(odds_alt))  # generate a list of booleans using list comprehension

    # TODO : use filter on non-numeric sequences
    lowers = list(filter(filterFunc2, chars))
    print(lowers)

    # TODO : use map to create a new sequence of values after applying a given function to each item
    squares = list(map(squareFunc, nums))
    print(sorted(squares))
    squares_alt = [pow(i, 2) for i in nums]
    print(sorted(squares_alt))  # can use list comprehension to achieve the same..

    # TODO :  use sorted and map to convert marks into alphabetical grades
    grades = sorted(grades)
    letter_grades = list(map(toGrade, grades))
    print(letter_grades)


if __name__ == '__main__': main()
