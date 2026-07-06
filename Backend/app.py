import json

from speech_to_text import transcribe_audio

from classifier import classify

AUDIO = r"C:\Users\Home\OneDrive\Desktop\STT_Proect\Backend\Voices\audio2.m4a"

print("Transcribing Audio...")

transcript = transcribe_audio(AUDIO)

with open(
    "outputs/transcript.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(transcript)

print("Transcript Saved.")

print()

print(transcript)

print()

print("Analyzing Transcript...")

result = classify(transcript)

with open(
    "outputs/summary.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        result,
        file,
        indent=4,
        ensure_ascii=False
    )

print()

print(result)

print()

print("Finished.")