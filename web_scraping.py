# web_scraping.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options #we will use chrome browser to take the screenshots
#but you can use any browser 
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up browser (headless = no window opens)
options = Options()
options.add_argument('--headless')  # Run without opening a browser window
options.add_argument('--window-size=1920,1080') # Default size for full-page screenshots, can be adjusted, but I took the default


# Create browser driver (using Chrome)
driver = webdriver.Chrome(options=options)

# Go to the website
driver.get("http://books.toscrape.com/")

# Take a screenshot and save it as a file
driver.save_screenshot("screenshot.png")

# Done!
driver.quit()
