import pyautogui
import time

hq_opened = False
barracks_opened = False
bldg_done = False
bldg_done2 = False
map_clicked = False
boss_killed = False
is_in_tutorial = True


def collect_rewards():
    pyautogui.click(711, 882)


def finish_upgrade():
    pyautogui.click(996, 939)  # finish building now (VIP)
    time.sleep(1)
    pyautogui.click(1163, 81)  # hit the X button top right


def click_hint_button():
    pyautogui.click(678, 883)


def parallel_space_download():
    if pyautogui.pixelMatchesColor(87, 170, (255, 196, 0)):  # open the store
        pyautogui.click(87, 170)
    if pyautogui.pixelMatchesColor(608, 111, (241, 243, 244)):  # click on search bar
        pyautogui.click(608, 111)
        time.sleep(0.5)
        # if pyautogui.pixelMatchesColor(170, 248, (128, 134, 139)):  # click on recent search
        pyautogui.click(361, 244)
    if pyautogui.pixelMatchesColor(307, 262, (85, 159, 255)):  # click on parallel space
        pyautogui.click(307, 262)
    if pyautogui.pixelMatchesColor(1645, 315, (1, 135, 95)):  # install
        pyautogui.click(1645, 315)
    if pyautogui.pixelMatchesColor(1138, 449, (1, 135, 95)):  # open
        pyautogui.click(1138, 449)


def clone_app():
    if pyautogui.pixelMatchesColor(879, 854, (65, 171, 253)):
        pyautogui.click(879, 854)
    if pyautogui.pixelMatchesColor(680, 996, (52, 166, 255)):
        pyautogui.click(680, 996)
    if pyautogui.pixelMatchesColor(1152, 584, (2, 151, 137)):
        pyautogui.tripleClick(1152, 584)
    if pyautogui.pixelMatchesColor(914, 705, (81, 81, 81)):
        pyautogui.click(914, 705)
    if pyautogui.pixelMatchesColor(666, 1021, (51, 165, 253)):
        pyautogui.click(666, 1021)
    if pyautogui.pixelMatchesColor(985, 616, (152, 152, 152)):
        pyautogui.click(985, 616)
    if pyautogui.pixelMatchesColor(906, 218, (249, 132, 105)):
        pyautogui.click(933, 246)
        time.sleep(1)
    if pyautogui.pixelMatchesColor(915, 515, (186, 34, 56)):
        pyautogui.click(765, 268)
        time.sleep(1)
        pyautogui.click(918, 511)
        time.sleep(1)
        pyautogui.click(690, 1009)
    if pyautogui.pixelMatchesColor(1130, 247, (174, 113, 92)):
        pyautogui.click(1130, 247)
    if pyautogui.pixelMatchesColor(922, 245, (97, 46, 38)):
        pyautogui.click(922, 245)


def remove_the_tutorial_guy():
    if pyautogui.pixelMatchesColor(808, 907, (88, 0, 12)):
        # time.sleep(1)  # might not be needed. leave for now
        pyautogui.click(808, 907)  # get rid of the tutorial guy
        # time.sleep(1)
        click_hint_button()
        # time.sleep(1)


def tutorial():
    global hq_opened
    global barracks_opened
    global bldg_done
    global bldg_done2
    global map_clicked
    global boss_killed
    global is_in_tutorial

    if is_in_tutorial is True:
        if pyautogui.pixelMatchesColor(677, 698, (33, 67, 88)) and hq_opened is False:
            hq_opened = True
            pyautogui.click(844, 617)  # open HQ

        if pyautogui.pixelMatchesColor(1087, 643, (0, 0, 0)):
            pyautogui.click(996, 939)  # upgrade button
            # time.sleep(0.5)
            finish_upgrade()
            # time.sleep(0.5)
            collect_rewards()  # collect rewards
            # time.sleep(0.5)
            click_hint_button()  # go to barracks
            # time.sleep(0.5)

        if pyautogui.pixelMatchesColor(733, 546, (186, 95, 100)) and barracks_opened is False:
            barracks_opened = True
            pyautogui.click(845, 666)  # open barracks

        if pyautogui.pixelMatchesColor(837, 956, (54, 161, 2)) and bldg_done is False:
            bldg_done = True
            pyautogui.click(837, 956)  # hit the build button
            # time.sleep(1)
            finish_upgrade()
            collect_rewards()
            # time.sleep(1)

        if pyautogui.pixelMatchesColor(910, 847, (133, 124, 109)) and bldg_done2 is False:
            bldg_done2 = True
            pyautogui.click(940, 657)  # open barracks
            # time.sleep(0.5)

        if pyautogui.pixelMatchesColor(757, 323, (59, 97, 59)) and bldg_done2 is True:
            pyautogui.click(936, 721)  # hit the train button
            # time.sleep(0.5)
            pyautogui.click(954, 934)  # hit the speed up button
            # time.sleep(1)
            pyautogui.click(922, 893)  # hit the insta train button
            # time.sleep(0.5)
            pyautogui.click(1154, 77)  # close barracks
            collect_rewards()

        if pyautogui.pixelMatchesColor(660, 968, (198, 246, 85)) and map_clicked is False:
            map_clicked = True
            pyautogui.click(719, 985)  # open map

        #  here im in world map
        if pyautogui.pixelMatchesColor(733, 789, (143, 0, 0)):
            pyautogui.click(719, 356)  # click on boss

        if pyautogui.pixelMatchesColor(901, 437, (220, 73, 0)):
            pyautogui.click(966, 814)  # attack boss

        if pyautogui.pixelMatchesColor(1149, 165, (255, 221, 64)):
            pyautogui.click(823, 321)  # select champ

        if pyautogui.pixelMatchesColor(1150, 243, (44, 142, 5)):
            pyautogui.click(818, 833)  # deploy troops
            time.sleep(0.5)
            pyautogui.click(1065, 823)  # send attack

        if pyautogui.pixelMatchesColor(675, 810, (171, 0, 0)) and pyautogui.pixelMatchesColor(711, 350,
                                                                                              (131, 131, 108)):
            pyautogui.click(707, 985)  # open city
            boss_killed = True

        if pyautogui.pixelMatchesColor(732, 541, (184, 79, 80)) and boss_killed is True:
            collect_rewards()
            is_in_tutorial = False  # never repeat any tutorial code again after this
