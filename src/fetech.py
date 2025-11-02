import os
import requests

# Two public datasets with shared columns ("country" and "year")
DATASETS = {
    "gdp": "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv",
    "population": "https://raw.githubusercontent.com/datasets/population/master/data/population.csv"
}

# Folder where raw data will be saved
RAW_DIR = "data/raw"

def download_url(name, url, target_file):
    os.makedirs(RAW_DIR, exist_ok=True)
   
    print(f" Attempting to download {name} dataset from {url}")
    
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(target_file, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f" {name} dataset saved to {target_file}\n")
    else:
        print(f" Couldn't download {name} automatically (HTTP {response.status_code}).")
        print(f" Please download manually from {url}\n")

def main():
    download_url("gdp", DATASETS["gdp"], os.path.join(RAW_DIR, "gdp.csv"))
    download_url("population", DATASETS["population"], os.path.join(RAW_DIR, "population.csv"))

if __name__ == "__main__":
    main()
