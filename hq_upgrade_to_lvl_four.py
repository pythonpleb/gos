import pyautogui
import time
from do_tutorial import click_hint_button
from upgrade_mines import start_mines_upg_again

hq_to_four = True
water_upgraded = False
fuel_upgraded = False
do_mines = False
count = 0

do_drag = False
drag_done = False
do_main_bldgs = False
wall_upgraded = False
lab_upgraded = False

upgrade_lab_stuff = False

is_in_tech = False
hq_lvl_3 = False
fuel_refinery_lvl_3 = False
waterworks_lvl_3 = False
wall_lvl_3 = False
hq_upgrade_four_done = False
asked_for_help = False


def build_mines(a):
    global do_mines

    if a is True:
        do_mines = True
    else:
        do_mines = False


def do_lvl_2_upgrade():
    pyautogui.click(1034, 941)  # hit upgrade button
    time.sleep(0.5)
    pyautogui.click(1034, 941)  # insta finish
    pyautogui.click(1161, 75)  # close bldg


def mines():
    global water_upgraded
    global fuel_upgraded
    global do_mines
    global do_drag

    if do_mines is True:
        click_hint_button()
        if pyautogui.pixelMatchesColor(819, 623, (255, 55, 55)):  # collect rss from bldgs
            pyautogui.click(826, 636)  # collect metal
            pyautogui.click(999, 713)  # collect fuel
            pyautogui.click(1157, 748)  # collect money
            pyautogui.click(1099, 597)  # collect water
            pyautogui.click(914, 521)  # collect food

        if pyautogui.pixelMatchesColor(829, 499, (177, 78, 42)) and water_upgraded is False:
            pyautogui.click(1080, 689)  # click on water bldg

        if pyautogui.pixelMatchesColor(845, 75, (252, 217, 63)):
            do_lvl_2_upgrade()
            water_upgraded = True

        if pyautogui.pixelMatchesColor(1114, 625, (32, 165, 142)) and water_upgraded is True and fuel_upgraded is False:
            pyautogui.click(983, 785)  # click on fuel bldg

        if pyautogui.pixelMatchesColor(987, 76, (248, 208, 60)):
            do_lvl_2_upgrade()
            fuel_upgraded = True
            do_mines = False
            do_drag = True


def drag_mouse():
    global count
    global do_drag
    global do_main_bldgs
    global drag_done
    global hq_lvl_3

    if count == 0 and do_drag is True:
        pyautogui.moveTo(1026, 491)
        pyautogui.dragTo(858, 855, 2, button='left')
        count += 1
        do_drag = False
        do_main_bldgs = True

    if count == 1 and hq_lvl_3 is True:
        pyautogui.moveTo(808, 599)
        pyautogui.dragTo(834, 310, 2, button='left')
        drag_done = True
        hq_lvl_3 = False
        count += 1

    if count == 2 and wall_lvl_3 is True:
        pyautogui.moveTo(950, 478)
        pyautogui.dragTo(911, 868, 2, button='left')
        count += 1


def lab_upgrades():
    global is_in_tech
    global upgrade_lab_stuff
    global lab_upgraded

    if upgrade_lab_stuff is True:
        if pyautogui.pixelMatchesColor(845, 932, (51, 154, 0)):
            pyautogui.click(845, 932)  # click on build
            time.sleep(0.5)
            pyautogui.click(1116, 945)  # insta finish lvl 1
            # time.sleep(0.5)
            pyautogui.click(1116, 945)  # click on upgrade
            # time.sleep(0.5)
            pyautogui.click(1116, 945)  # insta finish lvl 2

        if pyautogui.pixelMatchesColor(859, 944, (76, 76, 76)):
            pyautogui.click(1014, 240)  # click on tech button
            is_in_tech = True

        if is_in_tech is True:
            pyautogui.click(826, 330)  # click on research speed
            if pyautogui.pixelMatchesColor(886, 573, (77, 182, 0)):
                pyautogui.click(886, 573)  # hit the research button

        if pyautogui.pixelMatchesColor(711, 480, (214, 87, 39)):
            pyautogui.click(876, 508)  # click on construction
            if pyautogui.pixelMatchesColor(922, 567, (77, 179, 0)):
                pyautogui.click(885, 584)  # hit the research button

        if pyautogui.pixelMatchesColor(743, 497, (69, 68, 110)):
            pyautogui.click(874, 504)  # click the food production
            if pyautogui.pixelMatchesColor(882, 595, (76, 180, 0)):
                pyautogui.click(882, 595)  # hit the research button

        if pyautogui.pixelMatchesColor(1152, 934, (0, 115, 146)):
            pyautogui.click(1152, 934)  # click the time help button

        if pyautogui.pixelMatchesColor(1182, 315, (112, 108, 107)):
            pyautogui.click(1167, 77)  # click the X button top right
            is_in_tech = False
            upgrade_lab_stuff = False
            lab_upgraded = True


def main_bldgs():
    global do_main_bldgs
    global wall_upgraded
    global upgrade_lab_stuff
    global hq_lvl_3
    global fuel_refinery_lvl_3
    global waterworks_lvl_3
    global wall_lvl_3
    global hq_upgrade_four_done
    global drag_done
    global asked_for_help

    if do_main_bldgs is True:
        
        if wall_lvl_3 is True:
            pyautogui.click(836, 239)  # open HQ

            if pyautogui.pixelMatchesColor(985, 932, (55, 161, 0)):
                pyautogui.click(985, 932)  # hit the upgrade button
            if pyautogui.pixelMatchesColor(989, 921, (0, 127, 157)):
                pyautogui.click(985, 932)  # hit the time help button
                asked_for_help = True
                wall_lvl_3 = False

        if asked_for_help is True:
            pyautogui.click(1008, 950)  # insta skip bldg
            if pyautogui.pixelMatchesColor(800, 542, (3, 7, 38)):
                start_mines_upg_again(True)
                pyautogui.click(910, 896)
            pyautogui.click(1161, 85)  # close HQ
            asked_for_help = False
            do_main_bldgs = False

        if wall_upgraded is False:
            pyautogui.click(908, 469)  # click on wall
            do_lvl_2_upgrade()
            wall_upgraded = True

        if lab_upgraded is False and wall_upgraded is True:
            pyautogui.click(901, 348)  # open lab
            upgrade_lab_stuff = True

        if lab_upgraded is True and pyautogui.pixelMatchesColor(778, 339, (231, 131, 55)):
            pyautogui.click(930, 187)  # open HQ
            do_lvl_2_upgrade()
            hq_lvl_3 = True

        if drag_done is True:
            pyautogui.click(840, 826)  # open fuel refinery bldg
            do_lvl_2_upgrade()
            fuel_refinery_lvl_3 = True
            drag_done = False

        if fuel_refinery_lvl_3 is True:
            pyautogui.click(953, 756)
            do_lvl_2_upgrade()
            waterworks_lvl_3 = True
            fuel_refinery_lvl_3 = False

        if waterworks_lvl_3 is True:
            pyautogui.click(918, 216)
            do_lvl_2_upgrade()
            wall_lvl_3 = True
            waterworks_lvl_3 = False
