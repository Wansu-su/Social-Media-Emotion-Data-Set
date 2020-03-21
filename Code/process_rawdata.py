import pandas as pd
import emoji
import re
import itertools
#process  linguistic anomalies ,such as spelling mistakes
from spelling_correct import correct_text_generic
#from emotion_predictor import EmotionPredictor


# Pandas presentation options
#pd.options.display.max_colwidth = 150   # show whole tweet's content
#pd.options.display.width = 200          # don't break columns
#pd.options.display.max_columns = 8      # maximal number of columns

def remove_url(tweet):
    # Preprocessing the tweets

    tweet = re.sub(r"^https://t.co/[a-zA-Z0-9]*\s", " ", tweet)
    tweet = re.sub(r"\s+https://t.co/[a-zA-Z0-9]*\s", " ", tweet)
    tweet = re.sub(r"\s+https://t.co/[a-zA-Z0-9]*$", " ", tweet)
  # tweet = tweet.lower()
    '''
    correct the misspelled words but just checking that 
    each character should occur not more than 2 times in every word.  

    '''
    tweet = ''.join(''.join(s)[:2] for _, s in itertools.groupby(tweet))

    return tweet




file_raw = 'raw#excitement.csv'
file_new = 'clean#excitement.csv'
# read the raw data draw a table;
tweets_table = pd.read_csv(file_raw,usecols=["id","text","created_at"])
raw_rows =len(tweets_table)
print (raw_rows)


#step1:  according to the raw data ,write the correct functions to clean the data
#remove urls and linguistic anomalies

clean_text=[correct_text_generic(remove_url(tw)) for tw in tweets_table.text.tolist()]


new_table=tweets_table.drop('text',axis=1,inplace=False)
new_table["new_text"]=clean_text

# step2: check and delete duplicated data
print(new_table.new_text.duplicated(keep ="first"))
new_table=new_table.drop_duplicates(subset=['new_text'],keep ="first")

print(new_table)
print ("duplicated tweets are "+ str(len(new_table)-raw_rows))




new_table.to_csv(file_new, mode='a',encoding="utf-8")









