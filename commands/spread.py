import yfinance as yf

def get_option_prices(ticker: str, expiration_date: str, strike_price: float, option_type: str):
    # Fetch stock data from yfinance
    stock = yf.Ticker(ticker)
    
    # Fetch options chain for the given expiration date
    try:
        option_chain = stock.option_chain(expiration_date)
    except Exception as e:
        return f"❌ Error fetching option chain for {ticker.upper()} on {expiration_date}: {e}"

    # Determine whether we are looking for 'calls' or 'puts'
    options = option_chain.calls if option_type.lower() == 'call' else option_chain.puts

    # Find the specific option by strike price
    option = options[options['strike'] == strike_price]

    if option.empty:
        return f"⚠️ No {option_type} option found for {ticker.upper()} with strike price ${strike_price} on {expiration_date}."

    # Extract the ask, bid, and mark prices
    ask_price = option['ask'].values[0]
    bid_price = option['bid'].values[0]
    mark_price = (ask_price + bid_price) / 2  # Mark price is the average of ask and bid

    # Format the response
    response = (
        f"📈 **Options Spread for {ticker.upper()}** 📈\n"
        f"🗓 **Expiration Date:** {expiration_date}\n"
        f"🔔 **Strike Price:** ${strike_price}\n"
        f"💲 **Ask Price:** ${ask_price}\n"
        f"💲 **Bid Price:** ${bid_price}\n"
        f"📊 **Mark Price:** ${mark_price}"
    )
    
    return response
