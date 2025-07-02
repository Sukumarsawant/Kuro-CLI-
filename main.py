# Entry point to run 
import os 
from listen import get_voice_input
from gemini_ai import get_command_from_gemini
import uuid #random number
from speak import speak
import subprocess
from execute import execute_command,strip_clear

spoken_text = get_voice_input()

if spoken_text :
    command = get_command_from_gemini(spoken_text)
    # print(f"Gemini interprete : {command}")
    cmd = strip_clear(command)
    execute_command(cmd)
    print(cmd)
    # speak(cmd)

else:
    print("No speech detected please check your microphone")




    