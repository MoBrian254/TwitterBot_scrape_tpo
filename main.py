import tweepy
import json
import time

# Set up your Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Search for tweets related to tree planting organizations
query = "tree planting organization"
tweets = tweepy.Cursor(api.search, q=query, tweet_mode='extended').items(10)

# Like, follow, and scrape tweets
results = []
for tweet in tweets:
    try:
        # Like the tweet
        api.create_favorite(tweet.id)
        time.sleep(5)

        # Follow the user
        api.create_friendship(tweet.user.screen_name)
        time.sleep(5)

        # Scrape tweet information
        tweet_info = {
            'user': tweet.user.screen_name,
            'text': tweet.full_text,
            'created_at': str(tweet.created_at),
            'favorite_count': tweet.favorite_count,
            'retweet_count': tweet.retweet_count
        }
        results.append(tweet_info)
    except tweepy.TweepError as e:
        print(f"Error processing tweet {tweet.id}: {e}")

# Output results to a JSON file
output_file = 'twitter_results.json'
with open(output_file, 'w') as json_file:
    json.dump(results, json_file, indent=4)

print(f"Bot finished. Results saved to {output_file}")
