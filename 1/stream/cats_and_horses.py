from constants import CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
from datetime import timedelta, datetime
from time import sleep
from twitter import TwitterStream
from utils import oauth_login, save_json

track = "Broncos, Panthers"  # Tweets for Broncos OR Panthers
locations = '-73.313057,41.236511,-68.826305,44.933163'  # New England geo zone

NUMBER_OF_COLLECTIONS = 5
COLLECTION_TIME = 2.5  # in minutes
WAIT_TIME = 10  # in minutes

date_format = '%m/%d/%Y %H:%M:%S'

broncos, panthers, counts = [], [], []
for counter in range(1, NUMBER_OF_COLLECTIONS + 1):
    print '------------------------------------------'
    print 'COLLECTION NUMBER', counter
    broncos_counter, panthers_counter = 0, 0
    count_dict = {'start_time': datetime.now().strftime(format=date_format)}

    # Create a stream instance
    auth = oauth_login(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, token=OAUTH_TOKEN, token_secret=OAUTH_TOKEN_SECRET)
    twitter_stream = TwitterStream(auth=auth)
    stream = twitter_stream.statuses.filter(track=track, locations=locations)

    endTime = datetime.now() + timedelta(minutes=COLLECTION_TIME)
    while datetime.now() <= endTime:  # collect tweets while current time is less than endTime
        for tweet in stream:
            if 'text' in tweet.keys():
                if datetime.now() > endTime:
                    break
                elif 'Broncos' in tweet['text'] and 'Panthers' in tweet['text']:
                    broncos.append(tweet), panthers.append(tweet)
                    broncos_counter += 1
                    panthers_counter += 1
                    print 'Panthers: %s, Broncos: %s' % (panthers_counter, broncos_counter)
                elif 'Broncos' in tweet['text']:
                    broncos.append(tweet)
                    broncos_counter += 1
                    print 'Broncos: %s' % broncos_counter
                elif 'Panthers' in tweet['text']:
                    panthers.append(tweet)
                    panthers_counter += 1
                    print 'Panthers: %s' % panthers_counter
                else:
                    print 'continue', tweet['text']
                    continue
        count_dict['broncos'] = broncos_counter
        count_dict['panthers'] = panthers_counter
        count_dict['end_time'] = datetime.now().strftime(format=date_format)
        counts.append(count_dict)

    print counts
    if counter != NUMBER_OF_COLLECTIONS:
        print 'Sleeping until %s' % (datetime.now() + timedelta(minutes=WAIT_TIME))
        sleep(WAIT_TIME * 60)
    else:
        print '------------------------------------------'

save_json('json/counts', counts)
save_json('json/broncos', broncos)
save_json('json/panthers', panthers)
