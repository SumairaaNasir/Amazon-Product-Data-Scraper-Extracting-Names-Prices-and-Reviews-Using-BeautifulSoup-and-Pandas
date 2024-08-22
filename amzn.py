import pandas as pd
from bs4 import BeautifulSoup

# Step 1: Read the HTML file
with open('amazon2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Step 2: Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Find all the desired <div> elements
cards = soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-vo8l48qglv7yn2w1wwffhqo34k s-latency-cf-section puis-card-border')

# Step 4: Initialize lists to store the extracted data
names = []
prices = []
reviews = []

# Step 5: Extract data from each card
for card in cards:
    # Extract Name
    name_tag = card.find('span', class_='a-size-medium a-color-base a-text-normal')
    name = name_tag.get_text(strip=True) if name_tag else ""

    # Extract Price
    price_tag = card.find('span', class_='a-price-whole')
    price = price_tag.get_text(strip=True) if price_tag else ""

    # Extract Reviews
    reviews_tag = card.find('span', class_='a-size-base a-color-secondary')
    review = reviews_tag.get_text(strip=True) if reviews_tag else ""

    # Append the data to lists
    names.append(name)
    prices.append(price)
    reviews.append(review)

# Step 6: Create a DataFrame to store the data
data = {
    'Name': names,
    'Price': prices,
    'Reviews': reviews
}
df = pd.DataFrame(data)

# Step 7: Write the DataFrame to an Excel file
df.to_excel('amazon_data2.xlsx', index=False)

print("Data has been written to 'amazon_data2.xlsx'")
