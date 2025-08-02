import yfinance as yf
import pandas as pd

def fetch_stock_data(symbol, period="6mo", interval="1d"):
    try:
        df = yf.download(symbol, period=period, interval=interval)
        if df.empty:
            raise ValueError(f"No data found for {symbol}")
        df.dropna(inplace=True)
        return df
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return pd.DataFrame()
