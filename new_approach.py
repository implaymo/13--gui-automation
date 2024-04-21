import pyautogui 
from PIL import ImageGrab
import time

light_theme = False
dark_theme = False



def screenshot(): 
    image = ImageGrab.grab().convert('L')
    image.save("game_image.jpg")
    image_data = image.load()
    check_background_theme(image_data)
    detect_object(image_data)
    
def check_background_theme(image_data):
    x = 0 
    y = 0  
    color = image_data[x, y]
    if color < 50:
        dark_theme = True
        return dark_theme
    else:
        light_theme = True
        return light_theme
    
def detect_object(image_data):
    if dark_theme: 
        for x in range(200, 500):
            for y in range(500, 800): 
                object_color = image_data[x, y]               
                if object_color > 170:
                    print(f"WHITE OBJECT {object_color}") 
                    pyautogui.keyDown('up')
    else:
        for x in range(200, 500):
            for y in range(300, 670):         
                object_color = image_data[x, y]
                if object_color < 70:                   
                    print(f"BLACK OBJECT {object_color}")  
                    pyautogui.keyDown('up')
     
pyautogui.hotkey('win', 'down')
pyautogui.click()             
pyautogui.press("space")
time.sleep(2)

game_on = True
while game_on:
    screenshot()
                                   