def calculate_rate(kind: str, lines: list) -> int:
    sum = {}
    for i in range(len(lines[0])):
        sum[i] = 0
    if kind == "gamma":
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if lines[i][j] == "1":
                    sum[j] += 1
        gamma_rate = ""
        for i in range(len(lines[0])):
            if sum[i] >= (len(lines) / 2):
                gamma_rate += "1"
            else:
                gamma_rate += "0"
        gamma_rate = int(gamma_rate, 2)
        return gamma_rate
    if kind == "epsilon":
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if lines[i][j] == "1":
                    sum[j] += 1
        epsilon_rate = ""
        for i in range(len(lines[0])):
            if sum[i] <= (len(lines) / 2):
                epsilon_rate += "1"
            else:
                epsilon_rate += "0"
        epsilon_rate = int(epsilon_rate, 2)
        return epsilon_rate


def calculate_most_common(position: int, lines: list) -> list:
    if len(lines) == 1:
        return lines[0]
    else:
        sum = 0
        for i in range(len(lines)):
            if lines[i][position] == "1":
                sum += 1
        temp = []
        if sum >= (len(lines) / 2):
            for line in lines:
                if line[position] == "1":
                    temp.append(line)
        else:
            for line in lines:
                if line[position] == "0":
                    temp.append(line)
        return calculate_most_common(position + 1, temp)


def calculate_least_common(position: int, lines: list) -> list:
    if len(lines) == 1:
        return lines[0]
    else:
        sum = 0
        for i in range(len(lines)):
            if lines[i][position] == "1":
                sum += 1
        temp = []
        if sum >= (len(lines) / 2):
            for line in lines:
                if line[position] == "0":
                    temp.append(line)
        else:
            for line in lines:
                if line[position] == "1":
                    temp.append(line)
        return calculate_least_common(position + 1, temp)


def part1():
    with open("input.txt", "r") as file:
        lines = [line.rstrip() for line in file.readlines()]
        binary = calculate_rate("gamma", lines)
        epsilon = calculate_rate("epsilon", lines)

        consumption = binary * epsilon
        print(f"Power consumption of the submarine is: {consumption}")


def part2():
    with open("input.txt", "r") as file:
        lines = [line.rstrip() for line in file.readlines()]
        most_common = int(calculate_most_common(0, lines), 2)
        least_common = int(calculate_least_common(0, lines), 2)
        print(most_common, least_common)
        print(
            f"The life support rating of the submarine is: {most_common * least_common}"
        )


part2()
