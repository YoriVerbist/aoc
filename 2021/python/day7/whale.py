import math


def part_1():
    with open("input.txt") as file:
        line = file.readline().strip("\n")
        positions = [int(num) for num in line.split(",")]
        fuel = find_cheapest_position(positions, "normal")
        print(fuel)


def part_2():
    with open("test.txt") as file:
        line = file.readline().strip("\n")
        positions = [int(num) for num in line.split(",")]
        fuel = find_cheapest_position(positions, "stacking")
        print(fuel)


def find_cheapest_position(positions, counting_type):
    min_pos = min(positions)
    max_pos = max(positions)
    current_pos = sum(positions) // len(positions)
    possible_possitions = {i: math.inf for i in range(min_pos, max_pos + 1)}
    while True:
        total = 0
        if counting_type == "normal":
            for value in positions:
                total += abs(current_pos - value)
        if counting_type == "stacking":
            for value in positions:
                total += sum([x for x in range(abs(current_pos - value) + 1)])
        possible_possitions[current_pos] = total
        if (
            possible_possitions[current_pos] < possible_possitions[current_pos + 1]
            and possible_possitions[current_pos] < possible_possitions[current_pos - 1]
            and possible_possitions[current_pos + 1] != math.inf
            and possible_possitions[current_pos - 1] != math.inf
        ):
            return total
        elif possible_possitions[current_pos] > possible_possitions[current_pos + 1]:
            current_pos += 1
        else:
            current_pos -= 1


part_1()
part_2()
