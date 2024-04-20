from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import ImageGrab
import time

def detect_objetcs(i):
    whole_screen = ImageGrab.grab(bbox=(0, 350, 1700, 850))
    whole_screen.save(f"screenshots/game_image{i}.jpg")
    whole_screen.close()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://elgoog.im/dinosaur-game/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)


accept_cookies = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')))

accept_cookies.click()

start_game = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "body")))

start_game.send_keys(Keys.SPACE)

time.sleep(2)
for i in range(60):
    detect_objetcs(i)


    