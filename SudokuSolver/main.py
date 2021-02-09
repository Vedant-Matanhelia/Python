"""
This is a sudoku solver.
"""

# The main sudoku
sudoku = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]


def displayBoard(board) -> None:
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            for j in range(11):
                print('- ', end='')
            print()

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print('|', end=' ')

            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end=' ')


def getPos(board) -> tuple:
    for i in (range(len(board))):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j


def checkRow(pos: tuple, board, num):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
        else:
            continue
    return True


def checkCol(pos: tuple, board, num):
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
        else:
            continue
    return True


def checkBox(pos: tuple, board, num):
    x = pos[1] // 3
    y = pos[0] // 3
    for i in range(y*3, (y*3)+3):
        for j in range(x*3, (x*3)+3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def checkValid(pos: tuple, board, num):
    if (checkBox(pos, board, num) and checkCol(pos, board, num)) and checkRow(pos, board, num):
        return True
    else:
        return False


def solve(board):
    space = getPos(board)
    if not space:
        return True  # We have found a solution
    else:
        for i in range(1, 10):
            if checkValid(space, board, i):
                board[space[0]][space[1]] = i

                if solve(board):
                    return True
                else:
                    print(f"backtracking at position {space} and number is {i}")
                    board[space[0]][space[1]] = 0
    return False


if __name__ == '__main__':
    displayBoard(sudoku)
    solve(sudoku)
    displayBoard(sudoku)
