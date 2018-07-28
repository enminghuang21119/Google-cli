import urllib
import requests
import webbrowser
from bs4 import BeautifulSoup
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"
url = 'https://www.google.com/search'
print('Search:', end='', flush=True)
Q = input()
print('')
data = {'q': Q}
soup = requests.get(url, data, headers=headers)
soup = BeautifulSoup(soup.text, "lxml")
a = 1
sugs = []
for link in soup.find_all('h3', 'r'):
    temp = link.find('a')
    print(a, temp.text)
    sugs.append(temp['href'])
    a += 1
while True:
    Choose = input('Choose one:')
    Choose = int(Choose) - 1
    webbrowser.open_new_tab(sugs[Choose])