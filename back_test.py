def backtest(df):
    balance = 100000.0
    position = 0.0
    entry_price = 0.0
    wins = 0
    trades = 0

    for i in range(len(df)):
        price = df['Close'].iloc[i].item()  # fix warning

        if df['Signal'].iloc[i] == 'BUY' and position == 0:
            position = balance / price
            entry_price = price

        elif df['Signal'].iloc[i] == 'SELL' and position > 0:
            balance = position * price
            if price > entry_price:
                wins += 1
            position = 0
            trades += 1

    if position > 0:
        last_price = df['Close'].iloc[-1].item()
        balance = position * last_price

    pnl = round(balance - 100000, 2)
    win_ratio = round((wins / trades) * 100, 2) if trades > 0 else 0
    return pnl, win_ratio, trades
