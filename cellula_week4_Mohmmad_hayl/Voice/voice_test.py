from stt import SpeechToText


stt = SpeechToText()

result = stt.transcribe("test.wav")

print(result)