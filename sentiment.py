import pandas as pd
from textblob import TextBlob

postsdf = pd.read_csv('C:\dnd sentiment project\posts\posts.csv')
commentsdf = pd.read_csv('C:\dnd sentiment project\comments\comments.csv')

def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

postsdf['Sentiment'] = postsdf['title'].apply(get_sentiment)
commentsdf['Sentiment'] = commentsdf['body'].apply(get_sentiment)

postsdf.to_csv('C:\dnd sentiment project\posts\sentimentposts.csv', index=False)
commentsdf.to_csv("C:\dnd sentiment project\comments\sentimentcomments.csv", index=False)

print("Sentiment analysis completed and saved to output files.")