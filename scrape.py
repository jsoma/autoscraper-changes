import requests

import pandas as pd
from bs4 import BeautifulSoup

response = requests.get("https://www.bbc.com/")
doc = BeautifulSoup(response.text, 'html.parser')

stories = doc.select('.media-list__item')

rows = []

for story in stories:
    row = {}

    row['title'] = story.select_one('h3').text.strip()

    try:
        row['href'] = story.select_one('.media__link, .reel__link')['href']
    except:
        pass

    try:
        row['tag'] = story.select_one('.media__tag').text.strip()
    except:
        pass

    try:
        row['summary'] = story.select_one('.media__summary').text.strip()
    except:
        pass

    rows.append(row)

df = pd.DataFrame(rows)
df.to_csv("bbc-headlines.csv", index=False)
