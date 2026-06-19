import speech_recognition as sr

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("🎤 Listening...")

        audio = recognizer.listen(
            source,
            phrase_time_limit=5
        )

    try:

        text = recognizer.recognize_google(
            audio
        )

        print("You:", text)

        return text

    except Exception as e:

        print("Listen Error:", e)

        return ""