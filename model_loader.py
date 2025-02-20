import openai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAI API Setup
openai.api_key = OPENAI_API_KEY

def generate_code_completion(prompt):
    """Generates AI-based code completion using OpenAI's API."""
    try:
        response = openai.Completion.create(
            engine="code-davinci-002",  # OpenAI's Codex engine for code completion
            prompt=prompt,
            max_tokens=100,
            temperature=0.3,
            stop=["\n\n"]  # Stop generation at double new line
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
