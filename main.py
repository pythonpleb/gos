import pyautogui
from parallel_space_setup import download_parallel_space, clone_app
from tutorial import start_tutorial
from join_league import join
from upg_farm_buildings import collect_and_upg
from hq_lvl_three import do_hq
from lab_research import tech_upg
from mines_lvl_three import do_mines
from mines_lvl_four import upg_mines_to_four
from main_bldgs_upg import do_main_bldgs, second_half_bldgs


def mouse_position():
    x, y = pyautogui.position()
    print(x, y)


def main():
    # parallel_space_setup.py
    download_parallel_space()
    clone_app()

    # tutorial.py
    start_tutorial()

    # join_league.py
    join()

    # upg_farm_buildings.py
    collect_and_upg()

    # hq_lvl_three.py
    do_hq()

    # lab_research.py
    tech_upg()

    # mines_lvl_three.py
    do_mines()

    # mines_lvl_four.py
    upg_mines_to_four()

    # main bldgs_upg.py
    do_main_bldgs()
    second_half_bldgs()


if __name__ == '__main__':
    while True:
        mouse_position()
        main()
