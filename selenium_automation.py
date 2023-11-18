from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

book_details = []
def scrape_data(url,driver):
    # Scrape data (name, price, rating)
    driver.get(url)
    book_elements = driver.find_elements(By.CLASS_NAME,'_4ddWXP')  # Adjust based on the website's HTML structure
    

    for book_element in book_elements:
        try:
            name = book_element.find_element(By.CLASS_NAME,"s1Q9rs").text
            print(name)
        except Exception:
            name = None
        try: 
            price = book_element.find_element(By.CLASS_NAME,"_30jeq3").text
        except Exception:
            price = None
        try:
            rating = book_element.find_element(By.CLASS_NAME,"_3LWZlK").text
        except Exception:
            rating = None  
        book_details.append({"name": name, "price": price, "rating": rating})
    with open("book_details_of_hindi.csv", "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Name", "Price", "Rating"])
        for book in book_details:
            csv_writer.writerow([book["name"], book["price"], book["rating"]])

# Set up the Selenium WebDriver
driver = webdriver.Chrome()

# Navigate to the e-commerce website
driver.get("https://www.flipkart.com/")

# Perform a search for Hindi Books
search_box = driver.find_element(By.NAME, 'q')  # Adjust based on the website's HTML structure
search_box.send_keys("Hindi Books")
search_box.submit()

navi = driver.find_elements(By.CLASS_NAME,'ge-49M')
for a in navi:
    url = a.get_attribute('href')
    print(url)
    scrape_data(url,driver = webdriver.Chrome())
