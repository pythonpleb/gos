import pyautogui
from upg_main_bldgs import start_main_bldgs_upg

start_mines = False
count = 0
count2 = 0

water_done = False
fuel_done = False
metal_done = False
farm_done = False
money_done = False


def start_mines_upg_again(a):
    global start_mines

    if a is True:
        start_mines = True
    else:
        start_mines = False


def drag_mouse_to_mines():
    global count
    if count == 0:
        pyautogui.moveTo(773, 786)
        pyautogui.dragTo(848, 277, 2, button='left')
        count += 1


def drag_to_bldgs():
    global count2
    if count2 == 0:
        pyautogui.moveTo(1137, 465)
        pyautogui.dragTo(695, 906, 2, button='left')
        count2 += 1


def preform_upgrades(num):
    for i in range(num):
        pyautogui.click(995, 923)


def close_bldg_screen():
    if pyautogui.pixelMatchesColor(856, 921, (69, 69, 69)):
        pyautogui.click(1166, 73)  # close bldg


def mines_to_level_4():
    global water_done
    global fuel_done
    global metal_done
    global money_done
    global farm_done
    global start_mines

    if start_mines is True:
        drag_mouse_to_mines()
        if water_done is False:
            pyautogui.click(993, 631)  # open water bldg
            preform_upgrades(2)
            close_bldg_screen()
            water_done = True

        if fuel_done is False:
            pyautogui.click(880, 720)  # open fuel bldg
            preform_upgrades(2)
            close_bldg_screen()
            fuel_done = True

        if money_done is False:
            pyautogui.click(1099, 798)  # open money bldg
            preform_upgrades(6)
            close_bldg_screen()
            money_done = True

        if metal_done is False:
            pyautogui.click(754, 678)  # open metal bldg
            preform_upgrades(6)
            close_bldg_screen()
            metal_done = True

        if farm_done is False:
            pyautogui.click(830, 556)  # open farm bldg
            preform_upgrades(6)
            close_bldg_screen()
            farm_done = True
            drag_to_bldgs()
            start_main_bldgs_upg(True)
            start_mines = False
