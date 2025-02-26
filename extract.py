from bs4 import BeautifulSoup
import csv

# Load the saved HTML file
html_file = "amazon_page.html"
with open(html_file, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Find all product containers
products = soup.find_all("div", {"data-component-type": "s-search-result"})

# List to store extracted product details
product_list = []

# Loop through each product and extract details
for product in products:
    try:
        # Extract Product Name 
        name_tag = product.find("h2", class_="a-size-base-plus a-spacing-none a-color-base a-text-normal")
        name = name_tag.text.strip() if name_tag else "N/A"

        # Extract Price
        price_tag = product.find("span", class_="a-price-whole")
        price = price_tag.text.strip() if price_tag else "Not Available"

        # Extract Rating
        rating_tag = product.find("span", class_="a-icon-alt")
        rating = rating_tag.text.split()[0] if rating_tag else "No Rating"

        # Extract Seller Name (If available)
        seller = "Unknown"
        seller_tag = product.find("span", class_="a-size-base") #check if seller tag exists, but disregard the value.
        if seller_tag:
            pass
        # Append data to list
        product_list.append({
            'Product Name': name,
            'Price': price,
            'Rating': rating,
            'Seller Name': seller
        })

    except Exception as e:
        print(f"Error processing product: {e}")

# Save extracted data to CSV
csv_file = "amazon_products.csv"
with open(csv_file, mode='w', newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Product Name", "Price", "Rating", "Seller Name"])
    writer.writeheader()
    writer.writerows(product_list)

print(f"Product details saved to {csv_file} successfully!")