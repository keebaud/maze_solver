from graphics import Window
from maze import Maze
import random

def main():
    num_rows = 32
    num_cols = 40
    margin = 20
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    maze._break_entrance_and_exit()

    maze._break_walls_r(random.randint(0, num_rows - 1), random.randint(0, num_cols - 1))

    maze._reset_cells_visited()

    maze.solve()

    win.wait_for_close()

main()