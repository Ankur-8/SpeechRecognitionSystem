# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import assemblyai as aai

aai.settings.api_key = "39acb8bbe99041e8a873e7c487969b88"
transcriber = aai.Transcriber()

# transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
transcript = transcriber.transcribe("./input.wav")

print(transcript.text)