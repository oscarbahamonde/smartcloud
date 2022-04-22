URL = 'https://santanatura.com.pe/blog/page/'
from requests import get
from bs4 import BeautifulSoup

with open('data.js', 'w+') as j:
    j.write('export default [')
    for i in range(1, 17):
        url = URL + str(i)
        response = get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for post in soup.find_all('a', class_ = 'post-more'):
            print(post)
            link=get(post['href']).text
            s = BeautifulSoup(link, 'html.parser')
            title = s.find('h1').text
            time = s.find('time').text
            content = []
            cont = ''
            for p in s.find_all('p'):
                content.append(p.text)
            for i in content:
                cont += i
                print(i)
            j.write('{title: "' + title + '", time: "' + time + '", content: "' + cont + '"},\n')
    j.write('];')
    