#login page automation
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window
url = "https://www.saucedemo.com/"
driver.get(url)
time.sleep(2)

'''
ID locators
username = user-name
 password = password
 loginbutton = login-button

 Xpath Locators
 username = 
 relative xpath:
 //*[@id="user-name"]
 Absolute xpath:
/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input


 password= 
 //*[@id="password"]
 /html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input

 loginbutton = 
//*[@id="login-button"]
/html/body/div/div/div[2]/div[1]/div/div/form/input
'''
#to find elements / Locators
# username = driver.find_element(By.ID, "user-name")
username = driver.find_element(By.XPATH, "//*[@id='user-name']")
# password = driver.find_element(By.ID, "password")
password = driver.find_element(By.XPATH, "//*[@id='password']")
# login_button = driver.find_element(By.ID, "login-button")
login_button = driver.find_element(By.XPATH, "//*[@id='login-button']")





#action
username.send_keys("standard_user")
time.sleep(2)

password.send_keys("secret_sauce")
time.sleep(2)

login_button.click()
time.sleep(2)

if driver.current_url == "https://www.saucedemo.com/inventory.html":
    print(f"login sucessfull")

else: 
    print(f"Login failed")



time.sleep(2)






driver.quit()