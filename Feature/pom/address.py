from selenium.webdriver.common.by import By
class name_email:
    _NAME_INPUT = (By.XPATH, "//input[@id='name']")
    _EMAIL_INPUT = (By.XPATH, "//input[@id='email']")
    def __init__(self, driver):
        self.driver = driver
    def enter_name_email(self, name, email):
        self.driver.find_element(*self._NAME_INPUT).send_keys(name)
        self.driver.find_element(*self._EMAIL_INPUT).send_keys(email)
