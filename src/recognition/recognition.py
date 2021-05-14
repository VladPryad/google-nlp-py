from google.cloud import speech
import os
import config

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = config.GOOGLE_APPLICATION_CREDENTIALS

def Recognise():

    client = speech.SpeechClient()

    gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"

    audio = speech.RecognitionAudio(uri=gcs_uri)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))
        print("Confidence: {}".format(result.alternatives[0].confidence))