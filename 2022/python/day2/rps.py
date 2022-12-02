def get_winner(X, Y):
    match X:
        case "A":
            match Y:
                case "X":
                    return 4
                case "Y":
                    return 8
                case "Z":
                    return 3
        case "B":
            match Y:
                case "X":
                    return 1
                case "Y":
                    return 5
                case "Z":
                    return 9
        case "C":
            match Y:
                case "X":
                    return 7
                case "Y":
                    return 2
                case "Z":
                    return 6

def get_predicted_winner(X, Y):
    match X:
        case "A":
            match Y:
                case "X":
                    return 3
                case "Y":
                    return 4
                case "Z":
                    return 8
        case "B":
            match Y:
                case "X":
                    return 1
                case "Y":
                    return 5
                case "Z":
                    return 9
        case "C":
            match Y:
                case "X":
                    return 2
                case "Y":
                    return 6
                case "Z":
                    return 7

if __name__ == "__main__":
    with open("test.txt") as file:
        lines = file.readlines()
        xs = [x.split(" ")[0] for x in lines]
        ys = [y.split(" ")[1].strip("\n") for y in lines]
        scores = list(map(get_winner, xs, ys))
        print("part 1:", sum(scores))
        scores = list(map(get_predicted_winner, xs, ys))
        print("part 2:", sum(scores))
