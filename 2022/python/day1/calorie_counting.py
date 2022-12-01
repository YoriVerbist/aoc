if __name__ == "__main__":
    with open("input.txt") as file:
        calories = list(
            map(
                lambda x: sum(map(int, x.strip().split("\n"))),
                file.read().split("\n\n"),
            )
        )
        print("part 1:", max(calories))
        print("part 2:", sum(sorted(calories, reverse=True)[0:3]))
