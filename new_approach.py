import pyautogui 
from PIL import ImageGrab
import time

count = 0
light_theme = False
dark_theme = False
x_min_cac = 300                        
x_max_cac = 320
y_min_cac = 790
y_max_cac = 800

x_min_bird = 450                          
x_max_bird = 520
y_min_bird = 730
y_max_bird = 735  
 
sleep_time = time.sleep(0)
objects_color_light = 85
objects_color_dark = 84      

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
    x = 1780
    y = 400  
    color = image_data[x, y]
    if color < 160:
        change_to_dark_theme()
    else:
        change_to_light_theme()
        
def change_jump_timing():
    global count, x_min_cac, x_max_cac
    if count > 30:
        x_min_cac = 360
        x_max_cac = 410        
    elif count > 45:
        x_min_cac = 800
        x_max_cac = 930
    elif count > 70:
        x_min_cac = 1100
        x_max_cac = 1250            
    return x_min_cac, x_max_cac
              
def detect_object_cactus(image_data):
    global count
    change_jump_timing()
    if dark_theme:
        for x in range(x_min_cac, x_max_cac):
            for y in range(y_min_cac, y_max_cac):  
                object_color = image_data[x, y]
                if object_color > objects_color_light:
                    pyautogui.press("space")
                    count += 1
                    print(count)
                    return
    elif light_theme:
        for x in range(x_min_cac, x_max_cac):
            for y in range(y_min_cac, y_max_cac):  
                object_color = image_data[x, y]
                if object_color < objects_color_dark:
                    pyautogui.press("space")
                    count += 1
                    print(count)
                    return
                    
def detect_object_birds(image_data):
    global count
    change_jump_timing()
    if dark_theme:
         for x in range(x_min_bird, x_max_bird):
            for y in range(y_min_bird, y_max_bird):           
                object_color = image_data[x, y]               
                if object_color > objects_color_light:
                    pyautogui.press("space")
                    count += 1
                    return
    elif light_theme:
        for x in range(x_min_bird, x_max_bird):              
            for y in range(y_min_bird, y_max_bird):           
                object_color = image_data[x, y]        
                if object_color < objects_color_dark:                   
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
                                   