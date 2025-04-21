from geometry import *
from window import Window

class Cell():
    def __init__(self, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.__win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        

        line_to_draw  = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            self.__win.draw_line(line_to_draw, "black")
        else:
            self.__win.draw_line(line_to_draw, "white")

        line_to_draw  = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self.__win.draw_line(line_to_draw, "black")
        else:
            self.__win.draw_line(line_to_draw, "white")

        line_to_draw  = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self.__win.draw_line(line_to_draw, "black")
        else:
            self.__win.draw_line(line_to_draw, "white")

        line_to_draw  = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self.__win.draw_line(line_to_draw, "black")
        else:
            self.__win.draw_line(line_to_draw, "white")
    
    def get_center(self):
        center_x = (self.__x1 + self.__x2) //2
        center_y = (self.__y1 + self.__y2) //2

        return Point(center_x,center_y)

    def draw_move(self, to_cell, undo=False):
        c1 = self.get_center()
        c2 = to_cell.get_center()

        color = "red"
        if undo:
            color = "gray"

        line_to_draw = Line(c1,c2)
        self.__win.draw_line(line_to_draw, color)
        
