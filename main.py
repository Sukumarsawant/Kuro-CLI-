# Entry point to run 
import os 
from listen import get_voice_input
from gemini_ai import get_command_from_gemini
import uuid #random number
from speak import speak
import subprocess
from execute import execute_command,strip_clear

def main():
    print("Kuro is Listening...")

    while True:
        spoken_text = get_voice_input()

        if spoken_text:
            # Exit condition
            if spoken_text.strip().lower() in ["exit", "quit", "stop", "close"]:
                print("Exiting on command.")
                speak("Goodbye.")
                break

            command = get_command_from_gemini(spoken_text)
            cmd = strip_clear(command)
            execute_command(cmd)
            print(cmd)
            # speak(cmd)

        else:
            print("No speech detected, please check your microphone.")

if __name__ == "__main__":
    main()


    