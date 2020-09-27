import pyautogui
from manager import remove_tutorial_guy, press_hint, do_upgrade, get_tutorial_rewards, do_build, do_train
from join_league import league

is_in_tutorial = False
upg_hq = False
upg_barracks = False
train_troops = False
kill_boss = False


def tutorial(boolean):
    global is_in_tutorial
    if boolean is False:
        is_in_tutorial = False
    if boolean is True:
        is_in_tutorial = True


def start_tutorial():
    global upg_hq
    global upg_barracks
    global train_troops
    global kill_boss
    global is_in_tutorial

    remove_tutorial_guy()

    if is_in_tutorial is True:
        if upg_hq is False:
            upg_hq = True
            press_hint()

        if upg_hq is True and upg_barracks is False:
            upg_barracks = True
            if pyautogui.pixelMatchesColor(875, 818, (85, 110, 29)):
                pyautogui.click(896, 642)  # open HQ
            do_upgrade(1)
            get_tutorial_rewards(1)
            press_hint()

        if upg_barracks is True:
            upg_barracks = False
            train_troops = True
            if pyautogui.pixelMatchesColor(735, 628, (87, 90, 72)):
                pyautogui.click(890, 667)  # open barracks
            do_build()
            pyautogui.click(708, 877)
            press_hint()

        if train_troops is True:
            train_troops = False
            kill_boss = True
            if pyautogui.pixelMatchesColor(737, 567, (100, 138, 166)):
                pyautogui.click(839, 658)  # open barracks
            do_train()
            get_tutorial_rewards(1)
            press_hint()

        if kill_boss is True:
            kill_boss = False

            if pyautogui.pixelMatchesColor(726, 741, (40, 213, 185)):
                pyautogui.click(708, 985)  # open map

            if pyautogui.pixelMatchesColor(702, 413, (231, 144, 20)):
                pyautogui.click(716, 353)  # click on boss

            if pyautogui.pixelMatchesColor(1017, 447, (238, 105, 0)):
                pyautogui.click(940, 818)  # attack boss

            if pyautogui.pixelMatchesColor(810, 295, (37, 155, 209)):
                pyautogui.click(774, 295)  # select champion

            if pyautogui.pixelMatchesColor(806, 831, (77, 179, 0)):
                pyautogui.click(806, 831)  # auto deploy button

            if pyautogui.pixelMatchesColor(1057, 851, (90, 202, 25)):
                pyautogui.click(1057, 851)  # press attack button

            if pyautogui.pixelMatchesColor(709, 365, (147, 144, 129)):
                is_in_tutorial = False
                league(True)
                pyautogui.click(715, 979)  # go to city

