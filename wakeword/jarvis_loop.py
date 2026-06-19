from wakeword.listener import wait_for_wake_word
from voice.listen import listen
from voice.speak import speak
import requests

while True:

    try:

        wait_for_wake_word()

        speak("Yes Yeswanth")

        print("🎤 Waiting for command...")

        command = listen()

        if not command:
            continue

        print("Command:", command)

        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={
                "message": command
            }
        )

        answer = response.json()["response"]

        print("Jarvis:", answer)

        speak(answer)

    except KeyboardInterrupt:
        print("Stopping Jarvis...")
        break

    except Exception as e:
        print("Error:", e)