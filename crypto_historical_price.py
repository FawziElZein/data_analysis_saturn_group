from yahoofinancials import YahooFinancials
import pandas as pd
from pandas_data_handler import return_create_statement_from_df,return_insert_into_sql_statement_from_df
from database_handler import execute_query,create_connection,parse_date_columns
from lookups import InputTypes

def get_coin_name(coin_symbol):

    if coin_symbol == 'BTC':
        return 'bitcoin'
    if coin_symbol == 'ETH':
        return 'ethereum'
    if coin_symbol == 'USDT':
        return 'tether'
    if coin_symbol == 'BNB':
        return 'binancecoin'
    if coin_symbol == 'XRP':
        return 'xrp'
    if coin_symbol == 'LTC':
        return 'litecoin'
    if coin_symbol == 'USDC':
        return 'usdcoin'
    if coin_symbol == 'DOGE':
        return 'dogecoin'
    if coin_symbol == 'TRX':
        return 'tron'
    if coin_symbol == 'BUSD':
        return 'binance_usd'
    return 'unknown'

def get_historical_prices():
    tickers = ['BTC-USD', 'ETH-USD', 'USDT-USD','BNB-USD','XRP-USD','LTC-USD','USDC-USD','DOGE-USD','TRX-USD','BUSD-USD']
    start_date = '2008-01-01'
    end_date = '2023-03-1'

    data = {}
    for ticker in tickers:
        yahoo_financials = YahooFinancials(ticker)
        historical_data = yahoo_financials.get_historical_price_data(start_date, end_date, "daily")
        data[ticker] = historical_data[ticker]['prices']
    dfs = []
    titles = []
    for ticker, prices in data.items():
        df = pd.DataFrame(prices)
        parse_date_columns(df)
        df = df.drop('date', axis=1).set_index('formatted_date')
        df['volume'] = df['volume'].astype(float)
        title = f'{get_coin_name(ticker[:-4])}_historical_price'
        titles.append(title)
        dfs.append(df)
    return dfs,titles