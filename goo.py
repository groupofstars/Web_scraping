import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the search query and URL
query = 'Facebook'
url = f'https://registry.elevategreece.gov.gr?q={query}'

# Set the headers to simulate a browser request
headers = {
    
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

# Send a GET request with the query and headers
response = requests.get(url, headers=headers)

# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all search result items in the page
results = soup.find_all('div', class_='g')

# Parse the title and link from each search result
items = []
for r in results:
    # Skip any non-search-result DIVs
    if not r.find('a'):
        continue
    
    # Extract the title and link from the search result
    title = r.find('h3').get_text()
    url = r.find('a')['href']
    
    # Only include Facebook pages in the results
    # if url.startswith('https://www.facebook.com/'):
    items.append({'title': title, 'url': url})

# Write the results to an Excel file
df = pd.DataFrame(items, columns=['title', 'url'])
df.to_excel('facebook_search_results.xlsx', index=False)