from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_bottom_wall = False
    c.has_right_wall = False
    c.draw(50, 50, 100, 100)

    d = Cell(win)
    d.has_top_wall = False
    d.draw(50, 100, 100, 150)

    e = Cell(win)
    e.has_left_wall = False
    e.draw(100, 50, 150, 100)

    d.draw_move(c, True)
    e.draw_move(c)

    win.wait_for_close()

main()