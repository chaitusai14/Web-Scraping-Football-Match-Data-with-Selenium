from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import Select
import time

# For mac silicon users: Command to execute in terminal if chromedriver is
# not able to open the given website
# xattr -d com.apple.quarantine chromedriver

# Website to scrape football match data
website = "https://www.adamchoi.co.uk/overs/detailed"

# Path to your ChromeDriver, adjust this path based on your system
path = "/Users/saichaitanya/Downloads/chromedriver-mac-arm64/chromedriver"

# Initialize a new Chrome browser instance using the ChromeDriver
driver = webdriver.Chrome(path)

# Open the website with the Chrome browser
driver.get(website)

# Find and click the "All matches" button using XPath
all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()

# Select the country "Germany" from the dropdown using the 'id' of the dropdown element
dropdown = Select(driver.find_element_by_id("country"))
dropdown.select_by_visible_text("Germany") # Adjust the country name based on your preference

# Pause for 3 seconds to allow the page to load the filtered data
time.sleep(3)

# Retrieve all match data by finding all table row (<tr>) elements
matches = driver.find_elements_by_tag_name('tr')

# Initialize empty lists to store match data
date = []
home_team = []
score = []
away_team = []

# Loop through each row (match) and extract data from the columns
for match in matches:
    date.append(match.find_element_by_xpath("./td[1]").text)
    home_team.append(match.find_element_by_xpath("./td[2]").text)
    score.append(match.find_element_by_xpath("./td[3]").text)
    away_team.append(match.find_element_by_xpath("./td[4]").text)

# Create a dictionary with the extracted data
dict_matches = {'date':date, 'home_team':home_team, 'score':score, 'away_team':away_team}
df = pd.DataFrame(dict_matches)
print(df.head())
df.to_csv("All_matches_data_adamchoi.csv", index=False)
# driver.quit()
