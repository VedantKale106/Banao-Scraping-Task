# Amazon Product Scraper

This repository contains Python scripts to scrape product information from Amazon's search results for power banks. It uses Selenium for web automation and BeautifulSoup for HTML parsing.

## Files

-   `download.py`: This script uses Selenium to navigate to an Amazon search results page for power banks, scrolls down to load more products, and saves the page source as an HTML file (`amazon_page.html`).
-   `extract.py`: This script parses the saved HTML file using BeautifulSoup, extracts product names, prices, ratings, and seller names, and saves the data to a CSV file (`amazon_products.csv`).
-   `amazon_products.csv`: This CSV file contains the extracted product data.
-   `amazon_page.html`: This HTML file is the downloaded webpage used for scraping.

## Prerequisites

-   Python 3.x
-   Selenium (`pip install selenium`)
-   BeautifulSoup4 (`pip install beautifulsoup4`)
-   webdriver-manager (`pip install webdriver-manager`)

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd amazon-product-scraper
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    or
    ```bash
    pip install selenium beautifulsoup4 webdriver-manager
    ```

## Usage

1.  **Download the Amazon page source:**

    ```bash
    python download.py
    ```

    This will create `amazon_page.html`.

2.  **Extract product data:**

    ```bash
    python extract.py
    ```

    This will create `amazon_products.csv`.

## Explanation of Scripts

### `download.py`

-      Uses Selenium with Chrome to automate browsing.
-      Sets Chrome to headless mode to run without opening a browser window.
-      Disables automation detection to prevent Amazon from blocking the script.
-      Navigates to the specified Amazon URL.
-      Waits for the product section to load.
-      Scrolls down multiple times to load more products.
-      Saves the page source to `amazon_page.html`.

### `extract.py`

-      Uses BeautifulSoup to parse the `amazon_page.html` file.
-      Finds all product containers using their `data-component-type` attribute.
-      Extracts product names, prices, and ratings using their respective HTML tags and classes.
-   Extracts Seller name, but defaults to "Unknown" as the seller names were not easily accessible using the current html structure.
-      Handles potential errors during data extraction.
-      Saves the extracted data to `amazon_products.csv` using the `csv` module.

## Example Output (CSV)

```csv
Product Name,Price,Rating,Seller Name
Ambrane 20000mAh Power Bank,1,699,3.9,Unknown
ElevOne by Ambrane 10000mAh Slim & Compact Powerbank,599,3.9,Unknown
alain store Pocket Charge Alain Store 3-In-1 Camping Working Emergency Large Capacity 5000Mah External Mobile Battery Charger Detachable Connectors (Black),1,399,3.5,Unknown
...
