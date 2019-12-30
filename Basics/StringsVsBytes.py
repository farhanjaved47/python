"""
Farhan Javed
farhan.javed47@gmail.com
12/30/2019
Basic differences between strings and bytes
"""
# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values.
# Strings cannot be treated like an array of characters (like in other languages)


def main():
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = 'This is a string'
    print(s)

    # TODO : Try combining the two
    # print(s + b)
    # TODO : Bytes and strings need to be properly encoded and decoded before you can work on them together
    s2 = b.decode('utf-8')
    print(s + s2)
    b2 = s.encode('utf-8')
    print(b + b2)

if __name__ == '__main__': main()
