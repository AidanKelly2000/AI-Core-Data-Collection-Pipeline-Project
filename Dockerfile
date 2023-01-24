# Specify image:tag
FROM python:3.9.12

# Set the current working directory
WORKDIR /AI-Core-Data-Collection-Pipeline-Project

# Install the Chrome webdriver
RUN Invoke-WebRequest -Uri "https://chromedriver.storage.googleapis.com/85.0.4183.87/chromedriver_win32.zip" -OutFile "chromedriver.zip"
RUN Expand-Archive -Path "chromedriver.zip" -DestinationPath "C:\chromedriver"
RUN $env:path += ";C:\chromedriver"

# Copy in all files of the directory to the Docker Image
COPY . .

# Install needed dependencies
RUN pip install -r requirements.txt

ENV CHROME_BIN=/usr/bin/google-chrome
CMD ["python", "input_for_scraper.py"]