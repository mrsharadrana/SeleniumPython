from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="F:\\Python\\Selenium\\Library\\chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
print(driver.title)
# Single Input Field

txtMsg = driver.find_element_by_xpath("//input[@id='user-message']")
print(txtMsg.text)
txtMsg.clear()
msg = "Hello this is my message"
txtMsg.send_keys(msg)
time.sleep(3)
popup = driver.find_element_by_xpath("//a[@title='Close']")
popup.click()
btnShowMsg = driver.find_element_by_xpath("//form[@id='get-input']/button")
btnShowMsg.click()
time.sleep(1)
lblMsg = driver.find_element_by_xpath("//*[@id='display']")
print(lblMsg.text)
# Two Input Fields

txtsum1 = driver.find_element_by_id("sum1")
if txtsum1.is_enabled():
    txtsum1.send_keys(10)
else:
    driver.implicitly_wait(5)
    txtsum1.send_keys(10)
txtsum2 = driver.find_element_by_id("sum2")
if txtsum2.is_enabled():
    txtsum2.send_keys(20)
else:
    driver.implicitly_wait(5)
    txtsum2.send_keys(20)
btnGetTotal = driver.find_element_by_xpath("//*[@id='gettotal']/button")
if btnGetTotal.is_enabled():
    btnGetTotal.click()
else:
    print("Unable to Click")
lblDisplayValue = driver.find_element_by_xpath("//*[@id='displayvalue']")
if lblDisplayValue.is_displayed():
    print(lblDisplayValue.text)
else:
    driver.implicitly_wait(3)
    print(lblDisplayValue.text)
driver.quit()
