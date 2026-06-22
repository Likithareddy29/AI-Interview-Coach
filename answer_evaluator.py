from groq import Groq

from config import GROQ_API_KEY

client = Groq(
    api_key=GROQ_API_KEY
)

def evaluate_answer(question, answer):

    prompt = f"""
    Interview Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate the answer.

    Give:
    1. Score out of 10
    2. Strengths
    3. Improvements
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