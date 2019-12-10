def main():
    myList = [1, 2, 3, 4, 5]  # this is a list. Initialized by square brackets []
    myList[4] = 7  # list are mutable. This means that you can change their content after initialization.

    for i in myList:
        print("Value in list : " + str(i))

    myTuple = (1, 2, 3, 4, 5)  # this is a tuple. Initialized by round brackets ( )

    for i in myTuple:
        print("Value in tuple: " + str(i))

    # myTuple[4] = 8  # Tuples are immutable. Running this command will throw an error.

    #  Tuples preferred unless you know for sure that you have to change the values.

    oneArgRange = range(5)  # this call only gives the start parameter to range
    for i in oneArgRange:
        print("value in one argument range : " + str(i))

    twoArgRange = range(5, 10)  # this call gives the start and end parameter to range
    for i in twoArgRange:
        print("value in two argument range : " + str(i))

    fullArgRange = range(5, 50, 5)  # this call gives start, end and the step parameter
    for i in fullArgRange:
        print("value in complete argument range : " + str(i))

    #  end parameter values are non inclusive in range.
    #  range is also immutable
    listFromRange = list(range(1, 100, 10))  # mutable lists can be made from immutable range
    listFromRange[2] = 0
    for i in listFromRange:
        print("Value in List made from range : " + str(i))

    #  Dictionaries are a structure of key value pairs and are mutable

    myDict = {'keyOne': 1, 'keyTwo': 2, 'keyThree': 3, 'keyFour': 4, 'keyFive': 5}

    myDict['keyThree'] = 33
    for key, value in myDict.items() :
        print("Printing dictionary key value pairs : " + key + " " + str(value))

main()