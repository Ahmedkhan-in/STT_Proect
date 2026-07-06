import json

from speech_to_text import transcribe_audio

from classifier import classify 

AUDIO_PATH = "C:\\Users\\Home\\OneDrive\\Desktop\\STT_Proect\\Backend\\Voices\\audio.m4a"

print("Transcribing Audio...")

transcript = transcribe_audio(AUDIO_PATH)

with open("outputs/transcript.txt","w", encoding="utf-8") as f:

    f.write(transcript)

print("Transcript Saved.")

print()

print(transcript)

print()

print("Analyzing Transcript...")

result = classify(transcript)

with open("outputs/summary.json","w", encoding="utf-8") as f:

    json.dump(result, f, indent=4, ensure_ascii=False)

print()

print(result)

print()

print("Finished.")