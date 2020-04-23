import twitter
import time
import pandas as pd


def gather(search_keyword):
    final = pd.DataFrame.from_dict({'text': ['0'], 'date': ['0'], 'favs': [0], 'retweet': [0]})
    for i in range(100):
        tweets_fetched = twitter_api.GetSearch(search_keyword, count=150, lang="en", since="2019-01-01")
        for status in tweets_fetched:
            tweet_info = {"text": status.full_text,
             "date": status.created_at,
             "favs": status.favorite_count,
             "retweet": status.retweet_count}
            final = final.append(tweet_info, ignore_index = True)
        final.drop(0).to_csv("full {} 3.csv".format(str(searchterm)), index=False)
        time.sleep(960)


# initialize api instance and set search term
twitter_api = twitter.Api(consumer_key='0CclE9gqNjQ0q33243DLwBrvs',
                          consumer_secret='WILMfZp0Udp4FBw0lOUrukzzHkQzIIDXXFdB1acdvtQyak6rxS',
                          access_token_key='1247729640363433984-W0srSXnxhXw3aDqJxs3z7PWJrNyNxu',
                          access_token_secret='zOXfkmFc3eIoTdwQ0rteswrwFnMdODZdqHQBoY6LtLSew',
                          tweet_mode = "extended")

searchterm = "bitcoin"

# main
time.sleep(960)
gather(searchterm)
