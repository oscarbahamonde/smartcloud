ROOT_URL:str = 'https://fitosana.com.pe/'

from bs4 import BeautifulSoup
from requests import get
from wget import download

# env variable
ROOT_URL = 'http://fitosana.com.pe/'

# global variables
urls_array = [ROOT_URL]
imgs_array = []
not_allowed = ['javascript:', 'mailto:', 'tel:', '#', 'facebook.com', 'twitter.com', 'google.com', 'linkedin.com', 'instagram.com']
out_dir = './out/'
output_urls_file_format = '.js'

def getURL()->list:
    for url in urls_array:
        response = get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            h = link['href']
            if h not in not_allowed and h not in urls_array and h.startswith('https://fitosana.com.pe'):
                urls_array.append(h)
                print(h)
            else:
                continue
    return urls_array

def writeToJS(lista:list)->None:
    with open(out_dir + ROOT_URL + output_urls_file_format, 'w') as f:
        f.write('export default [')
        for url in lista:
            f.write('"' + url + '",')
        f.write('];')

def getImg()->list:
    for url in urls_array:
        response = get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('img', src=True):
            h = link['src']
            if h not in not_allowed and h not in imgs_array and h.startswith(ROOT_URL):
                imgs_array.append(h)
                print(h)
            else:
                continue
    return imgs_array


def  downloadImg(lista:list)->None:
    for url in lista:
        download(url, out_dir)
        
if __name__ == '__main__':
    getURL()
    writeToJS(urls_array)
    getImg()
    downloadImg(imgs_array)