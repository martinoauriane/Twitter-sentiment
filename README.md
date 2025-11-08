# Twitter-sentiment

![alt](./twitter.jpg)

Try to analyze the emotions of a tweet to determine whether it's on the overall neutral, positive or negative

Stack

Python

Pandas

Transformers

## Launch project

Start by running the script launch.sh. Running this script will enable you to install all required dependencies, as well as creating a venv environnement compatible with python updates and libraries installation with pip.

```
bash launch.sh
```

## From csv to DataFrame with pandas library

First, we collect, the data that interest us via a csv file. Then, we use the library Pandas to get an exploitable array, a DataFrame.

## Assessing sentiment with transformers library

After having cleaned our DataFrame, using the likes of a cleanTweet function and dropping undefined values, we use the transformers library to affect a score to every tweet.

#### Why not Text Blob?

Transformers is powerful Python library created by Hugging Face that allows you to use open-source AI models. In our case it's a helpful use, as we need AI to analyze the sentiment of a tweet. We could have used TextBlob instead of Transformers, but the result would not have been the same. Text blob doesn't use AI model to infer sentiment. While it's more CPU friendly, it's clearly not as accurate. The main issue is it doesn't really understand context.

For example, accordint to the context of the sentence, "good" can either be positive or negative. For example, we humans know that "It was not good" is a negative tweet. However, Text Blob would simply tokenize this sentence and attribute a score to each world. "not" and "good" would end up giving a pretty neutral score to this sentence, while we humans clearly know it's a negative tweet. Hence the use of NLP AI.

## Statistics vizualisation

Once this score is established, we can visualize the frequency of neutral, positive and negative tweets.
