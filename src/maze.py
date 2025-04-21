from cell import Cell
import time

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
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win

        self.cells = []
        self.create_cells()

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
        if self.__win == None:
            return

        cell_x = self.x1 + j * self.cell_size_x
        cell_y = self.y1 + i * self.cell_size_y
        cell_x2 = cell_x + self.cell_size_x
        cell_y2 = cell_y + self.cell_size_y

        self.cells[i][j].draw(cell_x,cell_y,cell_x2,cell_y2)
        self.animate()

    def animate(self):
        if self._win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def break_entrance_and_exit(self):
        entrance_cell = self.cells[0][0]
        entrance_cell.has_top_wall = False
        self.draw_cell(0,0)

        exit_x = self.num_rows -1
        exit_y =  self.num_cols -1
        exit_cell = self.cells[exit_x][ exit_y]

        exit_cell.has_bottom_wall = False
        self.draw_cell(exit_x, exit_y)
