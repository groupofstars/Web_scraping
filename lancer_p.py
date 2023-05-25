import requests
from bs4 import BeautifulSoup
import re

# Send a GET request to the Facebook Developers website

# access_token = 'insert_access_token_here'
base_url = 'https://www.freelancer.com'

    # Create API endpoint by combining base URL with desired parameters
endpoint = f"{base_url}"
try:
    response = requests.get(endpoint)
    # .json()
except requests.exceptions.RequestException as e:
    print('Error:', e)

# url = "https://developers.facebook.com/docs/"
# response = requests.get(url)

# Parse the HTML content with BeautifulSoup
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # continue parsing HTML content here
else:
    print('Error:', response.status_code)
# Extract the relevant information (page titles and URLs)
links = []
for link in soup.find_all("div"):
    title = link.get_text()
    # print(title)
    url = link.get("href")
    # if url.startswith("/details/"):
    links.append({"title": title, "url": url})

# Search for matches based on target keywords
target_keywords = ["PHP", "multiple"]
matched_links = []
for link in links:
    for keyword in target_keywords:
        if re.search(keyword, link["title"], re.IGNORECASE):
            matched_links.append(link)

# Print the matched links
for link in  links:
    print(f'{link["title"]}: {url} -- {link["url"]}')


import pandas as pd
# Rest of the code goes here...

# Create a pandas DataFrame with the matched_links list
df = pd.DataFrame(links)

# Write the DataFrame to an Excel file
df.to_excel("matched_links.xlsx", index=False)