# Write your solution here

# Write your solution here

def column_correct(sudoku: list, column_no: int):
   

    numbers_checked = []
    for j in range(len(sudoku)):
        if sudoku[j][column_no] > 0 and sudoku[j][column_no] in numbers_checked:
            return False
        numbers_checked.append(sudoku[j][column_no])
    return True
            


            


if __name__ == "__main__":
    
    print(column_correct())




