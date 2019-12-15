"""
Farhan Javed
farhan.javed47@gmail.com
12/15/2019
Basic Math functionality in python 3 - IterTools module
https://docs.python.org/3/library/math.html
"""
import itertools


def main():
    # Infinite Counting
    for x in itertools.count(50, 100):  # will count from 50 to infinity
        print(x)
        if x == 150:  # or any other condition
            break
    counter = 0
    # Infinite Cycling
    for c in itertools.cycle([1, 'a', 2, 'b']):
        print(c)
        counter += 1
        if counter == 20:
            break
    # Infinite Repeating

    for r in itertools.repeat(True):
        print(r)
        counter += 1
        if counter == 40:
            break
    # Permutations and Combinations
    # Permutations is different orders of things. Order does matter - Factorial
    # Combinations takes different combinations of a smaller set from a larger set. Order does not matter.

    election = {1: 'Barb', 2: 'Karen', 3: 'Erin'}
    for p in itertools.permutations(election.values()):
        print(p)  # 3! basically

    colors_for_painting = ['Red', 'Blue', 'Orange', 'Purple', 'Pink']
    for c in itertools.combinations(colors_for_painting, 2):
        print(c)


if __name__ == '__main__': main()
