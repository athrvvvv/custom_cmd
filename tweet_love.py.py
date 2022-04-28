import tweepy

CONSUMER_KEY = 'fbTwwtc05OtCpmk0FlSJCihM7'
CONSUMER_SECRET = 'KjV104KT5GBlZqF30yqbaK9Pem8moz65CCayMgmEegOapZSM6P'
ACCESS_TOKEN = '1476579939939803138-PpQdtfO4CoxwBrhYmyLokFINbKJOPm'
ACCESS_TOKEN_SECRET = 'pgPjrKzhFXECMrau04uFumflwoO24a1quKz1cjAOqH4Aq'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

status = "Testing!"
api.update_status(status=status)
