import pyautogui
import time
from manager import do_upgrade_beta
from main_bldgs_upg import upg_main_bldgs

mines_upg_to_four = False
drag = True
drag2 = False
fuel = False
metal = False
food = False
water = False
money = False


def mines_to_four(boolean):
    global mines_upg_to_four

    if boolean is False:
        mines_upg_to_four = False
    if boolean is True:
        mines_upg_to_four = True


def upg_mines_to_four():
    global drag
    global drag2
    global food
    global water
    global metal
    global money
    global fuel
    global mines_upg_to_four

    if mines_upg_to_four is True:
        if drag is True:
            pyautogui.moveTo(795, 579)
            pyautogui.dragTo(836, 207, 2, button='left')
            drag = False
            metal = True

        if pyautogui.pixelMatchesColor(795, 469, (197, 176, 129)) and metal is True:
            pyautogui.click(748, 726)  # open metal bldg
            time.sleep(0.5)
            do_upgrade_beta(3)
            time.sleep(0.5)
            metal = False
            fuel = True

        if pyautogui.pixelMatchesColor(795, 479, (190, 170, 117)) and fuel is True:
            pyautogui.click(849, 793)  # open fuel bldg
            time.sleep(0.5)
            do_upgrade_beta(1)
            time.sleep(0.5)
            fuel = False
            money = True

        if pyautogui.pixelMatchesColor(792, 488, (187, 172, 116)) and money is True:
            pyautogui.click(1036, 833)  # open money bldg
            time.sleep(0.5)
            do_upgrade_beta(3)
            time.sleep(0.5)
            money = False
            water = True

        if pyautogui.pixelMatchesColor(794, 489, (183, 170, 109)) and water is True:
            pyautogui.click(939, 696)  # open water bldg
            time.sleep(0.5)
            do_upgrade_beta(2)
            time.sleep(0.5)
            water = False
            food = True

        if pyautogui.pixelMatchesColor(790, 493, (182, 172, 116)) and food is True:
            pyautogui.click(787, 617)  # open food bldg
            time.sleep(0.5)
            do_upgrade_beta(3)
            time.sleep(0.5)
            food = False
            drag2 = True

        if drag2 is True:
            pyautogui.moveTo(1094, 338)
            pyautogui.dragTo(727, 718, 2, button='left')
            drag2 = False
            upg_main_bldgs(True)
            mines_upg_to_four = False
