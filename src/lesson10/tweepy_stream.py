import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import pprint

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="KMjHlUfyPYKKUeAe0RDHNR9hF"
consumer_secret="N6BAq3tBDYJFifOf3x2BY6GVrQsSNAv6UtyjDD3vfd5JVurZeh"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="24120310-glx1bRsJQImQqMH1pVWaQPC1SwypiMF0rOxnh4zbw"
access_token_secret="YsIF5OegErPZhVShiY9jJhJihmYZ4HP4yc1VBJuu4wmmf"

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
This is a basic listener that just prints received tweets to stdout.

"""
    def on_data(self, data):
        # data_str = data.decode('string_escape').strip()
        data_json = json.loads(data)
        print data_json['text'].encode('utf-8')
        sys.stdout.flush()
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=[sys.argv[1]])
