from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time

# Initialize a WebDriver
chrome_driver_path = 'C:/Users/rishi/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# URL of the page to scrape
base_url = "https://www.shanghairanking.com/rankings/arwu/2023"

# Open the initial page
driver.get(base_url)

# Create an empty DataFrame to store all results
df = pd.DataFrame(columns=['Rank', 'University'])

page_counter = 1  # Initialize page counter

while True:
    if page_counter > 35:  # Check if page counter exceeds 35
        print("Reached page limit of 35, stopping script.")
        break

    try:
        # Wait for the table to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "rk-table")))

        # Extract data from the table
        table = driver.find_element(By.CLASS_NAME, "rk-table")
        for row in table.find_elements(By.TAG_NAME, 'tr')[1:]:  # Skip the header row
            cols = row.find_elements(By.TAG_NAME, 'td')
            rank = cols[0].text.strip()
            university = cols[1].text.strip().split('\n')[0]  # Get the university name
            print(rank,university)
            # Append data to DataFrame
            df = df.append({'Rank': rank, 'University': university}, ignore_index=True)

        # Find the 'Next' button and click
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ant-pagination-next"))
        )
        next_button = driver.find_element(By.CLASS_NAME, "ant-pagination-next")
        next_button.click()

        # Increment page counter and print it
        page_counter += 1
        print(f"Clicked 'Next' button, now moving to page {page_counter}")

        # Wait for the page to load before proceeding to the next iteration
        time.sleep(5)

    except NoSuchElementException:
        # 'Next' button is not found, break the loop (end of pagination)
        print("Reached the last page.")
        break
    except Exception as e:
        print(f"An error occurred on page {page_counter}: {str(e)}")
        break

# Close the WebDriver
driver.quit()

# Print the DataFrame
print(df)

df.to_csv("shanghai.csv",index=False)

