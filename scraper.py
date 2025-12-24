import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1")
    if title:
        print("Page title:", title.text.strip())
    else:
        print("Title not found")
else:
    print("Failed to retrieve page")
