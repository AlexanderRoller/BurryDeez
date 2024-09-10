import yfinance as yf

def calculate_intrinsic_value(option_type: str, ticker: str, strike_price: float):
    stock = yf.Ticker(ticker)
    stock_info = stock.info

    # Attempt to fetch the most current price available
    current_price = stock_info.get('currentPrice', stock_info.get('previousClose'))

    if not current_price:
        return f"❌ Could not retrieve any price for ticker **{ticker.upper()}**."

    # Default deliverable for standard options (100 shares per contract)
    standard_deliverable = 100

    # Calculate intrinsic value based on option type
    if option_type.lower() == 'call':
        intrinsic_value = max(0, (current_price - strike_price))
    elif option_type.lower() == 'put':
        intrinsic_value = max(0, (strike_price - current_price))
    else:
        return "⚠️ Invalid option type. Please use 'call' or 'put'."

    option_cost = intrinsic_value * standard_deliverable
    return (
        f"💡 **Intrinsic Value of {option_type.lower()} Option for {ticker.upper()}** 💡\n"
        f"💲 **Strike Price:** ${strike_price}\n"
        f"📦 **Deliverable:** {standard_deliverable} shares\n"
        f"📊 **Intrinsic Value:** **${intrinsic_value:.2f}**\n"
        f"💵 **Option Cost:** ${option_cost:.2f}\n"
    )
