import requests
from bs4 import BeautifulSoup
import re

access_token = 'insert_access_token_here'
base_url = 'https://graph.facebook.com'

# Create API endpoint by combining base URL with desired parameters
endpoint = f"{base_url}/me/feed?fields=message,created_time&access_token={access_token}"
response = requests.get(endpoint).json()

# Extract message and created_time fields from each post
post_data = [(post['message'], post['created_time']) for post in response['data']]

# Search for matches based on target keywords
target_keywords = ["API", "SDK"]
matched_links = []
for message, _ in post_data:
    # Parse the message content with BeautifulSoup
    soup = BeautifulSoup(message, "html.parser")
    links = soup.find_all("a")

    # Extract the title and URL from each link
    for link in links:
        title = link.get_text()
        url = link.get("href")
        if url and any(keyword.lower() in title.lower() for keyword in target_keywords):
            matched_links.append({"title": title, "url": url})

# Print the matched links
for link in matched_links:
    print(f'{link["title"]}: {link["url"]}')