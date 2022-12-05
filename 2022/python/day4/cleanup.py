def compare_all(sets):
    set1 = sets[0]
    set2 = sets[1]
    if set1 <= set2 or set1 >= set2:
        return 1
    else:
        return 0


def compare_any(sets):
    set1 = sets[0]
    set2 = sets[1]
    if set1 & set2 != set():
        return 1
    else:
        return 0


if __name__ == "__main__":
    with open("input.txt") as file:
        pairs = list(
            map(
                lambda x: x.strip("\n").split(","),
                file.readlines(),
            ),
        )
        xs = [int(x.split("-")[0]) for y in pairs for x in y]
        ys = [int(x.split("-")[1]) for y in pairs for x in y]
        ranges = [{z for z in range(x, y + 1)} for x, y in zip(xs, ys)]
        ranges = [ranges[i : i + 2] for i in range(0, len(ranges), 2)]
        count = map(compare_all, ranges)
        print("Part 1:", sum(count))
        overlap = map(compare_any, ranges)
        print("Part 2:", sum(overlap))
