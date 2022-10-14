import numpy as np

# sudoku_4 = np.array([[0, -2, 0, 0, -2, 0],
#                    [-1, -5, -2, -2, -5, -1],
#                    [0, -2, 0, 0, -1, 0],
#                    [0, -1, 0, 0, -2, 0],
#                    [-1, -5, -2, -2, -5, -1],
#                    [0, -1, 0, 0, -1, 0]]

# sudoku_6 = np.array([[0, -2, 0, 0, -2, 0],
#                    [-1, -5, -2, -2, -5, -1],
#                    [0, -2, 0, 0, -1, 0],
#                    [-1, -5, -2, -2, -5, -1],
#                    [0, -2, 0, 0, -1, 0],
#                    [0, -1, 0, 0, -2, 0],
#                    [-1, -5, -2, -2, -5, -1],
#                    [0, -1, 0, 0, -1, 0],
#                    [-1, -5, -2, -2, -5, -1],
#                    [0, -2, 0, 0, -1, 0]])

sudoku4 = np.array([[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]])
sudoku4_minmaj = np.array([[-1, 0, -1, 0], 
            [1, -1, -1, 1],
            [-1, 0, 1, 0],
            [1, 0, -1, 0],
            [1, -1, -1, 1],
            [1, 0, 1, 0]])


print(sudoku4, sudoku4_minmaj)

def find_next_empty(sudoku, size):
    for r in range(1, size):
        for c in range(1, size): 
            if sudoku[r][c] == 0:
                return r, c
    return None, None  

def find_next_empty(sudoku, size):
    for r in range(1, size):
        for c in range(1, size): 
            if sudoku[r][c] == 0:
                return r, c
    return None, None  


def is_valid(sudoku, guess, row, col, size):
    # figures out whether the guess at the row/col of the sudoku is a valid guess
    # returns True or False

    # for a guess to be valid, then we need to follow the sudoku rules
    # that number must not be repeated in the row, column, or 3x3 square that it appears in

    # let's start with the row
    row_vals = sudoku[row]
    if guess in row_vals:
        return False  # if we've repeated, then our guess is not valid!

    # now the column
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(sudoku[i][col])
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

    # # and then the square
    # row_start = (row // 3) * 3  # 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0
    # col_start = (col // 3) * 3

    # for r in range(row_start, row_start + 3):
    #     for c in range(col_start, col_start + 3):
    #         if sudoku[r][c] == guess:
    #             return False

    return True

def array_of_possibles(sudoku, sudoku_minmaj, size):
    minmaj = []
    for r in range(size):
        for c in range(size):
            for r_minmaj in range(sudoku_minmaj.size[0]):
                for c_minmaj in range(sudoku_minmaj.size[1]):
                    if sudoku_minmaj == 1 or sudoku_minmaj == -1:
                        minmaj.append(sudoku_minmaj[r][c])
                        minmaj.append(sudoku_minmaj[r+1][c])

                        sudoku[r][c] = minmaj
                        #ideia aqui é que o sudoku se torne os possiveis valores

                        # ex:
                        # [[2,3], [3,4], [1,2], [2,3]]

# if sudoku[r][c] == 0: sudoku[r][c] = [1,2,3,4] #at the beginning












    # return None, None  # if no spaces in the sudoku are empty (-2)
# def generate_parts(sudoku_size):
#     if sudoku_size == 4:
#         sudoku[r][c]
#         for r in range(-1,4):
#             for c in range(-1,4):  
#                 if sudoku[r][c] == 0:
#                     return r, c
#     # elif sudoku_size == 6:
#     # elif sudoku_size == 9:
#     # else:
#     #     return "erro"

# generate_parts(sudoku_size)

        