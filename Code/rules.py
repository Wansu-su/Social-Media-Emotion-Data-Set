import pandas as pd
import emoji
import re

from emotion_predictor import EmotionPredictor


# Pandas presentation options
pd.options.display.max_colwidth = 150   # show whole tweet's content
pd.options.display.width = 200          # don't break columns
pd.options.display.max_columns = 8      # maximal number of columns

#replace emojis with the text expression 
def process_emoji(tweet):

    tweet = emoji.demojize(tweet)
    tweet = tweet.replace(":"," ")
    tweet = ' '.join(tweet.split())

    return tweet

def removeContent(df:str, colname:str, *args):
    sens ='df[{}]'.format("|".join(["df.{}.str.contains('"'{}'"')".format(colname,x) for x in list(args)]))
    df_other_list1 = list(eval(sens)[colname])
    df_other_list2 = list(df[colname])
    ret = list(set(df_other_list2) ^ set(df_other_list1))
    result = df[df[colname].isin(ret)]
    return result    


tweets_table = pd.read_csv("clean#excitement.csv",usecols=["id","created_at","new_text"])

model = EmotionPredictor(classification='ekman', setting='mc', use_unison_model=True)
predictions = model.predict_classes([process_emoji(tw) for tw in tweets_table.new_text.tolist()])
#print(predictions, '\n')

tweets_table["emotion"]=predictions["Emotion"].tolist()

result=removeContent(tweets_table.astype(str),"emotion", 'Disgust', 'Fear','Sadness')

#print(result)
print(result.shape[0])
result=result.drop(['emotion'],axis=1)

result.to_csv("cs_excitement.csv", mode='a',encoding="utf-8",index=None)
