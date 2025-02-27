import csv
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode to avoid detection
options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid detection
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL to scrape
base_url = "https://www.bikewale.com/royalenfield-bikes/"

# Try accessing the page with error handling
try:
    driver.get(base_url)
    time.sleep(random.uniform(3, 6))  # Random delay to prevent blocking
    
    # Scroll down to load all dynamic content
    last_height = driver.execute_script("return document.body.scrollHeight")
    for _ in range(3):  # Adjust the range if needed
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for new content to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # Stop if no new content loads
        last_height = new_height

except Exception as e:
    print(" Error loading page:", e)
    driver.quit()
    exit()

# Get page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Extract all text from the page
page_text = soup.get_text(separator="\n", strip=True)

# Extract all image links
image_tags = soup.find_all("img")
image_urls = [
    urljoin(base_url, img['src'])  # Convert relative URLs to full URLs
    for img in image_tags
    if 'src' in img.attrs and "grey-16x9.svg" not in img['src']  # Remove blank placeholders
]

# Extract all hyperlinks (both absolute and relative)
link_tags = soup.find_all("a", href=True)
all_links = [
    urljoin(base_url, link['href'])  # Convert relative URLs to absolute
    for link in link_tags
    if not any(ext in link['href'] for ext in [".jpg", ".png", ".jpeg", ".svg"])  # Avoid image links
]

# Close the browser
driver.quit()

# Save page content to content.csv
with open("content.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Page Content"])
    writer.writerow([page_text])

# Save image links to image_links.txt
with open("image_links.csv", "w", encoding="utf-8") as file:
    for img_link in image_urls:
        file.write(img_link + "\n")

# Save all links to total.csv
with open("total.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    for link in all_links:
        writer.writerow([link])

print(" Data saved successfully: content.csv, image_links.txt, total.csv")
