import pyautogui 
from PIL import ImageGrab
import time

count = 0
light_theme = False
dark_theme = False
x_min_cac = 300                        
x_max_cac = 320
y_min_cac = 720
y_max_cac = 735

x_min_bird = 450                          
x_max_bird = 520
y_min_bird = 620
y_max_bird = 622  
 
white_object = 120
black_object = 90      

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
    x = 100
    y = 300  
    color = image_data[x, y]
    if color < 230:
        change_to_dark_theme()
    else:
        change_to_light_theme()
        
def change_jump_timing():
    global count, x_min_cac, x_max_cac
    if count > 20:
        x_min_cac = 500
        x_max_cac = 510        
    elif count > 30:
        x_min_cac = 900
        x_max_cac = 910
    elif count > 40:  
        x_min_cac = 1050
        x_max_cac = 1060 
    elif count > 60:
        x_min_cac = 1250
        x_max_cac = 1260                    
    return x_min_cac, x_max_cac
              
def detect_object_cactus(image_data):
    global count
    change_jump_timing()
    if dark_theme:
        for x in range(x_min_cac, x_max_cac):
            for y in range(y_min_cac, y_max_cac):  
                object_color = image_data[x, y]
                if object_color > white_object:
                    pyautogui.press("space")
                    count += 1
                    return
    elif light_theme:
        for x in range(x_min_cac, x_max_cac):
            for y in range(y_min_cac, y_max_cac):  
                object_color = image_data[x, y]
                if object_color < black_object:
                    pyautogui.press("space")
                    count += 1
                    print(count)
                    return
                    
def detect_object_birds(image_data):
    global count
    if dark_theme:
         for x in range(x_min_bird, x_max_bird):
            for y in range(y_min_bird, y_max_bird):           
                object_color = image_data[x, y]               
                if object_color > white_object:
                    pyautogui.press("space")
                    count += 1
                    return
    elif light_theme:
        for x in range(x_min_bird, x_max_bird):              
            for y in range(y_min_bird, y_max_bird):           
                object_color = image_data[x, y]        
                if object_color < black_object:                   
                    pyautogui.press("space")
                    count += 1
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
                                   