# Creating my class SudokuSolver 
class SudokuSolver():
    # Initializing the class SudokuSolver with the possibility to choose between 5 files
    def __init__(self):
        self.sudoku_txt = ["Sudoku-Board/sudoku1.txt",
                           "Sudoku-Board/sudoku2.txt",
                           "Sudoku-Board/sudoku3.txt",
                           "Sudoku-Board/sudoku4.txt",
                           "Sudoku-Board/sudoku5.txt"]
        self.grid = None

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
    
    def solve_selected_sudoku(self, file_index):
        if 1 <= file_index <= len(self.sudoku_txt):
            self.file_name = self.sudoku_txt[file_index - 1]
            self.grid = self.read_file(self.file_name)

            if self.solve_sudoku():
                print(f"""⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒
          Solution :
⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒""")
                self.print_grid()
                print(f"""⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒
Bravo! ton sudoku a été résolu!
⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒⌒""")
            else: 
                print("Désolée, je n'ai pas de solution.")
        else: 
            print("Erreur : veuillez choisir un nombre entre 1 et 5.")

    def print_sudoku_files(self):
        print("Veuillez choisir un fichier (entre 1 et 5) : \n")
        for i, file_name in enumerate (self.sudoku_txt, start=1):
            print(f"{i}. {file_name}")

# Once all the code is run, test with cProfile.run() to have the total run time taken
# by the entire code

import cProfile
cProfile.run("solve_sudoku(grid)")
