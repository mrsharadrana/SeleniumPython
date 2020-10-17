from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

browserName = "chrome"
if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())


def selectOption(webelement, value):
    if value[0] != "all":
        for x in webelement:
            print(x.text)
          #  for y in range(len(value)):
            for y in value:
                #if x.text == value[y]:
                if x.text == y:
                    x.click()
                    break
    else:
        try:
            for x in webelement:
                print(x.text)
                x.click()
        except Exception as ex:
            print(ex)


driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
print(driver.title)
driver.maximize_window()
time.sleep(5)
txtSelect = driver.find_element_by_id("justAnInputBox")
txtSelect.click()
time.sleep(3)
listOptions = driver.find_elements_by_xpath("//span[@class='comboTreeItemTitle']")

selectOption(listOptions, ['all'])
