from ai.ollama_client import ask_ai

print("Testing Ollama...")

response = ask_ai(
    "Say hello in one sentence."
)

print(response)