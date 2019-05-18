import time
from bs4 import BeautifulSoup
import requests
search=input("What do you want to ask: ")
search=search.replace(" ","+")
link="https://www.google.com/search?q="+search
headers = {'User-Agent': 'Mozilla/63.0.3 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0 Safari/12.0'}
source=requests.get(link, headers=headers).text
soup=BeautifulSoup(source,"html.parser")
#print(link)
#wob_t span weather
#DFlfde money
#cwcot gsrt 
soup=BeautifulSoup(source,"html.parser")
#print(soup.prettify())
answer=soup.find('div',{"class":"Z0LcW"})
print(answer.text)