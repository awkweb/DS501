from constants import CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
from twitter import TwitterStream
from utils import oauth_login, save_json

track = "Patriots"  # Tweets for Patriots

TOTAL_TWEETS = 2500

patriots = []
patriots_counter = 0

while patriots_counter < TOTAL_TWEETS:  # collect tweets while current time is less than endTime
    # Create a stream instance
    auth = oauth_login(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                       token=OAUTH_TOKEN, token_secret=OAUTH_TOKEN_SECRET)
    twitter_stream = TwitterStream(auth=auth)
    stream = twitter_stream.statuses.filter(track=track)
    counter = 0
    for tweet in stream:
        if patriots_counter == TOTAL_TWEETS:
            print 'break'
            break
        elif counter % 500 == 0 and counter != 0:
            print 'get new stream'
            break
        else:
            patriots.append(tweet)
            patriots_counter += 1
            counter += 1
            print patriots_counter, counter

save_json('json/patriots', patriots)
