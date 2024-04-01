import pygame
import backtracking_method_A
import backtracking_method_B
import brut_force_method_A



# Class to visualize Sudoku using Pygame
class SudokuVisualizer:

    # Initialize the Pygame window
    def __init__(self, filename):
        self.sudoku_solver_BA = backtracking_method_A.SudokuSolverBA(filename)
        self.sudoku_solver_BB = backtracking_method_B.SudokuSolverBB(filename)
        self.sudoku_solver_FBA = brut_force_method_A.SudokuSolverFBA(filename)
        self.width, self.height = 540, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sudoku Visualizer")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 40)
        self.selected = None
        self.running = True

    # Draw the Sudoku grid
    def draw_grid(self):
        for i in range(10):
            if i % 3 == 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(self.screen, (0, 0, 0), (60 * i, 0), (60 * i, 540), thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (0, 60 * i), (540, 60 * i), thickness)

    # List of sudoku grid from Sudoku_Boeard directory to select from. Display it into a selection bar
    def draw_sudoku_list(self):
        for i in range(5):  # Limiter à 5 éléments
            pygame.draw.rect(self.screen, (255, 255, 255), (60 * i, 540, 60, 60))
            text = self.font.render(str(i + 1), True, (0, 0, 0)) 
            self.screen.blit(text, (60 * i + 20, 550))


    # Draw the Sudoku grid with numbers
    def draw_sudoku(self):
        for i in range(9):
            for j in range(9):
                num = self.sudoku_solver.grid[i][j]
                if num != 0:
                    text = self.font.render(str(num), True, (0, 0, 0))
                    self.screen.blit(text, (60 * j + 20, 60 * i + 10))

    # Draw button to resolve the Sudoku grid using backtracking method
    def draw_solve_button(self):
        pygame.draw.rect(self.screen, (0, 255, 0), (540, 0, 60, 60))
        text = self.font.render("Solve", True, (0, 0, 0))
        self.screen.blit(text, (550, 10))

    def solve_selected_sudoku(self):
        if self.selected_solver == "Backtracking Méthode A":
            self.sudoku_solver_BA.solve()
        elif self.selected_solver == "Backtracking Méthode B":
            self.sudoku_solver_BB.solve()
        elif self.selected_solver == "Brute Force Méthode A":
            self.sudoku_solver_FBA.solve()

    def get_selected_solver(self, choice):
        if choice == 0:
            self.selected_solver = "Backtracking Méthode A"
        elif choice == 1:
            self.selected_solver = "Backtracking Méthode B"
        elif choice == 2:
            self.selected_solver = "Brute Force Méthode A"

    # Main function to visualize Sudoku using Pygame
    def main(self):
        while self.running:
            self.screen.fill((255, 255, 255))
            self.draw_grid()
            self.draw_sudoku()
            self.font_size = 35
            self.font = pygame.font.Font(None, self.font_size)
            self.draw_sudoku_list()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 0 <= x < 540 and 0 <= y < 540:
                        row, col = y // 60, x // 60
                        self.selected = (row, col)
                        self.solve_selected_sudoku()
                    elif 0 <= x < 540 and 540 <= y < 600:
                        choice = x // 60
                        selected_filename = f"Sudoku-Board/sudoku{choice + 1}.txt"
                        self.sudoku_solver_BA = backtracking_method_A.SudokuSolverBA(selected_filename)
                        self.sudoku_solver_BB = backtracking_method_B.SudokuSolverBB(selected_filename)
                        self.sudoku_solver_FBA = brut_force_method_A.SudokuSolverFBA(selected_filename)
                        self.get_selected_solver(choice)
                        
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    pygame.init()
    visualizer = SudokuVisualizer("Sudoku-Board/sudoku1.txt")       
    visualizer.main()

 
  


