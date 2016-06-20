import pyautogui
import os
import recipes
__author__ = 'dusti'

def __main__():
    gameScreenOffset = []
    gameScreenOffset[0], gameScreenOffset[1] = pyautogui.locateOnScreen('SCREENS\\MENUS\\MAIN_MENU_CROP.png')
    pyautogui.click(960 - gameScreenOffset[0], 490 - gameScreenOffset[1])
