from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Selenium WebDriver (Automatically installs ChromeDriver)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode to avoid detection
options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent bot detection
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Amazon URL to scrape
url = "https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar"
driver.get(url)

# Wait for the main product section to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "s-main-slot")))

# Scroll down multiple times to load more products
for _ in range(3):
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(2)

# Save the page source to an HTML file
html_file = "amazon_page.html"
with open(html_file, "w", encoding="utf-8") as file:
    file.write(driver.page_source)

print(f"HTML file saved: {html_file}")

# Close the browser
driver.quit()
