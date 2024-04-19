from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://elgoog.im/dinosaur-game/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)


accept_cookies = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')))

accept_cookies.click()

start_game = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-frame-error"]/div[6]/canvas')))

start_game.send_keys(Keys.SPACE).perform()