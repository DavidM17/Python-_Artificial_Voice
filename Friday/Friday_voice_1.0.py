import vlc
from pydub import AudioSegment
from pydub.playback import play
import numpy as np
from subprocess import check_output
import eng_to_ipa as ipa
word=ipa.convert("hello world")
word=list(word)
print(word)
def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })

    # convert the sound with altered frame rate to a standard frame rate
    # so that regular playback programs will work right. They often only
    # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

#slow_sound = speed_change(sound, 0.75)
#fast_sound = speed_change(sound, 2.0)



print(check_output(["espeak", "-q", "--ipa",'-v', 'en-us','hello  world']).decode('utf-8'))

sound  = AudioSegment.silent(duration=5000)
soundd  = AudioSegment.silent()
sound1 = AudioSegment.from_mp3('/home/david/Escritorio/Proyectos/sounds/h.wav')+10
sound2 = AudioSegment.from_mp3('/home/david/Escritorio/Proyectos/sounds/ə.wav')+11
sound3 = AudioSegment.from_mp3('/home/david/Escritorio/Proyectos/sounds/l.wav')+4
sound4 = AudioSegment.from_mp3('/home/david/Escritorio/Proyectos/sounds/oʊ.wav')+2


sound1 = sound.overlay(sound1, position=0)-20
# mix sound2 with sound1, starting at 5000ms into sound1)
output = sound1.overlay(sound2, position=50)
output = speed_change(output, 0.89) #0.88
output1 = output.overlay(sound3, position=100)+5
output2 = output.overlay(sound4, position=170)+2
output2 = speed_change(output2, 1)
#output2.export("hello.mp3",format='mp3')
#play(output2)


sound11 = AudioSegment.from_mp3('/home/david/Escritorio/Proyectos/sounds/w.wav')+10
sound22 = AudioSegment.from_mp3('/home/david/Escritorio/Proyectos/sounds/ɜ.wav')+11
sound33 = AudioSegment.from_mp3('/home/david/Escritorio/Proyectos/sounds/r.wav')+10
sound44 = AudioSegment.from_mp3('/home/david/Escritorio/Proyectos/sounds/l.wav')
sound55 = AudioSegment.from_mp3('/home/david/Escritorio/Proyectos/sounds/d.wav')
sound55 = speed_change(sound55, 0.88)

sound11 = soundd.overlay(sound11, position=0)
outputt = sound11.overlay(sound22, position=200)#400
outputt = outputt.overlay(sound33, position=350)#450
outputt = outputt.overlay(sound44, position=380)#500
outputt = outputt.overlay(sound55, position=400)#550

outputt = speed_change(outputt, 1)

outputt = output2.overlay(outputt, position=1000)

output2.export("hello.mp3",format='mp3')
play(outputt)
