# Write your solution here
def print_sudoku(sudoku: list):
    for i, row in enumerate(sudoku):
     
        for j, square in enumerate(row):
            if j % 3 == 0:  # add separator before every third square
                print(" ", end="")
            if square > 0:
                print(f" {square}", end="")
            else:
                print(" _", end="")
        print()
    

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number


if __name__ == "__main__":


    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)