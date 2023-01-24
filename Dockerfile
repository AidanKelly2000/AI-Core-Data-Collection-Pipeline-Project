# Specify image:tag
FROM python:latest

# Set the current working directory
WORKDIR /AI-Core-Data-Collection-Pipeline-Project

# Install needed dependencies
RUN pip install -r requirements.txt

# Copy in all files of the directory to the Docker Image
COPY . .

CMD ["python", "input_for_scraper.py"]