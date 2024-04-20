import pyautogui
from PIL import ImageGrab


def detect_objetcs(i):
    whole_screen = ImageGrab.grab(bbox=(0, 350, 1700, 850))
    whole_screen.save(f"screenshots/game_image{i}.jpg")
    whole_screen.close()


pyautogui.click()         
pyautogui.press("space")         