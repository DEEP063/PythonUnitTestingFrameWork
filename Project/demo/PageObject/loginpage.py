import time

from selenium.webdriver.common.by import By


class Loginpage():
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_by_id = "user-name"
        self.password_textbox_by_id = "password"
        self.login_button_by_id = "login-button"

    def login(self, username, password):
        time.sleep(3)
        self.driver.find_element(By.ID, self.username_textbox_by_id).send_keys(username)
        self.driver.find_element(By.ID, self.password_textbox_by_id).send_keys(password)
        self.driver.find_element(By.ID, self.login_button_by_id).click()
