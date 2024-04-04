import time
import sys

# Increase the recursion limit
sys.setrecursionlimit(3500)

# Print the current recursion limit to verify the change
print(sys.getrecursionlimit())

class Sudoku:
    def __init__(self, grid):
        self.grid = grid
        self.empty_cells = [(i, j) for i in range(9) for j in range(9) if self.grid[i][j] == 0]

    def is_valid(self, num, pos):
        for i in range(9):
            if self.grid[pos[0]][i] == num and pos[1] != i:
                return False
        for i in range(9):
            if self.grid[i][pos[1]] == num and pos[0] != i:
                return False
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if self.grid[i][j] == num and (i,j) != pos:
                    return False
        return True

    def solve(self):
        if not self.empty_cells:
            return True
        else:
            row, col = self.empty_cells[0]

        for num in range(1, 10):
            if self.is_valid(num, (row, col)):
                self.grid[row][col] = num

                if self.solve():
                    return True

                self.grid[row][col] = 0

        return False

    def print_grid(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    print("_", end=" ")
                else:
                    print(self.grid[i][j], end=" ")
            print()

def load_sudoku_grid(filename):
    with open(filename, 'r') as file:
        grid = []
        for line in file:
            row = list(map(int, line.strip().split()))
            grid.append(row)
    return grid

def select_grid():
    print("Select a Sudoku grid to solve:")
    grid_filenames = [
        'sudoku_grid1.txt',
        'sudoku_grid2.txt',
        'sudoku_grid3.txt',
        'sudoku_grid4.txt',
        'sudoku_grid5.txt'
    ]
    for i, filename in enumerate(grid_filenames, start=1):
        print(f"{i}. {filename}")
    while True:
        try:
            choice = int(input("Enter the number of the grid you want to solve: "))
            if 1 <= choice <= len(grid_filenames):
                return grid_filenames[choice - 1]
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def validate_grid(grid):
    if len(grid) != 9:
        return False
    for row in grid:
        if len(row) != 9:
            return False
    return True

def main():
    # Select a grid to solve
    selected_grid_filename = select_grid()
    
    # Load the selected Sudoku grid
    grid = load_sudoku_grid(selected_grid_filename)

    # Validate the grid format
    if not validate_grid(grid):
        print("The selected Sudoku grid is not correctly formatted.")
        return
    
    # Create a Sudoku instance and solve it
    sudoku = Sudoku(grid)
    start_time = time.time()
    if sudoku.solve():
        print("Sudoku solved!")
        sudoku.print_grid()
    else:
        print("No solution exists.")
    end_time = time.time()

    # Print the time taken to solve the Sudoku
    print(f"Solved in {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
