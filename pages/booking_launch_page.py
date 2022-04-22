import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from base.base_driver import BaseDriver


class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.driver = wait

    def AcceptCookies(self):
        # Accept the cookies
        self.wait_until_element_is_clickable(By.ID, "onetrust-accept-btn-handler").click()
        # time.sleep(1)

    def SearchHotelsGoingTo(self, GoingtoHotels):
        # Providing going on location with data "Bansko"
        searchbtn = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='ss']")
        searchbtn.click()
        searchbtn.send_keys(GoingtoHotels)
        # Select second hotel from drop down
        time.sleep(1)
        self.wait_until_element_is_clickable(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]").click()

    def SelectGoingDate(self, GoingtoDate):
        # Select start date/try incorect and corect date
        first_date = self.wait_until_element_is_clickable(By.XPATH, "//div[@class='bui-calendar']//tbody//td[@class='bui-calendar__date']"
                                                          ).find_elements(By.XPATH, "//div[@class='bui-calendar']//tbody//td[@class='bui-calendar__date']")
        for date in first_date:
            if date.get_attribute("data-date") == "GoingtoDate":  # mount 4
                date.click()
            # elif date.get_attribute("data-date") == "GoingtoDate":  # mount 5
            #     date.click()
            # break

    def SelectBackDate(self, BackDate):
        # Select back date/try incorect and corect date
        last_date = self.wait_until_element_is_clickable(By.XPATH, "//div[@class='xp__dates xp__group']"
                                                         ).find_elements(By.XPATH, "//div[@class='bui-calendar']//tbody//td[@class='bui-calendar__date']")
        for date in last_date:
            if date.get_attribute("data-date") == "BackDate":  # mount 4
                date.click()
            # elif date.get_attribute("data-date") == "BackDateY":  # mount 5
            #     date.click()
            # break

    def SelectKidsPlus(self):
        # Select more person/kids
        self.wait_until_element_is_clickable(By.XPATH, "//div[@class='xp__input-group xp__guests']").click()
        # time.sleep(4)
        self.wait_until_element_is_clickable(By.XPATH, "//button[@aria-label='Увеличете броя Деца']").click()
        # time.sleep(4)
        self.wait_until_element_is_clickable(By.XPATH, "//option[@value='8']").click()
        # Dropdown/select age of children
        # time.sleep(4)
        # driver.find_element(By.XPATH, "//option[@value='8']").click()

    def ClickBtnSearch(self):
        # Click and waiting for the searched hotel/respond from the DB
        self.wait_until_element_is_clickable(By.XPATH, "//span[@class='js-sb-submit-text ']").click()

