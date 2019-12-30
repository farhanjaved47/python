"""
Farhan Javed
farhan.javed47@gmail.com
12/30/2019
Enumeratoins in classes
"""
from enum import Enum, auto


# Can't have same names inside 1 class. Can have same values. In order to make values unique, import unique from enum
# and add the @unique decorator to the class
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    MELON = 4
    KIWI = auto()


def main():
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    print(Fruit.APPLE.name, Fruit.APPLE.value)
    print(Fruit.KIWI.name, Fruit.KIWI.value)

    myFruits = {}
    myFruits[Fruit.BANANA] = "It is a fruit"  # Using enums as hash values
    print(myFruits[Fruit.BANANA])


if __name__ == '__main__':
    main()
