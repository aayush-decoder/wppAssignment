def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or board[i] -i == col - row or board[i] + i == col + row:
            return False
    return True



def solve(board, row):
    if row == 8:
        return True

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col

            if solve(board, row + 1):
                return True

    return False



def print_board(board):
    for row in range(8):
        line = ['.'] * 8
        line[board[row]] = 'Q'
        print(' '.join(line))



board = [-1] * 8


solve(board, 0)

print_board(board)
