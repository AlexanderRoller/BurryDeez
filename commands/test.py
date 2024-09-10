from commands.price import get_stock_price
from commands.health import get_server_status
from commands.options_arb import calculate_options_arbitrage
from commands.value import calculate_intrinsic_value
from commands.spread import get_option_prices
from commands.rsa import calculate_reverse_split_arbitrage
from commands.occ import send_occ_alerts
from commands.sec import send_sec_alerts

async def test_all(ctx, bot, OCC_RSS_URL, SEC_RSS_URL, seen_entries):
    """
    Test all bot commands with sample inputs.
    """
    # Example inputs for testing
    test_ticker = "AAPL"  # Example ticker symbol for stock price and options
    test_strike_price = 150.0  # Example strike price
    test_expiration_date = "2024-12-20"  # Example expiration date
    test_option_type = "call"  # Example option type ('call' or 'put')
    test_split_ratio = "2:1"  # Example stock split ratio

    # Test stock price command
    await ctx.send("**Testing Stock Price Command**")
    stock_price_response = get_stock_price(test_ticker)
    await ctx.send(stock_price_response)

    # Test health check command
    await ctx.send("**Testing Server Health Command**")
    server_health_response = get_server_status()
    await ctx.send(server_health_response)

    # Test options arbitrage command
    await ctx.send("**Testing Options Arbitrage Command**")
    options_arb_response = calculate_options_arbitrage(test_ticker, test_strike_price, test_split_ratio)
    await ctx.send(options_arb_response)

    # Test intrinsic value command
    await ctx.send("**Testing Intrinsic Value Command**")
    intrinsic_value_response = calculate_intrinsic_value(test_option_type, test_ticker, test_strike_price)
    await ctx.send(intrinsic_value_response)

    # Test options spread command
    await ctx.send("**Testing Options Spread Command**")
    spread_response = get_option_prices(test_ticker, test_expiration_date, test_strike_price, test_option_type)
    await ctx.send(spread_response)

    # Test reverse split arbitrage command
    await ctx.send("**Testing Reverse Split Arbitrage Command**")
    rsa_response = calculate_reverse_split_arbitrage(test_ticker, test_split_ratio)
    await ctx.send(rsa_response)

    # Test OCC feed alerts
    await ctx.send("**Testing OCC Feed Alerts**")
    await send_occ_alerts(ctx.channel, OCC_RSS_URL, seen_entries)

    # Test SEC feed alerts
    await ctx.send("**Testing SEC Feed Alerts**")
    await send_sec_alerts(ctx.channel, SEC_RSS_URL, seen_entries)

    await ctx.send("✅ **All tests completed!**")
