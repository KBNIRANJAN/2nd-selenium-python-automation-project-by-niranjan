import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\balan\\PycharmProjects\\AT PROJECT 2\
              TC_PIM_001_UNIT1.py")
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_login(self):
        driver = self.driver
        driver.get(self.url)
        driver.find_element(By.XPATH, "//*[@placeholder='Username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//*[@placeholder='Password']").send_keys("admin123")
        driver.find_element(By.XPATH, value="//button[@type='submit']").click()
        driver.find_element(By.LINK_TEXT, "Admin").click()
        driver.find_element(By.XPATH, "//span[text()[normalize-space() = 'User Management']]").click()
        driver.find_element(By.XPATH, "//a[text() ='Users']").click()
        driver.find_element(By.XPATH, "//label[@class = 'oxd-label' and text() = 'User Role']/../"
                                      "following-sibling::div/div/div/*/*")
        driver.find_element(By.XPATH, "//div[@role='option']").is_enabled()
        driver.find_element(By.XPATH, "//label[@class = 'oxd-label' and text() = 'Status']/../"
                                      "following-sibling::div/div/div/*/*")
        driver.find_element(By.XPATH, "//div[@role='option']").is_selected()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main":
    unittest.main()
