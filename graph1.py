from tkinter import *
root = Tk()
root.geometry('800x400')
root.title("Pac - Man МФТИ")
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH, expand=10)
width_d = 2
canv.create_rectangle(10 - width_d , 10 - width_d, 770 - width_d, 290 - width_d, fill='white', outline='green',
                    width=width_d)
root.mainloop()

