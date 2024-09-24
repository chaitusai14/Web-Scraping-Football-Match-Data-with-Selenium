# Web-Scraping-Football-Match-Data-with-Selenium

## Table of Contents
1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Technologies Used](#technologies-used)
4. [Prerequisites](#prerequisites)
5. [Script Description](#script-description)
   - [Website Interaction](#website-interaction)
   - [Country Selection](#country-selection)
   - [Data Extraction](#data-extraction)
   - [Data Storage](#data-storage)
   - [Browser Automation](#browser-automation)
6. [How to Use](#how-to-use)
7. [Customization](#customization)
8. [Potential Improvements](#potential-improvements)

## Project Overview

This project is a Python-based web scraper designed to extract football match data from the [adamchoi.co.uk](https://www.adamchoi.co.uk/overs/detailed) website using Selenium. The script automatically navigates the website, interacts with a dropdown menu to select a specific country, and retrieves detailed match information including the date, home team, score, and away team. The collected data is then stored in a CSV file for further analysis or use.

## Key Features

- **Automated Web Interaction**: Uses Selenium to interact with the website’s elements, such as buttons and dropdown menus, simulating real-time user actions.
- **Customizable Country Selection**: The script is designed to select "Germany" from the dropdown menu by default, but this can be easily customized to select other countries.
- **XPath for Element Selection**: Utilizes XPath to reliably identify and interact with specific elements on the webpage, such as the "All matches" button and the columns within the match data table.
- **Match Data Extraction**: Retrieves detailed football match data such as:
  - Match date
  - Home team
  - Score
  - Away team
- **CSV Output**: All extracted data is stored in a CSV file (`All_matches_data_adamchoi.csv`) for easy access and analysis.
  
## Technologies Used

- **Selenium WebDriver**: For automating browser interactions.
- **Pandas**: For handling and storing scraped data.
- **ChromeDriver**: As the browser automation driver for Google Chrome.

## Prerequisites

Before running the script, make sure you have the following installed:

1. **Python 3.x**: Download from [here](https://www.python.org/downloads/).
2. **Selenium**: Install Selenium using pip:
   ```bash
   pip install selenium
   ```
3. **ChromeDriver**: 
   - Download the correct version of ChromeDriver that matches your version of Chrome.
   - Ensure the path to the ChromeDriver executable is correctly set in the script.

4. **Pandas**: Install Pandas using pip:
   ```bash
   pip install pandas
   ```

## Script Description

### Website Interaction
- The script first navigates to the football statistics page on the `adamchoi` website.
- It automatically clicks on the "All Matches" button to display a complete list of available matches using **XPath** for precise element targeting:
  ```python
  all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
  all_matches_button.click()
  ```

### Country Selection
- The script uses Selenium’s `Select` function to choose "Germany" from the dropdown menu. This selection can be easily modified to extract data for other countries.
- Here's how the script uses XPath and Selenium's `Select` to interact with the dropdown:
  ```python
  dropdown = Select(driver.find_element_by_id("country"))
  dropdown.select_by_visible_text("Germany")
  ```

### Data Extraction
- The script finds all match rows (`<tr>` elements) using the `find_elements_by_tag_name('tr')` method.
- Each column of the table (date, home team, score, and away team) is accessed using **XPath** for precise column selection:
  ```python
  date.append(match.find_element_by_xpath("./td[1]").text)
  home_team.append(match.find_element_by_xpath("./td[2]").text)
  score.append(match.find_element_by_xpath("./td[3]").text)
  away_team.append(match.find_element_by_xpath("./td[4]").text)
  ```

### Data Storage
- The extracted data is stored in a Python dictionary and converted into a Pandas DataFrame.
- The final DataFrame is saved as a CSV file (`All_matches_data_adamchoi.csv`) in the working directory.

### Browser Automation
- Once the scraping is complete, the Chrome browser is closed (ensure `driver.quit()` is uncommented in the script).

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/football-match-scraper.git
   ```
   
2. Set up your environment:
   - Ensure Python, Selenium, Pandas, and ChromeDriver are installed and configured correctly.

3. Run the script:
   ```bash
   python WebScrapingWithSelenium_adamchoi.py
   ```

4. Check the output:
   - After running the script, check for the CSV file named `All_matches_data_adamchoi.csv` in your working directory.
   
## Customization

- **Country Selection**: To scrape match data for another country, simply modify the following line:
  ```python
  dropdown.select_by_visible_text("Germany")
  ```
  Replace `"Germany"` with the desired country.

- **Browser Path**: Ensure the path to your ChromeDriver is correctly specified:
  ```python
  path = "/path/to/your/chromedriver"
  ```

## Potential Improvements

- **Dynamic Waiting**: Replace static sleep timers with Selenium's `WebDriverWait` to optimize performance and handle slow page loads more effectively.
- **Error Handling**: Implement additional error handling to ensure the script continues to run even if certain elements are not found or load times are slower than expected.
- **Multi-Country Scraping**: Enhance the script to scrape data from multiple countries in a single run.

