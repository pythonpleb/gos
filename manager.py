import pyautogui
import time


def remove_tutorial_guy():
    if pyautogui.pixelMatchesColor(775, 909, (114, 0, 16)):
        pyautogui.click(795, 922)  # click to remove the tutorial guy


def press_hint():
    if pyautogui.pixelMatchesColor(727, 886, (177, 9, 1)):
        pyautogui.click(676, 887)


def get_tutorial_rewards(clicks):
    if pyautogui.pixelMatchesColor(687, 882, (96, 242, 146)):
        for i in range(clicks):
            pyautogui.click(700, 888)


def get_rewards_beta(clicks):
    for i in range(clicks):
        pyautogui.click(700, 888)


def do_build():
    if pyautogui.pixelMatchesColor(855, 938, (54, 162, 0)):
        pyautogui.click(855, 938)  # press build button
        time.sleep(0.5)
        pyautogui.click(1039, 942)

    if pyautogui.pixelMatchesColor(1014, 934, (67, 67, 67)):
        pyautogui.click(1169, 76)  # close button


def do_build_beta():
    pyautogui.click(926, 922)  # press build
    time.sleep(0.5)
    pyautogui.click(1070, 926)  # skip build


def do_upgrade(num_of_lvls):
    clicks = num_of_lvls * 2

    if pyautogui.pixelMatchesColor(744, 480, (134, 130, 127)):
        for i in range(clicks):
            pyautogui.click(981, 934)  # upgrade
    pyautogui.click(1166, 78)  # press close button


def do_upgrade_beta(num_of_lvls):
    clicks = num_of_lvls * 2

    for i in range(clicks):
        time.sleep(0.2)
        pyautogui.click(992, 929)  # upgrade
    time.sleep(0.5)
    pyautogui.click(1166, 78)  # press close button


def do_train():
    if pyautogui.pixelMatchesColor(754, 317, (61, 99, 59)):
        pyautogui.click(890, 706)  # train button

    if pyautogui.pixelMatchesColor(985, 922, (196, 130, 0)):
        pyautogui.click(985, 922)  # build now

    if pyautogui.pixelMatchesColor(843, 896, (195, 127, 0)):
        pyautogui.click(843, 896)  # finish now

    if pyautogui.pixelMatchesColor(1166, 80, (194, 0, 0)):
        pyautogui.click(1166, 80)  # close button
