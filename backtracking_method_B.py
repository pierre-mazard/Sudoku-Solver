###### Sudoku text files ######
sudoku1="Sudoku-Board/sudoku1.txt"
sudoku2="Sudoku-Board/sudoku2.txt"
sudoku3="Sudoku-Board/sudoku3.txt"
sudoku4="Sudoku-Board/sudoku4.txt"
sudoku5="Sudoku-Board/sudoku5.txt"

## Beware, Isabelle, you must include the POO method to your code ! 
###### Reading file ######
def read_file(name_file):
    with open(name_file, 'r') as reading:
        grid = [[int(ch) if ch != '_' else 0 for ch in line.strip()] for line in reading]
        # Removing empty spaces and converting '_' into 0 
        return grid

###### Creating the function to solve sudoku ######
def solve_sudoku(grid):

### Fuction to check numbers and their positions ###
    def is_valid(num, row, col):

        # Loop to examine if the number exists
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        
        # Assigment of positions for rows and columns in a bloc of 3*3
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)

        # Check if my number exist in the bloc 3*3 with start_row, start_col
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False
                
        return True

### Function to solve sudoku with numbers to fill ###
### Indentification of empty rows and lines ###
    def solve_next_empty(row, col):
        # if we are at the end of lines and rows, sudoku is finished
        if row == 8 and col == 9:
            return True
        
        # if we are at the end of the line, we go to the next row
        if col == 9:
            row += 1
            col = 0

        # if row and line are full, go to the next line
        if grid[row][col] != 0:
            return solve_next_empty(row, col + 1)
        
        # Loop to introduce numbers from 1 to 9 at the empty spots 
        for num in range(1, 10):
            if is_valid(num, row, col):
                grid[row][col] = num

                # Solve the sudoku by replacing the empty spot with the exact number
                if solve_next_empty(row, col + 1):
                    return True
                
                # If it's not valide, back to 0 
                grid[row][col] = 0

        return False

    return solve_next_empty(0, 0)


###### Visualization of the sudoku grid ######
def print_grid(grid):
    for row in grid:
        print(row)


###### Running the programm ######
grid = read_file(sudoku5)

#  Excecution of my solve function and printing the result
if solve_sudoku(grid):
    print("Solution:")
    print_grid(grid)

else:
    print("No solution.")

## Once all the code is run, test with cProfile.run() to have the total run time taken
    #by the entire code

import cProfile

cProfile.run("solve_sudoku(grid)")
