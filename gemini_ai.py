import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

def get_command_from_gemini(user_input):
    model = genai.GenerativeModel("gemini-2.0-flash-lite")

    # WIll be updated later to avoid jailbreak - sukumar
    prompt = f"""
You are a terminal assistant. Your job is to return one of the following commands ONLY:

- add_file <filename>
- delete_file <filename>
- list_files

⚠️ Always return in this format, no extra text.

Examples:
User: create a file named notes  
Output: add_file notes.txt

User: remove the file called log  
Output: delete_file log.txt

User: create a cpp file name code
Output add_file code.cpp

User: show my files  
Output: list_files

Now respond to this:
User: {user_input}
Output:
"""
    # print("📦 Gemini raw output:", command)

    try:
        response = model.generate_content(prompt) #prompt + input 
        command = response.text.strip().lower()

        if command :
            return command
        # else:
        #     return "unknown"
    except Exception as e:
        print(f"❌ Gemini error: {e}")
        return "error"
