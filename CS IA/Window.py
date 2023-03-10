from graphics import *
import Button as bt
from tkinter import messagebox as msg, Label
import json


# super class
class Window:
    def __init__(self):
        self.win = GraphWin("Soccer Training Generator", 1000, 700)
        background = Image(Point(500, 350), "background2.png")
        background.draw(self.win)
        
    def create_button(self, color, text, center, size):
        button = bt.Button(self.win, color, text, center, size)
        return button

    def get_location(self):
        return self.win.getMouse()


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
        self.edit = self.create_button("light gray", "Edit", Point(60, 50), 50)
        self.drills = self.create_button("light gray", "Drills", Point(160, 50), 50)
        self.history = self.create_button("light gray", "History", Point(260, 50), 50)


class add_window(Window):
    def __init__(self):
        super().__init__()
        self.storage = {'Drill: ': "",
                        'Intensity: ': "",
                        'Difficulty: ': "",
                        'Type: ': " "
                        }

    @staticmethod
    def create_add_win():
        return add_window()

    def create_add_button(self):
        self.add = self.create_button("green", "Add", Point(500, 400), 50)
        self.back = self.create_button("red", "Back", Point(500, 600), 50)

    def input_box1(self):
        self.drill_name1 = Entry(Point(200, 500), 50)
        self.drill_name1.draw(self.win)
        self.text1 = Text(Point(190, 450), "What is your new drill: ")
        self.text1.setSize(18)
        self.text1.setTextColor("black")
        self.text1.draw(self.win)

    def input_box2(self):
        self.drill_name2 = Entry(Point(800, 500), 50)
        self.drill_name2.draw(self.win)
        self.text2 = Text(Point(790, 450), "Intensity (1-5): ")
        self.text2.setSize(18)
        self.text2.setTextColor("black")
        self.text2.draw(self.win)

    def input_box3(self):
        self.drill_name3 = Entry(Point(800, 200), 50)
        self.drill_name3.draw(self.win)
        self.text3 = Text(Point(790, 150), "Difficulty (1-5):  ")
        self.text3.setSize(18)
        self.text3.setTextColor("black")
        self.text3.draw(self.win)

    def input_box4(self):
        self.drill_name4 = Entry(Point(200, 200), 50)
        self.drill_name4.draw(self.win)
        self.text4 = Text(Point(190, 150), "Drill type: O, D or B ")
        self.text4.setSize(18)
        self.text4.setTextColor("black")
        self.text4.draw(self.win)

    def check_input(self):
        if self.drill_name1.getText() == "" and self.drill_name2.getText() == "" and self.drill_name3.getText() == "" and self.drill_name4.getText() == "":
            msg.showerror("Error", "Empty Box")
        else:
            msg.showinfo("Drills", "Drill is Added ")

    def save(self):
        l = (
            self.drill_name1.getText(), self.drill_name2.getText(), self.drill_name3.getText(),
            self.drill_name4.getText())
        i = 0
        for k, v in self.storage.items():
            value = l[i]
            self.storage[k] = value
            i += 1

        name = self.storage['Drill: ']
        pack = {name: self.storage}

        with open('drills.txt', 'a') as f:
            json.dump(pack, f)
            f.write('\n')


class delete_window(Window):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_delete_win():
        return delete_window()

    def create_delete_button(self):
        self.delete = self.create_button("green", "Delete", Point(750, 400), 50)

    def delete_box(self):
        self.entry_box = Entry(Point(750, 350), 50)
        self.entry_box.draw(self.win)
        self.box = Text(Point(750, 300), "What drill you want to delete (1 drill each) ")
        self.box.setSize(18)
        self.box.setTextColor("black")
        self.box.draw(self.win)

    def check_input2(self):
        if self.entry_box.getText() == "":
            msg.showerror("Error", "No drill is assigned to delete")
        else:
            msg.showinfo("Drills", "Drill is Delete ")

    import json

    def delete_drill(self):
        # Get the name of the drill to delete from the entry box
        delete_drill = self.entry_box.getText()
        # Load the data from the JSON file
        with open('drills.txt', 'r') as f:
            data = [json.loads(line) for line in f]
        # Find the drill to delete and remove it from the data
        for drill in data:
            if delete_drill in drill:
                data.remove(drill)
        # Write the updated data back to the JSON file
        with open('drills.txt', 'w') as f:
            for drill in data:
                f.write(json.dumps(drill) + '\n')

    def upload(self):
        with open('drills.txt', 'r') as f:
            ts = []
            for line in f:
                t = json.loads(line)
                ts.append(t)
        drills_text = "All Drills:\n\n"
        i = 1
        for t in ts:
            key = list(t.keys())[0]  # get the first key in the dictionary
            drill_type = t[key]["Type: "]  # get the value of "Type:"
            drills_text += f"{i}. {key} - {drill_type}\n"
            i += 1
        text = Text(Point(200, 100), drills_text)
        text.setSize(20)
        text.setTextColor("Black")
        text.draw(self.win)


class all_drills_window(Window):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_all_drills_win():
        return all_drills_window()

    def create_all_drills_button(self):
        self.back = self.create_button("red", "Back", Point(850, 600), 30)

    def show_drills(self):
        with open('drills.txt', 'r') as f:
            drills = []
            for line in f:
                drill = json.loads(line)
                drills.append(drill)

        drills_text = "All Drills:\n\n"
        i = 1
        for drill in drills:
            key = list(drill.keys())[0]  # get the first key in the dictionary
            drill_type = drill[key]["Type: "]  # get the value of "Type:"
            drills_text += f"{i}. {key} - {drill_type}\n"
            i += 1

        text = Text(Point(500, 100), drills_text)
        text.setSize(20)
        text.setTextColor("Black")
        text.draw(self.win)


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
        self.show = self.create_button("white", "storage", Point(850, 500), 50)


class history_window(Window):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_history_win():
        return history_window()

    def create_history_button(self):
        self.back = self.create_button("red", "Back", Point(850, 650), 50)
