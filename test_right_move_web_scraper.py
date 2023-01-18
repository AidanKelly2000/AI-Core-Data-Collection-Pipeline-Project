from new_rightmove_scraper import RightMoveScraper
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestRightMoveScraper(unittest.TestCase):

    def setUp(self):
        """
        This function sets up the initial conditions for each test case being
        carried out.

        It creates an instance of the RightMoveScraper class and gives it the
        variable name "scraper". 
        """
        self.scraper = RightMoveScraper()
    # @unittest.skip
    def test_search(self):
        """
        This test case checks if the search method uses the webdriver to 
        find the rightmove website.

        The assertEqual method is used to compare the actual output in the code 
        with the expected output of the code
        """
        actual_value = self.scraper.driver.current_url
        expected_value = f"https://www.rightmove.co.uk/property-for-sale/find.html?searchType=glasgow&locationIdentifier=REGION%5E550&insId=1&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false"
        self.assertEqual(actual_value, expected_value)

    # @unittest.skip
    def test_accept_cookies(self):
        """
        This test case Checks to see if the "accept_cookies" button is clicked
        """
        actual_value = self.scraper.accept_cookies()
        self.assertTrue(actual_value)

    # @unittest.skip
    def test_next_page(self):
        """
        This test case checks the functionality of the "next_page" method of the 
        RightMoveScraper class.

        It asserts that the next page button is enabled using the "is_enabled()"
        method. This test case is used to verify that the "next_page" method is able 
        to navigate to the next page of the selected area of houses being scraped.
        """
        self.scraper.accept_cookies()
        self.scraper.next_page()
        next_page_button = self.scraper.driver.find_element(By.XPATH, "//button[@class='pagination-button pagination-direction pagination-direction--next']")
        self.assertTrue(next_page_button.is_enabled())

    # @unittest.skip
    def test_get_all_images(self):
        """
        This test case checks if the get_all_images method is scraping images

        It uses the "assertGreater" to check that at least one image is in the container.
        """
        self.scraper.get_all_images()
        container = self.scraper.driver.find_element(By.ID, "propertySearch")
        image_containers = container.find_elements(By.XPATH, "div/div/div/div/div/div/div/div/div/div/div/div/a/div/div/div/img")
        self.assertGreater(len(image_containers), 0)
        self.assertIsInstance(image_containers, list)

    def tearDown(self):
        self.scraper.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=True)


# TODO: 1. Add this into Git Repository
# TODO: 2. Change search method to use url and a {query}
# TODO: 3. Add "WebdriverWait" to all things necessary. Found in Advanced Selenium prerequisite
# TODO: 4. get headless webdriver to run
# TODO: 5. get the url to work correctly in the search unittest, have it use {query} instead of "glasgow" in the url



# TODO: If the chrome driver stops working, do: webdriver manager or update to latest version in env
#       use this to update to latest chrome in envs automatically - https://pypi.org/project/webdriver-manager/, pip install webdriver-manager