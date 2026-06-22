from groq import Groq

from config import GROQ_API_KEY

client = Groq(
    api_key=GROQ_API_KEY
)

def improve_resume(resume_text):

    prompt = f"""
    Analyze this resume.

    Give:

    1. Resume Score out of 100
    2. Missing Skills
    3. Missing Projects
    4. ATS Improvements
    5. Interview Preparation Tips
    6. Final Suggestions

    Resume:
    {resume_text}
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