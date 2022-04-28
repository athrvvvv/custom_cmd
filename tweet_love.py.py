import tweepy

CONSUMER_KEY = 'API KEY'
CONSUMER_SECRET = 'API KEY SECRET'
ACCESS_TOKEN = 'ACCESS TOKEN'
ACCESS_TOKEN_SECRET = 'ACCESS TOKEN SECRET'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

status = "Testing!"
api.update_status(status=status)
