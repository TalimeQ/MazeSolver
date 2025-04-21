from tkinter import Tk, BOTH, Canvas
from geometry import Line,Point

class Window():
    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.canvas.pack()
        
        self.__is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update() 

    def wait_for_close(self):
        self.__is_running = True
        while(self.__is_running == True):
            self.redraw()

    def close(self):
        self.__is_running = False

    def draw_line(self,line,fill_color):
        line.draw(self.canvas,fill_color)

