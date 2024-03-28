import os
import time
import statistics
import cProfile
import itertools

class SudokuSolver:
    def __init__(self, filename):
        self.grid = self.load_sudoku(filename) 
        self.original_grid = [row[:] for row in self.grid]
        self.empty_cells = sum(row.count(0) for row in self.grid)

    def load_sudoku(self, filename):
        grid = []
        with open(filename, "r") as file:
            for line in file:
                row = [int(cell) if cell != "_" else 0 for cell in line.strip()]
                grid.append(row) 
        return grid 

    def is_valid_grid(self):
        for row in range(9):
            for col in range(9):
                num = self.grid[row][col]
                self.grid[row][col] = 0
                if not self.is_valid_move(row, col, num):
                    self.grid[row][col] = num
                    return False
                self.grid[row][col] = num
        return True


    def is_valid_move(self, row, col, num):
        for i in range(9):  
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False 

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3): 
            for j in range(start_col, start_col + 3):
                if self.grid[i][j] == num:
                    return False

        return True

    def brute_force_solve(self):
        numbers = list(range(1, 10))  # Numbers to fill the grid
        for row in range(9):
            if 0 in self.grid[row]:  # If the row contains empty cells
                permutations = itertools.permutations(numbers)  # Generate all permutations of numbers
                for permutation in permutations:
                    # Try to fill the row with the permutation
                    for col in range(9):
                        if self.grid[row][col] == 0:
                            self.grid[row][col] = permutation[col]
                    # If the grid is valid, move to the next row
                    if self.is_valid_grid():
                        break
                    # If the grid is not valid, reset the row and try the next permutation
                    else:
                        self.grid[row] = self.original_grid[row]
        return self.grid

    def print_sudoku(self):
        for row in self.grid:
            print(" ".join(str(cell) if cell != 0 else "_" for cell in row))

    def calculate_execution_time(self, num_trials):
        if num_trials <= 1:
            start_time = time.perf_counter()
            self.brute_force_solve()
            end_time = time.perf_counter()
            return end_time - start_time, 0, end_time - start_time

        execution_times = []
        for _ in range(num_trials):
            start_time = time.perf_counter()
            self.brute_force_solve()
            end_time = time.perf_counter() 
            execution_times.append(end_time - start_time) 

        avg_execution_time = statistics.mean(execution_times)
        std_deviation = statistics.stdev(execution_times)
        uncertainty = std_deviation / (num_trials ** 0.5)
        total_time = avg_execution_time + uncertainty

        return avg_execution_time, uncertainty, total_time

def main():
    while True:
        sudoku_folder = "Sudoku-Board"
        filenames = [os.path.join(sudoku_folder, f"sudoku{i}.txt") for i in range(1, 6)]

        print("Chose a Sudoku to solve:")
        for i, filename in enumerate(filenames, start=1):
            print(f"{i}. {filename}")

        choice = int(input("Enter the Sudoku number: ")) - 1
        selected_filename = filenames[choice] 

        num_trials = int(input("Enter the number of trials: "))
        print(f"Solving Sudoku in {selected_filename}:")

        solver = SudokuSolver(selected_filename)
        avg_time, uncertainty, total_time = solver.calculate_execution_time(num_trials)
        solver.print_sudoku()

        if num_trials == 1:
            print(f"\nNumber of empty cells: {solver.empty_cells}")
            print(f"Execution time: {avg_time * 1000:.35e} milliseconds\n")
        else:
            min_sig_figs = min(len(str(avg_time)), len(str(uncertainty)), len(str(total_time)))
            print(f"\nNumber of empty cells: {solver.empty_cells}")
            print(f"Number of trials: {num_trials}")
            print(f"Average execution time: {avg_time * 1000:.{min_sig_figs}e} milliseconds ± {uncertainty * 1000:.{min_sig_figs}e} milliseconds")
            print(f"Total time (including uncertainty): {total_time * 1000:.{min_sig_figs}e} milliseconds\n")

        choice = input("Do you want to retry (r) or quit (q)? ")
        if choice.lower() == "q":
            break

if __name__ == "__main__":
    cProfile.run('main()')
