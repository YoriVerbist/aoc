def calculate_rate(kind, lines):
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
        print(gamma_rate)
        gamma_rate = int(gamma_rate, 2)
        print(gamma_rate)
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


def part1():
    with open("input.txt", "r") as file:
        lines = [line.rstrip() for line in file.readlines()]
        binary = calculate_rate("gamma", lines)
        epsilon = calculate_rate("epsilon", lines)

        consumption = binary * epsilon
        print(f"Power consumption of the submarine is: {consumption}")


part2():
    with open("input.txt", 'r') as file:
        lines = line.rstrip() for line in file.realines()]

part2()
