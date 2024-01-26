import speech_recognition as sr

def recognize_speech():
    # Create a speech recognition object
    recognizer = sr.Recognizer()

    # Use the default microphone as the source
    with sr.Microphone() as source:
        print("Say something:")
        try:
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=1)
            
            # Listen to the user's speech
            audio = recognizer.listen(source, timeout=5)

            # Recognize the speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print("You said:", text)

        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print(f"Error connecting to Google API: {e}")

if __name__ == "__main__":
    recognize_speech()