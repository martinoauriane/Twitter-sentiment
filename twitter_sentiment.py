from transformers import pipeline
import pandas as pd
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# smaller, CPU-friendly model
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment"
)

## STEP 1: CREATE A DATAFRAME
df = pd.read_csv('./Tweets.csv')
df = df.dropna(subset=['text']) ## droping undefined values
df['CLEANEDTWEETS']=''
df['SENTIMENT']=0


## STEP 2: CLEAN TWEET
def cleanTweet(tweet):
  tweet = re.sub('@[A-Za-z0-9_]+', '', tweet) #removes @mentions
  tweet = re.sub('#', '', tweet) #removes hastag '#' symbol
  tweet = re.sub('\n', ' ', tweet)
  return tweet

df['CLEANEDTWEETS'] = df['text'].apply(cleanTweet) #apply cleanTweet function to the tweet

## STEP 3: DETERMINE WHETER A TWEET IS POSITIVE OR NEGATIVE

def get_sentiment(tweet):
  results = sentiment_pipeline(tweet) ## For that we're using sentiment_pipleine for transformers
  if not results:
        return 0, 'Neutral' 
  best = max(results, key=lambda x: x['score'])
  if best['label'] == 'LABEL_0':
        return -1, 'Negative'
  elif best['label'] == 'LABEL_1':
        return 0, 'Neutral'
  else:  
        return 1, 'Positive'

df[['SCORE','ANALYSIS']] = df['CLEANEDTWEETS'].apply(lambda x: pd.Series(get_sentiment(x)))
df = df.drop('selected_text', axis=1)

## STEP 4: CREATE STATISTICS ON FREQUENCY OF POSITIVE / NEGATIVE / NEUTRAL TWEETS

## exemple: Count occurrences of values in 'Name' column grouped by 'Age'
## grouped_counts = df.groupby('Age')['Name'].value_counts()
## the name Alice appears 25 times, Bob 30 times, Charlie 35 times. 

def getStatistics(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'

statistics = df['ANALYSIS'].value_counts() ## DataFrame.value_counts(): this function returns a series containing the frequency of each distinct row in the DataFrame.
print(statistics)

## Now, we can represent graphically thoses statistics. We're ploting a bar graph to show count of tweet sentiment
fig = plt.figure(figsize=(7,5))
color = ['green','grey','red']
statistics.plot(kind='bar',color = color)
plt.title('Value count of tweet polarity')
plt.ylabel('Count')
plt.xlabel('Polarity')
plt.grid(False)
plt.show()