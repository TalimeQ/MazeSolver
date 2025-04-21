import unittest
import random

from maze import Maze
class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_rows,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_cols,
        )

    def test_maze_create_entry_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1.break_entrance_and_exit()

        self.assertEqual(
            m1.cells[0][0].has_top_wall,
            False
        )

        self.assertEqual(
            m1.cells[num_rows - 1][ num_cols -1].has_bottom_wall,
            False
        )

    def test_maze_reset(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1.break_entrance_and_exit()
        
        random_x = random.randrange(0,num_rows)
        random_y = random.randrange(0,num_cols)

        m1.cells[random_x][random_y].visited = True
        m1.reset_cells_visited()

        self.assertEqual(m1.cells[random_x][random_y].visited, False)

if __name__ == "__main__":
    unittest.main()
