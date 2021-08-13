from tkinter import *


class Window:
    def __init__(self):
        self.canvas = Tk()
        self.canvas.geometry('400x400+500+200')
        self.canvas.title('My window')
        self.canvas.resizable(False, False)

    def run(self):
        self.canvas.mainloop()


if __name__ == '__main__':
    window = Window()
    window.run()

