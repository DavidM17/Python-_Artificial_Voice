from pydub import AudioSegment           #to save whitenoise to audio_segment
from pydub.generators import WhiteNoise  #to generate white noise
from pydub.playback import play          #needed to play the audio segement
#from threading import Thread             #for async background 


#whitenoise duration
duration = 5000  #duration in millisec
wn = WhiteNoise().to_audio_segment(duration=duration)-60


#def play_white_noise(segment,duration):
    #""" play whitenoise for given duration """
play(wn)

#instantiate thread
#white_noise = Thread(target=play_white_noise, args=(wn,duration))

#start the thread
#white_noise.start()