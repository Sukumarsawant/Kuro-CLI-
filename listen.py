import speech_recognition as sr

def get_voice_input():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Kuro is Listening ....")
    with microphone as source:
        audio = recognizer.listen(source) #listen from microphone

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
        return None
    except sr.RequestError:
        print("🚫 Network error or API problem.")
        return None
    

    