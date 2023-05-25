import requests
from bs4 import BeautifulSoup
import re

# Send a GET request to the Facebook Developers website
url = "https://developers.facebook.com/docs/"
response = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extract the relevant information (page titles and URLs)
links = []
for link in soup.find_all("a"):
    title = link.get_text()
    url = link.get("href")
    if url.startswith("/docs/"):
        links.append({"title": title, "url": url})

# Search for matches based on target keywords
target_keywords = ["API", "SDK"]
matched_links = []
for link in links:
    for keyword in target_keywords:
        if re.search(keyword, link["title"], re.IGNORECASE):
            matched_links.append(link)

# Print the matched links
for link in matched_links:
    print(f'{link["title"]}: {url}{link["url"]}')