from selenium.webdriver.common.by import By

import time


class Homepage():
    def __init__(self,driver):
        self.driver = driver

        self.hamburger_menu_button_id = "react-burger-menu-btn"
        self.logout_link_id = "logout_sidebar_link"

    def logout(self):
        self.driver.find_element(By.ID, self.hamburger_menu_button_id).click()
        time.sleep(3)
        self.driver.find_element(By.ID, self.logout_link_id).click()
