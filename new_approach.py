import pyautogui 
from PIL import ImageGrab
import time

light_theme = False
dark_theme = False
x_min = 360                          
x_max = 400
y_min_cac = 800
y_max_cac = 830
y_min_bird = 750
y_max_bird = 780          

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
    
def check_background_theme(image_data):
    x = 0 
    y = 300  
    color = image_data[x, y]
    if color < 150:
        change_to_dark_theme()
    else:
        change_to_light_theme()
              
def detect_object_cactus(image_data):
    if dark_theme:
        for x in range(x_min, x_max):
            for y in range(y_min_cac, y_max_cac):  
                object_color = image_data[x, y]
                if object_color > 100:
                    pyautogui.press("space")
                    return
    elif light_theme:
        for x in range(x_min, x_max):
            for y in range(y_min_cac, y_max_cac):  
                object_color = image_data[x, y]
                if object_color < 99:
                    pyautogui.press("space")
                    return
                    
def detect_object_birds(image_data):
    if dark_theme:
         for x in range(x_min, x_max):
            for y in range(y_min_bird, y_max_bird):           
                object_color = image_data[x, y]               
                if object_color > 100:
                    pyautogui.press("space")
                    return
    elif light_theme:
        for x in range(x_min, x_max):              
            for y in range(y_min_bird, y_max_bird):           
                object_color = image_data[x, y]        
                if object_color < 99:                   
                    pyautogui.press("space")
                    return                        

def screenshot(): 
    image = ImageGrab.grab().convert('L')
    image_data = image.load()
    check_background_theme(image_data)
    detect_object_cactus(image_data)
    detect_object_birds(image_data)
    
             
pyautogui.hotkey('win', 'down')
pyautogui.click()             
pyautogui.press("space")
time.sleep(2)

game_on = True
while game_on:
    screenshot()
                                   