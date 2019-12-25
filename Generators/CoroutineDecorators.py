"""
Farhan Javed
farhan.javed47@gmail.com
12/24/2019
CoRoutine decorators in order to remove priming the coroutine at run time.
"""


def coroutine_decorator(func):
    def wrap(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return wrap


@coroutine_decorator
def coroutine_example():
    while True:
        x = yield
        print(x)


def main():
    c = coroutine_example()
    c.send('Yayyy!')


if __name__ == '__main__': main()
