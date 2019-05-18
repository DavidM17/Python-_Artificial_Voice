#Tutorial
# This are the libraries you need to play the audio
from pydub import AudioSegment # To get the audios from a folder
from pydub.playback import play
import eng_to_ipa as ipa    #This is for convert english text to phonetic


a="hello"
a=ipa.convert(a)
print(a)
dur=1000
sound  = AudioSegment.silent(duration=dur) # A silent audio to later put the single audios on it 
pos=0
sound1 = AudioSegment.from_mp3('/home/david/Escritorio/Proyectos/lou/h.wav') #My friend phonetic voices
sound = sound.overlay(sound1, position=pos)
play(sound)

#There the sound 
#and after that you have to put all the audios together that apper in the phonetic the e the l the ou etc