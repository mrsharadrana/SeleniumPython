from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.spicejet.com/')
print(driver.title)
driver.maximize_window()
driver.implicitly_wait(5)

link_loginSignUp = driver.find_element_by_id('ctl00_HyperLinkLogin')
link_spiceClubMember = driver.find_element_by_xpath("//*[text()='SpiceClub Members']")
link_signUp = driver.find_element_by_xpath("//*[text()='Sign up']")
actController = ActionChains(driver)
actController.move_to_element(link_loginSignUp).perform()
time.sleep(2)
actController.move_to_element(link_spiceClubMember).perform()
link_signUp.click()