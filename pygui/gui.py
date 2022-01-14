import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        super().geometry('720x480')
        super().title('Main Window')
        

if __name__=="__main__":
    root=MainWindow()
    root.mainloop()





