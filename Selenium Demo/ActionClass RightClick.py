from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
print(driver.title)
driver.maximize_window()
driver.implicitly_wait(5)

button_rightClickMe = driver.find_element_by_xpath("//span[text()='right click me']")
controller = ActionChains(driver)
controller.context_click(button_rightClickMe).perform()
right_click_options = driver.find_elements(By.XPATH, "//div[@id='context-menu-layer']//following :: ul/li")
for x in right_click_options:
    print(x.text)
    if x.text == 'Delete':
        x.click()
        break
time.sleep(5)
alert = Alert(driver)
print(alert.text)
alert.accept()