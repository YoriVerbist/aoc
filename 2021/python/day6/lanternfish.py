def part_1():
    with open("test.txt") as file:
        lines = file.readline().strip("\n")
        fish = [int(line) for line in lines.split(",")]
        total_fish = spawn_fish(fish)
        print(len(total_fish))


def part_2():
    with open("input.txt") as file:
        lines = file.readline().strip("\n")
        temp = [int(line) for line in lines.split(",")]
        fish = {i: 0 for i in range(9)}
        for num in temp:
            fish[num] += 1

        total_fish = spawn_fish_fast(fish)
        print(sum(total_fish.values()))


def spawn_fish(fish):
    for _ in range(80):
        add_fish = 0
        for i, single_fish in enumerate(fish):
            if single_fish == 0:
                add_fish += 1
                fish[i] = 6
            else:
                fish[i] -= 1
        for _ in range(add_fish):
            fish.append(8)
    return fish


def spawn_fish_fast(fish):
    for _ in range(256):
        add_fish = 0
        for key, value in fish.items():
            if key == 0:
                add_fish = value
            else:
                fish[key - 1] = value
        fish[8] = add_fish
        fish[6] += add_fish
    return fish


part_1()
part_2()
