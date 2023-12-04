import re


def part_1(input: list) -> int:
    sum = 0
    for line in input:
        count = 0
        for num in line[1]:
            if num in line[0]:
                if count == 0:
                    count += 1
                else:
                    count *= 2
        sum += count
    return sum

def part_2(input: list) -> int:
    sum = 0
    for line in input:
        count = 0
        for num in line[1]:
            if num in line[0]:
                if count == 0:
                    count += 1
                else:
                    count *= 2
        sum += count
    return sum

if __name__ == "__main__":
    with open("example.txt", "r") as f:
        lines = f.readlines()
        input = []
        for line in lines:
            if ":" in line:
                line = line[line.find(":") + 1:]
            winning, own = line.split("|")
            winning = re.findall(r"\d+", winning)
            own = re.findall(r"\d+", own)
            input.append([winning, own])

    print("Part 1:", part_1(input))
    print("Part 2:", part_2(input))