# Bitwise Operators
# Farhan Javed
# farhan.javed47@gmail.com
# 12/2/2019


def main():
    x = 0x0a
    y = 0x02

    z = x & y  # bitwise and
    print(f'(hex) x is {x:02x}, y is {y:02x}, x & y is {z:02x}')
    print(f'(bin) x is {x:08b}, y is {y:08b}, x & y is {z:08b}')

    o = x or y  # bitwise or
    print(f'(hex) x is {x:02x}, y is {y:02x}, x or y is {o:02x}')
    print(f'(bin) x is {x:08b}, y is {y:08b}, x or y is {o:08b}')

    xr = x ^ y  # bitwise xor - helps to flip the bits.
    print(f'(hex) x is {x:02x}, y is {y:02x}, x xor y is {xr:02x}')
    print(f'(bin) x is {x:08b}, y is {y:08b}, x xor y is {xr:08b}')

    shiftLeft = x << y  # shift left operator
    print(f'(hex) x is {x:02x}, y is {y:02x}, x << y is {shiftLeft:02x}')
    print(f'(bin) x is {x:08b}, y is {y:08b}, x << y is {shiftLeft:08b}')

    shiftRight = x >> y  # shift right operator
    print(f'(hex) x is {x:02x}, y is {y:02x}, x >> y is {shiftRight:02x}')
    print(f'(bin) x is {x:08b}, y is {y:08b}, x >> y is {shiftRight:08b}')


main()

#  python operator precedence
#  https://docs.python.org/3/reference/expressions.html
