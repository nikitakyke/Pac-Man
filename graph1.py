from tkinter import *
def create_lab():
    root = Tk()
    root.geometry('760x400')
    root.title("Pac - Man.Version: MIPT")
    canv = Canvas(root,bg='white')
    canv.pack(fill=BOTH, expand=10)
    width_d = 2
    canv.create_rectangle(0 , 0, 760, 280, fill='black', outline='green',
                   width=0)
    canv.create_rectangle(40 , 40, 80, 240, fill='blue', outline='green',
                   width=0)
    canv.create_rectangle(120 , 40, 160, 240, fill='blue', outline='green',
                   width=0)
    canv.create_rectangle(200 , 40, 240, 240, fill='blue', outline='green',
                   width=0)
    canv.create_rectangle(40 , 40, 240, 80, fill='blue', outline='green',
                   width=0)
    
    canv.create_rectangle(280 , 40, 320, 240, fill='red', outline='green',
                   width=0)
    
    canv.create_rectangle(360 , 40, 400, 240, fill='green', outline='green',
                   width=0)
    canv.create_rectangle(360 , 40, 480, 160, fill='green', outline='green',
                   width=0)
    canv.create_rectangle(400 , 80, 440, 120, fill='black', outline='black',
                   width=0)
    
    canv.create_rectangle(520 , 40, 720, 80, fill='yellow', outline='black',
                   width=0)
    canv.create_rectangle(600, 40, 640, 240, fill='yellow', outline='black',
                   width=0)
    root.mainloop()
create_lab()

