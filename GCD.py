"""
Farhan Javed
farhan.javed47@gmail.com
12/09/2019
Find the greatest common divisor using Euclid's algorithm
"""


def gcd(a, b):
    while b != 0:
        t = a
        a = b
        b = t % b
    return a


def main():
    print(gcd(12, 4))
    print(gcd(60, 96))
    print(gcd(20, 8))


if __name__ == '__main__': main()
