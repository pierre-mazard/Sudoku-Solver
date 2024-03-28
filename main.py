import pygame
import backtracking_method_A


# Class to visualize Sudoku using Pygame
class SudokuVisualizer:

    # Initialize the Pygame window
    def __init__(self, filename):
        self.sudoku_solver = backtracking_method_A.SudokuSolver(filename)
        self.width, self.height = 1200, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sudoku Visualizer")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 40)
        self.selected = None
        self.running = True
        self.result_text = ""

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
        for i in range(5):  # 5 sudoku boards
            pygame.draw.rect(self.screen, (255, 255, 255), (60 * i, 540, 60, 60))
            text = self.font.render(str(i + 1), True, (0, 0, 0)) 
            self.screen.blit(text, (60 * i + 20, 550))

    # Draw the Sudoku grid with numbers
    def draw_sudoku(self):
        for i in range(9):
            for j in range(9):
                num = self.sudoku_solver.grid[i][j]
                if num != 0:
                    color = (0, 255, 0) if self.sudoku_solver.original_grid[i][j] == 0 else (0, 0, 0)
                    text = self.font.render(str(num), True, color)
                    self.screen.blit(text, (60 * j + 20, 60 * i + 10))
        
    # Draw button to solve the sudoku
    def draw_solve_button(self):
        smaller_font = pygame.font.Font(None, 30)
        pygame.draw.rect(self.screen, (255, 255, 255), (60 * 5, 540, 50, 50)) 
        text = smaller_font.render("Recursive Backtracking", True, (0, 0, 0))
        self.screen.blit(text, (60 * 5 + 5, 540 + 10))

    # Draw text on the screen
    def draw_text(self, text, position, font=None):
        if font is None:
            font = self.font
        text_surface = font.render(text, True, (0, 0, 0))
        self.screen.blit(text_surface, position)        

    #Draw the number of trials 
    def draw_trials(self):
        larger_font = pygame.font.Font(None, 35)
        self.draw_text("Number of trials", (60 * 11, 520), larger_font)  # New line to draw the text
        pygame.draw.rect(self.screen, (255, 255, 255), (60 * 12, 540, 60, 60))
        text = self.font.render(str(self.trials), True, (0, 0, 0)) 
        self.screen.blit(text, (60 * 12 + 20, 550))
        pygame.draw.rect(self.screen, (255, 255, 255), (60 * 13, 540, 30, 60))  # Box for "+" button
        text = self.font.render("+", True, (0, 0, 0)) 
        self.screen.blit(text, (60 * 13 + 10, 550))
        pygame.draw.rect(self.screen, (255, 255, 255), (60 * 11 + 30, 540, 30, 60))  # Box for "-" button
        text = self.font.render("-", True, (0, 0, 0)) 
        self.screen.blit(text, (60 * 11 + 40, 550))

    # Main function to visualize Sudoku using Pygame
    def main(self):
        self.trials = 1
        smaller_font = pygame.font.Font(None, 22)
        while self.running:
            self.screen.fill((255, 255, 255))
            self.draw_grid()
            self.draw_sudoku_list()
            self.draw_sudoku()
            self.draw_solve_button()
            self.draw_text(self.result_text, (550, 100), smaller_font)
            self.draw_trials()
            pygame.display.flip()
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if y < 540:
                        self.selected = (y // 60, x // 60)
                    elif 0 <= x < 300 and 540 <= y < 600:
                        self.sudoku_solver = backtracking_method_A.SudokuSolver(f"Sudoku-Board/sudoku{int(x / 60) + 1}.txt")
                        self.result_text = ""
                    elif 300 <= x < 400 and 540 <= y < 600:
                        self.sudoku_solver.solve_sudoku()
                        self.draw_sudoku()
                        avg_time, uncertainty, total_time = self.sudoku_solver.calculate_execution_time(self.trials)
                        empty_cells = self.sudoku_solver.empty_cells
                        self.result_text = f"Number of empty cells: {empty_cells}\n\nNumber of trials: {self.trials}\n\nAverage execution time: {avg_time* 1000:.35e} milliseconds\n\nUncertainty: {uncertainty* 1000:.35e} milliseconds\n\nTotal time: {total_time* 1000:.35e} milliseconds\n"  # Store the result text
                        pygame.display.flip()
                    elif 60 * 13 <= x < 60 * 14 and 540 <= y < 600:
                        self.trials += 1
                    elif 60 * 11 + 30 <= x < 60 * 12 and 540 <= y < 600 and self.trials > 1:
                        self.trials -= 1

if __name__ == "__main__":
    pygame.init()
    visualizer = SudokuVisualizer("Sudoku-Board/sudoku1.txt")
    visualizer.main()






 
  


