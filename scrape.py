import csv
from twitterscraper import query_tweets

if __name__ == '__main__':
	keyword = input("Enter key word to scrape tweets:")

	with open('tweets.csv', mode='w', encoding='utf-8') as tweet_file:
		fnames = ['tweet_id', 'tweet_text']
		tweet_writer = csv.DictWriter(tweet_file, fieldnames=fnames)
		
		tweet_writer.writeheader()
		for tweet in query_tweets(str(keyword), 10):
			tweet_writer.writerow({'tweet_id': int(tweet.id),
'tweet_text': str(tweet.text)})		
		tweet_file.close()

 