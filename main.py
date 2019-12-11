from tkinter import *
import graph as gr
import objects as obj
import time

root = Tk()
root.geometry('760x380')
root.title("Pac - Man.Version: MIPT")
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=10)
gr.canv = canv
obj.canv = canv

score = 0

def start():
	global level1_button, level2_button, level3_button, level4_button, level5_button, frame
	print("Выберите уровень игры")
	canv.delete("all")
	# Нижняя панель с кнопками
	frame = Frame(root)
	frame.pack(side=BOTTOM)
	#Кнопки, соответствующие уровням игры
	level5_button = Button(frame, text="5", command=level5, width=6)
	level5_button.pack(side=RIGHT)
	level4_button = Button(frame, text="4", command=level4, width=6)
	level4_button.pack(side=RIGHT)
	level3_button = Button(frame, text="3", command=level3, width=6)
	level3_button.pack(side=RIGHT)
	level2_button = Button(frame, text="2", command=level2, width=6)
	level2_button.pack(side=RIGHT)
	level1_button = Button(frame, text="1", command=level1, width=6)
	level1_button.pack(side=RIGHT)

def level1():
	global live, N_ghost
	live = 3
	# количество привидений
	N_ghost = 1
	#Удаление всех кнопок функкии start()
	level1_button.destroy()
	level2_button.destroy()
	level3_button.destroy()
	level4_button.destroy()
	level5_button.destroy()
	new_game()

def level2():
	global live, N_ghost
	live = 3
	# количество привидений
	N_ghost = 2
	# Удаление всех кнопок функкии start()
	level1_button.destroy()
	level2_button.destroy()
	level3_button.destroy()
	level4_button.destroy()
	level5_button.destroy()
	new_game()

def level3():
	global live, N_ghost
	live = 2
	# количество привидений
	N_ghost = 3
	# Удаление всех кнопок функкии start()
	level1_button.destroy()
	level2_button.destroy()
	level3_button.destroy()
	level4_button.destroy()
	level5_button.destroy()
	new_game()

def level4():
	global live, N_ghost
	live = 2
	# количество привидений
	N_ghost = 4
	# Удаление всех кнопок функкии start()
	level1_button.destroy()
	level2_button.destroy()
	level3_button.destroy()
	level4_button.destroy()
	level5_button.destroy()
	new_game()

def level5():
	global live, N_ghost
	live = 1
	# количество привидений
	N_ghost = 5
	# Удаление всех кнопок функкии start()
	level1_button.destroy()
	level2_button.destroy()
	level3_button.destroy()
	level4_button.destroy()
	level5_button.destroy()
	new_game()

def new_game():
	""""Функция новой игры"""
	global live, ghosts, pacman, label, live1_button, live2_button, live3_button, frame
	# Создание лабиринта
	gr.create_lab()
	# Вывод очков
	label = Label(bg='white', fg='black', width=20)
	label['text'] = score
	label.pack()
	print("Игра началась!")
	"""создание Pacman"""
	pacman = None
	pacman = obj.Pacman()
	live = 3
	# массив привидений
	ghosts = []
	"""создание привидений"""
	for i in range (N_ghost):
		new_ghost=obj.Ghost(7 - (i%6))
		ghosts += [new_ghost]
	#Управление кнопками с клавиатуры
	#Движение вверх
	root.bind("w", pacman.Button_up)
	root.bind("<Up>", pacman.Button_up)
	#Движение вниз
	root.bind("s", pacman.Button_down)
	root.bind("<Down>", pacman.Button_down)
	#Движение влево
	root.bind("a", pacman.Button_left)
	root.bind("<Left>", pacman.Button_left)
	#Движение вправо
	root.bind("d", pacman.Button_right)
	root.bind("<Right>", pacman.Button_right)

	game()

def game():
	global live, label
	for i in range(0,N_ghost, 1):
		ghosts[i].ghost_move(pacman)
		if ghosts[i].distance < 0.01:
			live -= 1
			screen = canv.create_text(380, 300, text = 'Game over!', font = '28')
			canv.update()
			time.sleep(3)
			start()
		#счет очков и вывод на экран
		score = pacman.record
		label['text'] = score
		if pacman.record == 50:
			screen = canv.create_text(380, 300, text = 'Victory!', font = '28')
			canv.update()
			time.sleep(3)
			start()
	root.after(300, game)

start()
mainloop()

if __name__ == "__main__":
	start()
