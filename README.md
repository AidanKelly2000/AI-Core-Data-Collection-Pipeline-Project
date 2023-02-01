# AI-Core-Data-Collection-Pipeline-Project

The purpose of this project was to learn how to extract data from websites and save it locally in a structured format. The technologies used were: datetime,
pathlib, selenium, pandas, requests, unittest2, chromedriver. The use of selenium was mainly for the web driver import and it was also used for accessing many diferrent web elements and in some cases clicking on them.

## Milestone 1

Github was chosen as the version control being used for this project. A remote repo was cloned into a local folder in order to begin the documenting of the code.

## Milestone 2

It was then time to choose a website to scrape. A short list of 10 websites was created and then from there it was broken down into which websites added the most value to a potential model. Right move was the website of choice as it had the potential of being used to build a house price prediction model in the future.

## Milestone 3

The first thing required to scrape a website is to create a scraper class. The methods were chosen for each required operation of the scraper, the scraper was ran in headless mode, as explained in milestone 6:

```python


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

        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=chrome_options)
        query = "glasgow"
        self.driver.get(f"https://www.rightmove.co.uk/property-for-sale/find.html?searchType={query}&locationIdentifier=REGION%5E550&insId=1&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false")
        self.delay = 10
```

Certain selenium methods were used to navigate web pages, methods such as scrolling, finding elements and accepting cookies.

An important implementation of the scraper class was to use the exact URL's of the web page to scrape the data, this lowered the computational cost of the program as it wasn't having to search through the websites search bar to locate the desired houses, it instead accessed them from the exact URL's provided. There was code implemented to allow the program to scrape as many pages as necessary, although this method wasn't required as only one page was being scraped to save time.

```python
if __name__ == "__main__":
    query = "glasgow"
    scraper = RightMoveScraper()
```

this if statement was used so that the scraper class only runs as a script but not when it's imported as a module in a different program. This is useful to implement to test to make sure your code is run directly or if it is being imported by something else.

## Milestone 4

The "get_all_images()" method is used to collect the images on the rightmove web pages. It is the main method of the scraper class as it collects the main container where the images are located and then scrapes them all using the XPATH's of the image locations. Not all images were scraped is this is a high computational cost, it uses up lots of storage space, this project was formulated mainly to learn how to use all the tools described.

There is then a for loop which will loop for each image scraped. 
```python

        for img in image_containers:

            # Replaces special characters in the title so that the image name can be saved without error
            
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
```

This loop is used to generate unique time stamped image id's which are then stored in a json file in a nested folder called "images/raw_data" and also saves the images scraped in a local file, within a nested folder called "images/glasgow_houses". 

The images are stored in a dictionary, each record in the dictionary has its unique ID, timestamp of when it was scraped and links to any images associated with it.

Each image was saved as <date>_<time>_<order of image>.<image file extension> i.e. 03102022_142011_1.jpg this allowed for me to be able to see when the latest group of images were generated.

## Milestone 5

In this milestone, docstrings were added to the methods created. This helped in giving context to viewers on what was happening in the code, it also reinforced my understanding of what the methods were doing.

It was important to add a unit test file to the website scraper so that if someone else were to use it they can see the outputs and variables, to again help their understanding of what the code is achieving. The tests were produced in the test_right_move_web_scraper.py file. The first test was used to see if the correct URL was being returned in the initialiser. The accept cookies test checks if the "accept_cookies" button is clicked. The next page button is checked if there is more than one page being scraped, although this method is skipped as it isn't in use for this scraper. The final test checks to see if there are elements going into the image_containers and if the image_containers is a list, it does this using asserGreater and assertIsInstance respectively.

The test file was formatted like this:

```python
from right_move_web_scraper import RightMoveScraper
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
        actual_url = self.scraper.driver.current_url
        query = "glasgow"
        expected_url = f"https://www.rightmove.co.uk/property-for-sale/find.html?searchType={query}&locationIdentifier=REGION%5E550&insId=1&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false"
        self.assertEqual(actual_url, expected_url)

    # @unittest.skip
    def test_accept_cookies(self):
        """
        This test case Checks to see if the "accept_cookies" button is clicked
        """
        actual_value = self.scraper.accept_cookies()
        self.assertTrue(actual_value)

    @unittest.skip
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
```

## Milestone 6

The scraper was ran in headless mode, which is when the GUI is not used and the computer does all the scraping by only running through the code and not producing a visualisation. 

One of the final steps of this project was using Docker to create an image and eventually deploy it to the cloud. The image was created using the following Dockerfile:

```python 
# Specify image:tag
FROM python:3.9.12

# Set the current working directory
WORKDIR /AI-Core-Data-Collection-Pipeline-Project

# Adding trusting keys to apt for repositories, you can download and add them using the following command
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Add Google Chrome. Use the following command for that
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Update apt
RUN apt-get -y update

# install google chrome
RUN apt-get install -y google-chrome-stable

# Now you need to download chromedriver. First you are going to download the zipfile containing the latest chromedriver release
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip

# Unzip the chromedriver
RUN apt-get install -yqq unzip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Copy in all files of the directory to the Docker Image
COPY . .

# Install needed dependencies
RUN pip install -r requirements.txt

EXPOSE 4444

# Run the scraper file using the python version specified in the container
CMD ["python", "input_for_scraper.py"]
```

This Dockerfile is used so that any laptop or computer whether its a mac, windows or linux, can use this code to run the scraper. It is used to store all the important features of the program, such as python verison, chrome driver, the imports such as selenium and the port/expose associated with selenium, which is 4444 both ways. 

A docker compose file was also created as a way of understanding how volumes worked and how images can be created from a compose file, which increases simplicity when running images. The volume was stored locally to see how the compose file worked:

```python
version: "3.9"

services:
  database:
    build: .
    ports:
      - "4444:4444"
    volumes:
      - .:/AI-Core-Data-Collection-Pipeline-Project



  # python:
  #   depends_on:
  #     - database
  #   build: .
```

## Milestone 7

The final step of the project was to automate the creation and upload of images. The images were uploaded to docker hub, which is used to store images remotely. This is what is known as a CI/CD pipeline, this was important as it allows the code to be changed and then directly pushed to docker hub straight from the CLI. 