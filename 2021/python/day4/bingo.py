import numpy as np


def initialize_empty_boards(boards):
    return np.zeros_like(boards)


def play_bingo(numbers, boards, part):
    empty_boards = initialize_empty_boards(boards)
    print(boards.shape, empty_boards.shape)
    winners = list()
    for num in numbers:
        positions = check_num_in_board(num, boards)
        if positions == set():
            continue
        for i, j, k in positions:
            empty_boards[i][j][k] = 1
            new_winners = check_winner(empty_boards, winners)
            winners = winners + new_winners
            if winners != list() and part == 1:
                sum = calculate_unmarked_numbers(
                    boards[winners[0]], empty_boards[winners[0]]
                )
                return winners, sum, num
            if len(winners) == len(boards) and part == 2:
                sum = calculate_unmarked_numbers(
                    boards[winners[-1]], empty_boards[winners[-1]]
                )
                return winners, sum, num
    print("here")


def calculate_unmarked_numbers(board, marker_board):
    sum = 0
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if marker_board[i][j] == 0:
                sum += num
    return sum


def check_winner(boards, already_won):
    winners = list()
    for i, board in enumerate(boards):
        if i in already_won or i in winners:
            continue
        for j, row in enumerate(board):
            if np.count_nonzero(row) == len(row):
                winners.append(i)
    # Check for vertical winners
    for i, board in enumerate(boards):
        if i in already_won or i in winners:
            continue
        temp = np.transpose(board)
        for j, row in enumerate(temp):
            if np.count_nonzero(row) == len(row):
                winners.append(i)
    return winners


def check_num_in_board(num, boards):
    pos = set()
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k, number in enumerate(row):
                if number == num:
                    pos.add((i, j, k))
    return pos


def get_input(filename):
    with open(filename, "r") as f:
        lines = [line.strip("\n") for line in f.readlines() if line != "\n"]
        numbers = [int(num) for num in lines[0].split(",")]
        boards = list()
        lines = lines[1:]
        pos = -1
        for i in range(len(lines)):
            row = lines[i].split(" ")
            temp = list()
            for num in row:
                if num == "":
                    continue
                temp.append(int(num))
            if i % 5 == 0:
                pos += 1
                boards.append([])
            boards[pos].append(temp)

        boards = np.array(boards)
        return numbers, boards


def part_1():
    filename = "input.txt"
    numbers, boards = get_input(filename)
    winner, sum, num = play_bingo(numbers, boards, 1)
    print(winner, sum, num)
    print(f"solution is: {sum * num}")


def part_2():
    filename = "input.txt"
    numbers, boards = get_input(filename)
    winner, sum, num = play_bingo(numbers, boards, 2)
    print(winner, sum, num)
    print(f"solution is: {sum * num}")


part_2()
