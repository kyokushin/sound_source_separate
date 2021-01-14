import numpy as np
import wave

n_sample = 40000
sample_rate = 16000

np.random.seed(0)

data = np.random.normal(scale=0.1, size=n_sample)

data_scale_adjust = data * np.iinfo(np.int16).max

wave_out = wave.open('./wgn_wave.wav', 'w')

wave_out.setnchannels(1)

wave_out.setsampwidth(2)

wave_out.setframerate(sample_rate)

wave_out.writeframes(data_scale_adjust)

wave_out.close()