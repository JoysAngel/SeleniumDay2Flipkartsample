from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

product = input("enter the product to be searched")
driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test started")
driver.maximize_window()
driver.get("https://www.flipkart.com/")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
time.sleep(1)
driver.find_element_by_name("q").send_keys(product)
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click()
time.sleep(5)
driver.close()
print("Testcase completed")

