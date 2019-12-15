"""
Farhan Javed
farhan.javed47@gmail.com
12/11/2019
Working with basic Python built in functions
"""


def minimum(a, b):
    return min(a, b)


def roundOff(number):
    return round(number)


def absoluteValue(number):
    return abs(number)


def power(base, exponent):
    return pow(base, exponent)


def main():
    print(min('Farhan', 'Farah'))  # string is compared based on which letter comes first
    print(round(41.3))
    print(absoluteValue(-2323.2))
    probabilityOfOne = 1/6
    numberOfTimes = 2
    print(power(probabilityOfOne, numberOfTimes))

    # Smallest to Largest
    pointsInAGame = [0, -10, -15, -2, 1, 12]
    sortedGame = sorted(pointsInAGame)
    print(sortedGame)

    names = ['Sue', 'Jerry', 'Linda']
    print(sorted(names))
    mixedCase_names = ['Sue', 'Jerry', 'Linda']
    print(sorted('My favourite child is Linda'.split(), key=str.upper))

    print(sorted(pointsInAGame, reverse=True))

    leaderBoard = {
        231: 'Farhan',
        123: 'Alfred',
        432: 'Ryan'
    }

    print( leaderBoard.get((sorted(leaderBoard, reverse=True))[0]))
    # print the value of the highest score in a dictionary
    # (Score, Name)

    students = [('alice', 'B', 12), ('eliza', 'A', 16), ('tega', 'C', 9), ('harry', 'A+', 18)]
    # name, grade, marks
    print(sorted(students, reverse=True, key=lambda student: student[2]))  # sorting on the marks of each student


if __name__ == '__main__': main()
