import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

BASE = "https://callofduty.fandom.com"
CATEGORY_URL = BASE + "/wiki/Category:Call_of_Duty_Characters"

def get_character_links():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    html = requests.get(CATEGORY_URL, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")

    links = []
    for a in soup.select("a.category-page__member-link"):
        href = a.get("href")
        if href and href.startswith("/wiki/"):
            links.append(BASE + href)

    return links


def parse_character_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")

    info = {"wiki_url": url}

    title = soup.find("h1", {"class": "page-header__title"})
    info["name"] = title.text.strip() if title else None

    infobox = soup.find("aside", {"class": "portable-infobox"})
    if infobox:
        for data in infobox.find_all("section"):
            label = data.find("h3")
            value = data.find("div")
            if label and value:
                key = label.text.strip().lower().replace(" ", "_")
                info[key] = value.text.strip()

    return info

def clean_dataset():
    print("Getting character links. . .")
    links = get_character_links()
    print("Found", len(links), "character pages")
    
    records = []

    for url in links:
        try:
            data = parse_character_page(url)
            records.append(data)
        except Exception as e:
            print("Error parsing:", url, e)

    df = pd.DataFrame(records)
    
    # Save JSON to the same folder as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(script_dir, "cod_characters.json")

    df.to_json(save_path, orient="records", indent=2)

    print("Saved JSON to:", save_path)

clean_dataset()