import numpy as np

def find_next_empty(sudoku, size):
    for r in range(1, size):
        for c in range(1, size): 
            if sudoku[r][c] == 0:
                return r, c
    return None, None  


def is_valid(sudoku, guess, row, col, size, sudoku_minmaj):

    row_vals = sudoku[row]
    if guess in row_vals:
        return False  

    col_vals = [sudoku[i][col] for i in range(1,size)]
    if guess in col_vals:
        return False

    if size == 4:
        row_start = (row // 2) * 2  
        col_start = (col // 2) * 2

    for r in range(row_start, row_start + 2):
        for c in range(col_start, col_start + 2):
            if sudoku[r][c] == guess:
                return False

    for r in range(1, size):
        for c in range(1, size):
            for sym in sudoku_minmaj[r][c]:
                print(sudoku4_minmaj[0][0])
                if sym[0] == -1:
                    if sudoku[r][c-1] < sudoku[r][c]:
                        return False
                elif sym[1] == -1:
                    if sudoku[r-1][c] < sudoku[r][c]:
                        return False
                elif sym[0] == 1:
                    if sudoku[r][c-1] > sudoku[r][c]:
                        return False
                elif sym[1] == 1:
                    if sudoku[r-1][c] > sudoku[r][c]:
                        return False
                else:
                    continue
    return True


def solve_sudoku(sudoku, sudoku_minmaj, size):

    print(sudoku_minmaj)

    row, col = find_next_empty(sudoku, size)

    if row is None: 
        return True

    for guess in range(1, size):  
        if is_valid(sudoku, guess, row, col, size, sudoku_minmaj):
            sudoku[row][col] = guess
            if solve_sudoku(sudoku):
                return True

        sudoku[row][col] = 0

    return False


sudoku4 = np.array([[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]])


sudoku4_minmaj = np.array([[[0, 0], [1, 0], [0, 0], [1, 0]],
                           [[0, -1], [1, 1], [0, 1], [-1, -1]],
                           [[0, 0], [-1, 0], [0, 0], [1, 0]],
                           [[0, -1], [-1, 1], [0, 1], [-1, -1]]])

solve_sudoku(sudoku4, sudoku4_minmaj, 4)