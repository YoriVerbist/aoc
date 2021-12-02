def part1():
    with open("input.txt", 'r') as file:
        lines = [line.rstrip().split(" ") for line in file.readlines()]
        hor = 0
        depth = 0
        for line in lines:
            direction = line[0]
            amount = int(line[-1])
            if direction == "forward":
                hor += amount
            elif direction == "down":
                depth += amount
            else:
                depth -= amount
        print(f"depth: {depth}, horizontal movement: {hor}")
        print(f"depth multiplied by horizontal movement is {hor * depth}")


def part2():
    with open("input.txt", 'r') as file:
        lines = [line.rstrip().split(" ") for line in file.readlines()]
        hor = 0
        depth = 0
        aim = 0
        for line in lines:
            direction = line[0]
            amount = int(line[-1])
            if direction == "forward":
                hor += amount
                depth += (amount * aim)
            elif direction == "down":
                aim += amount
            else:
                aim -= amount
        print(f"depth: {depth}, horizontal movement: {hor}")
        print(f"depth multiplied by horizontal movement is {hor * depth}")


part2()
