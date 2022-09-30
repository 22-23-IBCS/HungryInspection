import turtle
import random
import time

class Ve:

    def __init__(self, t):
        self.t = t
    
    def triangle(self, size = 50): #size is for if size does not have any value it wil automatically be 50
        self.t.fillcolor("blue") #filling the color for the image
        self.t.begin_fill()
        for i in range(3):
            self.t.right(120)
            self.t.forward(size)
        self.t.end_fill()
            
    def square(self, size = 100):
        self.t.fillcolor("red") #filling the color for the image
        self.t.begin_fill()
        for i in range(4):
            self.t.right(90)
            self.t.forward(size)
        self.t.end_fill()


    def polygon(self, size):
        side = int(random.randint(3,15))
        angle = 360/side
        self.t.fillcolor("green") #filling the color for the image
        self.t.begin_fill()
        for i in range(side):
            self.t.forward(size)
            self.t.left(angle)
        self.t.end_fill()


    def circle(self, size = 10):
        self.t.fillcolor("black") #filling the color for the image
        self.t.begin_fill()
        for i in range(35):
            self.t.forward(size)
            self.t.left(10)
        self.t.end_fill()
        self.t.hideturtle()

    def star(self, size):
        self.t.fillcolor("yellow")
        self.t.left(45)
        self.t.begin_fill()
        for i in range(5):
            self.t.forward(size)
            self.t.left(144)
        self.t.end_fill()
        
            
    def move(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def clear(self):
        self.t.clear()

    def randomshape(self, size = 100):
        for i in range(10):
            for colours in ["red", "magenta", "cyan", "blue", "black", "yellow", "green"]:
                self.t.color(colours)
                self.t.circle(100)
                self.t.right(10)
                
    def randomshape2(self, size = 100):
        for i in range(40):
            for colours in ["red", "magenta", "cyan", "blue", "black", "yellow", "green"]:
                self.t.color(colours)
                self.t.width(i/100+1)
                self.t.forward(i)
                self.t.left(10)
                

def main():

    canvas = turtle.Screen()
    canvas.bgcolor("white")
    canvas.title("Show Time")
    t = turtle.Turtle()
    t.shape("turtle")
    


    t.speed(0)
    art = Ve(t)
    art.move(0,0)


    art.square(400)
    time.sleep(2)
    art.clear()

    art.move(0, -200)
    art.polygon(100)
    time.sleep(2)
    art.clear()
    
    art.move(0, 0)
    art.triangle(100)
    time.sleep(2)
    art.clear()

    art.circle()
    time.sleep(2)
    art.clear()

    art.star(400)
    time.sleep(2)
    art.clear()

    art.randomshape()
    time.sleep(2)
    art.clear()

    art.randomshape2()
    time.sleep(2)
    art.clear()
    
        
   

if __name__ == "__main__":
    main()
