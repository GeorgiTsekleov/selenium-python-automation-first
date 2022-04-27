import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver
        # self.driver = wait
    def pagescroll(self):

        pageLength = self.driver.execute_script(
              "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(1)
            pageLength = self.driver.execute_script(
                  "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            if lastCount == pageLength:
                match = True
        time.sleep(4)
        # self.driver.execute_script("window.scrollTo(0,500)")
        # time.sleep(2)

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    #some lines from SDEV1

