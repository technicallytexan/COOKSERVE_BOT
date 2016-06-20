import pyautogui
import time
__author__ = 'dusti'
# RECIPES
# ONLY INCLUDES 1 STAR RECIPES


class Recipe:
    def __init__(self, command, image):
        self.com = command
        self.img = image


class BakedPotato:
    icon = 'SCREENS\\FOOD\\BAKED POTATO\\BAKED POTATO ICON.png'
    dry = Recipe('', 'SCREENS\\FOOD\\BAKED POTATO\\RECIPES\\THE DRY POTATO_CROP.png')
    plain = Recipe('b', 'SCREENS\\FOOD\\BAKED POTATO\\RECIPES\\PLAIN POTATO_CROP.png')
    litenCheesy = Recipe('cs', 'SCREENS\\FOOD\\BAKED POTATO\\RECIPES\\LITE N CHEESY POTATO_CROP.png')
    chivesAndBacon = Recipe('yhb', 'SCREENS\\FOOD\\BAKED POTATO\\RECIPES\\CHIVES AND BACON POTATO_CROP.png')
    lite = Recipe('sho', 'SCREENS\\FOOD\\BAKED POTATO\\RECIPES\\LITE POTATO_CROP.png')
    classicBaked = Recipe('csy', 'SCREENS\\FOOD\\BAKED POTATO\\RECIPES\\CLASSIC BAKED POTATO_CROP.png')
    classicwBacon = Recipe('csyb', 'SCREENS\\FOOD\\BAKED POTATO\\RECIPES\\CLASSIC POTATO W BACON_CROP.png')
    sour = Recipe('so', 'SCREENS\\FOOD\\BAKED POTATO\\RECIPES\\SOUR POTATO_CROP.png')
    sourwBacon = Recipe('sbo', 'SCREENS\\FOOD\\BAKED POTATO\\RECIPES\\SOUR POTATO W BACON_CROP.png')
    deluxe = Recipe('csyhbo', 'SCREENS\\FOOD\\BAKED POTATO\\RECIPES\\DELUXE POTATO_CROP.png')

    @staticmethod
    def make(recipe):
        pyautogui.typewrite(recipe.com)
        pyautogui.press('enter')


class Beer:
    icon = 'SCREENS\\FOOD\\BEER\\BEER ICON.png'
    @staticmethod
    def make():
        pyautogui.keyDown('down')
        time.sleep(2)
        pyautogui.keyUp('down')
        pyautogui.press('enter')


class CornDog:
    icon = 'SCREENS\\FOOD\\CORN DOG\\CORN DOG ICON.png'
    classic = Recipe('km', 'SCREENS\\FOOD\\CORN DOG\\RECIPES\\CLASSIC CORN DOG_CROP.png')
    red = Recipe('k', 'SCREENS\\FOOD\\CORN DOG\\RECIPES\\THE RED DOG_CROP.png')
    yellow = Recipe('m', 'SCREENS\\FOOD\\CORN DOG\\RECIPES\\THE YELLOW DOG_CROP.png')

    @staticmethod
    def make(recipe):
        pyautogui.typewrite(recipe.com)
        pyautogui.press('enter')


class FriedChicken:
    icon = 'SCREENS\\FOOD\\FRIED CHICKEN\\FRIED CHICKEN ICON.png'
    @staticmethod
    def make():
        pyautogui.keyDown('down')
        time.sleep(2)
        pyautogui.keyUp('down')
        pyautogui.press('p')
        pyautogui.press('enter')


class IceCream:
    icon = 'SCREENS\\FOOD\\ICE CREAM\\ICE CREAM ICON.png'
    cherryVanilla = Recipe('vvh', 'SCREENS\\FOOD\\ICE CREAM\\RECIPES\\CHERRY VANILLA_CROP.png')
    chocolateSprinkles = Recipe('ccp', 'SCREENS\\FOOD\\ICE CREAM\\RECIPES\\CHOCOLATE SPRINKLES_CROP.png')
    plainChocolate = Recipe('ccc', 'SCREENS\\FOOD\\ICE CREAM\\RECIPES\\PLAIN CHOCOLATE_CROP.png')
    plainVanilla = Recipe('vvv', 'SCREENS\\FOOD\\ICE CREAM\\RECIPES\\PLAIN VANILLA_CROP.png')
    yinAndYang = Recipe('vchp', 'SCREENS\\FOOD\\ICE CREAM\\RECIPES\\THE YIN AND YANG_CROP.png')
    vanillaAndChocolate = Recipe('vc', 'SCREENS\\FOOD\\ICE CREAM\\RECIPES\\VANILLA AND CHOCOLATE_CROP.png')

    @staticmethod
    def make(recipe):
        pyautogui.typewrite(recipe.com)
        pyautogui.press('enter')


