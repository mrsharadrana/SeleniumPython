from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="F:\\Python\\Selenium\\Library\\chromedriver.exe")
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
print("Title is :- " + driver.title)
chkbox = driver.find_element_by_id("isAgeSelected")
lblsucces = driver.find_element_by_id("txtAge")
if chkbox.is_selected():
    print("Already Selected")
else:
    chkbox.click()
    print(lblsucces.text)
time.sleep(5)

btnChckAll = driver.find_element_by_id("check1")
chkboxoption = driver.find_elements_by_class_name("cb1-element")
if btnChckAll.is_displayed():
    btnChckAll.click()
    print(btnChckAll.get_attribute("value"))
else:
    print("Button not displayed")
print(len(chkboxoption))
chkboxoption[1].click()
chkboxoption[2].click()
print(btnChckAll.get_attribute("value"))
assert btnChckAll.get_attribute("value") == "Check All", "Value Mismatched"
time.sleep(5)
driver.close()
