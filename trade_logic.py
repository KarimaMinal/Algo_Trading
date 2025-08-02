def generate_signals(df):
    if df.empty:
        return df

    df = df.copy()
    df['Signal'] = ''

    for i in range(len(df)):
        if df['rsi'].iloc[i] < 30 and df['ma20'].iloc[i] > df['ma50'].iloc[i]:
            df.at[df.index[i], 'Signal'] = 'BUY'
        elif df['rsi'].iloc[i] > 70 and df['ma20'].iloc[i] < df['ma50'].iloc[i]:
            df.at[df.index[i], 'Signal'] = 'SELL'

    return df
