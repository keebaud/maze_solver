import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._cells[0][0].has_bottom_wall,
            True
        )
        self.assertEqual(
            m1._cells[-1][-1].has_top_wall,
            True
        )
        self.assertEqual(
            m1._cells[-1][-1].has_bottom_wall,
            False
        )

    def test_clear_visited(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        m1._break_walls_r(num_rows // 2, num_cols // 2)
        visited_count = 0
        for i in range(num_cols):
            for j in range(num_rows):
                if m1._cells[i][j].visited:
                    visited_count += 1
        self.assertEqual(visited_count, num_rows * num_cols)
        m1._reset_cells_visited()
        visited_count = 0
        for i in range(num_cols):
            for j in range(num_rows):
                if m1._cells[i][j].visited:
                    visited_count += 1
        self.assertEqual(visited_count, 0)



if __name__ == "__main__":
    unittest.main()