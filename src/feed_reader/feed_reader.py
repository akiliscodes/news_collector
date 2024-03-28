import feedparser
import asyncio
import aiohttp
import json 
async def fetch_feed(session, url):
    async with session.get(url) as response:
        assert response.status == 200
        print(response.text)
        return await response.text()
    
async def parse_feed(entry):

    try:
        rss_url = entry.get('rss')
        async with aiohttp.ClientSession() as session:
            feed_text = await fetch_feed(session, rss_url)
            feed = feedparser.parse(feed_text)
            parsed_feeds = [{
                'source': entry.get('name', ''),
                'title': item.get('title', ''),
                'link': item.get('link', ''),
                'published': item.get('published', ''),
                'summary': item.get('summary', ''),
                'content': item.get('content', '')
            } for item in feed.entries]
        return  parsed_feeds
    except Exception as e:
        print(f"Error parsing feed from {entry.get('name')}: {str(e)}")

async def feed_fetcher(yaml_content):
    try:
        tasks = [parse_feed(entry) for entry in yaml_content]
        results = await asyncio.gather(*tasks)
        return [feed for sublist in results if sublist for feed in sublist]
    except Exception as e:
        print(f"Error fetching or parsing feeds: {str(e)}")

if __name__ == "__main__":

    folder = "config"
    feed_fetcher(folder) 