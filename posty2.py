from selenium import webdriver
import os
import time
import pandas as pd

def check_address(address):

    # Chrome path
    chrome_path = os.path.join(os.getcwd(), 'chromedriver')
    # Set up chrome driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(chrome_path, options=options)
    driver.get("https://postmates.com/")
    # Get element with id=location-typeahead-home-input
    element = driver.find_element_by_id("location-typeahead-home-input")
    # Enter text in element
    element.send_keys(address)
    # Get button with text="Find Food"
    time.sleep(2)
    button = driver.find_element_by_xpath("//button[text()='Find Food']")
    # Click button
    button.click()
    # Wait for page to load
    time.sleep(10)
    # Get span with text="Delivery Time"
    span = driver.find_element_by_xpath("//span[text()='  Delivery time']")
    span.click()
    time.sleep(10)
    # Get list of results
    names_raw = driver.find_elements_by_xpath("//h3")
    # Parse names
    names = [name.text for name in names_raw]
    # Get link to each result page where dev class='ag ci' with child a href
    links_raw = driver.find_elements_by_xpath("//div[@class='ag ci']/a")
    # Parse links
    links = [link.get_attribute('href') for link in links_raw]
    # Get list of wait times
    wait_times = driver.find_elements_by_xpath("//div[@class='ba bv e1 bw bx fe']")
    # Parse wait times
    wait_times = [wait_time.text for wait_time in wait_times]
    # Exclude empty strings
    wait_times = [wait_time for wait_time in wait_times if wait_time != '']

    # Print length of lists
    print(f"Names:{names[0:15]}")
    print(f"Wait Times:{wait_times[0:15]}")
    print(f"Links:{links[0:15]}")
    # print(ratings[0:15])

    # Combine  names, wait times, and links into a dataframe
    df = pd.DataFrame({'Name': names, 'Wait Time': wait_times, 'Link': links})
    # Close driver
    driver.close()
    # Return dataframe
    return df

# # Given link to restaurant page, return delivery fee
# def get_price(link):
#     # Chrome path
#     chrome_path = os.path.join(os.getcwd(), 'chromedriver')
#     # Set up chrome driver
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     driver = webdriver.Chrome(chrome_path, options=options)
#     driver.get(link)
#     # Get fee
#     fee = driver.find_element_by_xpath("//span[@class='ah bh']").text
#     # Close driver
#     driver.close()
#     return fee


if __name__ == '__main__':
    df = check_address("1 Apple Way")
    print(df)
    # price = get_price(link)
    # print(f"Resteraunt: {df.iloc[0]['Name']}")
    # print(f"Price: {price}")