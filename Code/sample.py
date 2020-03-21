import pandas as pd



tweets_table = pd.read_csv("cs_happy.csv",usecols=["id","created_at","new_text"])

sample_list =tweets_table[tweets_table.index%7==0].head(20)

print(sample_list)

sample_list.to_csv("sample_happy.csv", mode='a',encoding="utf-8",index=False)
