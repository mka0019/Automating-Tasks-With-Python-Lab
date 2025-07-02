# web_scraping.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options #we will use chrome browser to take the screenshots
#but you can use any browser 
import time

# List of webpages to take screenshots from. 
webpages = [
    "http://books.toscrape.com/",
    "https://www.gettyimages.com/detail/photo/cat-taking-a-selfie-royalty-free-image/1500448395?searchscope=image%2Cfilm&adppopup=true",
    "https://www.gettyimages.com/search/2/image-film?family=creative&phrase=cats"
]

# Set up Selenium Chrome in headless mode (no browser window)
options = Options()
options.add_argument("--headless")  # Don't show the browser
options.add_argument("--start-maximized")  # Start in full screen (as big as the screen can go for a good screenshot)
options.add_argument("--window-size=1920,1080")  # Default size for full-page screenshots, can be adjusted, but I took the default

# Start the driver
driver = webdriver.Chrome(options=options)

# Loop through the list of webpagesfound this in 
i = 1
for url in webpages:
    driver.get(url)
    time.sleep(2)# Wait for page to load

    # Take a screenshot and save it
    filename = f"screenshot_{i}.png" 
    driver.save_screenshot(filename)
    i += 1

# Close the browser
driver.quit()


