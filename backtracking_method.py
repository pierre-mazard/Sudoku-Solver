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

def calculate_execution_time(grid, num_trials):
    # calculate the execution time of the sudoku solver if num_trials is 1
    if num_trials <= 1:
        start_time = time.perf_counter()
        solve_sudoku(grid)
        end_time = time.perf_counter()
        return end_time - start_time, 0, end_time - start_time
    # calculate the average execution time, standard deviation, and total time
    execution_times = []
    for _ in range(num_trials):
        start_time = time.perf_counter()
        solve_sudoku(grid)
        end_time = time.perf_counter()
        execution_times.append(end_time - start_time)

    avg_execution_time = statistics.mean(execution_times)
    std_deviation = statistics.stdev(execution_times)
    uncertainty = std_deviation / (num_trials ** 0.5)
    total_time = avg_execution_time + uncertainty

    return avg_execution_time, uncertainty, total_time


def main():
    while True:  # loop to solve multiple sudokus
        sudoku_folder = "Sudoku-Board"
        filenames = [os.path.join(sudoku_folder, f"sudoku{i}.txt") for i in range(1, 6)]

        # print the list of available sudokus
        print("Chose a Sudoku to resolve:")
        for i, filename in enumerate(filenames, start=1):
            print(f"{i}. {filename}")

        # ask the user for the sudoku number
        choice = int(input("Enter the Sudoku number: ")) - 1
        selected_filename = filenames[choice]
        
        # ask the user for the number of trials
        num_trials = int(input("Enter the number of trials: "))
        print(f"Solving Sudoku in {selected_filename}:")
        
        # load the sudoku grid, calculate the execution time, and print the sudoku grid and execution time statistics 
        sudoku_grid = load_sudoku(selected_filename)
        empty_cells = sum(row.count(0) for row in sudoku_grid) # count the number of initially empty cells
        avg_time, uncertainty, total_time = calculate_execution_time(sudoku_grid, num_trials)
        print_sudoku(sudoku_grid)
        
        # print the number of initially empty cells
        print(f"\nNumber of initially empty cells: {empty_cells}")

        # print the execution time if num_trials is 1, else print the average execution time, standard deviation, and total time
        if num_trials == 1:
            print(f"Execution time : {avg_time:.6f} seconds\n")
        else:
            print(f"Number of trials: {num_trials}")
            print(f"Average execution time: {avg_time:.6f} seconds ± {uncertainty:.6f} seconds")
            print(f"Total time (including uncertainty): {total_time:.6f} seconds\n")

        # ask the user if they want to retry or quit
        choice = input("Do you want to retry (r) or quit (q)? ")
        if choice.lower() == "q":
            break

# execute the main function
if __name__ == "__main__":
    main()