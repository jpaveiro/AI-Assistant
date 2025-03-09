from audio_recorder.recorder import AudioRecorder
from audio_transcriber.transcriber import AudioTranscriber

if __name__ == "__main__":
    recorder = AudioRecorder()
    recorder.run()

    transcriber = AudioTranscriber()
    text = transcriber.transcribe(AudioRecorder.RECORD_FILE)

    print("Transcrição: ", text)
