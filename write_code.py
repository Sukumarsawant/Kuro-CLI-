import os
from speak import speak
from gemini_ai import get_code_from_gemini

def handle_code_write(gemini_response: str, check: int) -> int:
    """
    Tries to parse and handle a code-writing Gemini response.
    Returns:
        1 if code was written
        0 if response didn't match expected format
    """

    parts = gemini_response.strip().split(" ", 2)
    if len(parts) != 3:
        if check == 0:
            return 0  # signal to treat it like a shell command
        print("❌ Invalid code write format.")
        speak("I couldn't understand the file format for writing code.")
        return 0

    file_name, lang, topic = parts
    print(f"📝 Writing {lang} code for: {topic} into {file_name}")

    # Form prompt to request code
    code_prompt = f"Write full {lang} code for: {topic}. Only return raw code. No explanations."

    # Get code from Gemini
    code = get_code_from_gemini(code_prompt)
    if not code or "error" in code.lower():
        print("❌ Gemini failed to return code.")
        speak("Gemini failed to generate code.")
        return 0

    try:
        # Ensure directory exists if needed
        if "/" in file_name or "\\" in file_name:
            dir_path = os.path.dirname(file_name)
            if dir_path:
                os.makedirs(dir_path, exist_ok=True)

        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(code)

        print(f"✅ Code saved in {file_name}")
        speak(f"{topic} code written to {file_name}")
        return 1

    except Exception as e:
        print(f"❌ Error writing code to file: {e}")
        speak("I couldn't write the code due to an error.")
        return 0
