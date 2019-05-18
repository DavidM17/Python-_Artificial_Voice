#This is for search information in the web por qué escribo en ingles? xD ops eso no deberia pasar XD
from bs4 import BeautifulSoup
import requests
import time
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
global memory,sta
memory=""
sta=0
def search():
    global memory,sta
    query=input("Enter your query: ")
    query=query.lower()
    
    if sta==1:
        me=['su','his','her','their','ella','el','ellos','ellas','it']
        for i in range(len(me)):
            if me[i] in query:
                query=query.replace(me[i],"the")
                query=query+'of'+str(memory)

    keyword=query.replace(" ","+")
    google_search='https://www.google.com/search?q='+keyword
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0 Safari/537.36'}
    r=requests.get(google_search,headers=headers)
    soup=BeautifulSoup(r.text,"html.parser")
    
    url=soup.find_all("div",{"class":"Z0LcW"})
    sta=1
    c=['serie','series','movies','movie','pelicula','peliculas','catalogo','catalog','catalogos','catalogs']
    for i in range(len(c)):
        if c[i] in query:
            sta=1
            url=soup.find_all("span",{"class":"kltat"})

    w=['weather','clima','temperature','temperatura']
    for i in range(len(w)):
        if w[i] in query:
            url=soup.find_all("span",{"class":"wob_t"})
            sta=0
    n=['minus','plus','times','divided']
    for i in range(len(n)):
        if n[i] in query:
            url=soup.find_all("span",{"class":"cwcot gsrt","id":"cwos"})
            sta=0
    m=['dollar','dolar','euro']
    for i in range(len(m)):
        if m[i] in query:
            url=soup.find_all("span",{"class":"DFlfde","id":"knowledge-currency__tgt-amount"})
            sta=0
    
    if bool(url)==False:
        sta=1
        url=soup.find_all("span",{"class":"title"})
    if bool(url)==False:
        sta=0
        url=soup.find_all("span",{"class":"st"})
    
    for u in url:
        print(u.text)
        voice=gTTS(text=u.text,lang="en")
        voice.save('voice.wav')
        sound = AudioSegment.from_mp3('voice.wav')
        play(sound)
        memory=u.text
        search()
        break
    

if __name__ == '__main__':
    search()