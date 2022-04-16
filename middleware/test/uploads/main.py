from bs4 import BeautifulSoup
from requests import get

def getAllUrls(url:str):
    """
    Get all urls from a given url
    """
    urls = []
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
        print(link.get('href'))
    return urls

def getAllUrlsinWebSite(url:str):
    urls = [url]
    for i in urls:
        urls.append(getAllUrls(i))  # Recursive
    return urls