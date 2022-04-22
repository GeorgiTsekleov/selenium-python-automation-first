import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class SearchHotelsResults(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.driver = wait

    def filter_bath(self):
        self.wait_until_element_is_clickable(By.XPATH, "//div[contains(text(),'Басейн')]").click()
