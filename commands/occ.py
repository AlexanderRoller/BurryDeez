import feedparser
import re

def check_occ_feed(rss_url, seen_entries):
    occ_feed = feedparser.parse(rss_url)
    alerts = []
    
    for entry in occ_feed.entries:
        entry_id = entry.id if hasattr(entry, 'id') else entry.link
        if entry_id in seen_entries:
            continue

        description = entry.description.lower()
        if 'reverse split' in description:
            match = re.search(r'option symbol:\s*(\S+)', description, re.IGNORECASE)
            ticker_symbol = match.group(1) if match else 'Unknown'

            memo_match = re.search(r'#(\d+)', entry.title)
            memo_number = memo_match.group(1) if memo_match else 'Unknown'

            alerts.append({
                'title': entry.title,
                'ticker': ticker_symbol,
                'memo_number': memo_number,
                'link': entry.link
            })
            seen_entries.add(entry_id)

    return alerts

async def send_occ_alerts(channel, rss_url, seen_entries):
    occ_alerts = check_occ_feed(rss_url, seen_entries)
    role_id = 1275562147392524368

    for alert in occ_alerts:
        message = (
            f"<@&{role_id}> 🔔 **New Reverse Split Memo Alert:** **#{alert['memo_number']}**\n"
            f"**Ticker Symbol:** `{alert['ticker']}`\n"
            f"🔗 [Memo Link]({alert['link']})"
        )
        await channel.send(message)
