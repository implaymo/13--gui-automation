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
    image = ImageGrab.grab().convert('L')
    image_data = image.load()
    check_background_theme(image_data)
    detect_object(image_data)
    
def check_background_theme(image_data):
    x = 0 
    y = 300  
    color = image_data[x, y]
    if color < 200:
        change_to_dark_theme()
    else:
        change_to_light_theme()
              
def detect_object(image_data):
    if dark_theme:
        for x in range(340, 380):
                for y in range(800, 830):  
                    object_color = image_data[x, y]               
                    if object_color > 200:
                        pyautogui.press("space")
                        return
    if light_theme:
        for x in range(340, 380):
                for y in range(800, 830):          
                    object_color = image_data[x, y]        
                    if object_color < 200:                   
                        pyautogui.press("space")
                        return
     
pyautogui.hotkey('win', 'down')
pyautogui.click()             
pyautogui.press("space")
time.sleep(2)

game_on = True
while game_on:
    screenshot()
                                   