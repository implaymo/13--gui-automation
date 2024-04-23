import pyautogui 
from PIL import ImageGrab
import time

count = 0
light_theme = False
dark_theme = False
x_min_cac = 310                        
x_max_cac = 400
y_min_cac = 780
y_max_cac = 810

x_min_bird = 420                          
x_max_bird = 500
y_min_bird = 730
y_max_bird = 735  
 
sleep_time = time.sleep(0)
color_to_jump_dark = 90
color_to_jump_light = 84      

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
    y = 600  
    color = image_data[x, y]
    if color <= 90:
        change_to_dark_theme()
    else:
        change_to_light_theme()
        
def change_jump_timing_cactus():
    global count, x_min_cac, x_max_cac
    if count > 7:
        x_min_cac = 370                        
        x_max_cac = 450
    elif count > 50:
        x_min_cac = 430
        x_max_cac = 550              
    return x_min_cac, x_max_cac
              
def detect_object_cactus(image_data):
    global count
    change_jump_timing_cactus()
    if dark_theme:
        for x in range(x_min_cac, x_max_cac):
            for y in range(y_min_cac, y_max_cac):  
                object_color = image_data[x, y]
                if object_color > color_to_jump_dark:
                    pyautogui.press("space")
                    return
    elif light_theme:
        for x in range(x_min_cac, x_max_cac):
            for y in range(y_min_cac, y_max_cac):  
                object_color = image_data[x, y]
                if object_color < color_to_jump_light:
                    pyautogui.press("space")
                    count += 1
                    return
                    
def detect_object_birds(image_data):
    global count
    change_jump_timing_cactus()
    if dark_theme:
         for x in range(x_min_bird, x_max_bird):
            for y in range(y_min_bird, y_max_bird):           
                object_color = image_data[x, y]               
                if object_color > color_to_jump_dark:
                    pyautogui.press("space")
                    count += 1
                    return
    elif light_theme:
        for x in range(x_min_bird, x_max_bird):              
            for y in range(y_min_bird, y_max_bird):           
                object_color = image_data[x, y]        
                if object_color < color_to_jump_light:                   
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
                                   