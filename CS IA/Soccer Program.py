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
            m1 = history.get_location()
            if history.back.isClicked(m1):
                history.win.close()
                window = main_screen()
                m = window.get_location()

        if window.edit.isClicked(m):
            window.win.close()
            edit_win = edit_window.create_edit_win()
            edit_win.create_edit_button()
            m1 = edit_win.get_location()
            if edit_win.back.isClicked(m1):
                edit_win.win.close()
                window = main_screen()
                m = window.get_location()
            if edit_win.add.isClicked(m1):
                edit_win.win.close()
                add_win = add_window.create_add_win()
                add_win.create_add_button()
                add_win.input_box() #if this running the is Clicked function is not working
                m2 = add_win.get_location()
                if add_win.back.isClicked(m2):
                    add_win.win.close()
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
