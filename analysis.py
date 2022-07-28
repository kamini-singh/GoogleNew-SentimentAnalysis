import pandas as pd
from textblob import TextBlob
df=pd.read_csv("url")
polarity_score=[]

for i in range(0, df.shape[0]):
    score=TextBlob(df.iloc[i][0])
    score1= score.sentiment[0]
    polarity_score.append(score1)

df=pd.concat([df, pd.Series(polarity_score)], axis=1)
df.rename(columns={df.colums[1]: "sentiment"}, inplace= True)
total=len(df[df.sentiment])
positive=len(df[df.sentiment>.1]) / total
negative=len(df[df.sentiment<0])/ total

