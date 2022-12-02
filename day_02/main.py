from collections import defaultdict, Counter

"""
https://adventofcode.com/2022/day/2
"""

"""
mapping part one:
A : rock
B : paper
C : scissors

X : rock +1
Y : paper +2 
Z : scissors +3

win : +6
draw : +3
defeat : +0
"""

mapper_part_one = {
    "A X": 3 + 1,
    "A Y": 6 + 2,
    "A Z": 0 + 3,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 6 + 1,
    "C Y": 0 + 2,
    "C Z": 3 + 3
}

"""
mapping part two:
A : rock +1
B : paper +2
C : scissors +3

X : defeat +0
Y : draw +3 
Z : win +6

"""

mapper_part_two = {
    "A X": 0 + 3,
    "A Y": 3 + 1,
    "A Z": 6 + 2,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 0 + 2,
    "C Y": 3 + 3,
    "C Z": 6 + 1
}


with open(r"input.txt", "r") as file:
    strategy = [char.strip() for char in file.readlines()]

    result_part_one = 0
    result_part_two = 0
    for pair in strategy:
        if pair in mapper_part_one.keys():
            result_part_one += mapper_part_one[pair]
        if pair in mapper_part_two.keys():
            result_part_two += mapper_part_two[pair]

    print(result_part_one)
    print(result_part_two)


