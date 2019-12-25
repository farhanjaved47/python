"""
Farhan Javed
farhan.javed47@gmail.com
12/24/2019
Python context managers
"""
from contextlib import contextmanager


@contextmanager
def simple_context_manager(obj):
    try:
        # do something here
        obj.some_property += 1
        yield
    finally:
        # wrap up
        obj.some_property -= 1


class SomeObject(object):
    def __init__(self, arg):
        self.some_property = arg


def main():
    someObject = SomeObject(10)
    with simple_context_manager(someObject):
        print(someObject.some_property)
    print(someObject.some_property)


if __name__ == '__main__': main()
