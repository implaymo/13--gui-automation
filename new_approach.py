import pyautogui 
from PIL import ImageGrab
import time

light_theme = False
dark_theme = False

def change_to_dark_theme():
    global light_theme, dark_theme
    light_theme = False
    dark_theme = True
    return dark_theme, light_theme

def change_to_light_theme():
    global light_theme, dark_theme
    dark_theme = False
    light_theme = True
    return dark_theme, light_theme

def screenshot(): 
    image = ImageGrab.grab(bbox=(200, 600, 900, 870)).convert('L')
    image.save("game_image.jpg")
    image_data = image.load()
    check_background_theme(image_data)
    detect_object(image_data)
    
def check_background_theme(image_data):
    x = 0 
    y = 0  
    color = image_data[x, y]
    if color < 50:
        change_to_dark_theme()
        return dark_theme
    else:
        change_to_light_theme()
        return light_theme
    
    
def detect_object(image_data):
    if dark_theme:
        for x in range(250, 700):
            for y in range(100, 265): 
                object_color = image_data[x, y]               
                if object_color > 170:
                    print("DARK THEME")
                    print(x, y)
                    print(object_color) 
                    pyautogui.press("space")
    if light_theme:
        for x in range(250, 700):
            for y in range(100, 265):      
                object_color = image_data[x, y]        
                if object_color < 70:
                    print("LIGHT THEME")
                    print(x, y)
                    print(object_color)   
                    pyautogui.press("space")
  
pyautogui.hotkey('win', 'down')
pyautogui.click()         
pyautogui.press("space")
time.sleep(2)

game_on = True
while game_on:
    screenshot()
    