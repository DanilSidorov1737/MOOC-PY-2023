# Write your solution here

# Write your solution here

def row_correct(sudoku: list, row_no: int):
   

    numbers_checked = []
    for j in range(len(sudoku[row_no])):
        if sudoku[row_no][j] > 0 and sudoku[row_no][j] in numbers_checked:
            return False
        numbers_checked.append(sudoku[row_no][j])
    return True
            


            


if __name__ == "__main__":
    
    print(row_correct())




