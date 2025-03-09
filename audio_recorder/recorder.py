import pyaudio
import keyboard
import wave

class AudioRecorder:
    """Gerencia a gravação de áudio e salva o arquivo"""
    RATE = 44000
    FORMAT = pyaudio.paInt16
    FRAMES_PER_BUFFER = 1024
    CHANNELS = 1
    RECORD_FILE = "record.wav"
    START_RECORDING_KEY = ']'
    STOP_RECORDING_KEY = "esc"

    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            input = True,
            format = self.FORMAT,
            channels = self.CHANNELS,
            rate = self.RATE,
            frames_per_buffer = self.FRAMES_PER_BUFFER
        )
        self.frames = []
        self.recording = False

    def start_recording(self, event = None) -> None:
        """Inicia a gravação"""
        if not self.recording:
            print("Ouvindo...")
            self.frames = []
            self.recording = True
    
    def stop_recording(self, event=None) -> None:
        """Para a gravação"""
        if self.recording:
            print("Parando de ouvir...")
            self.recording = False

    def save_record(self) -> None:
        """Salva a gravação em um arquivo WAV"""
        with wave.open(self.RECORD_FILE, "wb") as record:
            record.setnchannels(self.CHANNELS)
            record.setframerate(self.RATE)
            record.setsampwidth(self.audio.get_sample_size(self.FORMAT))
            record.writeframes(b"".join(self.frames))
    
    def run(self) -> None:
        """Loop principal da gravação"""
        print(f"Pressione '{self.START_RECORDING_KEY}' para começar a gravar e '{self.STOP_RECORDING_KEY}' para parar.")

        keyboard.on_press_key(self.START_RECORDING_KEY, self.start_recording)
        keyboard.on_press_key(self.STOP_RECORDING_KEY, self.stop_recording)

        while True:
            if self.recording:
                self.frames.append(self.stream.read(self.FRAMES_PER_BUFFER, exception_on_overflow = False))
        
            if not self.recording and self.frames:
                break

        self.stream.close()
        self.audio.terminate()
        self.save_record()
        print("Gravação salva.")
