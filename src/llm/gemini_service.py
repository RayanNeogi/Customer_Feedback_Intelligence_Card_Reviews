import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

ROOT_DIR = Path(__file__).resolve().parents[2]
load_dotenv(ROOT_DIR / ".env")

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_ai(question, context):

    prompt = f"""
You are a Senior Customer Experience Consultant.

Below is customer feedback analytics data.

Context:
{context}

Question:
{question}

Instructions:

- Answer like an executive consultant.
- Give concise business insights.
- Mention risks.
- Mention priorities.
- Give actionable recommendations.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return completion.choices[0].message.content