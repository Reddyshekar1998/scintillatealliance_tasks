import csv

extracted_data = []
with open("book_details.csv", newline='') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        extracted_data.append(row)

image_prices = ['208','300']

result_dict = {"matching_prices": [], "price_discrepancies": []}

# Compare OCR-extracted prices with Selenium-scraped prices
for i, row in enumerate(extracted_data):
    try:
        ocr_price = image_prices[i]
        price = row["Price"].split('₹')[-1]

        if ocr_price == price:
            result_dict["matching_prices"].append({
                "Name": row["Name"],
                "Price": row["Price"],
                "Rating": row["Rating"]
            })
        else:
            result_dict["price_discrepancies"].append({
                "Name": row["Name"],
                "Price": price,
                "OCR_Price": ocr_price,
                "Rating": row["Rating"]
            })
    except IndexError:
        break

# Output the final report
print("Items with Matching Prices:")
for item in result_dict["matching_prices"]:
    print(item)

print("\nItems with Price Discrepancies:")
for item in result_dict["price_discrepancies"]:
    print(item)
