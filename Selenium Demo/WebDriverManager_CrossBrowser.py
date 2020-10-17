from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.common.by import By
import time

browserName = "firefox"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "IE":
    driver = webdriver.Ie(IEDriverManager().install())
else:
    print('Selected Browser na '+browserName)
    raise Exception('Driver not found')
driver.maximize_window()
driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")

print(driver.title)
time.sleep(5)
driver.quit()