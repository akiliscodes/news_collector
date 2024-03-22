import yaml
import glob
import os
import datetime
import jsonlines

def read_news_links(filepath):
    with open(filepath, "r") as file:
        data = yaml.safe_load(file)
    return data

def filter_yaml_files(folder_path):
    return [
        file_path
        for file_path in glob.glob(os.path.join(folder_path, "*.yml"))
    ]

async def save_to_jsonlines(data, output_folder):
    date_of_the_day = datetime.datetime.now().strftime("%Y-%m-%d")
    output_file = os.path.join(output_folder, f"extract_{date_of_the_day}.jsonl")
    with jsonlines.open(output_file, mode='w') as writer:
        for item in data:
            writer.write(item)



if __name__ == "__main__":

    folder_path = "config"
    result = filter_yaml_files(folder_path)
    print(result)
