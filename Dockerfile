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