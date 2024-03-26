# Code with object-oriented programming
#Sudoku text files
sudoku1="Sudoku-Board/sudoku1.txt"
sudoku2="Sudoku-Board/sudoku2.txt"
sudoku3="Sudoku-Board/sudoku3.txt"
sudoku4="Sudoku-Board/sudoku4.txt"
sudoku5="Sudoku-Board/sudoku5.txt"

# Creating my class SudokuSolver 
class SudokuSolver():
    # Initializing the class SudokuSolver : incorporating the file_name as the object to be processed
    def __init__(self, file_name):
        self.grid = self.read_file(file_name)
        #self.grid will be used as the principal object
    
    # Function to specify how to read the file
    def read_file(self, name_file):
        with open(name_file, 'r') as reading:
            grid = [[int(ch) if ch != '_' else 0 for ch in line.strip()] for line in reading]
            # Removing empty spaces and converting '_' into 0 
            return grid
            # my grid has now 0 instead of _

    # Function to solve the sudoku with the object 'grid'
    def solve_sudoku(self):

        # Fuction to check numbers and their positions
        def is_valid(num, row, col):

            # Loop to examine if the number exists
            for i in range(9):
                if self.grid[row][i] == num or self.grid[i][col] == num:
                    return False
            
            # Assigment of positions for rows and columns in a bloc of 3*3
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)

            # Check if my number exist in the bloc 3*3 with start_row, start_col
            for i in range(3):
                for j in range(3):
                    if self.grid[start_row + i][start_col + j] == num:
                        return False
                    
            return True

        # Function to solve sudoku with numbers to fill 
        # Indentification of empty rows and lines
        def solve_next_empty(row, col):
            # if we are at the end of lines and rows, sudoku is finished
            if row == 8 and col == 9:
                return True
            
            # if we are at the end of the line, we go to the next row
            if col == 9:
                row += 1
                col = 0

            # if row and line are full, go to the next line
            if self.grid[row][col] != 0:
                return solve_next_empty(row, col + 1)
            
            # Loop to introduce numbers from 1 to 9 at the empty spots 
            for num in range(1, 10):
                if is_valid(num, row, col):
                    self.grid[row][col] = num

                    # Solve the sudoku by replacing the empty spot with the exact number
                    if solve_next_empty(row, col + 1):
                        return True
                    
                    # If it's not valide, back to 0 
                    self.grid[row][col] = 0

            return False

        return solve_next_empty(0, 0)


    # Visualization of the sudoku grid 
    def print_grid(self):
        for row in self.grid:
            print(row)

    # Function to show the solved sudoku
    def show_solved_sudoku(self):

    #  Excecution of my solve function and printing the result
        if self.solve_sudoku():
            print("Solution: \n ")
            self.print_grid()
            print("Congratulation, your sudoku is solved")

        else:
            print("No solution.")


# Once all the code is run, test with cProfile.run() to have the total run time taken
# by the entire code

import cProfile

cProfile.run("solve_sudoku(grid)")
