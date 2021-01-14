import sounddevice as sd
import wave
import numpy as np

sample_wave_file='./CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav'

wav = wave.open(sample_wave_file)

data = wav.readframes(wav.getnframes())
data = np.frombuffer(data, dtype=np.int16)

sd.play(data, wav.getframerate())

print('再生開始')

status = sd.wait()