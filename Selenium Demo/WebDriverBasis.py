from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="F:\\Python\\Selenium\\Library\\chromedriver.exe")
driver.get("http://www.google.com")
print(driver.title)
driver.find_element(By.NAME, 'q') .send_keys('Testing')
list = driver.find_elements_by_css_selector('ul.erkvQe li')

for searchResult in list:
    print(searchResult.text)
    if searchResult.text == 'testing tools':
        searchResult.click()
        break

time.sleep(5)
driver.close()
driver.quit()