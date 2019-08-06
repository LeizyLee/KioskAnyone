class getWaveFile:
    def __init__(self):
        import pyaudio
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1  # only mono
        self.RATE = 16000
        self.CHUNK = 1024  # 확인 필요
        self.RECORD_SECONDS = 7  # 7초 녹음
        self.WAVE_OUTPUT_FILENAME = "file.wav"
        self.audio = pyaudio.PyAudio()

    def run(self):
        stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                                      rate=self.RATE, input=True,
                                      frames_per_buffer=self.CHUNK)
        print("녹음중...")
        frames = []
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            frames.append(data)
        print("녹음 끝")

        stream.stop_stream()
        stream.close()
        self.audio.terminate()

        import wave
        waveFile = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(self.CHANNELS)
        waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        waveFile.setframerate(self.RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()

if __name__ == '__main__':
    test = getWaveFile()
    test.run()
