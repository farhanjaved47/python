def main():
    myList = [1, 2, 3, 4, 5]  # this is a list. Initialized by square brackets []
    myList[4] = 7  # list are mutable. This means that you can change their content after initialization.

    for i in myList:
        print("Value in list : " + str(i))

    myTuple = (1, 2, 3, 4, 5)  # this is a tuple. Initialized by round brackets ( )

    for i in myTuple:
        print("Value in tuple: " + str(i))

    # myTuple[4] = 8  # Tuples are immutable. Running this command will throw an error.


main()