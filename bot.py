from binance.client import Client
from binance.exceptions import BinanceAPIException
from config import API_KEY, API_SECRET, TEST_MODE, DEFAULT_SYMBOL, DEFAULT_QUANTITY
from logger import setup_logger

logger = setup_logger()

class TradingBot:
    def __init__(self):
        try:
            self.client = Client(API_KEY, API_SECRET)
            logger.info("Successfully connected to Binance Futures API.")
        except Exception as e:
            logger.error(f"Error connecting to Binance: {e}")
            raise
        
    def place_market_order(self, symbol=DEFAULT_SYMBOL, side ="BUY", quantity=DEFAULT_QUANTITY):
        try:
            order_type=Client.ORDER_TYPE_MARKET
            side = side.upper()
            
            if TEST_MODE:
                logger.info(f"Test Mode ON - Simulating {side} order for {quantity} {symbol}")
                return {"status": "SIMULATED_ORDER_PLACED", "symbol": symbol, "side": side, "quantity": quantity}
            else:
                logger.info(f"Placing REAL {side} Spot market order: {symbol}, Qty: {quantity}")
                result = self.client.futures_create_order(
                    symbol = symbol,
                    side=side,
                    type= order_type,
                    quantity=quantity
                )
            
            logger.info(f"Order Placed successfully: {result}")
            return result
        
        except BinanceAPIException as api_err:
            logger.error(f"Binance API Error: {api_err.message}")
            return {"error": str(api_err)}
        
        except Exception as e:
            logger.error(f"Unexpected erroe: {e}") 
            return {"error": str(e)}   
                