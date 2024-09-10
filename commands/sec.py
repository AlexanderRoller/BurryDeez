import feedparser
import requests
from bs4 import BeautifulSoup

def fetch_latest_sec_filings(rss_url):
    feed = feedparser.parse(rss_url, agent="OSU AdminContact@<sample company domain>.com")
    return feed.entries

def get_accession(cik):
    cik = cik[:-1]
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    headers = {"User-Agent": "OSU AdminContact@<sample company domain>.com"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        filings_data = response.json()
        
        if 'filings' in filings_data and 'recent' in filings_data['filings'] and 'accessionNumber' in filings_data['filings']['recent']:
            accession_numbers = filings_data['filings']['recent']['accessionNumber']
            if isinstance(accession_numbers, list) and accession_numbers:
                return accession_numbers[0]
    except requests.exceptions.RequestException:
        pass
    
    return None

async def process_sec_index(cik_number, accession_number, channel):
    if not accession_number:
        return

    sec_url = f"https://www.sec.gov/Archives/edgar/data/{cik_number}/{accession_number}-index.htm"
    headers = {"User-Agent": "OSU AdminContact@<sample company domain>.com"}
    
    try:
        response = requests.get(sec_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', summary='Document Format Files')
        
        if not table:
            return

        table_rows = table.find_all('tr')
        target_row = None
        for row in table_rows:
            if '8-k' in row.text.lower():
                target_row = row
                break

        if target_row:
            link = target_row.find('a')['href']
            absolute_link = f"https://www.sec.gov{link}"
            htm_response = requests.get(absolute_link, headers=headers)
            htm_response.raise_for_status()
            htm_soup = BeautifulSoup(htm_response.content, 'html.parser')

            if "reverse stock split" in htm_soup.get_text().lower():
                await channel.send(
                    f"📑 **SEC Filing Alert** 📑\n"
                    f"🔗 [Document Link]({absolute_link}) contains **'reverse stock split'**."
                )
    except requests.exceptions.RequestException:
        pass

async def send_sec_alerts(channel, rss_url, seen_entries):
    """
    Fetch SEC feed, process the entries, and send alerts to the Discord channel.
    """
    sec_entries = fetch_latest_sec_filings(rss_url)
    
    for entry in sec_entries:
        entry_id = entry.id if hasattr(entry, 'id') else entry.link
        if entry_id in seen_entries:
            continue

        # Check if the 'cik' attribute exists, and log the entire entry if it doesn't
        if not hasattr(entry, 'cik'):
            print(f"Entry {entry_id} has no 'cik' attribute. Full entry: {entry}")
            continue  # Skip this entry if 'cik' is missing

        cik_number = entry.cik
        accession_number = get_accession(cik_number)
        await process_sec_index(cik_number, accession_number, channel)
        seen_entries.add(entry_id)
