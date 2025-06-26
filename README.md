This project is a simplified Binance Trading Bot built in Python.  
It allows users to simulate or place real spot market orders on Binance using the official Binance API.

Features:

1. Connects to Binance "Mainnet Spot API"

2. Place market buy/sell orders

3. Works on Binance Futures (USDT-M)

4. Logs all actions and errors to a file (bot.log)

5. Clean, modular Python code

How It Works:

The bot connects to Binance using your API key and secret. You run the bot through the terminal (cli.py), enter your trading symbol (like BTCUSDT), choose BUY or SELL, and enter the quantity. The bot then places a market order.

Steps to Run:

Clone the project folder into your system.

Install required packages using:
pip install -r requirements.txt

Set Up API Credentials:

Copy config_sample.py as config.py

Paste your Binance API key and secret inside config.py

Configuration Settings in config.py:

API_KEY: Your Binance API key

API_SECRET: Your Binance API secret

BASE_URL: Binance Futures base URL

DEFAULT_SYMBOL: Default symbol to trade (e.g., BTCUSDT)

DEFAULT_QUANTITY: Default trade quantity

TEST_MODE: True (for testing) or False (for live trading)

Run the Bot:
python cli.py

It will ask:

Trading symbol (default: BTCUSDT)

Order side (BUY or SELL)

Quantity (default: 0.01)

Check bot.log for all order logs and errors.

Project Structure:

bot.py: Main trading logic

cli.py: Command-line interface for user input

config.py: Your API keys

config_sample.py: Dummy config file for sharing

logger.py: Logging setup

requirements.txt: List of dependencies

README.md: Project instructions


Author:
Prasannakumar Bogachandrapu
