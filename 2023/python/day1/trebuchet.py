import re

DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def solve_part1(input: list) -> int:
    sum = 0
    for line in input:
        numbers = re.findall('[0-9]', line)
        sum += int(numbers[0] + numbers[-1])
    return sum

def solve_part2(input: list) -> int:
    sum = 0
    for line in input:
        numbers = re.findall('(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', line)
        tmp = numbers
        for i in range(len(numbers)):
            if tmp[i] in DIGITS:
                numbers[i] = DIGITS[tmp[i]]
        sum += int(numbers[0] + numbers[-1])
    return sum

if __name__ == "__main__":
    with open("puzzle.txt") as input_file:
        lines = input_file.readlines()
        print("Part 1:", solve_part1(lines))
        print("Part 2:", solve_part2(lines))
