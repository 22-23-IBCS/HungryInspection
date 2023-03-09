from Window import *


def main_screen():
    window = main_window.create_main_win()
    window.create_main_button()
    return window


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
            edit_win = edit_window.create_edit_win()
            edit_win.create_edit_button()
            m2 = edit_win.get_location()
            if edit_win.back.isClicked(m2):
                edit_win.win.close()
                window = main_screen()
                m = window.get_location()
            if edit_win.add.isClicked(m2):
                edit_win.win.close()
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
