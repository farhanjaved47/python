"""
Farhan Javed
farhan.javed47@gmail.com
12/24/2019
Generate a Fibonacci sequence using Python generators
"""


def fibonacci(n):
    print('In Fibonacci Generator')
    if n == 1:
        yield 1
    if n == 2:
        yield 1
        yield 1
    if n >= 3:
        base_number = 1
        yield base_number
        next_number = 1
        yield next_number
        for i in range(n-2):
            old_next_number = next_number
            next_number = next_number + base_number
            base_number = old_next_number
            yield next_number


def main():
    fibonacciObject = fibonacci(10)
    print(list(fibonacciObject))


if __name__ == '__main__':main()