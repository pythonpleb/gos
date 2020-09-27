import pyautogui
from manager import do_upgrade_beta
import time
from hq_lvl_three import hq_upg

is_at_farm_stage = False
upg_bldgs = False
water_upg = False
fuel_upg = False

food_collecting = False
water_collecting = False
fuel_collecting = False
metal_collecting = True
money_collecting = False


def farm(boolean):
    global is_at_farm_stage

    if boolean is False:
        is_at_farm_stage = False
    if boolean is True:
        is_at_farm_stage = True


def collect_and_upg():
    global upg_bldgs
    global is_at_farm_stage
    global fuel_upg
    global water_upg
    global food_collecting
    global water_collecting
    global fuel_collecting
    global metal_collecting
    global money_collecting

    if is_at_farm_stage is True:
        if pyautogui.pixelMatchesColor(821, 616, (255, 55, 55)) and metal_collecting is True:
            pyautogui.click(829, 631)  # get metal
            metal_collecting = False
            fuel_collecting = True
            time.sleep(0.2)

        if pyautogui.pixelMatchesColor(989, 675, (255, 55, 55)) and fuel_collecting is True:
            pyautogui.click(992, 701)  # get fuel
            fuel_collecting = False
            money_collecting = True
            time.sleep(0.2)

        if pyautogui.pixelMatchesColor(1150, 742, (250, 54, 54)) and money_collecting is True:
            pyautogui.click(1155, 772)  # get money
            money_collecting = False
            water_collecting = True
            time.sleep(0.2)

        if pyautogui.pixelMatchesColor(1076, 578, (255, 55, 55)) and water_collecting is True:
            pyautogui.click(1095, 613)  # get water
            water_collecting = False
            food_collecting = True
            time.sleep(0.2)

        if pyautogui.pixelMatchesColor(932, 510, (255, 55, 55)) and food_collecting is True:
            pyautogui.click(923, 536)  # get food
            food_collecting = False
            upg_bldgs = True

        if upg_bldgs is True:
            if water_upg is False and pyautogui.pixelMatchesColor(1140, 639, (152, 116, 89)):
                pyautogui.click(1094, 684)  # open waterworks
                time.sleep(0.5)
                do_upgrade_beta(1)
                time.sleep(0.5)
                water_upg = True

            if fuel_upg is False and pyautogui.pixelMatchesColor(1114, 623, (32, 158, 136)):
                pyautogui.click(991, 785)  # open fuel refinery
                time.sleep(0.5)
                do_upgrade_beta(1)
                time.sleep(0.5)
                upg_bldgs = False
                is_at_farm_stage = False
                fuel_upg = True
                hq_upg(True)
