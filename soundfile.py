from pydub import AudioSegment
from pydub.playback import play
import numpy as np
import simpleaudio as sa
from scipy.io.wavfile import read

#  using PyDub  and ffmpeg to slice an audio file and convert MP3 to WAV
song = AudioSegment.from_mp3("XC2628.mp3")
aud_start_num = 1000 * 1  # 1000 * lenght of audio in seconds
aud_end_num = 1000 * .3
aud_start = song[:aud_start_num]
aud_end = song[-aud_end_num:]
aud_start.export("XC2628_10Sec.wav", format="wav")
play(aud_start)  # slide five seconds of start of audio

#  using scipy to create a numpy array from audio
a = read("XC2628_10Sec.wav")
print("tuple")
print(a)
print(type(a))
a = np.array(a[1])
print("np array")
print(a)
print(type(a))
ffmpeg -i /home/jon//Documents/birdsong/C2628_10Sec.wav -filter_complex stereotools=phasel=1 -ac 1 /home/jon//Documents/birdsong/output.wav
# ffmpeg -i XC2628_10Sec.wav -map_channel 0.0.0 OUTPUT_CH0 -map_channel 0.0.1 OUTPUT_CH1
