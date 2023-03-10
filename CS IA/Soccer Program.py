from Window import *


def main_screen():
    window = main_window.create_main_win()
    window.create_main_button()
    return window

def edit_win():
    edit_win = edit_window.create_edit_win()
    edit_win.create_edit_button()
    return edit_win

def main():
    window = main_screen()
    m = window.get_location()

    while True:
        if window.quit.isClicked(m):
            window.win.close()
            break

        if window.history.isClicked(m):
            window.win.close()
            history = history_window.create_history_win()
            history.create_history_button()
            history.show_file()
            m1 = history.get_location()
            if history.back.isClicked(m1):
                history.win.close()
                window = main_screen()
                m = window.get_location()

        if window.edit.isClicked(m):
            window.win.close()
            edit = edit_win()
            m2 = edit.get_location()
            if edit.back.isClicked(m2):
                edit.win.close()
                window = main_screen()
                m = window.get_location()
            if edit.add.isClicked(m2):
                edit.win.close()
                add_win = add_window.create_add_win()
                add_win.create_add_button()
                add_win.input_box1()
                add_win.input_box2()
                add_win.input_box3()
                add_win.input_box4()
                m3 = add_win.get_location()
                if add_win.add.isClicked(m3):
                    add_win.win.close()
                    add_win.check_input()
                    add_win.save()
                if add_win.back.isClicked(m3):
                    add_win.win.close()
                    edit = edit_win()
                    m2 = edit.get_location()
            if edit.delete.isClicked(m2):
                edit.win.close()
                delete_win = delete_window.create_delete_win()
                delete_win.create_delete_button()
                delete_win.upload()
                delete_win.delete_box()
                m5 = delete_win.get_location()
                if delete_win.delete.isClicked(m5):
                    delete_win.check_input2()
                    delete_win.delete_drill()
                    delete_win.win.close()







        if window.drills.isClicked(m):
            window.win.close()
            drills = all_drills_window.create_all_drills_win()
            drills.create_all_drills_button()
            drills.show_drills()
            m4 = drills.get_location()
            if drills.back.isClicked(m4):
                drills.win.close()
                window = main_screen()
                m = window.get_location()

        if window.offense.isClicked(m) or window.defense.isClicked(m) or window.balance.isClicked(m):
            window.win.close()
            board = board_window.create_board()
            board.create_board_button()
            m1 = board.get_location()
            if board.back.isClicked(m1):
                board.win.close()
                window = main_screen()
                m = window.get_location()


if __name__ == "__main__":
    main()
