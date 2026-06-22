from groq import Groq
from config import GROQ_API_KEY

client = Groq(
    api_key=GROQ_API_KEY
)

def generate_jd_questions(
    resume_text,
    job_description
):

    prompt = f"""
You are a Senior Technical Interviewer.

Candidate Resume:
{resume_text}

Job Description:
{job_description}

Generate:

1. 5 HR Interview Questions

2. 5 Technical Interview Questions

The questions should be based mainly on the Job Description and partially on the candidate's resume.

Format the response neatly.
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