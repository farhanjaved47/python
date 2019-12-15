"""
Farhan Javed
farhan.javed47@gmail.com
12/15/2019
Basic Math functionality in python 3 - Random functions
https://docs.python.org/3/library/math.html
"""
import random


def main():
    print(random.random())  # prints a random number between 0 and 1
    decider = random.randrange(2)  # randrange(2) will give a value of 0 or 1 as it is exclusive.
    if decider:
        print('tails')
    elif not decider:
        print('heads')

    print(random.randrange(1, 7))  # mimic a dice roll

    lottery_winners = random.sample(range(100), 5)
    print(sorted(lottery_winners))

    possible_pets = ['cat', 'dog', 'lizard']
    print(random.choice(possible_pets))

    cards = ['Jack', 'Queen', 'King', 'Ace']
    random.shuffle(cards)
    print(cards)



if __name__ == '__main__': main()