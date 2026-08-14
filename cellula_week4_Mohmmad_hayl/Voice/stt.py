from faster_whisper import WhisperModel


class SpeechToText:
    def __init__(self, model_size="small", device="cpu", compute_type="int8"):
        self.model = WhisperModel(
            model_size,
            device=device,
            compute_type=compute_type
        )

    def transcribe(self, audio_path):
        segments, info = self.model.transcribe(
            audio_path,
            task="transcribe",
            beam_size=5,
            vad_filter=True
        )

        text = " ".join(segment.text.strip() for segment in segments)

        return {
            "text": text,
            "language": info.language,
            "language_probability": info.language_probability
        }