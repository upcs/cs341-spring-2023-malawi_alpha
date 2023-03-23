import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


class GoogleTestCase(unittest.TestCase):

    # Sets up browser
    def setUp(self):
        options_s = webdriver.ChromeOptions()
        options_s.add_argument('--headless')
        self.browser = webdriver.Chrome(options=options_s)
        self.addCleanup(self.browser.quit)
        # self.browser = webdriver.Chrome()
        # self.addCleanup(self.browser.quit)
        
    # Tests if login page exists
    def test_page_title(self):
        self.browser.get('http://10.12.116.141/')
        self.assertTrue('Login' == self.browser.title)
        
    # Tests if login works correctly
    def test_login(self):
        self.browser.get('http://10.12.116.141/')
        login_box = self.browser.find_element(By.NAME, 'token')
        login_box.send_keys('12345')
        login_box.submit()
        self.assertTrue('Teacher View' == self.browser.title)

    # Tests prinout button that shows every student's printout
    def test_all_prinout_button(self):
        self.browser.get(
            'http://10.12.116.141/teacher-view.php?ID=e9cbd2ea8015a084ce9cf83a3c65b51f8fa10a39/')
        print_button = self.browser.find_element(By.NAME, 'printout-button')
        print_button.click()
        self.assertEqual(self.browser.current_url,
                         'http://10.12.116.141/all-printout.php')

    # Tests the hyperlink in teacher-view
    def test_student_link(self):
        self.browser.get(
            'http://10.12.116.141/teacher-view.php?ID=e9cbd2ea8015a084ce9cf83a3c65b51f8fa10a39/')
        stu_link = self.browser.find_element(By.NAME, 'teacher-edit.php?ID=1')
        stu_link.click()
        self.assertEqual(self.browser.current_url,
                         'http://10.12.116.141/teacher-edit.php?ID=1')
        name = self.browser.find_element(By.NAME, 'name-section')
        expected_name = "FATIMA ANAFI's grades"
        self.assertEqual(name.text, expected_name)

    # Tests printout button in teacher-edit
    def test_single_printout_button(self):
        self.browser.get('http://10.12.116.141/teacher-edit.php?ID=1')
        print_button = self.browser.find_element(By.NAME, 'printout-button')
        print_button.click()
        self.assertEqual(self.browser.current_url,
                         'http://10.12.116.141/single-printout.php?ID=1')
        name = self.browser.find_element(By.NAME, 'name-text')
        expected_name = "FATIMA ANAFI"
        self.assertEqual(name.text, expected_name)

    # Tests if token checker button works correctly
    def test_token_checker_a(self):
        self.browser.get(
            'http://10.12.116.141/teacher-view.php?ID=e9cbd2ea8015a084ce9cf83a3c65b51f8fa10a39/')
        token_button = self.browser.find_element(By.NAME, 'token-button')
        token_text = self.browser.find_element(By.ID, 'token-text')
        alert = Alert(self.browser)

        token_text.send_keys('token')
        token_button.click()
        self.assertEqual(alert.text, 'Token is correct')
        alert.accept()

    def test_token_checker_b(self):
        self.browser.get(
            'http://10.12.116.141/teacher-view.php?ID=e9cbd2ea8015a084ce9cf83a3c65b51f8fa10a39/')
        token_button = self.browser.find_element(By.NAME, 'token-button')
        token_text = self.browser.find_element(By.ID, 'token-text')
        alert = Alert(self.browser)
        token_text.send_keys('wrongtoken')
        token_button.click()
        self.assertEqual(alert.text, 'Token is incorrect')
        alert.accept()

    def test_token_checker_c(self):
        self.browser.get(
            'http://10.12.116.141/teacher-view.php?ID=e9cbd2ea8015a084ce9cf83a3c65b51f8fa10a39/')
        token_button = self.browser.find_element(By.NAME, 'token-button')
        token_text = self.browser.find_element(By.ID, 'token-text')
        alert = Alert(self.browser)
        token_text.send_keys(" ")
        token_button.click()
        self.assertEqual(alert.text, 'Token is empty')
        alert.accept()

    def test_token_checker_d(self):
        self.browser.get(
            'http://10.12.116.141/teacher-view.php?ID=e9cbd2ea8015a084ce9cf83a3c65b51f8fa10a39/')
        token_button = self.browser.find_element(By.NAME, 'token-button')
        token_text = self.browser.find_element(By.ID, 'token-text')
        alert = Alert(self.browser)
        token_text.send_keys("*&%^%&&^%")
        token_button.click()
        self.assertEqual(alert.text, 'Token contains invalid characters')
        alert.accept()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(GoogleTestCase('test_page_title'))
    suite.addTest(GoogleTestCase('test_login'))
    suite.addTest(GoogleTestCase('test_all_prinout_button'))
    suite.addTest(GoogleTestCase('test_student_link'))
    suite.addTest(GoogleTestCase('test_single_printout_button'))
    suite.addTest(GoogleTestCase('test_token_checker_a'))
    suite.addTest(GoogleTestCase('test_token_checker_b'))
    suite.addTest(GoogleTestCase('test_token_checker_c'))
    suite.addTest(GoogleTestCase('test_token_checker_d'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
