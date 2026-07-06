from faster_whisper import WhisperModel

model = WhisperModel("small", device="cpu", compute_type="int8")

segments, info = model.transcribe(r"C:\Users\Home\OneDrive\Desktop\STT_Proect\Backend\Voices\audio.m4a")

for segment in segments:
    print(segment.text)