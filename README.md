# Sentiment_analysis
The specific task will be to collect a dataset and perform first analysis on it. To build this application, you will crawl Telegram messages, filter non-English messages, and compute the average sentiment over time.

1. The name of the student:
	Yerkebulan Bauyrzhanov (only one)

2. Datasource:

Data (the Telegram messages) was exported from https://t.me/CryptoComOfficial from May 1 to and including May 15, 2021. Data format: JSON.

3. Requirements:
Unzip files from the zip file in one directory. I use python version 3.8. 'Yerke_sentiment_analysis.py' script and static data are located in main folder.
Please check out requirements.txt to know about requirements according to software.

4. Libraries used in this project:

json, pandas, re, tqdm, textblob, plotly.express, langdetect

For sentiment analysis I used textblob library which is another extremely powerful NLP library for Python. TextBlob is built upon NLTK and provides an easy to use interface to the NLTK library. We will see how TextBlob can be used to perform a variety of NLP tasks ranging from parts-of-speech tagging to sentiment analysis, and language translation to text classification.. 

5. How to run Yerke_sentiment_analysis.py from the command line:


command: python .\Yerke_sentiment_analysis.py
purpose: read data from main folder, and do analysis.  
result: a plot of the number of messages per day and the average sentiment per day

Summary:

We can conclude that:

There were more negative messages on May 5, 2021 and May 11, 2021.

There were more positive messages on other days.
