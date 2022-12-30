import time
from selenium import webdriver
from selenium.webdriver import Keys
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
        self.driver.implicitly_wait(30)

    def test_login(self):
        driver = self.driver
        driver.get(self.url)
        driver.find_element(By.XPATH, "//*[@placeholder='Username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//*[@placeholder='Password']").send_keys("admin123")
        driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()
        driver.find_element(By.XPATH, "//*[@placeholder='Search']").is_displayed()
        wait = WebDriverWait(driver, 50)
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "PIM"))).click()
        # driver.find_element(By.XPATH, "(//div[@role='row'])[1]").click()
        driver.find_element(By.XPATH, "(//*[@class='oxd-icon-button oxd-table-cell-action-space'][2])[1]").click()
        driver.find_element(By.LINK_TEXT, "Salary").click()
        driver.find_element(By.XPATH, "(//button[@type='button'])[2]").click()
        driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys('CTC')
        driver.find_element(By.XPATH, "(//span)[77]").click()  # just give a click manually during automation
        driver.find_element(By.XPATH, "(//*[@class='oxd-input oxd-input--active'])[3]").send_keys(450000)
        driver.find_element(By.XPATH, "//*[@class='oxd-switch-wrapper']").click()
        driver.find_element(By.XPATH, "(//*[@class='oxd-input oxd-input--active'])[4]").send_keys(987456123)
        driver.find_element(By.XPATH, "(//span)[17]").click()  # just give a click manually during automation
        driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[5]").send_keys(143)
        driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[6]").send_keys(32000)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        def tearDown(self):
            self.driver.quit()

        if __name__ == "__main":
            unittest.main()
