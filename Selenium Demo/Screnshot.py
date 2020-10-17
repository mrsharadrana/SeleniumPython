from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
#Run in Headless
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://msncom/')
time.sleep(5)
#Used for current visible screen
#driver.get_screenshot_as_file('test.png')

# for Full page Screenshot we need to used javascript and run in headless mode
S= lambda X: driver.execute_script('return document.body.parentNode.scroll' +X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name('body').screenshot('test.png')
