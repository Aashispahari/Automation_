from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



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



username.send_keys("Standard_user")
password.send_keys("secret_sauce")
login_button.click()

driver.quit()
