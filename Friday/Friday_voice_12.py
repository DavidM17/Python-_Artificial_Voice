from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import WhiteNoise 
import eng_to_ipa as ipa

a=""
def voice(a):
    #a=input("Write:")
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
    #sound  = AudioSegment.silent(duration=dur)
    sound = WhiteNoise().to_audio_segment(duration=dur)-70
    pos=0
    for i in range(len(word)):
        pos=pos+120
        if ((word[i]==" ")|(word[i]=="*")):
            word[i]="_"
        
        vowel=['su','his','her','their','ella','el','ellos','ellas','it']
        for j in range(len(vowel)):
            if word[i] in vowel:
                sound1 = AudioSegment.from_mp3('/home/david/Escritorio/Proyectos/lou/'+str(word[i])+'.wav')+10
        
        sound1 = AudioSegment.from_mp3('/home/david/Escritorio/Proyectos/lou/'+str(word[i])+'.wav')
        sound = sound.overlay(sound1, position=pos)

    play(sound)
    octaves = 0.09

    new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))

    lowpitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
    play(lowpitch_sound)



