# Write your solution here

def sudoku_grid_correct(sudoku: list):
    
    # Check rows
    for i in range(len(sudoku)):
        rows_checked = []
        for j in range(len(sudoku)):
            if sudoku[i][j] > 0 and sudoku[i][j] in rows_checked:
                return False
            rows_checked.append(sudoku[i][j])
    
    # Check columns
    for i in range(len(sudoku)):
        cols_checked = []
        for j in range(len(sudoku)):
            if sudoku[j][i] > 0 and sudoku[j][i] in cols_checked:
                return False
            cols_checked.append(sudoku[j][i])

    # Check subgrids
    for row_no in range(0, 9, 3):
        for column_no in range(0, 9, 3):
            numbers_checked = []
            for i in range(row_no, row_no + 3):
                for j in range(column_no, column_no + 3):
                    number = sudoku[i][j]
                    if number != 0 and number in numbers_checked:
                        return False
                    numbers_checked.append(number)

    return True



if __name__ == "__main__":

    print(sudoku_grid_correct())    