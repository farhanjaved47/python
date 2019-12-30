"""
Farhan Javed
farhan.javed47@gmail.com
12/30/2019
Working with different Python comprehensions such as list, dictionary and set.
"""


def listComprehensions():
    # replacement for filter and map functions
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    evenSquared = [e ** 2 for e in evens]
    print(evenSquared)

    oddSquared = [e ** 2 for e in odds if 3 < e < 17]  # filter out using if statement
    print(oddSquared)


def dictionaryComprehension():
    ctemps = [0, 12, 34, 100]
    # build a dict with celsius as key and fahrenheit as value
    tempDict = {t: (t*9/5) + 32 for t in ctemps if t < 100}
    print(tempDict)
    print(tempDict[12])

    team1 = {"Jones": 24, "Jameson": 18}
    team2 = {"White": 12}

    newTeam = {k: v for team in (team1, team2) for k, v in team.items()}
    print(newTeam)


def setComprehension():
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]
    ftemps1 = {(t*9/5)+32 for t in ctemps}
    print(ftemps1)


def main():
    setComprehension()


if __name__ == '__main__':
    main()