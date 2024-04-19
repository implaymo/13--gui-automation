from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://elgoog.im/dinosaur-game/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
