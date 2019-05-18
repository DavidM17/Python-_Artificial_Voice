"""""
from bs4 import BeautifulSoup
import requests

def main():
    query=input("Enter your query: ")
    print(query)
    keyword=query.replace(" ","+")
    google_search='https://www.google.com/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q='+keyword
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r=requests.get(google_search,headers=headers)
    soup=BeautifulSoup(r.text,"html.parser")
    url=soup.find_all('span',{"class":"st"}) 
    
    for u in url:
        print(u.text)
        break

if __name__ == '__main__':
    main()
"""
import vlc
player = vlc.MediaPlayer("/home/david/Escritorio/Proyectos/Friday/voice.mp3")
player.play()