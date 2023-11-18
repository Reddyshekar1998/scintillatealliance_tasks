# Web Scraping Script for Book Details

## Overview

This Python script uses Selenium to scrape book details from an e-commerce website (in this case, Flipkart). It extracts information such as book name, price, and rating.

## Requirements

- Python 3.x
- pip
- Chrome WebDriver
- tesseract - for linux - sudo apt install tesseract-ocr and for windows mention the path of tesseract - I'm using linux

## Installation



1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    Download the Chrome WebDriver and tesseract make sure its location is in your system's PATH.

## Usage

1. Run the script:

    ```bash
    python selenium_automation.py
    ```


2. The script will open a Chrome browser, navigate to Flipkart, search for Hindi Books, and scrape book details.

3. The results will be saved in a CSV file named `book_details.csv`.

## Notes

- Make sure you have a stable internet connection.
- Adjust the script as needed based on changes to the website's HTML structure.

# TO run python Appium

1. Install dependencies:

    ```bash
    pip install Appium-Python-Client==2.6.0
    ```
2. Install appium server with version @2.0.0
	Install uiautomator2 driver for appium
    ```bash
    appium --version
    ```
# Output
    2.0.0

## Usage



1. Make sure that android studio emulator is running
2. To check emulator deviceName

    ```bash
  adb devices
    ```
# After installing the appium wait for to start server
# Change the deviceName in capabilities appium_automation.py

3. Run the script:

    ```bash
    appium
    python appium_automation.py
    ```



