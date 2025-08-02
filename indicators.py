import pandas as pd
import ta

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    # If df['Close'] is a DataFrame with 1 column, convert to Series
    close = df['Close']
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]  # Take the first column as Series

    # Calculate indicators
    df['rsi'] = ta.momentum.RSIIndicator(close=close).rsi()
    df['ma20'] = ta.trend.SMAIndicator(close=close, window=20).sma_indicator()
    df['ma50'] = ta.trend.SMAIndicator(close=close, window=50).sma_indicator()

    df.dropna(inplace=True)
    return df
