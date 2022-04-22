import time
import pytest
from pages.booking_launch_page import LaunchPage
from pages.search_hotels_results import SearchHotelsResults
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestSearchAndVirifyFilters():
    def test_search_hotels(self):
        #Launching Chrome browser and opening the travel web site
        lp = LaunchPage(self.driver)

        #Accept the cookies
        lp.AcceptCookies()
        # self.driver.execute_script("window.scrollTo(0,500)")
        # time.sleep(1)
        # lp.pagescroll()
        self.driver.execute_script("window.scrollTo(0,300)")
        time.sleep(1)
        #Providing going on location with data "Bansko" ## Select second hotel from drop down
        lp.SearchHotelsGoingTo("Bansko")

        #Select start date/try incorect and corect date
        # time.sleep(3)
        lp.SelectGoingDate("2022-04-23")
        # lp.SelectGoingDate(GoingtoDateY = "2022-05-23")

        #Select back date/try incorect and corect date
        lp.SelectBackDate("2022-04-25")
        time.sleep(3)
        #Select more person/kids
        #Dropdown/select age of children
        lp.SelectKidsPlus()

        #Click and waiting for the searched hotel/respond from the DB
        lp.ClickBtnSearch()

        sh = SearchHotelsResults(self.driver)
        # Scroll down and see more results is loading or cuple times scroling/
        sh.pagescroll()
        # Select option pools/bath
        sh.filter_bath()

        # Verify the all offers result is show with Handle dynamic scroll
        self.driver.execute_script("window.scrollTo(0,500)")
        time.sleep(3)

        self.driver.quit()
