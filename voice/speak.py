import os

def speak(text):
    text = text.replace('"', "")
    os.system(f'say "{text}"')