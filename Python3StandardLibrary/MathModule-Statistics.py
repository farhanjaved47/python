"""
Farhan Javed
farhan.javed47@gmail.com
12/15/2019
Basic Math functionality in python 3 - Statistics module
https://docs.python.org/3/library/math.html
"""
import statistics


def main():
    agesData = [10, 13, 14, 12, 11, 10, 11, 10, 15]
    print(statistics.mean(agesData))
    print(statistics.mode(agesData))
    print(statistics.median(agesData))
    print(sorted(agesData))

    print(statistics.variance(agesData))  # the variance can take an optional second argument of mean (xbar)
    print(statistics.stdev(agesData))  # the variance can take an optional second argument of mean (xbar)
    

if __name__ == '__main__': main()
