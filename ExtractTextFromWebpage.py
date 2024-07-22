import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = ' '.join([p.text for p in soup.find_all('p')])
    return text

url = "https://example.com"
extracted_text = extract_text_from_url(url)
print(f"Extracted text: {extracted_text}")
