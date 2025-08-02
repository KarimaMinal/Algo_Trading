# 📈 Algo_Trading System 

This is a Python-based mini **algorithmic trading system** that:
- Fetches stock data using Yahoo Finance (`yfinance`)
- Applies **RSI + Moving Average Crossover** strategy
- Trains a **Random Forest classifier** to predict price direction
- **Backtests** signals for profitability and win ratio
- Sends **Telegram alerts** for buy/sell signals
- Logs trades and analytics into **Google Sheets**

---

## 📂 Folder Structure
```
Algo_Trading/
├── main.py 
├── fetch_data.py 
├── indicators.py 
├── trade_logic.py 
├── model.py 
├── back_test.py 
├── gsheet.py 
├── telegram_chat.py 
├── .env 
├── service_account.json 
├── creds.json 
└── README.md 
```

---

## 🔧 Setup

### 1. Clone the Repo
```bash
git clone https://github.com/KarimaMinal/Algo_Trading.git
cd Algo_Trading

```
### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Running the Project
Option 1: Run as Script
```bash
python main.py
```
## 📊 Output
Google Sheets:

Sheet Trades: Logs all trades with signals

Sheet Summary: Shows P&L, win ratio

Sheet ML_Analytics: Shows ML accuracy for each symbol

## Telegram:

Instant alerts for buy/sell signals

## 📈 Strategies Used
RSI (Relative Strength Index):

Oversold below 30 (buy), overbought above 70 (sell)

## MA Crossover:

20-day MA vs 50-day MA for trend confirmation

## ML Model:

Random Forest classifier trained to predict if the next day’s close will be higher
