import re

"""
https://adventofcode.com/2022/day/4
"""

with open(r"input.txt", "r") as file:
    count_part1 = 0
    count_part2 = 0
    for line in file.readlines():
        line = [int(i) for i in re.findall(r"\d+", line)]
        if (line[0] <= line[2]) and (line[1] >= line[3]):
            count_part1 += 1
        elif (line[0] >= line[2]) and (line[1] <= line[3]):
            count_part1 += 1

        # part 2
        x = range(line[0], line[1]+1)
        y = range(line[2], line[3]+1)

        overlap = set(x) & set(y)
        if overlap:
            count_part2 += 1

    print(count_part1)
    print(count_part2)



