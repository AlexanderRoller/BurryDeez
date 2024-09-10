import yfinance as yf

def get_stock_price(ticker: str):
    stock = yf.Ticker(ticker)
    stock_info = stock.info

    current_price = stock_info.get('currentPrice', stock_info.get('previousClose'))
    previous_close = stock_info.get('previousClose', None)

    if current_price and previous_close:
        day_change = ((current_price - previous_close) / previous_close) * 100
        day_change_str = f"{day_change:.2f}%"
    else:
        day_change_str = "Unavailable"

    if current_price:
        response = (
            f"💹 **Current Price of {ticker.upper()}** 💹\n"
            f"💲 **Price:** **${current_price:.2f}**\n"
            f"📊 **Day Change:** {day_change_str}\n"
            f"Keep an eye on the market! 📈"
        )
    else:
        response = f"❌ Could not retrieve the price for ticker **{ticker.upper()}**."

    return response
