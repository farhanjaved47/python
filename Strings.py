"""
Farhan Javed
farhan.javed47@gmail.com
12/7/2019
Python String class functionality
https://docs.python.org/3/library/stdtypes.html
"""
# strings are objects in Python and we can always call methods on them as well.


def main():
    print('UPPER CASE'.upper())  # changes the string to all upper caps
    print('swaPPeD CasE'.swapcase())  # swaps the cases of the strings
    print('String formatting: {}'.format(11 * 3))
    print('only first letter is capitalized'.capitalize())  # only first letter is capitalized
    print('first letter of every word is capitalized'.title())  # capitalizes first letter of every word
    print('EVERYTHING IS IN LOWER CASE NOW'.casefold())  # everything is now is lowercase
    # Since strings are immutable, calling the above and other functions will return a copy of the string because as
    # discussed before, immutable objects are passed by value.
    s0 = 'string1'
    s00 = 'string2'
    s0super = s0 + s00  # string objects can be concatenated with a + sign.
    print(s0super)
    s1 = 'this string ' 'that string'  # string literals don't need a plus sign in between.
    print(s1)
    x = 12
    y = 5
    print('Formatting numbers : {first} {second}'.format(first=x, second=y))
    print('Formatting numbers : {0} {1} {0}'.format(x, y))

    # Splitting and Joining Strings
    s = 'We will divide this string into different parts'
    s1 = s.split()  # splits on the bases of spaces and removes them
    print(s1)
    split_on_i = s.split('i')  # splits on the basis of i and removes all the is
    print(split_on_i)

    s2 = ':'.join(s1)  # Join back the strings using whatever
    print(s2)


if __name__ == '__main__': main()