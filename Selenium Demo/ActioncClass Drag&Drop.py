from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://jqueryui.com/droppable/')
print(driver.title)
driver.maximize_window()
iframe_demo = driver.find_element_by_xpath("//*[@id='content']/iframe")
driver.switch_to.frame(iframe_demo)
image_source = driver.find_element_by_id('draggable')
textarea_target= driver.find_element_by_id('droppable')
controller = ActionChains(driver)
#controller.drag_and_drop(image_source, textarea_target).perform()
controller.click_and_hold(image_source).move_to_element(textarea_target).perform()
time.sleep(5)
driver.close()
