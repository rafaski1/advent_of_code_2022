"""
https://adventofcode.com/2022/day/3
"""

with open(r"input.txt", "r") as file:
    lines = []
    common_list = []
    common_list_num = []
    for i in file.readlines():
        line = [char for char in i.strip()]
        lines.append(line)
        first = line[:len(line) // 2]
        second = line[len(line) // 2:]
        for char in first:
            if char in second:
                common_list.append(char)
                break

    for char in common_list:
        if char.islower():
            common_list_num.append(ord(char) - 96)
        else:
            common_list_num.append(ord(char) - 64 + 26)

    print(common_list)
    print(common_list_num)
    print(sum(common_list_num))

    # part 2
    file.seek(0)
    common_list = []
    new_common_list_num = []
    for i in range(3, len(lines) + 3, 3):
        a = lines[i-3:i-2]
        b = lines[i-2:i-1]
        c = lines[i-1:i]
        common = set(a[0]) & set(b[0]) & set(c[0])
        common_list.extend(common)

    for char in common_list:
        if char.islower():
            new_common_list_num.append(ord(char) - 96)
        else:
            new_common_list_num.append(ord(char) - 64 + 26)

    print(common_list)
    print(new_common_list_num)
    print(sum(new_common_list_num))





