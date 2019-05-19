def run_quickstart():
    # [START speech_quickstart]
    import io
    import os

    # Imports the Google Cloud client library
    # [START migration_import]
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    # [END migration_import]

    # Instantiates a client
    # [START migration_client]
    client = speech.SpeechClient()
    # [END migration_client]

    # The name of the audio file to transcribe
    file_name = os.path.join('C:/Users/User/PycharmProjects/GUI_imageTest','.','file.wav')

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.cloud_speech_pb2.RecognitionAudio(content=content)

    config = types.cloud_speech_pb2.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='ko-KR')

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
    # [END speech_quickstart]

if __name__ == '__main__':
    run_quickstart()