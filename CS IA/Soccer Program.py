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

        if window.edit.isClicked(m):
            window.win.close()
            edit = edit_win()
            m = edit.get_location()

            while True:
                if edit.add.isClicked(m):
                    edit.win.close()
                    add_win = add_window.create_add_win()
                    add_win.create_add_button()
                    add_win.input_box1()
                    add_win.input_box2()
                    add_win.input_box3()
                    add_win.input_box4()
                    m = add_win.get_location()

                    while not add_win.back.isClicked(m):
                        if add_win.add.isClicked(m):
                            add_win.win.close()
                            add_win.check_input()
                            add_win.save()
                            break
                        m = add_win.get_location()

                    add_win.win.close()
                    edit = edit_win()
                    m = edit.get_location()

                elif edit.delete.isClicked(m):
                    edit.win.close()
                    delete_win = delete_window.create_delete_win()
                    delete_win.create_delete_button()
                    delete_win.upload()
                    delete_win.delete_box()
                    m = delete_win.get_location()

                    while not delete_win.back.isClicked(m):
                        if delete_win.delete.isClicked(m):
                            delete_win.check_input2()
                            delete_win.delete_drill()
                            break
                        m = delete_win.get_location()

                    delete_win.win.close()
                    edit = edit_win()
                    m = edit.get_location()

                elif edit.back.isClicked(m):
                    edit.win.close()
                    window = main_screen()
                    m = window.get_location()
                    break

        if window.drills.isClicked(m):
            window.win.close()
            drills = all_drills_window.create_all_drills_win()
            drills.create_all_drills_button()
            drills.show_drills()
            m = drills.get_location()
            while True:
                if drills.back.isClicked(m):
                    drills.win.close()
                    window = main_screen()
                    m = window.get_location()
                    break

        if window.plan.isClicked(m):
            window.win.close()
            board = board_window.create_board()
            board.create_board_button()
            board.choose_plan()
            board.choose_intensity()
            board.choose_difficulty()
            m7 = board.get_location()

            while True:
                if board.back.isClicked(m7):
                    board.win.close()
                    window = main_screen()
                    m = window.get_location()
                    break

                elif board.generate.isClicked(m7):
                    check = board.check_input3()
                    if check is True:
                        board.generate_plan()
                        plan = show_win.create_show_win()
                        plan.show_plan()
                        m7 = board.get_location()
                        board.win.close()
                        window = main_screen()
                        m = window.get_location()
                        break

        m = window.get_location()


if __name__ == "__main__":
    main()
