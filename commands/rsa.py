import yfinance as yf

def calculate_reverse_split_arbitrage(ticker: str, split_ratio: str):
    stock = yf.Ticker(ticker)
    stock_info = stock.info

    current_price = stock_info.get('currentPrice', stock_info.get('previousClose'))

    if not current_price:
        return f"❌ Could not retrieve the current price for ticker **{ticker.upper()}**."

    try:
        split_parts = split_ratio.split(':')
        split_ratio_value = float(split_parts[0]) / float(split_parts[1])
    except (IndexError, ValueError):
        return "⚠️ Invalid split ratio format. Please use 'numerator:denominator'."

    profitability = current_price * (split_ratio_value - 1)
    return f"📈 **Profitability of Reverse Split Arbitrage for {ticker.upper()}:** ${profitability:.2f}"
