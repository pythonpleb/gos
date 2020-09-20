import pyautogui

warehouse_done = False
barracks_done = False
storage_done = False
clone_lab_done = False
wall_done = False
radio_done = False

main_bldgs_upg = False


def start_main_bldgs_upg(a):
    global main_bldgs_upg

    if a is True:
        main_bldgs_upg = True
    else:
        main_bldgs_upg = False


def upg_new_bldg():
    if pyautogui.pixelMatchesColor(866, 936, (60, 173, 0)):
        pyautogui.click(866, 936)  # hit the build button
        pyautogui.click(1080, 932)  # insta upg button


def close_bldg():
    if pyautogui.pixelMatchesColor(885, 918, (81, 81, 81)):
        pyautogui.click(1166, 78)  # close bldg


def preform_upgrades(num):
    for i in range(num):
        pyautogui.click(1088, 929)  # hit this button as many times as num is equal to


def main_bldgs_again():
    global warehouse_done
    global barracks_done
    global clone_lab_done
    global storage_done
    global radio_done
    global wall_done

    if main_bldgs_upg is True:
        if warehouse_done is False:
            pyautogui.click(1132, 520)  # open warehouse
            upg_new_bldg()
            preform_upgrades(6)
            close_bldg()
            warehouse_done = True
            # good up to here

        if barracks_done is False:
            pyautogui.click(945, 316)  # open barracks
            preform_upgrades(2)
            close_bldg()
            barracks_done = True

        if warehouse_done is False:
            pyautogui.click(1089, 182)  # open warehouse
            upg_new_bldg()
            preform_upgrades(4)
            close_bldg()
            warehouse_done = True

        if clone_lab_done is False:
            pyautogui.click(807, 483)  # open clone lab
            upg_new_bldg()
            preform_upgrades(4)
            close_bldg()
            clone_lab_done = True

        if wall_done is False:
            pyautogui.click(773, 959)  # open wall
            preform_upgrades(2)
            close_bldg()
            # drag mouse now
            wall_done = True