class Lasagna:
    icon = 'SCREENS\\FOOD\\LASAGNA\\LASAGNA ICON.png'
    classicItalian = Recipe('pscrpscrpscr', 'SCREENS\\FOOD\\LASAGNA\\RECIPES\\CLASSIC ITALIAN LASAGNA_CROP.png')

    @staticmethod
    def make(recipe):
        pyautogui.typewrite(recipe.com)
        pyautogui.press('enter')


class Pasta:
    icon = 'SCREENS\\FOOD\\PASTA\\PASTA ICON.png'
    cheese = Recipe('c', 'SCREENS\\FOOD\\PASTA\\RECIPES\\CHEESE PASTA_CROP.png')
    cheesyChicken = Recipe('ckb', 'SCREENS\\FOOD\\PASTA\\RECIPES\\CHEESY CHICKEN PASTA_CROP.png')
    cheesyDeluxe = Recipe('cmkbpuso', 'SCREENS\\FOOD\\PASTA\\RECIPES\\CHEESY DELUXE PASTA_CROP.png')
    cheesyMeaty = Recipe('cmkb', 'SCREENS\\FOOD\\PASTA\\RECIPES\\CHEESY MEATY PASTA_CROP.png')
    cheesyOnion = Recipe('co', 'SCREENS\\FOOD\\PASTA\\RECIPES\\CHEESY ONION PASTA_CROP.png')
    cheesyVeggie = Recipe('cpuso', 'SCREENS\\FOOD\\PASTA\\RECIPES\\CHEESY VEGGIE PASTA_CROP.png')
    spaghetti = Recipe('rm', 'SCREENS\\FOOD\\PASTA\\RECIPES\\CLASSIC SPAGHETTI_CROP.png')
    hotBacon = Recipe('rbp', 'SCREENS\\FOOD\\PASTA\\RECIPES\\HOT BACON PASTA_CROP.png')
    redDeluxe = Recipe('rmkbpuso', 'SCREENS\\FOOD\\PASTA\\RECIPES\\RED DELUXE PASTA_CROP.png')
    redVeggie = Recipe('rpuso', 'SCREENS\\FOOD\\PASTA\\RECIPES\\RED VEGGIE PASTA_CROP.png')
    spaghettiDeluxe = Recipe('rmbus', 'SCREENS\\FOOD\\PASTA\\RECIPES\\SPAGHETTI DELUXE_CROP.png')
    theMeaty = Recipe('rmkb', 'SCREENS\\FOOD\\PASTA\\RECIPES\\THE MEATY PASTA_CROP.png')

    @staticmethod
    def make(recipe):
        pyautogui.typewrite(recipe.com)
        pyautogui.press('enter')


class Pretzel:
    icon = 'SCREENS\\FOOD\\PRETZEL\\PRETZEL ICON.png'
    cinnamon = Recipe('c', 'SCREENS\\FOOD\\PRETZEL\\RECIPES\\CINNAMON PRETZEL_CROP.png')
    butteryCurves = Recipe('b', 'SCREENS\\FOOD\\PRETZEL\\RECIPES\\THE BUTTERY CURVES_CROP.png')
    classic = Recipe('sb', 'SCREENS\\FOOD\\PRETZEL\\RECIPES\\THE CLASSIC PRETZEL_CROP.png')
    dryTwister = Recipe('', 'SCREENS\\FOOD\\PRETZEL\\RECIPES\\THE DRY TWISTER_CROP.png')
    saltyKnot = Recipe('s', 'SCREENS\\FOOD\\PRETZEL\\RECIPES\\THE SALTY KNOT_CROP.png')
    sweetTwist = Recipe('bc', 'SCREENS\\FOOD\\PRETZEL\\RECIPES\\THE SWEET TWIST_CROP.png')

    @staticmethod
    def make(recipe):
        pyautogui.typewrite(recipe.com)
        pyautogui.press('enter')


class Salad:
    icon = 'SCREENS\\FOOD\\SALAD\\SALAD ICON.png'
    cheesyLeaves = Recipe('rc', 'SCREENS\\FOOD\\SALAD\\RECIPES\\CHEESY LEAVES_CROP.png')
    cheesyPeppers = Recipe('co', 'SCREENS\\FOOD\\SALAD\\RECIPES\\CHEESY PEPPERS_CROP.png')
    house = Recipe('rcb', 'SCREENS\\FOOD\\SALAD\\RECIPES\\HOUSE SALAD_CROP.png')
    kidsDelight = Recipe('rc', 'SCREENS\\FOOD\\SALAD\\RECIPES\\KIDS DELIGHT_CROP.png')
    pepperRanch = Recipe('rco', 'SCREENS\\FOOD\\SALAD\\RECIPES\\PEPPER RANCH_CROP.png')
    saladVerde = Recipe('rg', 'SCREENS\\FOOD\\SALAD\\RECIPES\\SALAD VERDE_CROP.png')
    bigSalad = Recipe('cg', 'SCREENS\\FOOD\\SALAD\\RECIPES\\BIG SALAD_CROP.png')
    dryDeluxe = Recipe('mg', 'SCREENS\\FOOD\\SALAD\\RECIPES\\DRY DELUXE_CROP.png')
    dryGreens = Recipe('g', 'SCREENS\\FOOD\\SALAD\\RECIPES\\DRY GREENS_CROP.png')
    manhattan = Recipe('rcbomg', 'SCREENS\\FOOD\\SALAD\\RECIPES\\THE MANHATTAN_CROP.png')
    mix = Recipe('rcbo', 'SCREENS\\FOOD\\SALAD\\RECIPES\\THE MIX_CROP.png')
    tomatoRanch = Recipe('rcm', 'SCREENS\\FOOD\\SALAD\\RECIPES\\TOMATO RANCH_CROP.png')

    @staticmethod
    def make(recipe):
        pyautogui.typewrite(recipe.com)
        pyautogui.press('enter')


