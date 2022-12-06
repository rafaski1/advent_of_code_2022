"""
https://adventofcode.com/2022/day/6
"""

with open("input.txt", "r") as file:
    data = file.readline().strip()
    for i in range(4, len(data)):
        if len(set(data[i-4:i])) == 4:
            print(f"Part one answer: {i}")
            break

    # part two
    for i in range(14, len(data)):
        if len(set(data[i-14:i])) == 14:
            print(f"Part two answer: {i}")
            break
