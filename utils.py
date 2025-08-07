import os
from dotenv import load_dotenv
from google import genai

with open(".env", "w") as f:
    f.write("GOOGLE_API_KEY=AIzaSyABKfqcrhOf-pQ2c9I_IOcHsUI52FrYDEk")
try:    
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    client = genai.Client(api_key=api_key)
except Exception as e:
    print(f"Failed to connect with the api key.{e}")

def print_separator(title):
    print("-" * 30)
    print(f"\U0001F4CC {title}")
    print("-" * 30)

def get_llm_response(prompt):
    completion = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return completion.text
