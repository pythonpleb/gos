import pyautogui
from manager import press_hint
import time
from upg_farm_buildings import farm

is_joining_league = False


def league(boolean):
    global is_joining_league

    if boolean is False:
        is_joining_league = False
    if boolean is True:
        is_joining_league = True


def join():
    global is_joining_league

    if is_joining_league is True:
        if pyautogui.pixelMatchesColor(835, 887, (159, 0, 0)):
            pyautogui.click(707, 891)  # get rewards manually
            press_hint()

        if pyautogui.pixelMatchesColor(867, 623, (67, 158, 0)):
            pyautogui.click(940, 620)  # press join button

        if pyautogui.pixelMatchesColor(1168, 75, (194, 0, 0)):
            time.sleep(0.5)
            pyautogui.click(1168, 75)  # close league menu
            time.sleep(0.5)
            pyautogui.click(707, 891)
            time.sleep(0.5)
            press_hint()
            is_joining_league = False
            farm(True)
