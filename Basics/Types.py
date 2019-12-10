# Object types in Python
# Farhan Javed
# farhan.javed47@gmail.com
# 12/2/2019


def main():
    x = (1, 2, 3, 4, 5)
    print('x is {}'.format(x))
    print(type(x))

    y = (1, 'two', 3.0, [4,'four'], 5)
    print('y is {}'.format(y))
    print(type(y))

    print(type(y[1]))

    print(id(x))  # prints a unique number identifying x
    print(id(y))  # prints a unique number identifying y

    if x[0] is y[0]:  # is simply checks for similarity
        print('x[0] is the same as y[0]')
    else:
        print('x[0] is not the same as y[0]')

    #  finding out the type of an object using the isinstance function
    if isinstance(x, tuple):
        print('x is a tuple')
    elif isinstance(x, list):
        print('x is a list')
    else:
        print('x is neither a list, not a tuple')


main()