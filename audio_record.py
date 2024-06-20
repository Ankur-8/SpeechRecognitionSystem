import pyaudio
import wave

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format = FORMAT,
    rate = RATE,
    channels = CHANNELS,
    frames_per_buffer = FRAMES_PER_BUFFER,
    input = True
)

print("Recording started")

seconds = 5
frames = []

for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

audio = wave.open("input.wav", "wb")
audio.setnchannels(CHANNELS)
audio.setsampwidth(p.get_sample_size(FORMAT))
audio.setframerate(RATE)
audio.writeframes(b"".join(frames))
audio.close()