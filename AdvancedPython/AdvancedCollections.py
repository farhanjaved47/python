"""
Farhan Javed
farhan.javed47@gmail.com
12/30/2019
Working with the advanced set of collections in Python
"""
# Python has 4 basic collections types :
# Lists : Mutable sequence of values
# Tuples : Fixed sequence of values
# Set : Sequence of distinct values
# Dictionary : Collection of key-value pairs

# Python's collections module provides more collections such as :
# namedtuple : Tuple with named fields
# OrderedDict, defaultdict : Dictionaries with special properties
# Counter : Counts distinct values
# deque : Double-ended list objects (pronounced deck)
import collections
from collections import defaultdict, Counter, OrderedDict, deque
import string


def usingNamedTuples():
    # namedtuple is used to give meaning to an otherwise random tuple in terms of code readability
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    print(p1, p2)
    print(p1.x)
    print(p2.y)

    p1 = p1._replace(x=100)
    print(p1)


def usingDefaultDict():
    # defining a list of items we want to count
    fruits = ['apple', 'pear', 'orange', 'banana', 'apple', 'grape', 'banana', 'banana']
    # use a dictionary to count each element
    fruitCounter = defaultdict(int)
    # fruitCounter = defaultdict(lambda: 100)
    # in case of a normal dictionary, we'd have to add the condition to check if a key exists.
    # default dictionary takes care of that for us.
    for fruit in fruits:
        fruitCounter[fruit] += 1

    for (key, value) in fruitCounter.items():
        print(f'{key} : {value}')


def usingCounters():
    # Counters are a subclass of the dictionary class
    class1 = ['Farhan', 'Javed', 'Ali', 'Amna', 'Karim', 'Farhan', 'Hanya', 'Farukh', 'Farhan']
    class2 = ['Sandara', 'Bill', 'Sara', 'Joe', 'Christine', 'Andrew', 'Ali']

    c1 = Counter(class1)
    c2 = Counter(class2)

    print(c1['Farhan'])  # How many students in class1 named Farhan?
    print(sum(c1.values()), " students in class 1")  # How many students are in class 1
    c1.update(class2)  # Adds the class2 list as well
    print(sum(c1.values()), " students in class 1 and 2")

    # most common names in two classes - top 3
    print(c1.most_common(3))

    # separate the classes again
    c1.subtract(class2)
    print(sum(c1.values()), " students in class 1")  # How many students are in class 1

    # what's common between 2 classes
    print(c1 & c2)


def usingOrderedDict():
    sportsTeam = [("Royals", (18,12)), ("Rockets", (24, 6)),
                  ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                  ("Kinds", (15, 15)), ("Chargers", (20, 10)),
                  ("Jets", (16, 14)), ("Warriors", (25, 5)),
                  ]

    sortedTeams = sorted(sportsTeam, key=lambda t: t[1][0], reverse=True)

    # Create an ordered dict
    teams = OrderedDict(sortedTeams)
    print(teams)
    # can use popitem to pop the top item like a stack
    tm, wl = teams.popitem(False)
    print('Top team: ', tm, wl)

    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "b": 2, "c": 3})
    # check for equality
    print("Equality test : ", a == b)


def usingDeque():
    # double ended queue, pronounced "deck"
    d = deque(string.ascii_lowercase)
    print('Item count : ', str(len(d)))
    for element in d:
        print(element.upper(), end=",")

    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(d)


def main():
    usingDeque()


if __name__ == "__main__":
    main()
