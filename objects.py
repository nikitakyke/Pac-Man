from tkinter import *
from random import randrange as rnd, choice
import time
import graph as gr
"""Массив номеров закрышенных квадратиков на экране"""
Mat = [(2,2),(2,3),(2,4),(2,5),(2,6),(3,2),(4,2),(4,3),(4,4),(4,5),(4,6),(5,2),(6,2),(6,3),(6,4),(6,5),(6,6),
       (8,2),(8,3),(8,4),(8,5),(8,6),(10,2),(11,2),(12,2),(10,3),(12,3),(10,4),(11,2),(11,4),(12,4),(10,5),(10,6),
       (14,2),(15,2),(16,2),(17,2),(18,2),(16,3),(16,4),(16,5),(16,6)]
class Ball():
	def __init__(self, color ):
		'''начальные значения при создании шарика'''
		self.x = 1
		self.y = 1
		self.r = 20
		self.color = color 
		self.id = canv.create_oval(
				-20+40*self.x - self.r,
				-20+40*self.y - self.r,
				-20+40*self.x + self.r,
				-20+40*self.y + self.r,
				fill=self.color
		)
		self.record = 0
		self.v_up=0
		self.v_down=0
		self.v_left=0
		self.v_right=0
	def set_coords(self):
		"""Параметры рисования шарика"""
		canv.coords(
				self.id,
				-20+40*self.x - self.r,
				-20+40*self.y - self.r,
				-20+40*self.x + self.r,
				-20+40*self.y + self.r
				)
		
	def Button_up(self,event):
		'''движение вверх при нажатии кнопки ВВЕРХ'''
		if self.walls("up") == False:
			self.v_up = 1 
			self.v_down = 0
			self.v_left = 0
			self.v_right = 0
			self.move_up()
	def Button_down(self, event):
		'''движение вниз при нажатии кнопки ВНИЗ'''
		if self.walls("down") == False:
			self.v_up = 0
			self.v_down = 1
			self.v_left = 0
			self.v_right = 0
			self.move_down()
	def Button_left(self, event):
		'''движение влево при нажатии кнопки ВЛЕВО'''
		if self.walls("left") == False:
			self.v_up = 0
			self.v_down = 0
			self.v_left = 1
			self.v_right = 0
			self.move_left()
	def Button_right(self, event):
		'''движение вправо при нажатии кнопки ВПРАВО'''
		if self.walls("right") == False:
			self.v_up = 0
			self.v_down = 0
			self.v_left = 0
			self.v_right = 1
			self.move_right()
		
	def walls(self, indication):
		"""Функция проверки столкновения со стенками и кубиками, 
		вызывается отдельно для четырех движений"""
		check = False
		if indication =='up':
			if self.y<=1:
				check = True
			check = False
			for i in range(0, len(Mat), 1):
				if (self.x == Mat[i][0] and self.y == Mat[i][1] + 1) or self.y<=1:
					check = True
			return check
		if indication =='down':
			if self.y>=7:
				check = True
			for i in range(0, len(Mat), 1):
				if (self.x == Mat[i][0] and self.y == Mat[i][1] - 1) :
					check = True
			return check
		if indication =='left':
			if self.x<=1:
				check = True
			for i in range(0, len(Mat), 1):
				if (self.x == Mat[i][0] + 1 and self.y == Mat[i][1]):
					check = True
			return check     
		if indication =='right':
			if self.x>=19:
				check = True
			for i in range(0, len(Mat), 1):
				if (self.x == Mat[i][0] - 1 and self.y == Mat[i][1]):
					check = True
			return check
			
	"""Функции перемещения шарика"""   
	def move_up(self):
		check = self.walls('up')
		self.check_oval()
		while check == False:
			self.y-=self.v_up  
			self.check_oval()
			self.set_coords()
			canv.update()
			check = self.walls("up")
			time.sleep(0.13)
            
	def move_down(self):
		check = self.walls('down')
		self.check_oval()
		while check == False:
			self.y+=self.v_down
			self.check_oval()
			self.set_coords()
			canv.update()
			check = self.walls("down")
			time.sleep(0.13)
        
	def move_left(self):
		check = self.walls('left')
		self.check_oval()
		while check == False:
			self.x-=self.v_left
			self.check_oval()
			self.set_coords()
			canv.update()
			check = self.walls("left")
			time.sleep(0.13)
			
	def move_right(self):
		check = self.walls('right')
		self.check_oval()
		while check == False:
			self.x+=self.v_right
			self.check_oval()
			self.set_coords()
			canv.update()
			check = self.walls("right")
			time.sleep(0.13)
            
	def check_oval(self):
		"""Функция удаления еды"""
		for k in range (0, len(gr.B)):
			if self.x == gr.B[k][0] and self.y == gr.B[k][1]:
				self.record+=10
				gr.B[k][2].delete()
				gr.B[k] = (0, 0, gr.B[k][2])
				 
class Pacman(Ball):
	"""Создание дочернего класса Pacman"""
	def __init__(self):
		super().__init__(color='yellow')

class Ghost(Ball):
	"""Создание дочернего класса Ghost"""
	def __init__(self, y):
		'''начальные значения при создании при создании приведений'''
		self.x = 19
		self.y = y
		self.r = 20
		self.color = choice(['red','blue','purple'])
		self.id = canv.create_oval(
			-20 + 40 * self.x - self.r,
			-20 + 40 * self.y - self.r,
			-20 + 40 * self.x + self.r,
			-20 + 40 * self.y + self.r,
			fill=self.color
		)
	def ghost_move(self, pacman):
		self.r_start = ((pacman.x-self.x)**2 + 
										(pacman.y-self.y)**2)**(0.5)
		delta_r = [0, 0, 0, 0]
		if self.walls('up')==True:
			 delta_r[0] = -100
		else:
			delta_r[0] = -((pacman.x-self.x)**2 + 
							(pacman.y-self.y+1)**2)**(0.5)+ self.r_start
		if self.walls('down')==True:
			delta_r[1] = -100
		else:
			delta_r[1] = -((pacman.x-self.x)**2 +
							(pacman.y-self.y-1)**2)**(0.5)+ self.r_start
		if self.walls('right')==True:
			delta_r[2] = -100
		else:
			delta_r[2] =-((pacman.x-self.x-1)**2 +
							(pacman.y-self.y)**2)**(0.5)+ self.r_start
		if self.walls('left')==True:
			delta_r[3] = -100
		else:
			delta_r[3] =-((pacman.x-self.x+1)**2 +
							(pacman.y-self.y)**2)**(0.5)+ self.r_start
		
		if (delta_r[0]>=delta_r[1] and 
					delta_r[0]>=delta_r[2] and delta_r[0]>=delta_r[3]):
			self.y-=1
			self.set_coords()
		elif (delta_r[1]>=delta_r[0] and 
					delta_r[1]>=delta_r[2] and delta_r[1]>=delta_r[3]):
			self.y+=1
			self.set_coords()
		elif (delta_r[2]>=delta_r[0] and 
					delta_r[2]>=delta_r[1] and delta_r[2]>=delta_r[3]):
			self.x+=1
			self.set_coords()
		elif (delta_r[3]>=delta_r[0] and 
					delta_r[3]>=delta_r[1] and delta_r[3]>=delta_r[2]):
			self.x-=1
			self.set_coords()
		self.distance = ((self.x - pacman.x)**2+
							(self.y - pacman.y)**2)**(0.5)
		canv.update()
