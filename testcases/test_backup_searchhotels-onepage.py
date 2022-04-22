import time

import softest
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

class TestSearchAndVirifyFilter():
    def test_search_hotels(self):
        # Locators
        #FIRST PAGE
        BOOKING_URL = "https://www.booking.com/"
        ACTP_COOKIES = "onetrust-accept-btn-handler"
        GOINGON_PATH = "//input[@id='ss']"
        GOINGON_LOCATION = "Bansko"
        GOINGON_DROPDWN_PATH = "/html[1]/body[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]"

        DATE_TO_TRAVEL_MOUNT = "//div[@class='bui-calendar']//tbody//td[@class='bui-calendar__date']"
        FIRST_DATE_TO_TRAVEL_WRONG_DATA = "2022-04-1"
        FIRST_DATE_TO_TRAVEL_CORECT_DATA = "2022-05-20"

        SECOND_DATE_TO_TRAVEL_WRONG_DATA = "2022-04-5"
        SECOND_DATE_TO_TRAVEL_CORECT_DATA = "2022-05-29"

        SELECT_MORE_PERSON = "//div[@class='xp__input-group xp__guests']"
        SELECT_MORE_PERSON_PLUS = "//button[@aria-label='Увеличете броя Деца']"
        SELECT_CHILDREN = "//select[@name='age']"
        NUMBER_OF_CHILDREN = "9"

        PRES_SRCH_BTN_PATH = "//div[@class='sb-searchbox-submit-col -submit-button ']"

        #SECOND PAGE
        SELECT_POOLS_PATH = "//div[contains(text(),'Басейн') or contains(text()" \
                            ",'Закрит плувен басейн') or contains(text(),'Спа и Уелнес център')]"
        ACHAIN_GRANDARENA_HOTEL = "//div[contains(text(),'Кемпински Хотел Гранд Арена')]"
        ACHAIN_SHOWHOTEL_MAP = "//a[@id='hotel_sidebar_static_map']"

        #Launching Chrome browser and opening the travel web site
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[ElementClickInterceptedException])
        driver.get(BOOKING_URL)
        driver.maximize_window()
        #Accept the cookies
        wait.until(EC.element_to_be_clickable((By.ID, ACTP_COOKIES))).click()
        # time.sleep(1)
        #scroll and center the page
        driver.execute_script("window.scrollTo(0,300)")
        time.sleep(1)
        #Providing going on location with data "Bansko"
        searchbtn = driver.find_element(By.XPATH, GOINGON_PATH)
        # time.sleep(1)
        searchbtn.click()
        searchbtn.send_keys(GOINGON_LOCATION)
        #Select second hotel from drop down
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH, GOINGON_DROPDWN_PATH))).click()

        #Select start date/try incorect and corect date
        first_date = wait.until(EC.element_to_be_clickable((By.XPATH, DATE_TO_TRAVEL_MOUNT))
                                            ).find_elements(By.XPATH, DATE_TO_TRAVEL_MOUNT)
        for date in first_date:
            if date.get_attribute("data-date")  == FIRST_DATE_TO_TRAVEL_WRONG_DATA: #mount 4
                date.click()
                print("Selected date is wrong and we have a bug")
                time.sleep(1)
            elif date.get_attribute("data-date")  == FIRST_DATE_TO_TRAVEL_CORECT_DATA: #mount 5
                date.click()
                time.sleep(1)
                print("Selected first date is correct")
            # else:
            #     print("Please change/Check the 'DATE_TO_TRAVEL_MOUNT' path and/or change correct dates")


        #Select back date/try incorect and corect date
        last_date = driver.find_elements(By.XPATH, DATE_TO_TRAVEL_MOUNT)
        for date in last_date:
             if date.get_attribute("data-date") == SECOND_DATE_TO_TRAVEL_WRONG_DATA: #mount 4
                 date.click()
                 print("Selected date is wrong and we have a bug")
                 time.sleep(1)
             elif date.get_attribute("data-date") == SECOND_DATE_TO_TRAVEL_CORECT_DATA: #mount 5
                 date.click()
                 print("Selected second date is correct")
                 time.sleep(1)
             # else:
             #     print("Please change/Check the 'DATE_TO_TRAVEL_MOUNT' path and/or change correct dates")

        #Select more person/kids
        driver.find_element(By.XPATH, SELECT_MORE_PERSON).click()
        # time.sleep(1)
        driver.find_element(By.XPATH, SELECT_MORE_PERSON_PLUS).click()
        # time.sleep(1)
        #Dropdown/select age of children
        dropdown = driver.find_element(By.XPATH, SELECT_CHILDREN)
        # time.sleep(1)
        dd = Select(dropdown)
        dd.select_by_value(NUMBER_OF_CHILDREN)
        time.sleep(1)
        # driver.find_element(By.XPATH, "//option[@value='8']").click()
        #Click and waiting for the searched hotel/respond from the DB
        driver.find_element(By.XPATH, PRES_SRCH_BTN_PATH).click()
        #Scroll down and see more results is loading or cuple times scroling/
        driver.execute_script("window.scrollTo(0,500)")
        time.sleep(2)
        #Handle dynamic scroll
        # pageLength = driver.execute_script("window.scrollTo(0, document.body.scrollHeight"
        #                                    ");var pageLength=document.body.scrollHeight;return pageLength;")
        # match = False
        # while (match == False):
        #     lastCount = pageLength
        #     time.sleep(1)
        #     pageLength = driver.execute_script("window.scrollTo(0, document.body.scrollHeight"
        #                                        ");var pageLength=document.body.scrollHeight;return pageLength;")
        #     if lastCount == pageLength:
        #         match = True
        # time.sleep(4)

        #Select option pools/bath
        wait.until(EC.element_to_be_clickable((By.XPATH, SELECT_POOLS_PATH))
                                            ).find_element(By.XPATH, SELECT_POOLS_PATH).click()
        time.sleep(3)
        # Verify the all offers result from selected pools is showed
        driver.execute_script("window.scrollTo(0,200)")

        # Select 1st hotel from search page
        parent_handle = driver.current_window_handle

        # print(parent_handle)
        btn_achn = driver.find_element(By.XPATH, ACHAIN_GRANDARENA_HOTEL)
        achains = ActionChains(driver)
        time.sleep(1)
        achains.move_to_element(btn_achn).perform()
        time.sleep(1)
        btn_achn.click()

        # Swich to another page
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                time.sleep(4)
                btn_achn_map = driver.find_element(By.XPATH, ACHAIN_SHOWHOTEL_MAP)
                achains_map = ActionChains(driver)
                time.sleep(2)
                achains_map.move_to_element(btn_achn_map).perform()
                time.sleep(2)
                btn_achn_map.click()
                time.sleep(10)
                driver.close()
                time.sleep(2)
                break
        driver.quit()
        


bookingtest = TestSearchAndVirifyFilter() #create a object
bookingtest.test_search_hotels() #create a method