import csv
import os
import time
from datetime import datetime, timezone

import requests

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

SUBREDDITS = {
    "employment": ["unemployment", "povertyfinance"],
    "family_violence": ["abusiverelationships", "raisedbynarcissists"],
    "food_insecurity": ["Food_Bank", "Frugal"],
    "housing_insecurity": ["homeless", "Tenant"],
    "transportation": ["carfree", "disability"],
    "mixed": ["TrueOffMyChest", "Anxiety", "CasualConversation"]
}

def fetch_posts(subreddit: str, limit: int = 100) -> list:
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
    response = requests.get(url, headers=HEADERS, timeout=10)

    scraped_at = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    if response.status_code != 200:
        print(f"Failed to fetch r/{subreddit}: {response.status_code}")
        return []
    
    try:
        payload = response.json()
    except ValueError:
        print(f"Non-JSON response for r/{subreddit}")
        return []

    posts = []
    for post in payload.get("data", {}).get("children", []):
        data = post.get("data", {})

        title = data.get("title", "").strip()
        body = data.get("selftext", "").strip()

        if body.lower() in ["[removed]", "[deleted]"]:
            body = ""

        text = " ".join([title, body]).strip()

        if text:
            posts.append({
                "id": data.get("id", ""),
                "subreddit": data.get("subreddit", ""),
                "text": text,
                "scraped_at": scraped_at,
            })

    time.sleep(2)
    return posts


def scrape_domain(domain: str, subreddits: list, limit: int = 100):
    output_dir = os.path.join(ROOT_DIR, "data", "raw", "reddit")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{domain}.csv")

    all_posts = []

    for subreddit in subreddits:
        print(f"Fetching r/{subreddit}...")
        posts = fetch_posts(subreddit, limit)
        print(f"  Got {len(posts)} rows")
        all_posts.extend(posts)

    if not all_posts:
        print(f"No posts collected for {domain}, skipping file.")
        return
    
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "subreddit", "text", "scraped_at"])
        writer.writeheader()
        writer.writerows(all_posts)

    print(f"Saved {len(all_posts)} rows to data/raw/reddit/{domain}.csv")


if __name__ == "__main__":
    for domain, subreddits in SUBREDDITS.items():
        print(f"\nScraping domain: {domain}")
        scrape_domain(domain, subreddits)