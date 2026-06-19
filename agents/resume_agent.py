from ai.ollama_client import ask_ai

def analyze_job_description(job_text):

    prompt = f"""
You are an expert resume reviewer.

Analyze the following job description.

Provide:

1. Match Score (0-100)
2. Required Skills
3. Missing Skills
4. Resume Improvements
5. Interview Topics

Job Description:

{job_text}
"""

    return ask_ai(prompt)
