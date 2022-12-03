import string


def find_common_char(string):
    middle = len(string) // 2
    first = string[:middle]
    last = string[middle:]
    common = list(set(first) & set(last))
    return common[0]


def group_three(sacks):
    l = []
    count = 0
    group = []
    for sack in sacks:
        sack = sack.strip("\n")
        group.append(sack)
        count += 1
        if count % 3 == 0:
            l.append(group)
            group = []
    return l


def find_common_char_three_group(strings):
    return list(set(strings[0]) & set(strings[1]) & set(strings[2]))[0]


if __name__ == "__main__":
    alphabet = list(string.ascii_letters)
    with open("input.txt") as file:
        lines = file.readlines()
        values = list(map(find_common_char, lines))
        scores = [alphabet.index(letter) + 1 for letter in values]
        print("part 1:", sum(scores))
        groups = group_three(lines)
        values = list(map(find_common_char_three_group, groups))
        scores = [alphabet.index(letter) + 1 for letter in values]
        print("part 2:", sum(scores))
