""" Get the title of the free book of the day from Packt Publishing and tweet
about it."""

import tweepy
import requests
from bs4 import BeautifulSoup, SoupStrainer

import config


def parse_book_title():
    """Extract title of the free book of the day from the Packt website."""
    try:
        html = requests.get(config.URL, headers=config.HEADERS).text
    except Exception as e:
        print(f'Error requesting Packt URL: {e}')
        return None

    h2_tags = SoupStrainer('h2')
    soup = BeautifulSoup(html, "html.parser", parse_only=h2_tags)
    title = soup.find('h2').string.strip()
    return title


def update_twitter_status(tweet_body):
    """Post tweet_body as tweet to users timeline."""
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    try:
        api.update_status(tweet_body)
        return f'Tweet posted: {tweet_body}'
    except Exception as e:
        print(f'Error posting tweet: {e}')
        return None


if __name__ == '__main__':
    book_title = parse_book_title()
    tweet_body = ('Free Python book over at Packt today: '
                  f'{book_title} http://bit.ly/2yTdfIz')
    if book_title and 'python' in book_title.lower():
        print(update_twitter_status(tweet_body))
    else:
        print('Book title not tweeted: "', book_title, '"')
