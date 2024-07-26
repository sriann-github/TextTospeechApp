import os
import azure.cognitiveservices.speech as speechsdk # type: ignore
from ExtractTextFromWebpage import extract_text_from_url
from ExtractTextFromPdf import extract_text_from_pdf
import time

# Set up the subscription info for the Speech Service:
speech_key = "d5dc28d6367c4b17b8784134ab552517"
service_region = "EastUS"

def text_to_speech(text, language="en-US", voice="en-US-JennyNeural"):
    # Configure the speech service
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_synthesis_language = language
    speech_config.speech_synthesis_voice_name = voice
    
    # Enable detailed logging
    speech_config.set_property(speechsdk.PropertyId.Speech_LogFilename, "log.txt")
    
    # audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # Set up the audio output configuration to save to a file
    audio_config = speechsdk.audio.AudioOutputConfig(filename="outputFromRandomText.wav")

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
        print("Error details: {}".format(cancellation_details.error_details))
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))

"""def text_to_speech_with_retry(text, language="en-US", voice="en-US-JennyNeural", retries=3):
    for attempt in range(retries):
        try:
            text_to_speech(text, language, voice)
            break
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(2)  # wait before retrying
            else:
                print("All attempts failed.")"""


def split_text(text, max_length=500):
    # Split text into chunks of max_length characters without breaking words
    words = text.split()
    chunks = []
    current_chunk = ""
    for word in words:
        if len(current_chunk) + len(word) + 1 > max_length:
            chunks.append(current_chunk)
            current_chunk = word
        else:
            if current_chunk:
                current_chunk += " " + word
            else:
                current_chunk = word
    if current_chunk:
        chunks.append(current_chunk)
        text_to_process = "".join(chunks)
    return text_to_process


def process_text_with_retry(text, retries=3):
    text_to_process = split_text(text)
   # for chunk in chunks:
    for attempt in range(retries):
        try:
            text_to_speech(text_to_process, language="en-US", voice="en-US-JennyNeural")
            break
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(2)  # wait before retrying
            else:
                print("All attempts failed.")
                    
# Example call to the function
# text_to_use = extract_text_from_url("https://example.com")

# text_to_use = extract_text_from_pdf("Pluralsight-AI-Sandboxes.pdf")

text_to_use = "This is a random text that I am using as an example for demonstrating."
print(f"Extracted text: {text_to_use}")

process_text_with_retry(text_to_use)

