# AI-Core-Data-Collection-Pipeline-Project

The purpose of this project was to learn how to extract data from websites and save it locally in a structured format. The technologies used were: datetime,
pathlib, selenium, pandas, requests, unittest2, chromedriver. The use of selenium was mainly for the web driver import and it was also used for accessing many diferrent web elements and in some cases clicking on them.

## Milestone 1

Github was chosen as the version control being used for this project. A remote repo was cloned into a local folder in order to begin the documenting of the code.

## Milestone 2

It was then time to choose a website to scrape. A short list of 10 websites was created and then from there it was broken down into which websites added the most value to a potential model. Right move was the website of choice as it had the potential of being used to build a house price prediction model in the future.

## Milestone 3

The first thing required to scrape a website is to create a scraper class. The methods were chosen for each required operation of the scraper:

'''python
An explanation of the class and the code used for the initialiser:

class RightMoveScraper():
    
    This class is used to scrape data from the Rightmove website.

    By using selenium to access certain elements on the webpage such as buttons 
    and it also uses "XPATH" to accurately work out the correct sub heading of the 
    container it wants to access. the name == main is used so that the method names 
    of this class will only work specifically with this file. 

    Attributes:
        driver (webdriver.Chrome): Selenium webdriver to access the website.
    

    def __init__(self):

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
'''

Certain selenium methods were used to navigate web pages, methods such as scrolling, finding elements and accepting cookies.

An important implementation of the scraper class was to use the exact URL's of the web page to scrape the data, this lowered the computational cost of the program as it wasn't having to search through the websites search bar to locate the desired houses, it instead accessed them from the exact URL's provided. There was code implemented to allow the program to scrape as many pages as necessary, although this method wasn't required as only one page was being scraped to save time.

"""
- if __name__ == "__main__" 
"""

this if statement was used so that the scraper class only runs as a script but not when it's imported as a module in a different program. This is useful to implement to test to make sure your code is run directly or if it is being imported by something else.

## Milestone 4

The "get_all_images()" method is used to collect the images on the rightmove web pages. It is the main method of the scraper class as it collects the main container where the images are located and then scrapes them all using the XPATH's of the image locations. Not all images were scraped is this is a high computational cost, it uses up lots of storage space, this project was formulated mainly to learn how to use all the tools described.

There is then a for loop which will loop for each image scraped. This loop is used to generate unique time stamped image id's which are then stored in a json file in a nested folder called "images/raw_data" and also saves the images scraped in a local file, within a nested folder called "images/glasgow_houses". 

The images are stored in a dictionary, each record in the dictionary has its unique ID, timestamp of when it was scraped and links to any images associated with it.

Each image was saved as <date>_<time>_<order of image>.<image file extension> i.e. 03102022_142011_1.jpg this allowed for me to be able to see when the latest group of images were generated.

## Milestone 5

In this milestone, docstrings were added to the methods created. This helped in giving context to viewers on what was happening in the code, it also reinforced my understanding of what the methods were doing.

It was important to add a unit test file to the website scraper so that if someone else were to use it they can see the outputs and variables, to again help their understanding of what the code is achieving. The tests were produced in the test_right_move_web_scraper.py file. The first test was used to see if the correct URL was being returned in the initialiser. The accept cookies test checks if the "accept_cookies" button is clicked. The next page button is checked if there is more than one page being scraped, although this method is skipped as it isn't in use for this scraper. The final test checks to see if there are elements going into the image_containers and if the image_containers is a list, it does this using asserGreater and assertIsInstance respectively.

## Milestone 6