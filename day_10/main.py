with open("input.txt") as file:
    X = 1
    cycle = 0
    signal = 0
    cycles = [20, 60, 100, 140, 180, 220]
    rows = [0, 40, 80, 120, 160, 200]

    screen = [[" " for i in range(40)] for j in range(6)]

    for line in file.readlines():
        line = line.rstrip().split()
        if line[0] == "noop":
            sprite_position = [X - 1, X, X + 1]
            if cycle % 40 in sprite_position:
                screen[cycle // 40][cycle % 40] = "#"
            cycle += 1
            if cycle in cycles:
                signal += cycle * X
        elif line[0] == "addx":
            for i in range(2):
                sprite_position = [X - 1, X, X + 1]
                if cycle % 40 in sprite_position:
                    screen[cycle // 40][cycle % 40] = "#"
                cycle += 1
                if cycle in cycles:
                    signal += cycle * X
            X += int(line[1])

    print(f"part one: {signal}")

    for line in screen:
        print(line)



