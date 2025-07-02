import os
import platform
import subprocess
import re

def strip_clear(command):
    
    """
    Removes code block markers like ```bash from Gemini's response.
    """
    cleaned = re.sub(r"```(bash|shell)?", "", command)  # Remove ```bash or ```shell
    cleaned = cleaned.replace("```", "")  # Remove ending ```
    return cleaned.strip()


def execute_command(command):
    # Windows fallback for 'touch' command
    if platform.system() == "Windows" and command.startswith("touch "):
        filename = command[6:].strip()

        # Handle Unix-style escaping (e.g., in\ army → in army)
        filename = filename.replace("\\", "").strip('"')

        try:
            with open(filename, 'w') as f:
                pass
            return f"📁 File '{filename}' created successfully (Windows fallback)."
        except Exception as e:
            return f"❌ Failed to create file: {e}"

    # For all other commands, try subprocess
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout.strip() or "✅ Command executed."
    except subprocess.CalledProcessError as e:
        return f"❌ Command failed:\n{e.stderr.strip()}"
