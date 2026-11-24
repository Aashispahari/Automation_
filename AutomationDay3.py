from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.saucedemo.com/"
driver.get(url)
driver.implicitly_wait(20)
wait = WebDriverWait(driver,10)




# usernmae= driver.find_element(By.ID, "user-name")
# password= driver.find_element(By.ID, "password")

username = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
password = wait.until(EC.visibility_of_element_located((By.ID, "password")))

login_button =wait.until(EC.element_to_be_clickable((By.ID, "login-button")))

time.sleep(2)
# login_button= driver.find_element(By.ID, "login-button")



username.send_keys("standard_user")
password.send_keys("secret_sauce")

action =ActionChains(driver)
action.click(login_button).perform()
# login_button.click()
time.sleep(2)

# alert = driver.switch_to.alert
# alert.dismiss()

#dropdown 
# dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@aria-label='Sort products']")))

# #object created of class afer varibale:to pass varibale
# select = Select(dropdown)
# select.select_by_visible_text("Price (low to high)")
# time.sleep(2)

menu = driver.find_element(By.ID, "react-burger-menu-btn")
logout = driver.find_element(By.ID, "logout_sidebar_link")

# menu = wait.until(EC.element_to_be_clickable(By.ID,"react-burger-menu-btn"))
# logout = wait.until(EC.element_to_be_clickable(By.ID,"logout_sidebar_link"))

action.click(menu).perform()
time.sleep(2)
action.click(logout).perform()
time.sleep(2)


driver.quit()
