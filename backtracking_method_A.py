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
                row = [int(cell) if cell != "_" else 0 for cell in line.strip()] # Convert "_" to 0
                grid.append(row) 
        return grid 

    def is_valid_move(self, row, col, num): # Check if the number is valid to place in the cell 
        for i in range(9):  
            if self.grid[row][i] == num or self.grid[i][col] == num: # Check if the number is already present in the row or column  
                return False 

        start_row, start_col = 3 * (row // 3), 3 * (col // 3) # Check if the number is already present in the 3x3 grid  
        for i in range(start_row, start_row + 3): 
            for j in range(start_col, start_col + 3):
                if self.grid[i][j] == num:
                    return False

        return True

    def solve_sudoku(self): # Solve Sudoku using backtracking method 
        for row in range(9): # Find an empty cell to place a number
            for col in range(9): # Try placing numbers from 1 to 9 in the empty cell
                if self.grid[row][col] == 0: # If the number is valid, place it in the cell
                    for num in range(1, 10): # If the number is not valid, backtrack and try a different number
                        if self.is_valid_move(row, col, num): # If all numbers are tried and none are valid, backtrack to the previous cell
                            self.grid[row][col] = num # If the number is valid, place it in the cell
                            if self.solve_sudoku(): # Recursively solve the Sudoku grid
                                return True # If the Sudoku is solved, return True
                            self.grid[row][col] = 0 # If the Sudoku is not solved, backtrack and try a different number
                    return False # If all numbers are tried and none are valid, return False
        return True # If all cells are filled, return True

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

        print("Chose a Sudoku to solve:") # Display the list of Sudoku files to choose from
        for i, filename in enumerate(filenames, start=1):
            print(f"{i}. {filename}")

        choice = int(input("Enter the Sudoku number: ")) - 1  # Input the Sudoku number to solve
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