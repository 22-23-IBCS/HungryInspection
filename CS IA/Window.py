from graphics import *
import Button as bt
from tkinter import messagebox as msg


# super class
class Window:
    def __init__(self):
        self.win = GraphWin("Soccer Training Generator", 1000, 700)
        background = Image(Point(500, 350), "background.png")
        background.draw(self.win)

    def create_button(self, color, text, center, size):
        button = bt.Button(self.win, color, text, center, size)
        return button

    def get_location(self):
        return self.win.getMouse()

    def check_mouse(self):
        return self.win.checkMouse()


# subclass
class main_window(Window):
    def __init__(self):
        super().__init__()

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
        self.storage = {'Drill: ': "",
                        'Intensity Rate: ': "",
                        'Average Rate: ': "",
                        'Type: ': " "
                        }

    @staticmethod
    def create_add_win():
        return add_window()

    def create_add_button(self):
        self.add = self.create_button("green", "Next", Point(500, 400), 50)
        self.back = self.create_button("red", "Back", Point(500, 600), 50)

    def input_box1(self):
        self.drill_name1 = Entry(Point(200, 500), 30)
        self.drill_name1.draw(self.win)
        self.text1 = Text(Point(190, 450), "What is your new drill: ")
        self.text1.setSize(18)
        self.text1.setTextColor("black")
        self.text1.draw(self.win)


    def input_box2(self):
        self.drill_name2 = Entry(Point(800, 500), 30)
        self.drill_name2.draw(self.win)
        self.text2 = Text(Point(790, 450), "Intensity (1-5): ")
        self.text2.setSize(18)
        self.text2.setTextColor("black")
        self.text2.draw(self.win)

    def input_box3(self):
        self.drill_name3 = Entry(Point(800, 200), 30)
        self.drill_name3.draw(self.win)
        self.text3 = Text(Point(790, 150), "Difficulty (1-5):  ")
        self.text3.setSize(18)
        self.text3.setTextColor("black")
        self.text3.draw(self.win)

    def input_box4(self):
        self.drill_name4 = Entry(Point(200, 200), 30)
        self.drill_name4.draw(self.win)
        self.text4 = Text(Point(190, 150), "Drill type: O, D or B ")
        self.text4.setSize(18)
        self.text4.setTextColor("black")
        self.text4.draw(self.win)

    def check_input(self):
        drill = self.drill_name1
        if drill.getText() == "":
            msg.showerror("Error", "Empty Box")
        else:
            msg.showinfo("Drills", "Drill is Added ")

    def save(self):
        drill = self.drill_name1.getText()
        with open('drills.txt', 'a') as f:
            f.write('\n' + drill + '\n')
        return drill

    def update_storage(self):
        l = (self.drill_name1.getText(), self.drill_name2.getText(), self.drill_name3.getText(), self.drill_name4.getText())
        i = 0
        for k, v in self.storage.items():
            value = l[i]
            self.storage[k] = value
            i+=1
        return self.storage

    def show_storage(self):
        return list(self.storage.items())


class delete_window(Window):  # Work on this class
    def delete_drill(self):
        pass


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
        self.back = self.create_button("white", "Back", Point(850, 100), 50)
        self.add = self.create_button("white", "add", Point(850, 300), 50)
        self.delete = self.create_button("white", "delete", Point(850, 400), 50)
        self.show = self.create_button("white", "storage", Point(850,500), 50)


class history_window(Window):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_history_win():
        return history_window()

    def create_history_button(self):
        self.back = self.create_button("red", "Back", Point(850, 650), 50)

    def show_drills(self):
        drill_file = open('drills.txt', 'r')
        self.text = Text(Point(500, 100), str(drill_file.read()))
        self.text.setSize(15)
        self.text.setTextColor("white")
        self.text.draw(self.win)
