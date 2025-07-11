# from dotenv import load_dotenv
import json
import os
import google.generativeai as genai

def get_code_from_gemini(user_input):
    with open("config.json", "r") as f:
        GEMINI_API_KEY = json.load(f)["GEMINI_API_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.0-flash-lite")

    # WIll be updated later to avoid jailbreak - sukumar
    prompt = f"""
You are a terminal assistant.
Convert the following natural language instruction into a valid "WINDOWS" terminal command.
ONLY return the command (no explanations, no repetition, no markdown).

User: {user_input}
Shell:
 
if user is telling to write code in a file then reply in the following format
file_name lang_name which_code_u_want_to_write
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
