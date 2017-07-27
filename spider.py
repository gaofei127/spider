from bs4 import BeautifulSoup
import requests

url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'
wedata = requests.get(url)
soup = BeautifulSoup(wedata.text ,'lxml' )
titles = soup.select('div.item.name > a')
# print(titles)
