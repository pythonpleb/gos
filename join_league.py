import pyautogui
from do_tutorial import collect_rewards
from hq_upgrade_to_lvl_four import build_mines

is_joining_league = True


def join_league():
    global is_joining_league

    if is_joining_league is True:
        if pyautogui.pixelMatchesColor(1200, 790, (236, 236, 236)):
            pyautogui.click(1181, 766)  # click the "free" button to open league menu

        if pyautogui.pixelMatchesColor(925, 420, (244, 171, 33)):
            pyautogui.click(930, 612)  # click the join button

        if pyautogui.pixelMatchesColor(1160, 525, (98, 180, 180)):
            pyautogui.click(1181, 85)  # click the X button top right
            collect_rewards()
            is_joining_league = False
            build_mines(True)
