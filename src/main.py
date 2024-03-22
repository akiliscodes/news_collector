from utils.helpers import filter_yaml_files, read_news_links, save_to_jsonlines
from feed_reader.feed_reader import feed_fetcher
import asyncio
import aiohttp
import json
import os 

def fetch_data(folder):
    try:
        data_feed_filepaths = filter_yaml_files(folder)
        return data_feed_filepaths
    except:
        print("file not exist")
        
async def run_and_save(folder, output_folder):
    result = await main(folder)
    await save_to_jsonlines(result, output_folder)

async def main(folder):
    data_feed_filepaths = fetch_data(folder)
    data_feed = (read_news_links(x) for x in data_feed_filepaths)
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[feed_fetcher(data) for data in data_feed])
    return [feed for sublist in results if sublist for feed in sublist]

if __name__ == "__main__":
    folder = "config" 
    output_folder = f"data/raw"
    asyncio.run(run_and_save(folder, output_folder))

