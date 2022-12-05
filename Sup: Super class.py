from graphics import *

class Button(Rectangle):

    def __init__(self, win, p1, p2, color, text):
        super().__init__(p1, p2)
        super().draw(win)
        super().setFill(color)

        self.minX = p1.getX()
        self.maxX = p2.getX()
        self.minY = p1.getY()
        self.maxY = p2.getY()

        self.text = Text(Point((self.minX + self.maxX)/2, (self.minY + self.maxY)/2), text)
        self.text.draw(win)

    def isClicked(self, p):
        x = p.getX()
        y = p.getY()
        if x > self.minX:
            if x < self.maxX:
                if y > self.minY:
                    if y < self.maxY:
                        return True
        return False


def main():
    
    win = GraphWin("Button Example", 500, 500)
    Circle = Button(win, Point(300, 100), Point(400, 175), "Cyan", "Circle")
    Quit = Button(win, Point(300, 100), Point(200, 275), "Red", "Quit")

    
    while True:
        m = win.getMouse()


        if Circle.isClicked(m):
            for i in range(20):
                C = Circle(Point(250, 250), 50 + i*20)
                C.draw(win)

        if Quit.isCliked(m):
            break
    
if __name__ == "__main__":
    main()
