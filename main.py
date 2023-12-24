from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

url_path = "https://carrierrate.globaltranz.com/cr2/Account/Login"
driver.get(url_path)
user_name = driver.find_element(By.XPATH, '//*[@id="txtUserName"]')
password = driver.find_element(By.XPATH, '//*[@id="txtPassword"]')
login = driver.find_element(By.XPATH, '//*[@id="login_wrapper"]/div[2]/div/div[1]/div[4]/div[2]/input')
user_name.send_keys('blossomhill')
password.send_keys('Shipping107')
login.click()

time.sleep(30)

foam_1 = driver.find_element(By.XPATH, '//*[@id="reportGrid"]/div/div[2]/div[2]/div/div[1]/div/div[1]/div')
foam_1.click()

time.sleep(10)

# Get the page source after the dynamic content is loaded
page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')
tables = soup.find_all('table')

# Initialize a list to hold data for all tables
all_table_data = []

# Iterate through each table
for table_index, table in enumerate(tables):
    print(f"Processing Table {table_index + 1}")

    # Extract table data into a list of dictionaries for each table
    table_data = []

    # Find all rows in the table
    rows = table.find_all('tr')

    # Check if there are rows available
    if rows:
        # Extract headers from the first row
        headers = [header.text.strip() for header in rows[0].find_all(['th', 'td'])]
        print("Headers:", headers)

        for row_index, row in enumerate(rows[1:]):
            row_data = {headers[i]: cell.text.strip() for i, cell in enumerate(row.find_all(['th', 'td']))}
            table_data.append(row_data)
            print(f"Row {row_index + 1} Data:", row_data)

        # Append table data to the list for all tables
        all_table_data.extend(table_data)
    else:
        print("No rows found in the table.")
    print()

# Convert the table data for all tables to JSON
if all_table_data:
    json_data = json.dumps(all_table_data, indent=2)
    print("JSON Data:", json_data)

    # Save the JSON data to a text file
    with open('all_table_data.txt', 'w') as file:
        file.write(json_data)
    print("Data saved to 'all_table_data.txt'")
else:
    print("No tables found on the page.")

# ... (rest of your existing code)

driver.quit()