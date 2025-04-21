from cell import Cell
import time
import random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None,
    ):
        self.seed = seed
        if self.seed != None:
            random.seed(self.seed)

        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win

        self.cells = []
        self.create_cells()
        self.break_entrance_and_exit()
        self.break_walls_r(0,0)

    def create_cells(self):
        for i in range(0, self.num_rows):
            cells_row = []
            for j in  range(0, self.num_cols):
                cells_row.append(Cell(self.__win))
            self.cells.append(cells_row)

        for i in range(0, self.num_rows):
            for j in  range(0, self.num_cols):
                self.draw_cell(i,j)
        
        

    def draw_cell(self,i,j):
        if self.__win is None:
            return

        cell_x = self.x1 + j * self.cell_size_x
        cell_y = self.y1 + i * self.cell_size_y
        cell_x2 = cell_x + self.cell_size_x
        cell_y2 = cell_y + self.cell_size_y

        self.cells[i][j].draw(cell_x,cell_y,cell_x2,cell_y2)
        self.animate()

    def animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.01)

    def break_entrance_and_exit(self):
        entrance_cell = self.cells[0][0]
        entrance_cell.has_top_wall = False
        self.draw_cell(0,0)

        exit_x = self.num_rows -1
        exit_y =  self.num_cols -1
        exit_cell = self.cells[exit_x][ exit_y]

        exit_cell.has_bottom_wall = False
        self.draw_cell(exit_x, exit_y)

    def break_walls_r(self,i,j):
        self.cells[i][j].visited = True
        while True:
            values_to_visit = []
            if i + 1 in range(0, self.num_rows) and self.cells[i + 1][j].visited == False:
                values_to_visit.append((i + 1, j))
            if i - 1 in range(0, self.num_rows) and self.cells[i - 1][j].visited == False:
                values_to_visit.append((i -1 , j))
            if j + 1 in range(0, self.num_cols) and self.cells[i][j + 1].visited == False:
                values_to_visit.append((i, j + 1))
            if j - 1 in range(0, self.num_cols) and self.cells[i][j - 1].visited == False:
                values_to_visit.append((i, j  - 1))

            if len(values_to_visit) == 0:
                return


            choice = random.choice(values_to_visit)
            if choice[0] == i:
                if choice[1] > j:
                    # right
                    self.cells[i][j].has_right_wall = False
                    self.cells[choice[0]][choice[1]].has_left_wall = False
                    pass
                else:
                    #left
                    self.cells[i][j].has_left_wall = False
                    self.cells[choice[0]][choice[1]].has_right_wall = False
                    pass
            else:
                if choice[0] > i:
                    # bottom
                    self.cells[i][j].has_bottom_wall = False
                    self.cells[choice[0]][choice[1]].has_top_wall = False
                    pass
                else:
                    # top
                    self.cells[i][j].has_top_wall = False
                    self.cells[choice[0]][choice[1]].has_bottom_wall = False
                    pass

            self.draw_cell(i,j)
            self.break_walls_r(choice[0],choice[1])

