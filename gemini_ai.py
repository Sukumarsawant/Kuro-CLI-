import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

def get_command_from_gemini(user_input):
    model = genai.GenerativeModel("gemini-2.0-flash-lite")

    # WIll be updated later to avoid jailbreak - sukumar
    prompt = f"""
You are a terminal assistant.
Convert the following natural language instruction into a valid terminal command.
ONLY return the command (no explanations, no repetition, no markdown).

User: {user_input}
Shell:

"""
    # print("Gemini raw output:", command)

    try:
        response = model.generate_content(prompt) #prompt + input 
        command = response.text.strip().lower()

        if command :
            return command #will handle execution in main py
        # else:
        #     return "unknown"
    except Exception as e:
        print(f"❌ Gemini error: {e}")
        return "error"
