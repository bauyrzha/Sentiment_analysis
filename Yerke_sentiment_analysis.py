# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 21:49:47 2021

@author: Yerke
"""

#import necessary libraries
import json
import pandas as pd
import re
from tqdm import tqdm
from textblob import TextBlob
import plotly.express as px
from langdetect import detect

# Opening JSON file
f = open('result.json', encoding="utf8")
# returns JSON object as
# a dictionary
data = json.load(f)
messages = data['messages']
# Iterating through the json
# list
listo = []
for i in tqdm(messages):
    s = i['text']
    if 'SHIB' in s or 'DOGE.' in s:
        listo.append(i)
# Closing file
f.close()

# Remove Non-English messages 
# using search() to get only those strings with alphabets
clean_data = []
for i in tqdm(listo):
    s = i['text']
    if detect(s) == 'en':
        clean_data.append(i)
df = pd.DataFrame.from_dict(clean_data)

# leave only necessary columns
df = df[['date', 'text']] 

#create a functiom to clean data from emoji
def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

# remove emoji from data
df['text'] = df['text'].apply(remove_emoji)

# create a function to get the polarity 
def getPolarity(text):
    return TextBlob(text).sentiment.polarity

# create a new column
df['Polarity'] = df['text'].apply(getPolarity)


# Changing object type column to datetime
df['date'] = pd.to_datetime(df.date)

# Creating new column with just the date
df['date'] = df['date'].dt.date

# Get the average sentiment per day
df2 = df.groupby(df['date']).mean()

# reset index
df2 = df2.reset_index()

fig = px.bar(df2, x=df2['date'], y=df2['Polarity'])
fig.show()
