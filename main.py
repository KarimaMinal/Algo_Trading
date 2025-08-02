import pandas as pd
from fetch_data import fetch_stock_data
from indicators import add_indicators
from trade_logic import generate_signals
from model import train_model
from back_test import backtest
from gsheet import update_trades_sheet, update_summary_sheet, update_ml_sheet
from telegram_chat import send_alert
from dotenv import load_dotenv
import os
load_dotenv()
def run():
    SPREADSHEET_ID = os.getenv("Spreadsheet_id")  # Replace with your actual Google Sheet ID
    SHEET_TRADES = "Trades!A1"
    SHEET_SUMMARY = "Summary!A1"
    SHEET_ML = "ML_Analytics!A1"

    symbols = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS']
    all_trades = []
    summary_data = []
    ml_results = []

    for sym in symbols:
        df = fetch_stock_data(sym)
        if df.empty:
            print(f"Skipping {sym}: No data.")
            continue

        df = add_indicators(df)
        df = generate_signals(df)

        # Machine Learning Accuracy
        accuracy = train_model(df)
        ml_results.append([sym, round(accuracy, 2)])
        print(f"{sym} ML Prediction Accuracy: {accuracy:.2f}")

        # Collect trades
        trades = df[df['Signal'] != ''][['Close', 'Signal']].copy()
        if not trades.empty:
            trades['Symbol'] = sym
            trades['Date'] = trades.index.astype(str)
            trades = trades[['Symbol', 'Date', 'Close', 'Signal']]
            all_trades.append(trades)

            # Send Telegram Alerts
            for _, row in trades.iterrows():
                send_alert(f"{row['Symbol']} | {row['Date']} | {row['Signal']} at {row['Close']}")

        # Backtest
        pnl, win_ratio, total_trades = backtest(df)
        summary_data.append([sym, total_trades, pnl, win_ratio])

    # Push to Google Sheets
    if all_trades:
        trades_df = pd.concat(all_trades)
        update_trades_sheet(SPREADSHEET_ID, SHEET_TRADES, trades_df)

    summary_df = pd.DataFrame(summary_data, columns=['Symbol', 'Total Trades', 'Total P&L', 'Win Ratio'])
    update_summary_sheet(SPREADSHEET_ID, SHEET_SUMMARY, summary_df)

    ml_df = pd.DataFrame(ml_results, columns=['Symbol', 'Accuracy'])
    update_ml_sheet(SPREADSHEET_ID, SHEET_ML, ml_df)

if __name__ == "__main__":
    run()
