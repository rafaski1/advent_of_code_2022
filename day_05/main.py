import re

"""
https://adventofcode.com/2022/day/5
"""

stack = {
    1: ['T', 'D', 'W', 'Z', 'V', 'P'],
    2: ['L', 'S', 'W', 'V', 'F', 'J', 'D'],
    3: ['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H'],
    4: ['R', 'S', 'J'],
    5: ['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W'],
    6: ['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B'],
    7: ['V', 'J', 'P', 'C', 'B', 'D', 'N'],
    8: ['P', 'T', 'B', 'Q'],
    9: ['H', 'G', 'Z', 'R', 'C']
}

stack_copy = stack.copy()

top_stack_1 = ""
top_stack_2 = ""

with open(r"input.txt", "r") as file:
    for line in file.readlines()[10:]:
        line = [int(i) for i in re.findall(r"\d+", line)]
        quantity, from_stack, to_stack = line[0], line[1], line[2]

        for i in range(quantity):
            stack[to_stack].append(stack[from_stack][-1])
            stack[from_stack].pop()

        # part 2
        stack_copy[to_stack].extend(stack_copy[from_stack][-quantity:])
        del stack_copy[from_stack][-quantity:]

    for i in range(1, 10):
        top_stack_1 += stack.get(i)[-1]
        top_stack_2 += stack_copy.get(i)[-1]

    print(top_stack_1)
    print(top_stack_2)
