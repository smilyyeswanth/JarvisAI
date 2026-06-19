from ai.ollama_client import ask_ai

def compare_resume_to_jd(
    resume_text,
    job_description
):

    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze the resume against the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Return the result in this format:

ATS Match Score:
- Score: XX/100

Matching Skills:
- Skill 1
- Skill 2
- Skill 3

Missing Skills:
- Skill 1
- Skill 2
- Skill 3

Resume Improvements:
- Improvement 1
- Improvement 2
- Improvement 3

Interview Questions:
1. Question 1
2. Question 2
3. Question 3
"""

    return ask_ai(prompt)