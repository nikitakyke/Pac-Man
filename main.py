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
#количество привидений
N_ghost = 1

#Вывод очков
label = Label(bg='white', fg='black', width=20)
score = 0
label['text'] = score
label.pack()
live = 0

def start():
	print("Выберите количество привидений и жизней Pacman")
	canv.delete("all")
	frame = Frame(root)
	frame.pack(side=BOTTOM)
	start_button = Button(frame, text="Start", command=new_game, width=6)
	start_button.pack(side=RIGHT)

def new_game():
	global live, ghosts, pacman
	# Главная функция игры
	# Создание лабиринта
	gr.create_lab()

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
	# Нижняя панель с текущим временем игры и кнопками
	frame = Frame(root)
	frame.pack(side=BOTTOM)
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

# Вывод времени на экран
def game():
	global live
	for i in range(0,N_ghost, 1):
		ghosts[i].ghost_move(pacman)
		if ghosts[i].distance < 0.01:
			live -= 1
			screen = canv.create_text(380, 300, text = 'Game over!', font = '28')
			canv.update()
			time.sleep(3)
			new_game()
			game()
		#счет очков и вывод на экран
		score = pacman.record
		label['text'] = score
		if pacman.record == 50:
			screen = canv.create_text(380, 300, text = 'Victory!', font = '28')
			canv.update()
			time.sleep(3)
			new_game()
			game()
	root.after(300, game)
start()
#game()

mainloop()

if __name__ == "__main__":
	start()
