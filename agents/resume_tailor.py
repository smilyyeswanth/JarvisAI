from ai.ollama_client import ask_ai

def tailor_resume(
    resume_text,
    job_description
):

    prompt = f"""
You are an expert ATS resume writer.

Rewrite and optimize the resume for the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Requirements:
1. Increase ATS match score.
2. Add missing keywords naturally.
3. Keep the resume professional.
4. Preserve truthful experience.
5. Return the full tailored resume.
"""

    return ask_ai(prompt)