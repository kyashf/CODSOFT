import google.generativeai as genai
import sys
import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv('GEMINI_API_KEY')

def responce(task):
    sys.stdout.reconfigure(encoding='utf-8')
    genai.configure(api_key=KEY)

    generation_config = {
        "temperature": 0.7,
        "top_p": 0.85,
        "top_k": 50,
        "max_output_tokens": 100,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat()
    prompt = f"""
    Your role is to provide clear, concise guidance to help the user complete their to-do list task.
    Offer step-by-step instructions in a simple, easy-to-follow format, using short hints, in 100 words only.
    Do not include special characters like "*" in the text.
    
    User task: {task}
    """

    response = chat_session.send_message(prompt)
    guide = response.result.candidates[0].content.parts[0].text
    return guide

