from tkinter import *


class Window:
    def __init__(self):
        self.canvas = Tk()
        self.canvas.geometry('400x400+500+200')
        self.canvas.title('My window')
        self.canvas.resizable(False, False)
        self.label = Label(self.canvas, text='Label 1', bg='#42f5c2') # color picker

    def draw_widgets(self):
        self.label.pack(anchor=NW)
        Button(self.canvas, text='Go!', command=self.button_action).pack()

    def button_action(self):
        self.label.config(text='Goooo!')

    def run(self):
        self.draw_widgets()
        self.canvas.mainloop()


if __name__ == '__main__':
    window = Window()
    window.run()

