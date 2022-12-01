def part_1(cals):
    print(max(cals.values()))


def part_2(cals):
    cals = sorted(cals.values(), reverse=True)
    print(sum(cals[0:3]))


def parse_data(l):
    count = 0
    cals = {}
    cals[count] = 0
    for line in l:
        if line != "\n":
            cals[count] += int(line.strip("\n"))
        else:
            count += 1
            cals[count] = 0
    return cals


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()
        calories = parse_data(lines)
        part_1(calories)
        part_2(calories)
