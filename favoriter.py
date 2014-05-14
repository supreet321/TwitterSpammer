import tweepy
import setup
import time
import sys

def get_timeline(name, counts):
    api = setup.authorize()

    statuses =  api.user_timeline(screen_name=name, count=counts)
    
    for status in statuses:
        id = status.id_str
        api.create_favorite(id)
        time.sleep(5)        

if __name__ == "__main__":
    name = sys.argv[1]
    count = sys.argv[2]
    get_timeline(name, count)
