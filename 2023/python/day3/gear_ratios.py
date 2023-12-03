import re


def part_1(numbers: list, symbols: list) -> int:
    sum = 0
    already_added = list()
    for _, i_index, j_index in symbols:
        for num, num_index, num_start, num_end in numbers:
            if (i_index in range(num_index - 1, num_index + 2) 
            and j_index in range(num_start - 1, num_end + 2) 
            and (num, num_index, num_start, num_end) not in already_added):
                sum += int(num)
                already_added.append((num, num_index, num_start, num_end))
    return sum

if __name__ == "__main__":
    with open("puzzle.txt", "r") as f:
        lines = f.readlines()
        symbols = list()
        numbers = list()
        for i, line in enumerate(lines):
            line = line.strip("\n")
            num = re.findall(r"\d+", line)
            sym = re.findall(r"[^0-9.]", line)
            sym_pos = re.finditer(r"[^0-9.]", line)
            print(sym_pos)
            for number in num:
                numbers.append((number, i, line.find(number), line.find(number) + len(number) - 1))
            for symbol in sym:
                symbols.append((symbol, i, line.find(symbol)))


    print("Part 1:", part_1(numbers, symbols))