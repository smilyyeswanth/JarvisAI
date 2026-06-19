import speech_recognition as sr

def wait_for_wake_word():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("🎤 Calibrating microphone...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        recognizer.energy_threshold = 300
        recognizer.dynamic_energy_threshold = True

        print("🎤 Listening for wake word...")

        while True:

            try:

                audio = recognizer.listen(
                    source,
                    timeout=None,
                    phrase_time_limit=4
                )

                text = recognizer.recognize_google(
                    audio
                ).lower()

                print(f'Heard: "{text}"')
                
                if (
                     "jarvis" in text
                    or "jervis" in text
                    or "service" in text
                    or "hey jarvis" in text
                    or "hi jarvis" in text
                    or "hey j" in text
                   ):
                 print("✅ Wake word detected")
                return True
                

            except sr.UnknownValueError:
                pass

            except sr.RequestError as e:
                print(f"Speech service error: {e}")

            except Exception as e:
                print(f"Error: {e}")