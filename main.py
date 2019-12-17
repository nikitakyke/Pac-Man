from tkinter import *
import graph as gr
import objects as obj
import time
from PIL import ImageTk, Image

root = Tk()
root.geometry('760x380')
root.title("Pac - Man.Version: MIPT")
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=10)
gr.canv = canv
obj.canv = canv

"""Нижняя панель с кнопками"""
frame = Frame(root)
frame.pack(side=BOTTOM)
label = Label(bg='white', fg='black', width=20)
score = 0
def start():
	global level1_button, level2_button, level3_button, level4_button, level5_button, frame, background_label
	print("Выберите уровень игры")
	canv.delete("all")
	image = PhotoImage(file ="pacman.gif")
	background_label = Label(root, image=image)
	"""relheight = 0,925 - коэффициент рястяжения изображения"""
	background_label.place(x=0, y=0, relwidth=1, relheight=0.925) 
	background_label.image = image
	
	"""создание кнопок меню"""
	level5_button = Button(frame, text="5", command=level5, width=6)
	level4_button = Button(frame, text="4", command=level4, width=6)
	level3_button = Button(frame, text="3", command=level3, width=6)
	level2_button = Button(frame, text="2", command=level2, width=6)
	level1_button = Button(frame, text="1", command=level1, width=6)

	level5_button.pack(side=RIGHT)
	level4_button.pack(side=RIGHT)
	level3_button.pack(side=RIGHT)
	level2_button.pack(side=RIGHT)
	level1_button.pack(side=RIGHT)
	
	mainloop()
	
"""Вызов при нажатии на кнопки в меню"""
def level1():
	level(3, 1)
def level2():
	level(3, 2)
def level3():
	level(2, 2)
def level4():
	level(2, 3)
def level5():
	level(1, 3)
def level(k_live, N):
	"""Функция, общая для всех level"""
	global live, N_ghost, restart_button
	"""Количество жизней"""
	live = k_live
	background_label.destroy()
	"""Количество привидений"""
	N_ghost = N
	"""Удаление всех кнопок функкии start()"""
	level1_button.destroy()
	level2_button.destroy()
	level3_button.destroy()
	level4_button.destroy()
	level5_button.destroy()

	new_game()
	
def new_game():
	""""Функция новой игры"""
	global live, ghosts, pacman, label, restart_button
	"""Создание лабиринта"""
	gr.create_lab()
	label.pack()
	print("Игра началась!")
	"""Cоздание Pacman"""
	pacman = None
	pacman = obj.Pacman()
	"""Массив привидений"""
	ghosts = []
	"""Создание привидений"""
	for i in range (N_ghost):
		"""y0 - ширина окна"""
		y0=7
		new_ghost=obj.Ghost(y0-i)
		ghosts += [new_ghost]
	"""Управление кнопками с клавиатуры"""
	"""Движение вверх"""
	root.bind("w", pacman.Button_up)
	root.bind("<Up>", pacman.Button_up)
	"""Движение вниз"""
	root.bind("s", pacman.Button_down)
	root.bind("<Down>", pacman.Button_down)
	"""Движение влево"""
	root.bind("a", pacman.Button_left)
	root.bind("<Left>", pacman.Button_left)
	"""Движение вправо"""
	root.bind("d", pacman.Button_right)
	root.bind("<Right>", pacman.Button_right)
	
	game()

def game():
	global live, label, restart_button
	for i in range(0,N_ghost, 1):
		"""Движение привидений и проверка на столкновение"""
		ghosts[i].ghost_move(pacman)
		canv.update()
		if ghosts[i].distance < 1:
			live -= 1
		if live<=0:
			screen = canv.create_text(380, 300, text = 'Game over!', font = '28')
			canv.update()
			time.sleep(3)
			start()
	"""Счёт очков и вывод на экран"""
	score = pacman.record
	label['text'] = score
	"""max_record - максимальное количество очков"""
	max_record = 910
	if pacman.record == max_record:
		screen = canv.create_text(380, 300, text = 'Victory!', font = '28')
		canv.update()
		time.sleep(3)
		start()
	root.after(300, game)

start()
mainloop()

if __name__ == "__main__":
	start()
