import numpy as np


def initialize_empty_board(max):
    return np.zeros((max, max), dtype=int)


def get_board(filename):
    with open(filename, "r") as f:
        lines = [line.strip("\n").split(" -> ") for line in f.readlines()]
        max = find_min_max(lines) + 1
        empty_board = initialize_empty_board(max)
        for line in lines:
            x1, y1 = map(int, line[0].split(","))
            x2, y2 = map(int, line[1].split(","))
            if x1 == x2 or y1 == y2:
                if y1 == y2:
                    if x1 > x2:
                        x1, x2 = x2, x1
                    for i in range(x1, x2 + 1):
                        if empty_board[y1][i] != 0:
                            empty_board[y1][i] += 1
                        else:
                            empty_board[y1][i] = 1
                if x1 == x2:
                    if y1 > y2:
                        y1, y2 = y2, y1
                    for i in range(y1, y2 + 1):
                        if empty_board[i][x1] != 0:
                            empty_board[i][x1] += 1
                        else:
                            empty_board[i][x1] = 1
            else:
                print(y1, y2, x1, x2)
                for i in range((x2 - x1 + 1)):
                    if empty_board[y1 + i][x1 + i] != 0:
                        empty_board[y1 + i][x1 + i] += 1
                    else:
                        empty_board[y1 + i][x1 + i] = 1
        return empty_board


def find_min_max(l):
    temp = [num.split(",") for pair in l for num in pair]
    l = list(map(int, np.array(temp).flatten()))
    max_val = max(l)
    return max_val


def calculate_multiple(board):
    return np.count_nonzero(board > 1)


def part_1():
    filename = "test.txt"
    board = get_board(filename)
    print(board)
    sol = calculate_multiple(board)
    print(sol)


part_1()
