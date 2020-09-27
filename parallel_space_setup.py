import pyautogui
from tutorial import tutorial

is_downloaded = False
is_in_parallel_space = False

used = False
used1 = False


def download_parallel_space():
    global is_downloaded
    global is_in_parallel_space

    if is_downloaded is False:  # if parallel space hasn't been downloaded do this
        if pyautogui.pixelMatchesColor(87, 170, (255, 196, 0)):
            pyautogui.click(97, 170)  # open google play

        if pyautogui.pixelMatchesColor(622, 119, (241, 243, 244)):
            pyautogui.click(622, 119)  # click on search bar

        if pyautogui.pixelMatchesColor(171, 246, (146, 151, 155)):
            pyautogui.click(312, 248)  # click on recent search

        if pyautogui.pixelMatchesColor(316, 449, (255, 206, 25)):
            pyautogui.click(316, 448)  # click on parallel space app

        if pyautogui.pixelMatchesColor(602, 462, (74, 162, 255)):
            pyautogui.click(570, 527)  # click on paralle space if its in the other slot

        if pyautogui.pixelMatchesColor(1514, 272, (1, 135, 95)):
            pyautogui.click(1514, 272)  # click install button

        if pyautogui.pixelMatchesColor(972, 454, (1, 135, 95)):
            pyautogui.click(972, 454)  # click on open button
            is_downloaded = True
            is_in_parallel_space = True


def clone_app():
    global is_in_parallel_space
    global used
    global used1

    if is_in_parallel_space:
        if pyautogui.pixelMatchesColor(875, 850, (97, 185, 253)):
            pyautogui.click(875, 850)  # click agree button

        if pyautogui.pixelMatchesColor(701, 970, (52, 166, 255)) and used1 is False:
            pyautogui.click(701, 970)  # press blue button
            used1 = True

        if pyautogui.pixelMatchesColor(1120, 585, (56, 173, 162)):
            pyautogui.tripleClick(1135, 577)  # press allow x3

        if pyautogui.pixelMatchesColor(912, 705, (59, 59, 59)):
            pyautogui.click(912, 705)  # press start

        if pyautogui.pixelMatchesColor(1050, 996, (51, 165, 253)) and used is False:
            pyautogui.click(1050, 996)  # press blue button
            used = True

        if pyautogui.pixelMatchesColor(985, 618, (152, 152, 152)):
            pyautogui.click(985, 618)  # reject button

        if pyautogui.pixelMatchesColor(931, 223, (185, 185, 185)):
            pyautogui.click(931, 223)  # add app

        if pyautogui.pixelMatchesColor(916, 518, (158, 31, 44)):
            pyautogui.click(916, 518)  # select app to clone

        if pyautogui.pixelMatchesColor(1021, 459, (51, 165, 253)) and pyautogui.pixelMatchesColor(1053, 999,
                                                                                                  (51, 165, 253)):
            pyautogui.click(1053, 999)  # blue button to accept clone

        if pyautogui.pixelMatchesColor(939, 232, (176, 84, 58)):
            pyautogui.click(939, 232)  # open cloned app
            is_in_parallel_space = False
            tutorial(True)

        if pyautogui.pixelMatchesColor(1130, 222, (121, 30, 8)):
            pyautogui.click(1130, 222)  # open cloned app if its in the other slot
            is_in_parallel_space = False
            tutorial(True)
