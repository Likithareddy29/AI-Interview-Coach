from groq import Groq
from config import GROQ_API_KEY

client = Groq(
    api_key=GROQ_API_KEY
)

def analyze_jd(
    resume_text,
    job_description
):

    prompt = f"""
You are an ATS and Recruitment Expert.

Resume:
{resume_text}

Job Description:
{job_description}

Provide ONLY:

Provide ONLY:

1. Missing Skills
2. Missing Keywords
3. Projects To Add
4. Certifications To Add
5. Interview Preparation Tips
6. Final Recommendation

IMPORTANT:
Do NOT provide ATS Score.
Do NOT provide Match Percentage.
Do NOT provide Resume Score.
Do NOT provide Readiness Score.

Return only the requested sections.
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