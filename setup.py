import tweepy
import settings as SETTINGS

def authorize():

    auth = tweepy.OAuthHandler(SETTINGS.CONSUMER_KEY, SETTINGS.CONSUMER_TOKEN)
    auth.set_access_token(SETTINGS.ACCESS_KEY, SETTINGS.ACCESS_TOKEN)

    api = tweepy.API(auth)
    
    print api.me().name
    return api

if __name__ == "__main__":
    authorize()
