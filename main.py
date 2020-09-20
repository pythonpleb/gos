import pyautogui
from do_tutorial import parallel_space_download, clone_app, tutorial, remove_the_tutorial_guy
from join_league import join_league
from hq_upgrade_to_lvl_four import mines, drag_mouse, lab_upgrades, main_bldgs
from upgrade_mines import mines_to_level_4
from upg_main_bldgs import main_bldgs_again


pyautogui.PAUSE = 1  # add 1 sec delay before every pyautogui action


def print_mouse_pos():
    x, y = pyautogui.position()
    print(x, y)


def main():

    # from do_tutorial.py
    parallel_space_download()
    clone_app()
    tutorial()
    remove_the_tutorial_guy()

    # from join_league.py
    join_league()

    # from hq_upgrade_to_lvl_four.py
    mines()
    drag_mouse()
    main_bldgs()
    lab_upgrades()

    # from upgrade_mines.py
    mines_to_level_4()

    # from upg_main_bldgs.py
    main_bldgs_again()


if __name__ == '__main__':
    while True:
        # print_mouse_pos()
        main()
