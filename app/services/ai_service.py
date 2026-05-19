import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


async def ask_gemini(user_question: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_question,
            config=types.GenerateContentConfig(
                system_instruction=(
    "You are a smart and friendly AI assistant inside KazAvto Rental Bot. "
    "Answer naturally and clearly. "
    "You can answer general questions about cars, technology, daily life, and car rentals. "
    "Give complete answers, but keep them concise. "
    "Usually answer in 4-8 sentences. "
    "Do not cut your answer in the middle."
),
                max_output_tokens=800
            )
        )

        text = response.text

        if not text:
            return "🤖 Sorry, I could not generate a response."

        return text

    except Exception as e:
        print("Gemini API error:", e)
        return "🤖 Sorry, AI assistant is temporarily unavailable."