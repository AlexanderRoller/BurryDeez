# OCC Contract Adjustment Alert Bot

This Discord bot provides a suite of financial utilities designed to monitor corporate actions like reverse stock splits and help users stay informed about the stock market. It offers live stock price fetching, options intrinsic value calculation, and both **OCC** and **SEC** monitoring for reverse stock split memos. Additionally, the bot can track the server's health and provide insights on server membership.

## Features

- **📈 Live Stock Price Fetching**: Retrieve the most up-to-date stock prices during market hours, or the last available price after hours using the `yfinance` API.
  
- **💡 Intrinsic Value Calculation**: Calculate the intrinsic value of **call** or **put** options contracts. The bot takes into account the current stock price and strike price to determine whether the option has any inherent value.

- **📑 OCC Memo Monitoring**: The bot constantly checks the **OCC (Options Clearing Corporation)** RSS feed for memos related to **reverse stock splits**. Whenever a new memo is found, it sends an alert in a specified Discord channel, ensuring you never miss crucial corporate adjustments.

- **📰 SEC Filing Monitoring**: The bot also monitors the **SEC (Securities and Exchange Commission)** RSS feed for new filings, alerting users when relevant documents—such as those mentioning reverse stock splits—are published. It provides direct links to the SEC's filing pages.

- **🖥️ Server Health Monitoring**: Track your server's health with real-time updates on **CPU usage**, **memory usage**, **disk usage**, **uptime**, and even **component temperatures** (useful for monitoring Raspberry Pi or other hardware).

- **👥 User Count**: The bot can also provide the number of users currently in the Discord server.

---

## Prerequisites

Before using the bot, ensure you have the following installed:

- **Python 3.6 or higher**
- **Discord API Token**: You'll need to create a bot on the [Discord Developer Portal](https://discord.com/developers/applications) and get a token.
- **Dependencies**:
  - `discord.py`: For connecting to Discord and handling commands.
  - `feedparser`: To parse the RSS feeds from the OCC and SEC.
  - `yfinance`: To fetch real-time and historical stock data.
  - `psutil`: To monitor system performance for server health checks.
  - `requests`: To make HTTP requests (e.g., fetching SEC filings).
  - `beautifulsoup4`: For parsing SEC filing pages.

---

## Setup

To get started, follow these steps:

### 1. **Clone the Repository**
   First, clone the repository from GitHub to your local machine:
   ```bash
   git clone https://github.com/AlexanderRoller/BurryDeez.git
   ```

### 2. **Install Dependencies**
   Navigate to the project directory and install all required dependencies using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

### 3. **Configuration**

   Before running the bot, create a `.env` file in the root directory of the project. This file stores sensitive information like your Discord bot token and channel ID. Use the format below:

   ```plaintext
   BOT_TOKEN=your_discord_bot_token
   CHANNEL_ID=your_discord_channel_id
   RSS_URL=your_occ_rss_feed_url
   SEC_RSS_URL=your_sec_rss_feed_url
   ```

   - **BOT_TOKEN**: The token for your Discord bot.
   - **CHANNEL_ID**: The ID of the Discord channel where the bot will send alerts.
   - **RSS_URL**: The RSS feed URL for the OCC feed. (Example: `https://infomemo.theocc.com/rss`)
   - **SEC_RSS_URL**: The RSS feed URL for the SEC filings. (Example: `https://www.sec.gov/rss`)

---

## Usage

Once everything is set up, you can start the bot with the following command:

```bash
python main.py
```

The bot will immediately connect to Discord and begin monitoring the feeds, sending alerts and responding to commands in your designated channel.

---

## Commands

Here are the available commands you can use with the bot:

- **`!price [ticker]`**
  - **Description**: Fetches the current or most recent stock price for the specified ticker symbol.
  - **Example**: `!price AAPL` will return the most recent price for Apple Inc. 🍏

- **`!value [call or put] [ticker] [strike price]`**
  - **Description**: Calculates the intrinsic value of an options contract based on the current or last available stock price.
  - **Example**: `!value call AAPL 150` will calculate the intrinsic value of a call option for Apple with a strike price of $150.

- **`!arb [ticker] [split ratio]`**
  - **Description**: Calculates potential arbitrage opportunities for non-standard options based on a ticker and optional stock split ratio.
  - **Example**: `!arb AAPL 2:1` checks the arbitrage opportunity for Apple with a 2:1 stock split.

- **`!spread [ticker] [strike price] [expiration date] [call or put]`**
  - **Description**: Retrieves the ask, bid, and mark prices of the specified options contract.
  - **Example**: `!spread AAPL 150 2024-12-31 call` will return the pricing details for a call option expiring on December 31, 2024, with a strike price of $150.

- **`!rsa [ticker] [split ratio]`**
  - **Description**: Calculates the profitability of reverse split arbitrage.
  - **Example**: `!rsa AAPL 2:1` will return the calculated profitability of a reverse split arbitrage for Apple.

- **`!health`**
  - **Description**: Displays the server's current health status, including CPU usage, memory usage, disk usage, uptime, and temperature (if applicable).
  - **Example**: `!health` will return a status update on server performance.

- **`!usercount`**
  - **Description**: Returns the total number of members in the Discord server.
  - **Example**: `!usercount` will return the current member count of the server.

---

## Automatic Alerts

- **Reverse Split Memos**: The bot will send alerts when the OCC issues new memos related to reverse stock splits, ensuring you stay informed about market changes.
  
- **SEC Filings**: The bot monitors SEC filings related to reverse stock splits and will notify you with direct links to the filings in your Discord channel.

---

## Contributing

Contributions to this project are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b my-new-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin my-new-feature`).
5. Create a Pull Request, and we will review it!

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