class Soda:
    icon = 'SCREENS\\FOOD\\SODA\\SODA ICON.png'
    largeColaNoIce = Recipe('lcn', 'SCREENS\\FOOD\\SODA\\RECIPES\\LARGE COLA NO ICE_CROP.png')
    largeCola = Recipe('lci', 'SCREENS\\FOOD\\SODA\\RECIPES\\LARGE COLA_CROP.png')
    largeDiet = Recipe('ldi', 'SCREENS\\FOOD\\SODA\\RECIPES\\LARGE DIET_CROP.png')
    largeGrape = Recipe('lgi', 'SCREENS\\FOOD\\SODA\\RECIPES\\LARGE GRAPE_CROP.png')
    largeTea = Recipe('lti', 'SCREENS\\FOOD\\SODA\\RECIPES\\LARGE TEA_CROP.png')
    largeWater = Recipe('lwi', 'SCREENS\\FOOD\\SODA\\RECIPES\\LARGE WATER_CROP.png')
    mediumColaNoIce = Recipe('mcn', 'SCREENS\\FOOD\\SODA\\RECIPES\\MEDIUM COLA NO ICE_CROP.png')
    mediumCola = Recipe('mci', 'SCREENS\\FOOD\\SODA\\RECIPES\\MEDIUM COLA_CROP.png')
    mediumDiet = Recipe('mdi', 'SCREENS\\FOOD\\SODA\\RECIPES\\MEDIUM DIET_CROP.png')
    mediumGrape = Recipe('mgi', 'SCREENS\\FOOD\\SODA\\RECIPES\\MEDIUM GRAPE_CROP.png')
    mediumTea = Recipe('mti', 'SCREENS\\FOOD\\SODA\\RECIPES\\MEDIUM TEA_CROP.png')
    mediumWater = Recipe('mwi', 'SCREENS\\FOOD\\SODA\\RECIPES\\MEDIUM WATER_CROP.png')
    smallColaNoIce = Recipe('scn', 'SCREENS\\FOOD\\SODA\\RECIPES\\SMALL COLA NO ICE_CROP.png')
    smallCola = Recipe('sci', 'SCREENS\\FOOD\\SODA\\RECIPES\\SMALL COLA_CROP.png')
    smallDiet = Recipe('sdi', 'SCREENS\\FOOD\\SODA\\RECIPES\\SMALL DIET_CROP.png')
    smallGrape = Recipe('sgi', 'SCREENS\\FOOD\\SODA\\RECIPES\\SMALL GRAPE_CROP.png')
    smallTea = Recipe('sti', 'SCREENS\\FOOD\\SODA\\RECIPES\\SMALL TEA_CROP.png')
    smallWater = Recipe('swi', 'SCREENS\\FOOD\\SODA\\RECIPES\\SMALL WATER_CROP.png')

    @staticmethod
    def make(recipe):
        if recipe.com[0] == 'm':
            pyautogui.press('up')
        elif recipe.com[0] == 'l':
            pyautogui.press('up')
            pyautogui.press('up')
        if recipe.com[1] == 't':
            pyautogui.press('right')
        elif recipe.com[1] == 'g':
            pyautogui.press('right')
            pyautogui.press('right')
        elif recipe.com[1] == 'w':
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
        elif recipe.com[1] == 'd':
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
        if recipe.com[2] == 'i':
            pyautogui.press('i')
        pyautogui.press('down')
        pyautogui.press('enter')


class Sopapillas:
    icon = 'SCREENS\\FOOD\\SOPAPILLAS\\SOPAPILLAS ICON.png'
    deliciousLite = Recipe('n', 'SCREENS\\FOOD\\SOPAPILLAS\\RECIPES\\DELICIOUS LITE SOPAPILLAS_CROP.png')
    delicious = Recipe('s', 'SCREENS\\FOOD\\SOPAPILLAS\\RECIPES\\DELICIOUS SOPAPILLAS_CROP.png')

    @staticmethod
    def make(recipe):
        pyautogui.keyDown('down')
        time.sleep(2)
        pyautogui.keyUp('down')
        pyautogui.press('p')
        if recipe.com == 's':
            pyautogui.press(recipe.com)
        pyautogui.press('enter')