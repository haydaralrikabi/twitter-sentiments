import tweepy
from textblob import TextBlob

apiKey = 'api key here'
apiSecretKey = 'api secret key here'
accessToken = 'access token here'
accessTokenSecret = 'access token secret here'

# Create the authentication variable.
# Format keys for tweepy's processing.
auth = tweepy.OAuthHandler(apiKey, apiSecretKey)
auth.set_access_token(accessToken, accessTokenSecret)

# Access Twitter's API
api = tweepy.API(auth)

# Search Twitter for tweets that contain the word 'Trump', as an example
publicTweets = api.search('Trump')

for tweet in publicTweets:
    # Select just the text string from all the other tweet's info
    print(tweet.text)
    analysis = TextBlob(tweet.text)

    if (analysis.sentiment.polarity < 0):
        print('Not Happy -> ' + '\U0001F621')
    elif (analysis.sentiment.polarity > 0):
        print('Glad -> ' + '\U0001F600')
    else:
        print('Neutral -> ' + '\U0001F610')

    print('--------------------')
