import whisper

class AudioTranscriber:
    """Realiza a transcrição do aúdio utilizando o Whisper da OpenAI"""
    def __init__(self, model = "base"):
        self.model = whisper.load_model(model)

    def transcribe(self, audio_file: str) -> str:
        """Transcreve o áudio já gravado"""
        result = self.model.transcribe(audio_file)
        return result["text"]
