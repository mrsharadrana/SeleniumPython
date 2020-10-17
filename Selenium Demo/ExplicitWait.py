from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://app.hubspot.com/')
print(driver.title)
driver.maximize_window()

wait = WebDriverWait(driver, 10)
#text_userName = wait.until(ec.presence_of_element_located((By.ID, 'username')))
text_userName = wait.until(ec.element_to_be_clickable((By.ID, 'username')))
text_userName.send_keys("test@gmail.com")
text_passWord = wait.until(ec.presence_of_element_located((By.ID, 'password')))
text_passWord.send_keys("Sharad@1994")
button_login = wait.until(ec.element_to_be_clickable((By.ID, 'loginBtn')))
button_login.click()
