from bot import TradingBot
from config import DEFAULT_QUANTITY, DEFAULT_SYMBOL
import sys

def get_user_input(prompt_message, default_value):
    message = f"{prompt_message} (Default: {default_value}): "
    user_input = input(message).strip()
    
    if user_input == "":
        return default_value
    else:
        return user_input
    
def main():
    print("Welcome to Binance Trading Bot")
    print("This Bot will place a market order on Binance Futures")
    print()
    
    symbol = get_user_input("Enter the trading pair", DEFAULT_SYMBOL)
    
    side_input = get_user_input("Enter the order side", "BUY")
    order_side = side_input.upper()
    quantity_input = get_user_input("Enter the quantity to trade", str(DEFAULT_QUANTITY))

    try:
        quantity = float(quantity_input)
        if quantity<=0:
            print("Quantity must be positive number")
            sys.exit(1)
    except ValueError:
        print("Invalid quantity. Please enter a number like 0.01.")
        sys.exit(1)
        
    if order_side not in ["BUY", "SELL"]:
        print("Invalid order side. please enter only 'BUY' or 'SELL'.")
        sys.exit(1)
        
        
    bot = TradingBot()
    
    
    print("Sending order to Binance")
    result = bot.place_market_order(symbol=symbol, side=order_side, quantity=quantity)
    
    print("Done Order Process Complete")
    print("\n Result:")
    print(result)
    print("check 'bot.log' for full logs and API details.")
    
if __name__ == "__main__":
    main()

    
               