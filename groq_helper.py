from groq import Groq

from config import GROQ_API_KEY

client = Groq(
    api_key=GROQ_API_KEY
)

def generate_ai_questions(resume_text):

    prompt = f"""
    You are a technical interviewer.

    Based on this resume generate:

    5 HR Interview Questions

    5 Technical Interview Questions

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