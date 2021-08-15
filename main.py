from tkinter import *


class Window:
    def __init__(self):
        self.canvas = Tk()
        self.canvas.geometry('400x400+500+200')
        self.canvas.title('My window')
        self.canvas.resizable(False, False)
        self.label = Label(self.canvas, text='Label 1', bg='#42f5c2') # color picker
        self.entry = Entry(self.canvas)

    def draw_widgets(self):
        frame = LabelFrame(self.canvas, text='LabelFrame')
        frame.pack(padx=10, pady=10, fill=X)

        self.entry.pack()
        Button(frame, text='Go!', command=self.button_action).pack(side=LEFT, padx=10, pady=10)
        self.label.pack(anchor=CENTER)

    def button_action(self):
        self.label.config(text=self.get_entry())

    def get_entry(self):
        return self.entry.get()

    def run(self):
        self.draw_widgets()
        self.canvas.mainloop()


if __name__ == '__main__':
    window = Window()
    window.run()

