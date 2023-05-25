import requests
from bs4 import BeautifulSoup

url = "https://www.freelancer.com/projects/unity-3d/Unity-expert-needed-36573434/details"
keyword = "expert"

response = requests.get(url)
page_content = response.content

soup = BeautifulSoup(page_content, 'html.parser')
keyword_instances = soup.find_all(string=lambda string: keyword in string.lower())

num_instances = len(keyword_instances)

print(f"The keyword '{keyword}' appears {num_instances} times on the page.")