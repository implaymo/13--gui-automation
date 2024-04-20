import pyautogui 
from PIL import ImageGrab
import time


def detect_objetcs(i): 
    whole_screen = ImageGrab.grab(bbox=(150, 530, 1700, 900))
    whole_screen.save(f"screenshots/game_image{i}.jpg")
    whole_screen.close()

pyautogui.hotkey('win', 'down')
pyautogui.click()         
pyautogui.press("space")
time.sleep(2)
for i in range(10):
    detect_objetcs(i)          