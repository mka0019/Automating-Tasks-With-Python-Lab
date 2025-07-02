# took the code from the lab, and with some research and AI helped with the below code
# http://books.toscrape.com/ > fake site that can used for testing.
#  I didn't want to use a real sites just in case of legal troubles. 



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv # Once the data is scraped, it will export the data into a CSV
import time

# Set up Chrome driver
options = Options()
# options.add_argument('--headless')  # Uncomment to run headless
driver = webdriver.Chrome(options=options)

# Open website
driver.get("http://books.toscrape.com/")

# Prepare CSV file
csv_file = open('products.csv', mode='w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Book Title'])

while True:
    time.sleep(1)  # Wait for page to load

    # Extract book titles
    product_elements = driver.find_elements(By.CSS_SELECTOR, 'article.product_pod h3 a')
    for product in product_elements:
        title = product.get_attribute('title')  # Book title is in the 'title' attribute
        csv_writer.writerow([title])

    # Check for "next" page
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, 'li.next a')
        next_button.click()
    except:
        break

# Cleanup
csv_file.close()
driver.quit()
print("Scraping complete. Data saved to products.csv.")
