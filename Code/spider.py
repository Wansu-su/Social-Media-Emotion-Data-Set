import tweepy as tw
from tweepy import OAuthHandler
import pandas as pd
import re

consumer_key = 'HyBSnEgNJGgN6yjyC0DA5X9AV'
consumer_secret = 'K0RDZqCIHs1bo5S8caueIPnUZM0niVXUMeB7RunZ1020V1bGaQ'
access_token = '1230280840283873281-okpIu4iqip6cIbs6Tl762G0fDe95Fo'
access_secret = 'CPZJzXb2IruMA7rGVauOAhCOrthqXhjd4xCT17ON0asHq'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

#need to remove retweets as they contain duplicate content
tfilter = " -filter:retweets"

emo1 ="#happy"
emo2 ="#pleasant"
emo3 ="#surprise"
emo4 ="#fear"
emo5 ="#angry"
emo6 ="#excitement"

positive =" :)"
negitive =" :("

#design the search words,the "-" is used to prevent the overlap hashtags
search_words1 = emo6 +" -"+emo1+" -"+emo2+" -"+emo3+" -"+emo4+" -"+emo5+tfilter

api = tw.API(auth,wait_on_rate_limit=True ,wait_on_rate_limit_notify=True)

tweets = tw.Cursor(api.search,
              q=search_words1,
              lang="en", tweet_mode='extended'
              ).items(200)


users_locs_text = [[tweet.id, tweet.full_text, tweet.created_at] for tweet in tweets]

#print([tweet.created_at for tweet in tweets])

tweet_table = pd.DataFrame(data=users_locs_text, 
                   columns=["id","text","created_at"])


tweet_table.to_csv("raw"+emo6+".csv", mode='a',encoding="utf-8")



#print([remove_url(tweet.text) for tweet in tweets])



