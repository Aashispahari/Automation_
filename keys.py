from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
action = ActionChains(driver)
url = "https://formy-project.herokuapp.com/scroll"
driver.get(url)
driver.maximize_window()
# content = driver.find_element(By.TAG_NAME,"body")
# content.send_keys(Keys.END)
# time.sleep(2)
username = driver.find_element(By.ID, "name")
username.send_keys("Aashish")
time.sleep(2)

#selects all
action.key_down(Keys.CONTROL).perform()
action.send_keys("a")
action.key_up(Keys.CONTROL).perform()

#copys content
action.key_down(Keys.CONTROL).perform()
action.send_keys("c")
action.key_up(Keys.CONTROL).perform()

#changes to another field
action.send_keys(Keys.TAB)

#pastes content
action.key_down(Keys.CONTROL).perform()
action.send_keys("v")
action.key_up(Keys.CONTROL).perform()


time.sleep(3)

driver.quit()
