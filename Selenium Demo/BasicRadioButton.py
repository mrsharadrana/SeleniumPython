from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="F:\\Python\\Selenium\\Library\\chromedriver.exe")
driver.implicitly_wait(2)
driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")
driver.maximize_window()
print(driver.title)
radioGender = driver.find_elements_by_xpath("//input[@name='optradio']")
btnCheckedValue = driver.find_element_by_xpath("//button[@id='buttoncheck']")
lblMsg = driver.find_element_by_xpath("(//button[@id='buttoncheck' ]//following :: p)[1]")
for x in radioGender:
    # print(x.get_attribute("value"))
    if x.get_attribute("value") == "Female":
        x.click()
btnCheckedValue.click()
print(lblMsg.text)

time.sleep(5)

radioGender = driver.find_elements_by_xpath("//input[@name='gender']")
radioAge = driver.find_elements_by_xpath("//input[@name='ageGroup']")
btnGetValues = driver.find_element_by_xpath("//*[text()='Get values']")
lblMsg = driver.find_element_by_xpath("//p[@class='groupradiobutton']")
for x in radioGender:
    # print(x.get_attribute("value"))
    if x.get_attribute("value") == 'Male':
        x.click()
for x in radioAge:
    # print(x.get_attribute("value"))
    if x.get_attribute("value") == "5 - 15":
        x.click()
btnGetValues.click()

print(lblMsg.text)
time.sleep(10)
driver.quit()
