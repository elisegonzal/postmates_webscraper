import pandas as pd
import csv
import re

with open('postmates_scrape.csv') as file:
    df = pd.read_csv(file)
    print(len(df))
    pickup_pattern = re.compile(r"\?diningMode=PICKUP$")
    pickup_links = [link for link in df['Link'] if re.search(pickup_pattern, link)]
    # pickup_i = []
    # df.drop(df.index[df.Link.any() in pickup_i], inplace=True)
    df = df[~df['Link'].isin(pickup_links)]
    # print([df.index[df.Link == i] for i in df["Link"]])
    print(len(df))