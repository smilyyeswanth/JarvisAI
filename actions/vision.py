import ollama
import subprocess
import os

def analyze_screen():
    screenshot_path = "/tmp/jarvis_screen.png"

    # Capture screenshot
    subprocess.run(
        ["screencapture", "-x", screenshot_path],
        check=True
    )

    # Verify screenshot exists
    if not os.path.exists(screenshot_path):
        return "Screenshot capture failed."

    try:
        response = ollama.chat(
            model="llava",
            messages=[
                {
                    "role": "user",
                    "content": "Describe everything visible on this screen.",
                    "images": [screenshot_path]
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"Vision analysis failed: {e}"