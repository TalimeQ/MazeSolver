from cell import Cell
from window import Window
from geometry import *

def main():
    win = Window(800, 600)
    cell = Cell(100, 100 , 200, 200, win)
    cell.draw()

    win.wait_for_close()



main()