"""
Farhan Javed
farhan.javed47@gmail.com
12/24/2019
Python Coroutines
"""


def counter(string):
    count = 0
    try:
        while True:
            item = yield
            if isinstance(item, str):
                if item in string:
                    count += 1
                    print(item)
                else:
                    print('Not a match')
            else:
                print('Not a String')
    except GeneratorExit:
        print(count)


def main():
    c = counter('Islamabad')
    next(c)  # Priming the coroutine
    c.send('Islam')
    c.send('slam')
    c.send('abad')
    c.send('Islma')

if __name__ == '__main__' : main()



