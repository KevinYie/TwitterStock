We are trying to predict stock behavior with LSTM models and the addition of twitter sentiments at the granularity at the level of per day sentiments. 

Sentiment analysis of gathered tweets are executed using VADER, BERT (trained on Sentiment140 dataset), as well as an LSTM classifier trained on manually curated twitter sentiment dataset. 

Stock data is obtained through Yahoo Finances and Twitter data is sourced directly from the API.
