from random import randrange as rnd, choice
import time
"""Массив номеров закрашенных квадратиков на экране"""
Mat = [(2,2),(2,3),(2,4),(2,5),(2,6),(3,2),(4,2),(4,3),(4,4),(4,5),(4,6),(5,2),(6,2),(6,3),(6,4),(6,5),(6,6),
       (8,2),(8,3),(8,4),(8,5),(8,6),(10,2),(11,2),(12,2),(10,3),(12,3),(10,4),(11,2),(11,4),(12,4),(10,5),(10,6),
       (14,2),(15,2),(16,2),(17,2),(18,2),(16,3),(16,4),(16,5),(16,6)]
class Ball():
    def __init__(self, color):
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
        self.v_up = 1 
        self.v_down = 0
        self.v_left = 0
        self.v_right = 0
        self.move_up()
    def Button_down(self,event):
        '''движение вниз при нажатии кнопки ВНИЗ'''
        self.v_up = 0
        self.v_down = 1
        self.v_left = 0
        self.v_right = 0
        self.move_down()
    def Button_left(self,event):
        '''движение влево при нажатии кнопки ВЛЕВО'''
        self.v_up = 0
        self.v_down = 0
        self.v_left = 1
        self.v_right = 0
        self.move_left()
    def Button_right(self,event):
        '''движение вправо при нажатии кнопки ВПРАВО'''
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
        while check == False:
            time.sleep(0.1)
            self.y-=self.v_up
            self.set_coords()
            canv.update()
            check = self.walls("up")
            
    def move_down(self):
        check = self.walls('down')
        while check == False:
            time.sleep(0.1)
            self.y+=self.v_down
            self.set_coords()
            canv.update()
            check = self.walls("down")
        
    def move_left(self):
        check = self.walls('left')
        while check == False:
            time.sleep(0.1)
            self.x-=self.v_left
            self.set_coords()
            canv.update()
            check = self.walls("left")
        
    def move_right(self):
        check = self.walls('right')
        while check == False:
            time.sleep(0.1)
            self.x+=self.v_right
            self.set_coords()
            canv.update()
            check = self.walls("right")

class Pacman(Ball):
    """Создание дочернего класса Pacman"""
    def __init__(self):
        super().__init__(color='yellow')

class Ghost(Ball):
    """Создание дочернего класса Ghost"""
    def __init__(self):
        '''начальные значения при создании при создании приведений'''
        self.x = 19
        self.y = 7
        self.r = 20
        self.color = choice(['red','blue','purple'])
        self.id = canv.create_oval(
            -20 + 40 * self.x - self.r,
            -20 + 40 * self.y - self.r,
            -20 + 40 * self.x + self.r,
            -20 + 40 * self.y + self.r,
            fill=self.color
        )
        self.v_up = 0
        self.v_down = 0
        self.v_left = 0
        self.v_right = 0
