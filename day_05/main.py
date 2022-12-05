import re

"""
https://adventofcode.com/2022/day/5
"""

stack = {
    1: ["P", "V", "Z", "W", "D", "T"],
    2: ["D", "J", "F", "V", "W", "S", "L"],
    3: ["H", "B", "T", "V", "S", "L", "M", "Z"],
    4: ["J", "S", "R"],
    5: ["W", "L", "M", "F", "G", "B", "Z", "C"],
    6: ["B", "G", "R", "Z", "H", "V", "W", "Q"],
    7: ["N", "D", "B", "C", "P", "J", "V"],
    8: ["Q", "B", "T", "P"],
    9: ["C", "R", "Z", "G", "H"]
}

top_stack = ""
with open(r"input.txt", "r") as file:
    for line in file.readlines()[10:]:
        line = [int(i) for i in re.findall(r"\d+", line)]
        quantity, from_stack, to_stack = line[0], line[1], line[2]

        for i in range(quantity):
            stack[to_stack].append(stack[from_stack][-1])
            stack[from_stack].pop()

    for i in range(1, 10):
        top_stack += stack.get(i)[-1]

    print(top_stack)
