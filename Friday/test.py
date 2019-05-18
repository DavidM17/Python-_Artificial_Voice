from pydub import AudioSegment
from pydub.playback import play
import eng_to_ipa as ipa

a=""
while True:
    a=input("Write:")
    word=ipa.convert(a)
    word=list(word)

    w_size=len(word)
    w_corr=["aɪ","aʊ","eɪ","oʊ","ɔɪ","eə","ɪə","ʊə","dʒ","tʃ","əʊ"]

    t_word=[]
    t=0
    for i in range(w_size-1):
        t_word=word[i]+word[i+1]
        
        for j in range(10):
            if (t_word==w_corr[j]):
                word[i]=w_corr[j]
                t=t+1
                for k in range(w_size-i-2):
                    word[i+1+k]=word[i+2+k]
                    
    word=word[0:w_size-t]

    quote="ˈ"
    y=0
    for i in range(len(word)):
        if (word[i]==quote):
            y=y+1
            for k in range(len(word)-i-1):
                word[i+k]=word[i+1+k]

    word=word[0:len(word)-y]
    print(word)
    dur=(len(word)/5)*1200
    sound  = AudioSegment.silent(duration=dur)
    pos=0
    for i in range(len(word)):
        pos=pos+120
        if ((word[i]==" ")|(word[i]=="*")):
            word[i]="_"
        sound1 = AudioSegment.from_mp3('/home/david/Escritorio/Proyectos/lou/'+str(word[i])+'.wav') 
        sound = sound.overlay(sound1, position=pos)
    play(sound)
    sound.export("test.mp3")




