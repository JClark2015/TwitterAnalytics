from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv
import pandas as pd

with open('tweets.csv', mode='r', encoding='utf-8') as tweet_file:
	df = pd.read_csv(tweet_file)	
tweet_file.close()

words = WordCloud().generate(str(df['tweet_text']))

# Generate plot
plt.imshow(words)
plt.axis("off")
plt.show()


