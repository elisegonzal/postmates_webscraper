from selenium import webdriver
import os
import time
import pandas as pd
import re
import numpy as np

def get_distance(address, file):
    # Chrome path
    chrome_path = os.path.join(os.getcwd(), 'chromedriver')
    # Set up chrome driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=chrome_path, options=options)

    df = file
    df['Distance to Delivery'] = np.NaN

    print(df.Link)

    for link in df.Link:
        driver.get(link)
        # Get distance
        distances = driver.find_elements_by_xpath("//div[@class='ba mj bb bw bx ff']")
        distances = [distance.text for distance in distances]
        distance_pattern = re.compile(re.search(r"[0-9]*[0-9].?[0-9]?\smi"))
        for distance in distances:
            if distance != '' and re.search(distance_pattern, distance):
                df[df['Link'] == link]['Distance to Delivery'] = distance
        distances = [re.search(distance_pattern, fee).group(0) for distance in delivery_fees 
                        if fee != '' and re.search(distance_pattern, fee)]

    # Close driver
    driver.close()
    # Return dataframe
    return df


if __name__ == '__main__':
    with open('postmates_scrape.csv') as csvfile:
        file = pd.read_csv(csvfile)
        df = get_distance("1 Apple Way", file)
    print(df)
    # price = get_price(link)
    # print(f"Resteraunt: {df.iloc[0]['Name']}")
    # print(f"Price: {price}")