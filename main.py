from tkinter import *
#import datetime
import graph as gr
import objects as obj
import time
def main():
	# Главная функция игры
	root = Tk()
	root.geometry('760x380')
	root.title("Pac - Man.Version: MIPT")
	canv = Canvas(root, bg='white')
	canv.pack(fill=BOTH, expand=10)
	
	print("Игра началась!")
	"""time_0 = datetime.datetime.now()"""
	
	# Создание лабиринта
	gr.canv = canv
	gr.create_lab()
	"""создание шарика"""
	obj.canv = canv
	#new_ball=b.Ball()
	"""создание пакмана"""
	pacman = obj.Pacman()
	"""создание привидений"""
	ghosts = []
	for i in range (1):
		new_ghost=obj.Ghost()
		ghosts += [new_ghost]
	# Нижняя панель с текущим временем игры и кнопками
	frame = Frame(root)
	frame.pack(side=BOTTOM)

	"""# Вывод времени на экран
	time = datetime.datetime.now()
	delta_time = time - time_0
	displayed_time = StringVar()
	displayed_time.set("Время игры: " + str(delta_time))
	time_label = Label(frame, textvariable=displayed_time, width=30)
	time_label.pack(side=LEFT)
"""
	# Кнопка "Up"
	"""up_button = Button(frame, text=" Up ", height=2,
							command=new_ball.Button_up)
	up_button.pack(side=TOP)
	# Кнопка "Down"
	down_button = Button(frame, text="Down", height=2, 
						command=new_ball.Button_down)
	down_button.pack(side=BOTTOM)
	#Кнопка "Left"
	left_button = Button(frame, text="Left", width=6,
							command=new_ball.Button_left)
	left_button.pack(side=LEFT)
	# Кнопка "Right"
	right_button = Button(frame, text="Right", width=6, 
						command=new_ball.Button_right)
	right_button.pack(side=RIGHT)"""
	
	# Управление кнопками с клавиатуры
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
	
	#Вывод очков
	score = 0
	label = Label(bg='white', fg='black', width=20)
	label['text'] = score
	label.pack()
	#obj.Ghost.angle_x(pacman)
	mainloop()


if __name__ == "__main__":
    main()
