from tkinter import *

def create_lab():
	"""Создание экрана и лабиринта"""
	#Лабиринт
	canv.create_rectangle(0, 0, 760, 280, fill='black', outline='green',
                          width=0)
	#Буква M
	canv.create_rectangle(40, 40, 80, 240, fill='blue', outline='green',
                          width=0)
	canv.create_rectangle(120, 40, 160, 240, fill='blue', outline='green',
                          width=0)
	canv.create_rectangle(200, 40, 240, 240, fill='blue', outline='green',
                          width=0)
	canv.create_rectangle(40, 40, 240, 80, fill='blue', outline='green',
                          width=0)

	#Буква I
	canv.create_rectangle(280, 40, 320, 240, fill='red', outline='green',
                          width=0)

	#Буква P
	canv.create_rectangle(360, 40, 400, 240, fill='green', outline='green',
                          width=0)
	canv.create_rectangle(360, 40, 480, 160, fill='green', outline='green',
                          width=0)
	canv.create_rectangle(400, 80, 440, 120, fill='black', outline='black',
                          width=0)

	#Буква T
	canv.create_rectangle(520, 40, 720, 80, fill='yellow', outline='black',
                          width=0)
	canv.create_rectangle(600, 40, 640, 240, fill='yellow', outline='black',
                          width=0)
