"""
Farhan Javed
farhan.javed47@gmail.com
12/23/2019
Generating a list of even integers between 1 to N using python generators
"""


# normal function
def even_integers_function(n):
    result = []
    for i in range(n):
        if not(i % 2):
            result.append(i)
        return result


# The generator function yields a Generator object which then yields the values
def even_integers_generator(n):
    for i in range(n):
        if not(i % 2):
            yield i


def list_comprehension():
    squares = [x**2 for x in range(10)]
    return squares


# generator expressions are another way of writing generators. Similar to list comprehensions. Returns generator object
def generator_expression(upper):
    return (n for n in range(upper) if n % 2 == 0)


# We can use expressions to create objects as a result of some operation on another object.
# For example we can create a generator object of all upper case names from another list of names
def upper_case_names_generator(names_list):
    return (names.upper() for names in names_list)


# Or convert all items in a list from different data types to integers.
def convert_to_int(mixed_list):
    return (int(n) for n in mixed_list)


def main():
    # squares = list_comprehension()
    # print('List comprehension: ' + str(squares))
    # generatorExpression = generator_expression(10)
    # print('Generator expression : ' + str(generatorExpression))
    # print(list(generatorExpression))
    # names_list = ['Farhan', 'Javed']
    # upperCaseNames = upper_case_names_generator(names_list)
    # print(list(upperCaseNames))
    # mixedList = [1, 2, 2.22, '5', '12']
    # intsList = convert_to_int(mixedList)
    # print(list(intsList))
    evenIntegers = even_integers_generator(10)
    for i in range(5):
        print(next(evenIntegers))
    newEvenIntegers = even_integers_generator(6)
    for i in newEvenIntegers:  # Can use the generatorObject in a for loop as well.
        print(i)
    for i in even_integers_generator(5):  # can even pass the generator function in the loop
        print(i)
    for i in (i for i in range(10)):  # Lastly, can even pass the generator expression in the for loop as well.
        print(i)
    print(max(i for i in range(10)))  # Can pass generator expressions as arguments in other functions
"""
evenIntegers = even_integers_generator(10)
print(list(evenIntegers))
for i in range(5):
    print(next(evenIntegers))
https://stackoverflow.com/questions/59457337/calling-nextgeneratorobject-after-printlistgeneratorobject-throws-a-stopite
"""


if __name__ == '__main__': main()