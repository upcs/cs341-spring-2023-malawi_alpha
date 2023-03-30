import unittest
from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
class testGoogle(unittest.TestCase):
    def runTest(self):
        driver = webdriver.Chrome(PATH)
        driver.get("https://www.google.com")
        assert "Google" in driver.title
        driver.quit()
unittest.main()