import numpy as np


def initialize_empty_boards(boards: list) -> np.ndarray:
    return np.zeros_like(boards)


def check_winner(boards: list) -> int:
    boards = boards.tolist()
    for i in range(len(boards)):
        # Check for horizontal winners
        for row in boards[i]:
            if row.count(1) == len(row) and row[0] != None:
                return i
        # Check for vertical winners
        for col in range(len(boards[i][0])):
            check = []
            for row in boards[i]:
                check.append(row[col])
            if check.count(1) == len(check) and check[0] != None:
                return i
    return -1


def check_if_num_in_board(num: int, board: list) -> list:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == num:
                return [i, j]
    return []


def play_bingo(draws: list, boards: list) -> list:
    empty_boards = initialize_empty_boards(boards)
    for num in draws:
        for i in range(len(boards)):
            in_board = check_if_num_in_board(num, boards[i])
            if in_board != []:
                empty_boards[i][in_board[0]][in_board[1]] = 1
        board_nr = check_winner(empty_boards)
        if board_nr != -1:
            return board_nr, empty_boards, num


def calculate_non_marked(board, empty_board):
    sum = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if empty_board[i][j] == 0:
                sum += board[i][j]
    return sum


def part1():
    with open("input.txt", "r") as file:
        lines = [line.rstrip() for line in file.readlines()]
        draws = [int(num) for num in lines[0].split(",")]
        boards = [[]]
        lines = lines[2:]
        pos = 0
        for i in range(len(lines)):
            if lines[i] == "":
                boards.append([])
                pos += 1
            else:
                temp = []
                for num in lines[i].split(" "):
                    if num == "":
                        continue
                    temp.append(int(num))
                boards[pos].append(temp)

        boards = np.array(boards)
        board_nr, empty_boards, num = play_bingo(draws, boards)
        total = calculate_non_marked(boards[board_nr], empty_boards[board_nr])
        print(f"Final score is: {total * num}")


part1()
