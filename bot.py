# import threading
from typing import Optional

from xchangelib import xchange_client
import asyncio

import numpy as np

# STOCKS = ["EPT", "DLO", "MKU", "IGM", "BRV"]
ETFS = ["SCP", "JAK"]
# STOCKS = ["EPT", "DLO", "MKU", "BRV"]

class MyXchangeClient(xchange_client.XChangeClient):
    '''A shell client with the methods that can be implemented to interact with the xchange.'''

    def __init__(self, host: str, username: str, password: str):
        super().__init__(host, username, password)

    async def bot_handle_cancel_response(self, order_id: str, success: bool, error: Optional[str]) -> None:
        order = self.open_orders[order_id]
        print(f"{'Market' if order[2] else 'Limit'} Order ID {order_id} cancelled, {order[1]} unfilled")

    async def bot_handle_order_fill(self, order_id: str, qty: int, price: int):
        print("order fill", self.positions)

    async def bot_handle_order_rejected(self, order_id: str, reason: str) -> None:
        print("order rejected because of ", reason)


    async def bot_handle_trade_msg(self, symbol: str, price: int, qty: int):
        # print("something was traded")
        pass

    async def bot_handle_book_update(self, symbol: str) -> None:
        # # print("book update")
        # pass
        
        #MY IMPLEMENTATION
        if symbol == "JMS":
            book = self.order_books["JMS"]
            book = self.order_books["JMS"]
            if book.asks and book.bids:
                best_ask = min(book.asks)
                best_bid = max(book.bids)
                if best_bid < 4999:
                        await self.place_order("JMS", 1, xchange_client.Side.BUY, best_bid+1)
                        await asyncio.sleep(1)
                if best_ask > 5001:
                    await self.place_order("JMS", 1, xchange_client.Side.SELL, best_ask-1)
                    await asyncio.sleep(1)
                # await self.place_order("JMS", 2, xchange_client.Side.SELL, 5000)
                # await asyncio.sleep(3)

        # if symbol == "JAK": 
        #     book = self.order_books[symbol]
        #     book = self.order_books[symbol]
        #     if book.asks and book.bids:
        #         best_ask = min(book.asks)
        #         best_bid = max(book.bids)
        #         market_price = (best_ask + best_bid) // 2
        #         spread = best_ask - best_bid
        #         # if self.positions["SCP"] >= 1:
        #         #     print("selling back", symbol)
        #         #     await self.place_order("SCP", 1, xchange_client.Side.SELL, best_ask-1)
        #         #     await asyncio.sleep(2)

        #         if best_bid < market_price:
        #                 await self.place_order("JAK", 1, xchange_client.Side.BUY, best_bid+1)
        #                 await asyncio.sleep(.5)
        #         if best_ask > market_price:
        #                 await self.place_order("JAK", 1, xchange_client.Side.SELL, best_ask-1)
        #                 await asyncio.sleep(.5)
                
                # # Define increments based on the spread
                # if spread <= 2:
                #     bid_increment = 1  # Small increment for narrow spreads
                #     ask_decrement = 1
                # elif spread <= 5:
                #     bid_increment = 2  # Slightly larger increments for moderate spreads
                #     ask_decrement = 2
                # else:
                #     bid_increment = 3  # More aggressive positioning for wider spreads
                #     ask_decrement = 3

                # # Implementing the order logic with adjusted increments
                # if best_bid < market_price:
                #     new_bid_price = best_bid + bid_increment
                #     if new_bid_price < best_ask:  # Ensure not crossing the spread
                #         await self.place_order(symbol, 1, xchange_client.Side.BUY, new_bid_price)
                #         await asyncio.sleep(.5)  # Shorter sleep, adjust as necessary
                # if best_ask > market_price:
                #     new_ask_price = best_ask - ask_decrement
                #     if new_ask_price > best_bid:  # Ensure not crossing the spread
                #         await self.place_order(symbol, 1, xchange_client.Side.SELL, new_ask_price)
                #         await asyncio.sleep(.5)

                

                # # Calculate bid and ask increments dynamically based on volatility
                # volatility = np.std([price for price, qty in book.asks.items()]+[price for price, qty in book.bids.items()])
                # bid_increment = min(max(int(volatility), 1), 3)  # Clamp the increment value between 1 and 3
                # ask_decrement = bid_increment  # Symmetric for simplicity, adjust if needed

                # # Position management to prevent overexposure
                # current_position = self.positions.get(symbol, 0)
                # max_position = 5  # Maximum number of shares to hold at any time
                # position_adjustment_factor = max(1, (max_position - abs(current_position)) // 2)

                # # Corrected use of qty based on position adjustment factor
                # if best_bid < market_price and current_position < max_position:
                #     new_bid_price = best_bid + bid_increment
                #     qty_to_buy = min(position_adjustment_factor, max_position - current_position)  # Ensure not to exceed max_position
                #     if new_bid_price < best_ask and qty_to_buy > 0:
                #         await self.place_order(symbol, qty_to_buy, xchange_client.Side.BUY, new_bid_price)
                #         await asyncio.sleep(1)

                # # Sell order logic
                # if best_ask > market_price and current_position > -max_position:
                #     new_ask_price = best_ask - ask_decrement
                #     qty_to_sell = min(position_adjustment_factor, current_position + max_position)  # Ensure not to exceed max_position
                #     if new_ask_price > best_bid and qty_to_sell > 0:
                #         await self.place_order(symbol, qty_to_sell, xchange_client.Side.SELL, new_ask_price)
                #         await asyncio.sleep(1)
                
                


        # if symbol in ETFS:
        #     book = self.order_books[symbol]
        #     book = self.order_books[symbol]
        #     if book.asks and book.bids:
        #         best_ask = min(book.asks)
        #         best_bid = max(book.bids)

        #         # if best_bid < 4999:
        #         #     await self.place_order("JMS", 1, xchange_client.Side.BUY, best_bid+1)
        #         #     await asyncio.sleep(1)
        #         # if best_ask > 5000:
        #         #     await self.place_order("JMS", 1, xchange_client.Side.SELL, best_ask-1)
        #         #     await asyncio.sleep(1)
                

        #         #DO NOT RUN THIS CODE - money lost
        #         # market_price = (best_ask + best_bid) // 2
        #         # self.target_spread = 1
        #         # spread = market_price * self.target_spread // 100

        #         # our_bid = market_price - spread
        #         # our_ask = market_price + spread

        #         # await self.place_order(symbol, 1, xchange_client.Side.SELL, our_bid)
        #         # await self.place_order(symbol, 1, xchange_client.Side.BUY, our_ask)
                
        #         # applies pennying method
        #         # if best_ask - 1 > best_bid + 1:
        #         #     await self.place_order(symbol, 1, xchange_client.Side.BUY, best_bid + 1)
        #         #     await asyncio.sleep(2)
        #         #     await self.place_order(symbol, 1, xchange_client.Side.SELL, best_ask - 1)
        #         #     await asyncio.sleep(5)
                
                
        #         # await self.place_order(symbol, 1, xchange_client.Side.SELL, best_ask - 1)
        #         # await asyncio.sleep(2)
        #         # await self.place_order(symbol, 1, xchange_client.Side.BUY, best_bid + 1)
        #         # await asyncio.sleep(6)

        #         if self.positions[symbol] >= 3:
        #             print("selling back", symbol)
        #             await self.place_order(symbol, 1, xchange_client.Side.SELL, best_ask - 2)
        #             await asyncio.sleep(2)
        #         elif self.positions[symbol] <= -3:
        #             print("buying back", symbol)
        #             await self.place_order(symbol, 1, xchange_client.Side.BUY, best_bid + 2)
        #             await asyncio.sleep(2)
        #         else:
        #             print("passed through check for", symbol)
        #             await self.place_order(symbol, 1, xchange_client.Side.SELL, best_ask - 1)
        #             await asyncio.sleep(2)
        #             await self.place_order(symbol, 1, xchange_client.Side.BUY, best_bid + 1)
        #             await asyncio.sleep(6)


        # if symbol in ["EPT", "IGM"]:
        #     book = self.order_books[symbol]
        #     if book.asks and book.bids:
        #         best_ask = min(book.asks)
        #         best_bid = max(book.bids)

        #         spread = await self.calculate_spread("EPT", "IGM")
        #         mean_spread = np.mean(spread)
        #         standard_spread = np.std(spread)

               

        #         if (spread[-1] > mean_spread + 2 * standard_spread):
        #             await self.place_order("EPT", 1, xchange_client.Side.BUY)
        #             await self.place_order("IGM", 1, xchange_client.Side.SELL)
        #         elif spread[-1] < mean_spread - 2 * standard_spread:
        #             await self.place_order("EPT", 1, xchange_client.Side.SELL)
        #             await self.place_order("IGM", 1, xchange_client.Side.BUY)
            


    async def bot_handle_swap_response(self, swap: str, qty: int, success: bool):
        # print("Swap response")
        # pass

        """
        1.) check prices on market
        2.) get within that margin (penny)
        3.) ???
        4.) profit


        we should prob add a check that makes sure our 
        """

    # my method
    async def calculate_spread(self, symbol1, symbol2):
        prices1 = self.get_historical_prices(symbol1)
        prices2 = self.get_historical_prices(symbol2)
        spread = prices1 - prices2
        return spread
        
    def get_historical_prices(self, symbol):
        return np.random.normal(size=100)

        
        
    async def trade(self):
        """This is a task that is started right before the bot connects and runs in the background."""
        await asyncio.sleep(5)
        print("attempting to trade")
        # await self.place_order("BRV",3, xchange_client.Side.SELL, 7)

        #MY IMPLEMENTATION: implement pennying
        while True:
            await asyncio.sleep(3)
            # for etf in ETFS:
            #     await self.bot_handle_book_update(etf)
            await self.bot_handle_book_update("JMS")

            

            # spread = self.calculate_spread("EPT", "IGM")
            # mean_spread = np.mean(spread)
            # standard_spread = np.std(spread)

            # if (spread[-1] > mean_spread + 2 * standard_spread):
            #     await self.place_order("EPT", 10, xchange_client.Side.BUY)
            #     await self.place_order("IGM", 10, xchange_client.Side.SELL)
            # elif spread[-1] < mean_spread - 2 * standard_spread:
            #     await self.place_order("EPT", 10, xchange_client.Side.SELL)
            #     await self.place_order("IGM", 10, xchange_client.Side.BUY)


        # Cancelling an order
        order_to_cancel = await self.place_order("BRV",3, xchange_client.Side.BUY, 5)
        await asyncio.sleep(5)
        await self.cancel_order(order_to_cancel)

        # Placing Swap requests
        await self.place_swap_order('toJAK', 1)
        await asyncio.sleep(5)
        await self.place_swap_order('fromSCP', 1)
        await asyncio.sleep(5)

        # Placing an order that gets rejected for exceeding qty limits
        await self.place_order("BRV",1000, xchange_client.Side.SELL, 7)
        await asyncio.sleep(5)

        # Placing a market order
        market_order_id = await self.place_order("BRV",10, xchange_client.Side.SELL)
        print("Market Order ID:", market_order_id)
        await asyncio.sleep(5)

        # Viewing Positions
        print("My positions:", self.positions)

    async def view_books(self):
        """Prints the books every 3 seconds."""
        while True:
            await asyncio.sleep(3)
            for security, book in self.order_books.items():
                sorted_bids = sorted((k,v) for k,v in book.bids.items() if v != 0)
                sorted_asks = sorted((k,v) for k,v in book.asks.items() if v != 0)
                print(f"Bids for {security}:\n{sorted_bids}")
                print(f"Asks for {security}:\n{sorted_asks}")

    async def start(self):
        """
        Creates tasks that can be run in the background. Then connects to the exchange
        and listens for messages.
        """
        asyncio.create_task(self.trade())
        # asyncio.create_task(self.view_books())
        await self.connect()
    

async def main():
    SERVER = 'dayof.uchicagotradingcompetition.com:3333' # run on sandbox
    my_client = MyXchangeClient(SERVER,"harvard_stanford_buffalo_upenn","golem-slowbro-5512")
    await my_client.start()
    return

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(main())



