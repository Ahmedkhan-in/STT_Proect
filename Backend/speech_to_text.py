from faster_whisper import WhisperModel

from config import WHISPER_MODEL
from config import DEVICE
from config import COMPUTE_TYPE

model = WhisperModel(
    WHISPER_MODEL,
    device=DEVICE,
    compute_type=COMPUTE_TYPE
)


def transcribe_audio(audio_path):

    segments, _ = model.transcribe(audio_path)

    transcript = " ".join(
        segment.text.strip()
        for segment in segments
    )

    return transcript