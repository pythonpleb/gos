import pyautogui
import time
from manager import do_upgrade_beta
from mines_lvl_four import mines_to_four

mines_upg = False
drag = True
drag2 = False
fuel_upg = False
wall = False
hq = False


def mines(boolean):
    global mines_upg

    if boolean is False:
        mines_upg = False
    if boolean is True:
        mines_upg = True


def do_mines():
    global drag
    global drag2
    global fuel_upg
    global wall
    global hq
    global mines_upg

    if mines_upg is True:
        if drag is True:
            pyautogui.moveTo(846, 664)
            pyautogui.dragTo(865, 238, 2, button='left')
            drag = False
            fuel_upg = True

        if pyautogui.pixelMatchesColor(827, 835, (229, 212, 163)) and fuel_upg is True:
            pyautogui.click(867, 805)  # open fuel refinery
            time.sleep(0.5)
            do_upgrade_beta(1)
            time.sleep(0.5)
            fuel_upg = False
            drag2 = True

        if drag2 is True:
            pyautogui.moveTo(849, 501)
            pyautogui.dragTo(777, 838, 2, button='left')
            drag2 = False
            wall = True

        if pyautogui.pixelMatchesColor(802, 389, (188, 154, 90)) and wall is True:
            pyautogui.click(900, 491)  # open wall
            time.sleep(0.5)
            do_upgrade_beta(1)
            time.sleep(0.5)
            wall = False
            hq = True

        # TODO: find a better pixel to search for
        if pyautogui.pixelMatchesColor(801, 389, (175, 141, 75)) and hq is True:
            pyautogui.click(931, 192)  # open hq
            time.sleep(0.5)
            do_upgrade_beta(1)
            time.sleep(0.5)
            hq = False

        if pyautogui.pixelMatchesColor(1156, 322, (254, 220, 64)):
            pyautogui.click(1166, 288)  # free skip build button
            mines_upg = False
            time.sleep(0.5)
            mines_to_four(True)
