import os
import time
import statistics

# Class to solve Sudoku using backtracking method
class SudokuSolver:
    def __init__(self, filename):
        self.grid = self.load_sudoku(filename) 
        self.empty_cells = sum(row.count(0) for row in self.grid) # Count number of empty cells

    def load_sudoku(self, filename): # Load Sudoku from file
        grid = []
        with open(filename, "r") as file:
            for line in file:
                row = [int(cell) if cell != "_" else 0 for cell in line.strip()]
                grid.append(row)
        return grid

    def is_valid_move(self, row, col, num): # Check if the number is valid to place in the cell 
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.grid[i][j] == num:
                    return False

        return True

    def solve_sudoku(self): # Solve Sudoku using backtracking method 
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid_move(row, col, num):
                            self.grid[row][col] = num
                            if self.solve_sudoku():
                                return True
                            self.grid[row][col] = 0
                    return False
        return True

    def print_sudoku(self): # Print the solved Sudoku grid to the console 
        for row in self.grid:
            print(" ".join(str(cell) if cell != 0 else "_" for cell in row))

    def calculate_execution_time(self, num_trials): # Calculate the execution time to solve Sudoku and return the average, uncertainty, and total time 
        if num_trials <= 1: # If number of trials is 1, calculate only the execution time
            start_time = time.perf_counter()
            self.solve_sudoku()
            end_time = time.perf_counter()
            return end_time - start_time, 0, end_time - start_time

        execution_times = []
        for _ in range(num_trials): # Perform multiple trials to calculate average execution time 
            start_time = time.perf_counter()
            self.solve_sudoku()
            end_time = time.perf_counter() 
            execution_times.append(end_time - start_time) 

        avg_execution_time = statistics.mean(execution_times) # Calculate average execution time 
        std_deviation = statistics.stdev(execution_times) # Calculate standard deviation of execution time
        uncertainty = std_deviation / (num_trials ** 0.5) # Calculate uncertainty in execution time
        total_time = avg_execution_time + uncertainty # Calculate total time including uncertainty

        return avg_execution_time, uncertainty, total_time

def main(): # Main function to solve Sudoku using backtracking method 
    while True:
        sudoku_folder = "Sudoku-Board"
        filenames = [os.path.join(sudoku_folder, f"sudoku{i}.txt") for i in range(1, 6)]

        print("Choose a Sudoku to solve:") # Display the list of Sudoku files to choose from
        for i, filename in enumerate(filenames, start=1):
            print(f"{i}. {filename}")

        choice = int(input("Enter the Sudoku number: ")) - 1
        selected_filename = filenames[choice]

        num_trials = int(input("Enter the number of trials: ")) # Input the number of trials to calculate average execution time
        print(f"Solving Sudoku in {selected_filename}:")

        solver = SudokuSolver(selected_filename) # Create SudokuSolver object
        avg_time, uncertainty, total_time = solver.calculate_execution_time(num_trials) # Calculate average execution time to solve Sudoku 
        solver.print_sudoku() # Print the solved Sudoku grid to the console 

        if num_trials == 1: # Display the execution time, number of empty cells, and total time 
            print(f"\nNumber of empty cells: {solver.empty_cells}")
            print(f"Execution time: {avg_time * 1000:.35e} milliseconds\n")
        else: # Display the average execution time, uncertainty, number of empty cells, and total time 
            min_sig_figs = min(len(str(avg_time)), len(str(uncertainty)), len(str(total_time)))
            print(f"\nNumber of empty cells: {solver.empty_cells}")
            print(f"Number of trials: {num_trials}")
            print(f"Average execution time: {avg_time * 1000:.{min_sig_figs}e} milliseconds ± {uncertainty * 1000:.{min_sig_figs}e} milliseconds")
            print(f"Total time (including uncertainty): {total_time * 1000:.{min_sig_figs}e} milliseconds\n")

        choice = input("Do you want to retry (r) or quit (q)? ") # Ask user if they want to retry or quit
        if choice.lower() == "q":
            break

if __name__ == "__main__":
    main()