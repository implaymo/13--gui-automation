import pyautogui 
from PIL import ImageGrab, Image
import os
import time

light_theme = False
dark_theme = False


screenshots_folder_path = "./screenshots"
bird_to_tuck_y_position = 570
other_obstacales_y_position = 630

def screenshot(i): 
    image = ImageGrab.grab(bbox=(150, 530, 900, 900)).convert('L')
    image.save(f"screenshots/game_image{i}.jpg")
    image_data = image.load()
    get_background_color(image_data)

def get_background_color(image_data):
    x = 0 
    y = 0  
    color = image_data[x, y]
    print(color)
    if color < 50:
        dark_theme = True
        print("DARK THEME")
    else:
        light_theme = True
        print("LIGHT THEME")

pyautogui.hotkey('win', 'down')
pyautogui.click()         
pyautogui.press("space")
time.sleep(2)
for i in range(10):
    time.sleep(1)
    screenshot(i)  
    