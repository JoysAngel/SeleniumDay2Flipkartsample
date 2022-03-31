from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

username = input("Enter the username :")
password = input("Enter the password :")

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test started")
driver.maximize_window()
driver.get("https://www.instagram.com/")
time.sleep(5)
driver.find_element_by_name("username").send_keys(username)
time.sleep(2)
driver.find_element_by_name("password").send_keys(password)
time.sleep(2)
driver.find_element_by_class_name("sqdOP").send_keys(Keys.ENTER)
time.sleep(5)
driver.close()
print("Test completed")
