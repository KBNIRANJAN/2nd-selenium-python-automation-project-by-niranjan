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
        self.driver.implicitly_wait(30)

    def test_login(self):
        driver = self.driver
        driver.get(self.url)
        driver.find_element(By.XPATH, "//*[@placeholder='Username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//*[@placeholder='Password']").send_keys("admin123")
        driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()
        driver.find_element(By.XPATH, "//*[@placeholder='Search']").is_displayed()
        menu_elements = driver.find_elements(By.XPATH, "//ul[@class='oxd-main-menu']/li/a/span")
        expected_menu_list = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard',
                              'Directory', 'Maintenance', 'Buzz']
        wait = WebDriverWait(driver, 40)
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "PIM"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add Employee"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@placeholder='First Name']"))).send_keys('niranjan')
        driver.find_element(By.XPATH, "//*[@placeholder='Last Name']").send_keys('gg')
        driver.find_element(By.XPATH, "//div[@class='oxd-switch-wrapper']/*").click()
        # PLEASE CLICK ON CREATE LOGIN DETAILS BUTTON MANUALLY DURING THE AUTOMATION when above locator is not working
        driver.find_element(By.XPATH, "(//input[@autocomplete='off'])[1]").send_keys('nirangan')
        driver.find_element(By.XPATH, "(//input[@autocomplete='off'])[2]").send_keys('6302868175#ng')
        driver.find_element(By.XPATH, "(//input[@autocomplete='off'])[3]").send_keys('6302868175#ng')
        #wait.until(EC.presence_of_element_located((By.XPATH, " //*[@fdprocessedid='re58h']"))).clear()
       # wait.until(EC.presence_of_element_located((By.XPATH, " //*[@fdprocessedid='re58h']"))).send_keys(6302868)
        driver.find_element(By.XPATH, "//*[@type='submit']").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main":
    unittest.main()
