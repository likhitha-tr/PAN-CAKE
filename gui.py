import tkinter as tk
from PIL import Image, ImageTk

class AssistanceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry('600x600')

        self.bg = ImageTk.PhotoImage(Image.open("images/background.png"))
        bg = Label(self.root, image=self.bg)
        bg.place(x=0, y=0)

        self.centre = ImageTk.PhotoImage(Image.open("images/frame_image.jpg"))
        left = Label(self.root, image=self.centre)
        left.place(x=100, y=100, width=400, height=400)

        start = Button(self.root, text='START', font=("times new roman", 14), command=self.start_option)
        start.place(x=150, y=520)

        close = Button(self.root, text='CLOSE', font=("times new roman", 14), command=self.close_window)
        close.place(x=350, y=520)

    def start_option(self):
        # code for start option
        pass

    def close_window(self):
        self.root.destroy()