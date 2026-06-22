from groq import Groq
from config import GROQ_API_KEY

client = Groq(
    api_key=GROQ_API_KEY
)

def improve_resume_for_jd(
    resume_text,
    job_description
):

    prompt = f"""
You are an ATS Expert and Senior Recruiter.

Candidate Resume:
{resume_text}

Job Description:
{job_description}

Analyze the resume against the job description.

Provide:

1. Missing Skills
2. Missing Keywords
3. Resume Strengths
4. Resume Weaknesses
5. Projects To Add
6. Certifications To Add
7. Interview Preparation Tips
8. Final Recommendation

IMPORTANT:
Do NOT provide ATS Score.
Do NOT provide Resume Score.
Do NOT provide Match Percentage.
Do NOT provide Readiness Score.


Give a professional response.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content