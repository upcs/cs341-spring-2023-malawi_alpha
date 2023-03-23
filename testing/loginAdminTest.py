import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
PATH = "C:\Program Files (x86)\chromedriver.exe"
class testLoginAdmin(unittest.TestCase):
    def runTest(self):
        driver = webdriver.Chrome(PATH)
        driver.get("http://10.12.116.141")
        print(driver.title)
        login = driver.find_element(By.ID, "token")
        login.send_keys("54321")
        login.submit()
        print(driver.current_url)
        assert "admin" in driver.current_url
        driver.close()
unittest.main()