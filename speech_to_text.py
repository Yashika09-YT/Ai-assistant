import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening... Speak something:")
            audio = r.listen(source)  # Capture the audio input

        # Attempt to recognize the speech using Google Speech Recognition
        voice_data = r.recognize_google(audio)
        print(voice_data)
        return voice_data

    except sr.UnknownValueError:  # Handle cases where speech isn't recognized
        print("Google Speech Recognition could not understand the audio. Please try again.")

    except sr.RequestError as e:  # Handle API request errors
        print(f"Could not request results from Google Speech Recognition service; {e}")

    except Exception as e:  # Handle any other exceptions
        print(f"An unexpected error occurred: {e}")

# Call the function
speech_to_text()


