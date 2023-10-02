import pandas as pd
from numpy import NaN
import re
import nltk
import datetime
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from pandas_data_handler import download_csv_to_dataframe,get_online_csv_into_df_list

def get_coin_symbol(coin_name):
        if coin_name == 'bitcoin':
            return 'BTC'
        if coin_name == 'ethereum':
            return 'ETH'
        if coin_name == 'tether':
            return 'USDT'
        if coin_name == 'binancecoin':
            return 'BNB'
        if coin_name == 'xrp':
            return 'XRP'
        if coin_name == 'litecoin':
            return 'LTC'
        if coin_name == 'usdcoin':
            return 'USDC'
        if coin_name == 'dogecoin':
            return 'DOGE'
        if coin_name == 'tron':
            return 'TRX'
        if coin_name == 'binance_usd':
            return 'BUSD'
        return coin_name.upper()



def preprocess_text(text):
    # Preprocessing function
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    if isinstance(text, str):
        # remove punctuation and special characters
        text = re.sub(r'[^\w\s]', '', text)  # r'[^\w\s]' : matches any character that is not a word character (alphanumeric or underscore) or a whitespace character
        # convert to lowercase
        text = text.lower()
        # tokenize text
        tokens = nltk.word_tokenize(text)
        # remove stop words
        tokens = [token for token in tokens if token not in stop_words]
        # lemmatize text
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
        # join tokens back into text
        text = ' '.join(tokens)
    return text



def analyze_sentiment(resources):
    df_list, df_titles = get_online_csv_into_df_list(resources)
    
    df_list_results = []
    
    for [df,text_column],df_title in zip(df_list,df_titles):
        # Remove rows with "na" values
        df = df.dropna(subset=[text_column])

        # Fill missing values in text_column column with an empty string
        df[text_column] = df[text_column].fillna('')
        # to lower text
        df[text_column] = df[text_column].str.lower()
        # Preprocess the text_column column
        df[text_column] = df[text_column].apply(preprocess_text)
        
        # Initialize the VADER sentiment analyzer
        sid = SentimentIntensityAnalyzer()

        # Calculate sentiment scores and add them to the DataFrame
        df['scores'] = df[text_column].apply(lambda tweet_text: sid.polarity_scores(tweet_text))
        df['compound'] = df['scores'].apply(lambda score_dict: score_dict['compound'])
        df = df.drop('scores', axis=1)
        if df_title == 'crypto_tweets':
            df['new_coins'] = df['new_coins'].apply(lambda coins_string: [get_coin_symbol(coin) for coin in coins_string[1:-1].split(',')])
                
        # Create a new column for sentiment_type and classify based on the compound score
        df['sentiment_type'] = df['compound'].apply(lambda avg_compound: 'POSITIVE' if avg_compound > 0 else 'NEUTRAL' if avg_compound == 0 else 'NEGATIVE')
        df_list_results.append(df)

    return df_list_results,df_titles

