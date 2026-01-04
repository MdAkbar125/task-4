import requests
from bs4 import BeautifulSoup
import csv

# Website URL (safe for scraping)
url = "https://books.toscrape.com/"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all products
products = soup.find_all("article", class_="product_pod")

# Create CSV file
with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Rating"])

    for product in products:
        name = product.h3.a["title"]
        price = product.find("p", class_="price_color").text
        rating = product.find("p", class_="star-rating")["class"][1]

        writer.writerow([name, price, rating])

print("✅ Data extracted and saved to products.csv")
