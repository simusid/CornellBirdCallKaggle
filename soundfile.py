import numpy as np
import simpleaudio as sa
import os
import subprocess
from pydub import AudioSegment
from pydub.playback import play

from scipy.io.wavfile import read

source_file = "/home/jon//Documents/birdsong/cat.wav"  # here is the audio fil

#  using PyDub  and ffmpeg to slice an audio file and convert MP3 to WAV
song = AudioSegment.from_mp3(source_file)
aud_start_num = 1000 * 1  # 1000 * lenght of audio in seconds
aud_end_num = 1000 * .3 
aud_start = song[:aud_start_num]
aud_end = song[-aud_end_num:]
aud_start.export("test_file", format="wav")
play(aud_start)  # slide five seconds of start of audio

#  using scipy to create a numpy array from audio
a = read(source_file)
print("tuple")
print(a)
print(type(a))
a = np.array(a[1])
print("np array")
print(a)
print(type(a))
os.chdir('/home/jon/Documents/birdsong/')
subprocess.call(['ffmpeg', '-i', 'cat.wav', '-map_channel', '0.0.0', 'left.wav', '-map_channel', '0.0.1', 'right.wav'])
# subprocess.call(['ffmpeg', '-i', 'output.avi', '-t', '5', 'out.gif'])
# os.system (ffmpeg -i /home/jon/Documents/birdsong/cat.wav -map_channel 0.0.0 left.wav -map_channel 0.0.1 right.wav)
#  os.system (ffmpeg -i bird_sound -filter_complex stereotools=phasel=1 -ac 1 /home/jon//Documents/birdsong/output.wav)
# ffmpeg -i XC2628_10Sec.wav -map_channel 0.0.0 OUTPUT_CH0 -map_channel 0.0.1 OUTPUT_CH1
# -filter_complex "[0:a]channelsplit=channel_layout=stereo[left][right]" -map "[left]" left.wav -map "[right]" right.wav