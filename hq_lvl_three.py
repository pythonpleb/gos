import pyautogui
import time
from manager import do_upgrade_beta, do_build_beta
from lab_research import tech

upg_hq = False
dragged = False
wall_upg = False
hq_upgraded = False
lab_upgraded = False


def hq_upg(boolean):
    global upg_hq

    if boolean is False:
        upg_hq = False
    if boolean is True:
        upg_hq = True


def do_hq():
    global dragged
    global wall_upg
    global hq_upgraded
    global upg_hq

    if upg_hq is True:
        if dragged is False:
            pyautogui.moveTo(1040, 337)
            time.sleep(0.2)
            pyautogui.dragTo(906, 800, 2, button='left')
            dragged = True

        if pyautogui.pixelMatchesColor(948, 563, (144, 81, 35)) and wall_upg is False:
            pyautogui.click(948, 563)  # open wall
            time.sleep(0.5)
            do_upgrade_beta(1)
            time.sleep(0.5)
            wall_upg = True

        if pyautogui.pixelMatchesColor(948, 563, (144, 81, 35)) and hq_upgraded is False:
            pyautogui.click(958, 266)  # open hq
            time.sleep(0.5)
            do_upgrade_beta(1)
            time.sleep(0.5)
            hq_upgraded = True

        if pyautogui.pixelMatchesColor(948, 563, (144, 81, 35)) and lab_upgraded is False:
            pyautogui.click(891, 456)  # open lab
            time.sleep(1)
            do_build_beta()
            do_upgrade_beta(1)
            time.sleep(0.5)
            tech(True)
            upg_hq = False

