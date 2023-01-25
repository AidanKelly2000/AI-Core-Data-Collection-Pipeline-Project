from datetime import datetime
from pathlib import Path
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest.main import main
import json
import os
import pandas as pd
import requests
import time

# TODO: Add in a way that stops duplicates of images being added

class RightMoveScraper():
    """
    This class is used to scrape data from the Rightmove website.

    By using selenium to access certain elements on the webpage such as buttons 
    and it also uses "XPATH" to accurately work out the correct sub heading of the 
    container it wants to access. the name == main is used so that the method names 
    of this class will only work specifically with this file. 

    Attributes:
        driver (webdriver.Chrome): Selenium webdriver to access the website.

    """
    def __init__(self):
        """
        This function initialises the webdriver to access the Google Chrome browser.

        It uses selenium's webdriver function to access the google chrome browser and 
        get the subsequent URL. 

        """
        chrome_options = Options()
        # #chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # # chrome_options.headless = True # also works
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Chrome()
        query = "glasgow"
        self.driver.get(f"https://www.rightmove.co.uk/property-for-sale/find.html?searchType={query}&locationIdentifier=REGION%5E550&insId=1&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false")
        self.delay = 10
        
# TODO: Add in the wait until functions to all elements being accessed

    def search(self):
        """
        This function specifies the website that the webdriver is searching for.

        Navigates to the Rightmove website using the Selenium webdriver's "get" method.  

        """

    def accept_cookies(self):
        """
        This function bypasses the website's cookie policy by clicking on the "Allow all cookies" button.

        Uses the "find_element" method from Selenium's webdriver along with the "By" and "XPATH"
        to locate and click on the button.
        
        """
       
        
        try:
            # body class='header-rebranding rebranded-logo'
            #WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, "//*[@class='header-rebranding rebranded-logo']"))
            time.sleep(1)
            print("Frame Ready!")
            wait = WebDriverWait(self.driver, self.delay)
            accept_cookies_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Allow all cookies']")))
            print("Accept Cookies Button Ready!")
            # accept_button = self.driver.find_element(By.XPATH, "//button[@aria-label='Allow all cookies']")
            accept_cookies_button.click()
            time.sleep(1)
            print(accept_cookies_button)
        except TimeoutException:
            print("Loading took too much time!")

        return True

    def search_for_houses(self):
        """
        This function is used to locate houses in a specific area of the UK by 
        passing a keyword to the search bar.

        The root branch of the search bar is found using the "By" and "ID" from "find_element" method, then 
        the "XPATH" is used from there and sends a string of keywords to the search
        bar using the "send_keys" method. It then uses a series of "XPATH" and click to access 
        different elements on the pages, as explained previously.

        """
        search_bar = self.driver.find_element(By.ID, "_3I545u3msIUhJ6tHw7P9AZ")
        send_key_word = search_bar.find_element(By.XPATH, "div[1]/div/div/div/div/input").send_keys("Glasgow")
        time.sleep(1)

        search_for_sale_houses = self.driver.find_element(By.XPATH, "//button[@class='ksc_button large primary searchPanelControls ']")
        time.sleep(1)
        search_for_sale_houses.click()
        properties_button = self.driver.find_element(By.XPATH, "//button[@id='submit']")
        time.sleep(1)
        properties_button.click()
        
    def next_page(self):
        """
        This function navigates to the next page of the selected area of houses being scraped
        
        Uses the "find_element" method from Selenium's webdriver along with the "By" and "XPATH"
        to locate and click on the "next" button on the website.

        """
        next_page_button = self.driver.find_element(By.XPATH, "//button[@class='pagination-button pagination-direction pagination-direction--next']")
        time.sleep(1)
        next_page_button.click()
        return True

    def get_all_images(self):
        """
        Scrapes images and text from the Rightmove website for the selected area and pages.
        
        This method navigates to the Rightmove website, accepts the cookies, searches for 
        houses in a specific area, and navigates through a specified number of pages. It 
        uses selenium's webdriver and "XPATH" to access the elements on the website and scrapes 
        the images and text on the pages. New Directories are created using the "Path" class from
        the import "pathlib" and the method "mkdir". The images with there associated text are saved based on the time they 
        were generated, they are also shared in a "json" file in a dictionary.

        """
        # self.search()
        self.accept_cookies()
        # self.search_for_houses()
        # page_number = 0
        # Scrapes through 10 pages of house listings
        # while page_number < 9:
        time.sleep(2)
        # scrolls to the specific height of 8000, going down the page
        self.driver.execute_script("window.scrollTo(0, 8000);")
        time.sleep(2)

        
        # try:
        # #     container = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.ID, "propertySearch")))
        # # propertySearch is the id of the container that holds all the images of the result
        
        #     wait = WebDriverWait(self.driver, self.delay)
        #     container = wait.until(EC.presence_of_element_located((By.ID, "propertySearch")))
        #     image_containers = wait.until(EC.presence_of_all_elements_located((By.XPATH, "div/div/div/div/div/div/div/div/div/div/div/div/a/div/div/div/img"))) 

        container = self.driver.find_element(By.ID, "propertySearch") 
        # uses xpath to locate the element that holds the image
        image_containers = container.find_elements(By.XPATH, "div/div/div/div/div/div/div/div/div/div/div/div/a/div/div/div/img") 
        # A dictionary to store all the images and associated data
        images = {}

    # def create_image_folders(self, image_containers):
    #     images = {}


        for img in image_containers:


            # TODO: use pandas to clean the title
            # Replaces special characters in the title so that the image name can be saved without error
            # if code randomly stops, it may be due to the name being saved having special characters that need replaced ^^
            
            title = img.get_attribute('alt').lower()
            # Create a DataFrame from the title string
            df = pd.DataFrame([title], columns=['title'])
            # Replace unwanted characters with '-'
            df['title'] = df['title'].str.replace(r'[^\w\s]+', '-', regex=True)
            # Assign the cleaned title back to the title variable
            title = df['title'].iloc[0]
            img_src = img.get_attribute('src')

            timestamp = datetime.now().strftime("%Y-%m-%d_[%H_%M_%S]")
            # Create a unique ID for the image by combining the image, timestamp, and title
            image_id = "image_{}_{}_{}".format(img, timestamp, title)
            images[image_id] = {"img_id": image_id, "timestamp": timestamp, "img_src": img_src, "Title": title}
            # Create a directory to save the images if it doesn't already exist
            query_dir = "images/glasgow_houses"
            Path(query_dir).mkdir(parents=True, exist_ok=True)
            # Create a unique file name for the image by combining the timestamp, title, and file extension
            img_name = "{}_{}{}".format(timestamp, title, os.path.splitext(img_src)[1])
            fp = f"{query_dir}/{img_name}"    
            # Get the image data from the URL  
            img_data = self.get_img_bytes_from_url(img_src)
            # Save the image to the directory using the unique file name
            with open(fp, 'wb') as handler:
                handler.write(img_data)
            # Create a directory to save the json file if it doesn't already exist
            query_dir_2 = "images/raw_data"
            Path(query_dir_2).mkdir(parents=True, exist_ok=True)
            # Create a file path for the json file
            file_path = f"{query_dir_2}/right_move_images.json"
            # Save the images dictionary to a file
            with open(file_path, "w") as f:
                json.dump(images, f)

            # self.next_page()
            # page_number += 1

        # except TimeoutException:
        #     print("Loading took too much time!")

    def get_img_bytes_from_url(self, img_url):
        return requests.get(img_url).content
        
# if __name__ == "__main__":
    # query = "glasgow"
    # scraper = RightMoveScraper()
    # scraper.get_all_images()