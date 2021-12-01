import math

def part1():
    with open("input.txt", 'r') as file:
        lines = file.readlines()
        last = math.inf
        sum = 0
        for line in lines:
            line = int(line.rstrip())
            if line > last:
                sum += 1
            last = line
    print(sum)


def part2():
    with open("input.txt", 'r') as file:
        lines = file.readlines()
        last = math.inf
        sum = 0
        for i in range(len(lines)):
            if i + 2 >= len(lines):
                break
            line = int(lines[i].rstrip())
            current = line + int(lines[i + 1].rstrip()) + int(lines[i + 2].rstrip())
            if current > last:
                sum += 1
            last = current
    print(sum)
            

part2()
