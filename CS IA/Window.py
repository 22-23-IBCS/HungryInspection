from graphics import *
import Button as bt
from tkinter import messagebox as msg
import json
import itertools

# super class
class Window:
    def __init__(self):
        self.win = GraphWin("Soccer Training Generator", 1300, 700)
        background = Image(Point(500, 350), "background.png")
        background.draw(self.win)

    def create_button(self, color, text, center, size):
        button = bt.Button(self.win, color, text, center, size)
        return button

    def get_location(self):
        return self.win.getMouse()


class main_window(Window):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_main_win():
        return main_window()

    def create_main_button(self):
        self.quit = self.create_button("red", "Quit", Point(1200, 50), 50)
        self.plan = self.create_button("light gray", "Generate Plan", Point(650, 650), 85)
        self.edit = self.create_button("light gray", "Edit", Point(60, 50), 50)
        self.drills = self.create_button("light gray", "All Drills", Point(160, 50), 50)
        self.note = Text(Point(650, 100),
                         "Small note: double click any where if return from another window to main window")
        self.note.setSize(18)
        self.note.setTextColor("white")
        self.note.draw(self.win)

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
        self.add = self.create_button("green", "Add", Point(1200, 400), 50)
        self.back = self.create_button("red", "Back", Point(1200, 600), 50)

    def input_box1(self):
        self.drill_name1 = Entry(Point(200, 600), 50)
        self.drill_name1.draw(self.win)
        self.text1 = Text(Point(190, 550), "What is your new drill: ")
        self.text1.setSize(18)
        self.text1.setTextColor("white")
        self.text1.draw(self.win)

    def input_box2(self):
        self.drill_name2 = Entry(Point(900, 600), 50)
        self.drill_name2.draw(self.win)
        self.text2 = Text(Point(890, 550), "Intensity (1-5): ")
        self.text2.setSize(18)
        self.text2.setTextColor("white")
        self.text2.draw(self.win)

    def input_box3(self):
        self.drill_name3 = Entry(Point(900, 200), 50)
        self.drill_name3.draw(self.win)
        self.text3 = Text(Point(890, 150), "Difficulty (1-5):  ")
        self.text3.setSize(18)
        self.text3.setTextColor("white")
        self.text3.draw(self.win)

    def input_box4(self):
        self.drill_name4 = Entry(Point(200, 200), 50)
        self.drill_name4.draw(self.win)
        self.text4 = Text(Point(190, 150), "Drill type: O, D or B ")
        self.text4.setSize(18)
        self.text4.setTextColor("white")
        self.text4.draw(self.win)

    def check_input(self):
        if self.drill_name1.getText() == "" and self.drill_name2.getText() == "" and self.drill_name3.getText() == "" and self.drill_name4.getText() == "":
            msg.showerror("Error", "Empty Box")
        else:
            msg.showinfo("Drills", "Drill is Added ")

    def save(self):
        d = (
            self.drill_name1.getText(), self.drill_name2.getText(),
            self.drill_name3.getText(), self.drill_name4.getText())
        i = 0
        for k, v in self.storage.items():
            value = d[i]
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
        self.delete = self.create_button("green", "Delete", Point(1000, 400), 50)
        self.back = self.create_button("red", "Back", Point(1000, 600), 50)
        self.note = Text(Point(650, 50),
                         "Small note: Please type in the exact drill format as seen in the screen (a space could also mess you up)\n "
                         "No need to type in the drill type")
        self.note.setSize(18)
        self.note.setTextColor("white")
        self.note.draw(self.win)


    def delete_box(self):
        self.entry_box = Entry(Point(1000, 200), 50)
        self.entry_box.draw(self.win)
        self.box = Text(Point(990, 150), "What drill you want to delete (1 drill each) ")
        self.box.setSize(18)
        self.box.setTextColor("white")
        self.box.draw(self.win)

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
    def check_input2(self):
        with open('drills.txt', 'r') as f:
            data = [json.loads(line) for line in f]
        if self.entry_box.getText() == "":
            msg.showerror("Error", "No drill is assigned to delete")
        else:
            found = False
            for drill in data:
                if self.entry_box.getText() in drill.keys():
                    found = True
                    break
            if found:
                msg.showinfo("Drills", "Drill is Delete ")
            else:
                msg.showinfo("Drills", "Drill is not found. Please type again ")

    def upload(self):
        with open('drills.txt', 'r') as f:
            ts = []
            for line in f:
                t = json.loads(line)
                ts.append(t)
        drills_text = "All Drills:\n"
        i = 1
        for t in ts:
            key = list(t.keys())[0]  # get the first key in the dictionary
            drill_type = t[key]["Type: "]  # get the value of "Type:"
            drills_text += f"{i}. {key} - {drill_type}\n"
            i += 1
        text = Text(Point(320, 370), drills_text)
        text.setSize(20)
        text.setTextColor("white")
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

        drills_text = "All Drills:\n"
        i = 1
        for drill in drills:
            key = list(drill.keys())[0]  # get the first key in the dictionary
            drill_type = drill[key]["Type: "]  # get the value of "Type:"
            drills_text += f"{i}. {key} - {drill_type}\n"
            i += 1

        text = Text(Point(600, 320), drills_text)
        text.setSize(20)
        text.setTextColor("white")
        text.draw(self.win)


