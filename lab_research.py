import pyautogui
import time
from mines_lvl_three import mines

tech_res = False
res_speed = False
construction = False
food_prod = False
close_lab = False
ask_for_help = False


def tech(boolean):
    global tech_res

    if boolean is False:
        tech_res = False
    if boolean is True:
        tech_res = True


def do_research():
    if pyautogui.pixelMatchesColor(944, 569, (78, 183, 0)):
        pyautogui.click(944, 569)


def tech_upg():
    global res_speed
    global construction
    global food_prod
    global close_lab
    global ask_for_help
    global tech_res

    if tech_res is True:
        if pyautogui.pixelMatchesColor(816, 417, (238, 150, 66)):
            pyautogui.click(930, 428)  # open lab
            time.sleep(1)

        if pyautogui.pixelMatchesColor(741, 542, (218, 159, 148)):
            pyautogui.click(1011, 241)  # click on tech tab
            res_speed = True

        if res_speed is True:
            pyautogui.click(806, 343)  # click on research speed
            time.sleep(0.5)
            do_research()
            res_speed = False
            construction = True

        if pyautogui.pixelMatchesColor(1183, 311, (117, 113, 112)) and construction is True:
            pyautogui.click(843, 464)  # click on construction
            time.sleep(0.5)
            do_research()
            ask_for_help = True
            construction = False
            food_prod = True

        if pyautogui.pixelMatchesColor(989, 922, (0, 130, 161)) and ask_for_help is True:
            time.sleep(0.5)
            pyautogui.click(1008, 939)  # ask for time help
            time.sleep(0.5)
            ask_for_help = False

        if pyautogui.pixelMatchesColor(1178, 311, (119, 115, 114)) and food_prod is True:
            pyautogui.click(854, 484)  # click on food production
            time.sleep(0.5)
            do_research()
            food_prod = False
            close_lab = True

        if close_lab is True:
            time.sleep(0.5)
            pyautogui.click(1162, 73)  # close lab
            time.sleep(0.5)
            close_lab = False
            mines(True)
            tech_res = False
