import os
import time
import statistics

def load_sudoku(filename):
    # load the sudoku grid from the file
    grid = []
    with open(filename, "r") as file:
        for line in file:
            row = [int(cell) if cell != "_" else 0 for cell in line.strip()]
            grid.append(row)
    return grid

def is_valid_move(grid, row, col, num):
    # check if the number is already present in the row, column, or 3x3 grid
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
    while True:  # loop to solve multiple sudokus
        sudoku_folder = "Sudoku-Board"
        filenames = [os.path.join(sudoku_folder, f"sudoku{i}.txt") for i in range(1, 6)]

        print("Chose a Sudoku to resolve:")
        for i, filename in enumerate(filenames, start=1):
            print(f"{i}. {filename}")

        choice = int(input("Enter the Sudoku number: ")) - 1
        selected_filename = filenames[choice]

        print(f"Solving Sudoku in {selected_filename}:")
        sudoku_grid = load_sudoku(selected_filename)

        # Perform multiple trials to calculate average execution time
        num_trials = 20 # number of trials to perform for each sudoku grid to calculate average execution time and standard deviation 
        execution_times = []
        for _ in range(num_trials):
            start_time = time.perf_counter()
            solve_sudoku(sudoku_grid)
            end_time = time.perf_counter()
            execution_times.append(end_time - start_time) # record the execution time for each trial 

        # Calculate average execution time and standard deviation
        avg_execution_time = statistics.mean(execution_times)
        std_deviation = statistics.stdev(execution_times)

        # Calculate the uncertainty (standard error of the mean)
        uncertainty = std_deviation / (num_trials ** 0.5)

        total_time = avg_execution_time + uncertainty # total time including uncertainty 

        print_sudoku(sudoku_grid)
        #print number of trials, average execution time, standard deviation, and total time
        print(f"\nNumber of trials: {num_trials}")
        print(f"Average execution time: {avg_execution_time:.6f} seconds ± {uncertainty:.6f} seconds")
        print(f"Total time (including uncertainty): {total_time:.6f} seconds\n")

        choice = input("Do you want to retry (r) or quit (q)? ")
        if choice.lower() == "q":
            break
