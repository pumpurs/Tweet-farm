from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time 
import json

ckey = 'consumer key'
csecret = 'comsumer seecret'
atoken = 'a token'	
asecret = 'a seecret'  


class listener(StreamListener):
    def on_data(self, data):

        tweet = json.loads(data)
        
        #print time.time()
        text = tweet['text']
        name = tweet['user']['name']
        screenName = tweet['user']['screen_name']

        print name.encode('utf-8')
        print text.encode('utf-8')
        print '\n'
         
        # into the data file
        with open('minedData', 'a') as outfile:
            json.dump({'time': time.time(), 'screenName': screenName, 'text': text, 'name': name}, outfile, indent = 4, sort_keys=True)
            #outfile.write(',')
            outfile.write('\n')

        return True

    def on_error(self, status):
        print status


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["positivus"])

