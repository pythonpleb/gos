import pyautogui
import time
from manager import do_upgrade_beta, do_build_beta, get_rewards_beta

main_bldgs = False
second_half_of_bldgs = False
workshop = True
barracks = False
storage = False
clone_lab = False
lab = False
wall = False
radio_tower = False
drag = False


def upg_main_bldgs(boolean):
    global main_bldgs

    if boolean is False:
        main_bldgs = False
    if boolean is True:
        main_bldgs = True


def do_main_bldgs():
    global workshop
    global barracks
    global storage
    global clone_lab
    global wall
    global main_bldgs
    global drag
    global second_half_of_bldgs

    if main_bldgs is True:
        if pyautogui.pixelMatchesColor(1169, 469, (87, 54, 29)) and workshop is True:
            pyautogui.click(1146, 493)  # open workshop
            time.sleep(0.5)
            do_build_beta()
            time.sleep(0.5)
            do_upgrade_beta(4)  # 3 lvls
            time.sleep(0.5)
            workshop = False
            clone_lab = True

        if pyautogui.pixelMatchesColor(1140, 560, (237, 227, 179)) and clone_lab is True:
            pyautogui.click(824, 468)  # open clone lab
            time.sleep(0.5)  # adding delays because its going too fast
            do_build_beta()
            time.sleep(0.5)
            do_upgrade_beta(2)
            time.sleep(0.5)
            clone_lab = False
            barracks = True

        if pyautogui.pixelMatchesColor(793, 526, (142, 67, 13)) and barracks is True:
            pyautogui.click(901, 297)  # open barracks
            time.sleep(0.5)
            do_upgrade_beta(1)
            time.sleep(0.5)
            barracks = False
            storage = True

        if pyautogui.pixelMatchesColor(815, 213, (96, 131, 163)) and storage is True:
            pyautogui.click(1097, 178)  # open storage
            time.sleep(0.5)
            do_build_beta()
            time.sleep(0.5)
            do_upgrade_beta(2)
            time.sleep(0.5)
            storage = False
            wall = True

        if pyautogui.pixelMatchesColor(1141, 577, (237, 193, 158)) and wall is True:
            pyautogui.click(1029, 675)  # open wall
            time.sleep(0.5)
            do_upgrade_beta(1)
            time.sleep(0.5)
            wall = False
            second_half_of_bldgs = True
            main_bldgs = False
            drag = True


def second_half_bldgs():
    global drag
    global lab
    global radio_tower
    global second_half_of_bldgs

    if second_half_of_bldgs is True:
        if drag is True:
            pyautogui.moveTo(764, 679)
            pyautogui.dragTo(1111, 852, 2, button='left')
            drag = False
            lab = True

        if pyautogui.pixelMatchesColor(777, 518, (191, 92, 32)) and lab is True:
            pyautogui.click(848, 530)  # open lab
            time.sleep(0.8)
            do_upgrade_beta(2)
            time.sleep(0.8)
            lab = False
            radio_tower = True

        if pyautogui.pixelMatchesColor(811, 421, (100, 85, 52)) and radio_tower is True:
            pyautogui.click(741, 361)  # open radio tower
            time.sleep(0.5)
            do_upgrade_beta(2)
            time.sleep(0.5)
            get_rewards_beta(40)
            # TODO: add boolean to move on to the next stage here
            radio_tower = False
            second_half_of_bldgs = False
