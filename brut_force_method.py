import os
import time

def load_sudoku(filename):
    # load the sudoku grid from the file
    grid = []
    with open(filename, "r") as file:
        for line in file:
            row = [int(cell) if cell != "_" else 0 for cell in line.strip()]
            grid.append(row)
    return grid

def is_valid_move(grid, row, col, num):
    # check if the number is already present in the row, column or 3x3 grid
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

def solve_sudoku(grid):
    # solve the sudoku using backtracking
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def print_sudoku(grid):
    # print the sudoku grid
    for row in grid:
        print(" ".join(str(cell) if cell != 0 else "_" for cell in row))

if __name__ == "__main__":
    while True: # loop to solve multiple sudokus
        sudoku_folder = "Sudoku-Board"
        filenames = [os.path.join(sudoku_folder, f"sudoku{i}.txt") for i in range(1, 6)]

        print("Chose a Sudoku to resolve :")
        for i, filename in enumerate(filenames, start=1):
            print(f"{i}. {filename}")

        choice = int(input("Enter the Sudoku number : ")) - 1
        selected_filename = filenames[choice]

        print(f"Solving Sudoku in {selected_filename}:")
        sudoku_grid = load_sudoku(selected_filename)
        
        # solve the sudoku and measure the execution time
        # start_time = time.perf_counter()
        solve_sudoku(sudoku_grid)
        # end_time = time.perf_counter()

        # calculate the total time and uncertainty
        # execution_time = end_time - start_time 
        # uncertainty = 0.1 
        # total_time = execution_time + uncertainty 

        # print the solved sudoku and the execution time
        print_sudoku(sudoku_grid)
        # print(f"Execution time : {total_time:.6f} secondes ± {uncertainty:.6f} secondes\n")

        # ask the user if they want to solve another sudoku
        choice = input("Do you want to retry (r) or quit (q) ? ")
        if choice.lower() == "q":
            break
