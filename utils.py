import os
from dotenv import load_dotenv
from google import genai

with open(".env", "w") as f:
    f.write("GOOGLE_API_KEY=AIzaSyABKfqcrhOf-pQ2c9I_IOcHsUI52FrYDEk")
    
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

def print_separator(title=""):
    """Print a separator with an optional title."""
    print("\n" + "-" * 30)
    if title:
        print(f"\U0001F4CC {title}")
    print("-" * 30)

def get_llm_response(prompt):
    completion = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return completion.text
