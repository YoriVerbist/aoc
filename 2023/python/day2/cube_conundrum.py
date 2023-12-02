import re

def part_1(colors: dict) -> int:
    sum = 0
    for key in colors.keys():
        if any(x > 12 for x in colors[key]["red"]): 
            continue
        if any(x > 13 for x in colors[key]["green"]): 
            continue
        if any(x > 14 for x in colors[key]["blue"]): 
            continue
        sum += int(key)
    return sum


if __name__ == "__main__":
    with open("puzzle.txt") as file:
        lines = file.readlines()
        colors = dict()
        for line in lines:
            game_id = int(re.findall("[0-9]+", line)[0])
            colors[game_id] = {"blue": [], "red": [], "green": []}
            color_amounts = line.replace(";", ",").replace(":", ",").split(",")[1:]
            for col in color_amounts:
                number = re.findall("[0-9]+", col)[0]
                if "blue" in col:
                    colors[game_id]["blue"].append(int(number))
                if "red" in col:
                    colors[game_id]["red"].append(int(number))
                if "green" in col:
                    colors[game_id]["green"].append(int(number))
        print(colors)
    print("Part 1:", part_1(colors))
