"""
Farhan Javed
farhan.javed47@gmail.com
12/05/2019
Basic functionality for creating and implementing classes in Python including Inheritance and Iterator Objects.
https://docs.python.org/3/reference/datamodel.html#special-method-names
"""


class RevStr(str):  # lowercase class names are predefined classes
    def __str__(self):
        return self[::-1]


class Animal:
    def __init__(self, **kwargs):  # constructor of the class
        if 'type' in kwargs:
            self._type = kwargs['type']  # variables with _ means it only exists with an object and not with the class.
        if 'name' in kwargs:
            self._name = kwargs['name']
        if 'sound' in kwargs:
            self._sound = kwargs['sound']

    def type(self, t=None):
        if t:
            self._type = t
        try:
            return self._type
        except AttributeError:
            return None

    def name(self, n=None):
        if n:
            self._name = n
        try:
            return self._name
        except AttributeError:
            return None

    def sound(self, s=None):
        if s:
            self._sound = s
        try:
            return self._sound
        except AttributeError:
            return None

    def __str__(self):  # built in method for string representation.
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}'


def print_animals(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal object')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


class Duck(Animal):  # Inheritance is implemented by simply writing the parent class name in paranthesis.
    def __init__(self, **kwargs):
        self._type = 'duck'
        if 'type' in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)


class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)

    def kill(self, target):
        print(f'{self.name()} will now kill all {target}!')


class InclusiveRange:
    def __init__(self, *args):
        numargs = len(args)
        self._start = 0
        self._step = 1

        if numargs < 1:
            raise TypeError(f'expected at least 1 argument, for {numargs}')
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start, self._stop, self._step) = args
        else:
            raise TypeError(f'Expected at most 3 arguments, got {numargs}')

        self._next = self._start

    def __iter__(self):  # identifies the InclusiveRange object as the iterator object
        return self

    def __next__(self):
        if self._next > self._stop:
            raise StopIteration
        else:
            _r = self._next
            self._next += self._step
            return _r


def main():
    simba = Kitten(name='fluffy', sound='rawr')
    donald = Duck(name='donald', sound='quack')
    print_animals(simba)
    print_animals(donald)
    simba.kill('humans')

    reverse_this = RevStr("Hakuna Matata")
    print(reverse_this)

    for n in InclusiveRange(25):
        print(n, end=' ')
    print()
    for n in InclusiveRange(5, 25):
        print(n, end=' ')
    print()
    for n in InclusiveRange(0,25,5):
        print(n, end=' ')
    print()

if __name__ == "__main__": main()
