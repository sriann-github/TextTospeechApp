import os
import azure.cognitiveservices.speech as speechsdk

# Set up the subscription info for the Speech Service:
speech_key = "6a3c5829299347ff827de052096608d7"
service_region = "EastUS"

def text_to_speech(text, language="en-US", voice="en-US-JennyNeural"):
    # Configure the speech service
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_synthesis_language = language
    speech_config.speech_synthesis_voice_name = voice
    
    # Set up the audio output configuration
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # Create a synthesizer instance
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    
    # Perform the text-to-speech conversion
    result = synthesizer.speak_text_async(text).get()

    # Handle the result of the synthesis
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))

# Example call to the function
text_to_speech("Hello, how are you?", language="en-US", voice="en-US-JennyNeural")
