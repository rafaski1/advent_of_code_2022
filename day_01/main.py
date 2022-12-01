url = "https://adventofcode.com/2022/day/1"

with open(r"input.txt", "r") as file:
    elf = 0
    elf_list = []

    all_calories = [line.rstrip() for line in file]

    for cal in all_calories:
        if cal:
            elf += int(cal)
        else:
            elf_list.append(elf)
            elf = 0

    top_three_elfs = sum(sorted(elf_list)[-3:])

    print(f"The elf carrying most calories, carries: {max(elf_list)} calories")
    print(f"Top 3 elfs carry in total: {top_three_elfs} calories")

