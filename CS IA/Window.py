from graphics import *
from Button import *


# super class
class Window:
    def __init__(self):
        self.win = GraphWin("Soccer Training Generator", 1000, 700)
        self.win.setBackground("gray")


    def create_button(self, color, text, center, size):
        button = Button(self.win, color, text, center, size)
        return button

    def get_location(self):
        return self.win.getMouse()



# subclass
class main_window(Window):
    def __init__(self):
        super().__init__()
        '''background = Image(Point(500, 350), "backgroundd.png")
        background.draw(self.win)'''

    @staticmethod
    def create_main_win():
        return main_window()

    def create_main_button(self):
        self.quit = self.create_button("red", "Quit", Point(900, 50), 50)
        self.defense = self.create_button("light gray", "Defence", Point(100, 650), 85)
        self.offense = self.create_button("light gray", "Offense", Point(900, 650), 85)
        self.balance = self.create_button("light gray", "Balance", Point(480, 650), 85)
        self.edit = self.create_button("light gray", "Drills/ Edit", Point(60, 50), 50)
        self.history = self.create_button("light gray", "History", Point(160, 50), 50)


class add_window(Window):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_add_win():
        return add_window()

    def create_add_button(self):
        self.add = self.create_button("green", "Add", Point(500, 400), 50)
        self.back = self.create_button("red", "Back", Point(500, 600), 50)


    def input_box(self):
        input_box = Entry(Point(500, 350), 30)
        input_box.draw(self.win)
        self.text = Text(Point(480, 300), "What is your new drill (Assign (O), (B) or (D) in the end: ")
        self.text.setSize(18)
        self.text.setTextColor("white")
        self.text.draw(self.win)
        self.txt = Text(Point(500, 500), '')
        self.txt.draw(self.win)
        while True:
            drill = input_box.getText()
            self.txt.setText(drill)

    def save(self, drill):
        with open('drills.txt', 'a') as f:
            f.write(drill + '\n')


class board_window(Window):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_board():
        return board_window()

    def create_board_button(self):
        self.next = self.create_button("light gray", "Next", Point(850, 300), 50)
        self.back = self.create_button("red", "Back", Point(850, 400), 50)


class edit_window(Window):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_edit_win():
        return edit_window()

    def create_edit_button(self):
        self.back = self.create_button("red", "Back", Point(850, 350), 50)
        self.add = self.create_button("yellow", "add", Point(850, 300), 50)
        self.delete = self.create_button("blue", "delete", Point(850, 400), 50)


class history_window(Window):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_history_win():
        return history_window()

    def create_history_button(self):
        self.history = self.create_button("light gray", "Past Drills", Point(500, 50), 50)
        self.back = self.create_button("red", "Back", Point(850, 650), 50)
