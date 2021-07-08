# Tweets' Sentiment By Topic 

This project allows you to search Twitter for tweets about a certain topic, then shows you the sentiment / mood of the tweet (not happy, neutral, glad).

## Script Structure

This project uses two libraries:

- `tweetpy`: to connect to the Twitter API.
- `textblob`: to parse the info returned with each tweet.

## Customising The Code

1. Create a [Twitter Developer account](https://developer.twitter.com).
2. Create a new app there.
3. Copy the new app's credentials and paste them in their related variables in this code:
   `apiKey`, `apiSecretKey`, `accessToken`, and `accessTokenSecret`.
4. To amend the topic that you woud like to search for its sentiments in Twitter, edit the following string used in this variable:
   `publicTweets = api.search('Trump')`

## How To Run

Depending of your running version of Python, In the terminal type 

```
python index.py 
```

or 

```
python3 index.py
```

You should get a list of tweets about the topic you are searching for in the following format:

```
Tweet text
Emoji
Line separator
```

.
