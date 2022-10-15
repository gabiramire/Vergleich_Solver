import numpy as np


def prepare_sudoku(sudoku, sudoku_minmaj, size):
    for r in range(size):
        for c in range(size):
            if sudoku[r][c] == 0:
                sudoku[r][c] = [1,2,3,4]
    sudoku = check_possibilities(sudoku, sudoku_minmaj, size)
    

def check_possibilities(sudoku, sudoku_minmaj, size):

    for r in range(size):
        for c in range(size):
            sym = sudoku_minmaj[r][c]
            for i in sym:
                if i == -1:
                    sudoku[r][c].pop()
                elif i == 1:
                    sudoku[r][c].remove(sudoku[r][c][0])

    for r in range(size):
        print("shcneevers")




sudoku4 = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]


sudoku4_minmaj = [[[0, 0, -1, 1], [1, 0, 0, -1], [0, 0, -1, -1], [1, 0, 0, 1]],
                [[0, -1, -1, 0], [1, 1, 0, 0], [0, 1, 1, 0], [-1, -1, 0, 0]],
                [[0, 0, 1, 1], [-1, 0, 0, -1], [0, 0, -1, -1], [1, 0, 0, 1]],
                [[0, -1, 1, 0], [-1, 1, 0, 0], [0, 1, 1, 0], [-1, -1, 0, 0]]]

print(prepare_sudoku(sudoku4, sudoku4_minmaj, 4))