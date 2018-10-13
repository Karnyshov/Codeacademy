board = []

for x in range(5):
    board.append(["O"] * 5)


def print_board(board_in):
    for x in board_in:
        print(board_in[1:x])


print_board(board)