class show_win(Window):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_show_win():
        return show_win()

    def show_plan(self):
        with open('plan.txt', 'r') as f:
            data = json.load(f)

        drills_text = "Your plan \n\n\n"
        for drill_values in data.values():
            for i, day in enumerate(drill_values):
                day_plan = ', '.join(day['Day {} plan'.format(i + 1)])
                avg_intensity = day['Average intensity']
                avg_difficulty = day['Average difficulty']
                drills_text += f"Day {i + 1}: {day_plan}\n"
                drills_text += f"Average intensity: {avg_intensity}, Average difficulty: {avg_difficulty}\n\n"

        text = Text(Point(500, 300), drills_text)
        text.setSize(20)
        text.setTextColor("white")
        text.draw(self.win)


class board_window(Window):
    def __init__(self):
        super().__init__()
        self.data = {'Type: ': "",
                     'Intensity: ': "",
                     'Difficulty: ': ""}

    @staticmethod
    def create_board():
        return board_window()

    def create_board_button(self):
        self.generate = self.create_button("green", "Generate", Point(650, 600), 50)
        self.back = self.create_button("red", "back", Point(1200, 200), 50)
        self.note = Text(Point(650, 50),
                         "Small note: use . instead of , for decimal \n"
                         "Need at least 9 drills for the program to work \n "
                         "Click anywhere in the Generating Window to go back to the main window and choose other options")
        self.note.setSize(18)
        self.note.setTextColor("white")
        self.note.draw(self.win)

    def choose_plan(self):
        self.entry_box1 = Entry(Point(650, 200), 50)
        self.entry_box1.draw(self.win)
        self.box = Text(Point(650, 150), "What type of plan do you want? Offense/ Defense")
        self.box.setSize(18)
        self.box.setTextColor("white")
        self.box.draw(self.win)

    def choose_intensity(self):
        self.entry_box2 = Entry(Point(400, 450), 50)
        self.entry_box2.draw(self.win)
        self.box = Text(Point(400, 400), "At what average intensity? [1 - 5]")
        self.box.setSize(18)
        self.box.setTextColor("white")
        self.box.draw(self.win)

    def choose_difficulty(self):
        self.entry_box3 = Entry(Point(900, 450), 50)
        self.entry_box3.draw(self.win)
        self.box = Text(Point(900, 400), "At what average difficulty? [1 - 5]")
        self.box.setSize(18)
        self.box.setTextColor("white")
        self.box.draw(self.win)

    def get_offense_values(self):

        with open('drills.txt', 'r') as f:
            data = [json.loads(line) for line in f]

        off_dict = {}

        for drill in data:
            drill_name = list(drill.keys())[0]
            drill_type = drill[drill_name]['Type: ']

            if drill_type == 'O' or drill_type == 'B':
                off_dict[drill_name] = {'Difficulty': drill[drill_name]['Difficulty: '],
                                        'Intensity': drill[drill_name]['Intensity: ']}
        return off_dict

    def get_defense_values(self):

        with open('drills.txt', 'r') as f:
            data = [json.loads(line) for line in f]

        def_dict = {}

        for drill in data:
            drill_name = list(drill.keys())[0]
            drill_type = drill[drill_name]['Type: ']

            if drill_type == 'D' or drill_type == 'B':
                def_dict[drill_name] = {'Difficulty': drill[drill_name]['Difficulty: '],
                                        'Intensity': drill[drill_name]['Intensity: ']}
        return def_dict

    def check_input3(self):
        if self.entry_box1.getText() == "" or self.entry_box2.getText() == "" or self.entry_box3.getText() == "":
            msg.showerror("Error", "Please put in the input")
            return False

        elif self.entry_box1.getText() != "" and self.entry_box2.getText() != "" and self.entry_box3.getText() != "":
            data = ("offense", "defense")
            num1 = self.entry_box2.getText()
            num2 = self.entry_box3.getText()
            try:
                num1 = float(num1)
                num2 = float(num2)
            except ValueError:
                msg.showerror("Plan",
                              "Input for average intensity or difficulty is invalid. Please only use integer or float")
                return False

            if self.entry_box1.getText() in data and isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
                msg.showinfo("Plan", "Drill is generating")
                return True
            elif self.entry_box1.getText() not in data:
                msg.showerror("Plan",
                              "Please type in correctly 'offense' or 'defense' for the first box")
            elif self.entry_box1.getText() in data and (
                    not isinstance(num1, (int, float)) or not isinstance(num2, (int, float))):
                msg.showerror("Plan",
                              "Input for average intensity or difficulty is invalid. Please only use integer or float")
                return False
            else:
                msg.showerror("Plan", "Unexpected input. Please try again.")
                return False

    def generate_plan(self):
        plan_type = self.entry_box1.getText()
        intensity = self.entry_box2.getText()
        difficulty = self.entry_box3.getText()

        off_data = self.get_offense_values()
        def_data = self.get_defense_values()

        best_drills = None
        best_avg_difficulty = float('inf')
        best_avg_intensity = float('inf')

        if plan_type.lower() == "offense":
            data = off_data
        elif plan_type.lower() == "defense":
            data = def_data
        else:
            return "Invalid plan type"

        best = []
        for i in range(1, 4):
            for candidate_drills in itertools.combinations(data, 3):
                intensity_sum = 0
                difficulty_sum = 0
                for name in candidate_drills:
                    intensity_sum += float(data[name]['Intensity'])
                    difficulty_sum += float(data[name]['Difficulty'])
                intensity_avg = intensity_sum / 3
                difficulty_avg = difficulty_sum / 3
                diff_from_target = abs(difficulty_avg - float(difficulty))
                intensity_from_target = abs(intensity_avg - float(intensity))

                if diff_from_target < best_avg_difficulty or diff_from_target == best_avg_difficulty \
                        and intensity_from_target < best_avg_intensity or intensity_from_target == best_avg_intensity:
                    best_avg_difficulty = difficulty_avg
                    best_avg_intensity = intensity_avg
                    best_drills = candidate_drills

            plan = {"Day {} plan".format(i): best_drills,
                    "Average intensity": best_avg_intensity,
                    "Average difficulty": best_avg_difficulty}

            best.append(plan)

            # Remove the chosen drills from the original dict
            if plan_type.lower() == "offense":
                for drill_name in best_drills:
                    if drill_name in off_data:
                        del off_data[drill_name]
            elif plan_type.lower() == "defense":
                for drill_name in best_drills:
                    if drill_name in def_data:
                        del def_data[drill_name]

        i_d = "Drill Type: " + str(plan_type) + ", " + " Intensity: " + str(intensity) + ", " + "Difficulty: " + str(
            difficulty)
        pack = {i_d: best}

        with open('plan.txt', 'w') as f:
            json.dump(pack, f)
            f.write('\n')


class edit_window(Window):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_edit_win():
        return edit_window()

    def create_edit_button(self):
        self.back = self.create_button("white", "Back", Point(1100, 100), 50)
        self.add = self.create_button("white", "add", Point(1100, 300), 50)
        self.delete = self.create_button("white", "delete", Point(1100, 400), 50)
