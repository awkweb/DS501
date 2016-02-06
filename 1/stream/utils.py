import io
import json
import twitter


def oauth_login(token, token_secret, consumer_key, consumer_secret):
    """
    Snag an auth from Twitter
    """
    auth = twitter.oauth.OAuth(token, token_secret,
                               consumer_key, consumer_secret)
    return auth


def save_json(filename, data):
    """
    Save json data to a filename
    """
    print 'Saving data into {0}.json...'.format(filename)
    with io.open('{0}.json'.format(filename),
                 'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))


def load_json(filename):
    """
    Load json data from a filename
    """
    print 'Loading data from {0}.json...'.format(filename)
    with open('{0}.json'.format(filename)) as f:
        return json.load(f)