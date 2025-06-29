# Entry point to run 
import os 
from listen import get_voice_input
from gemini_ai import get_command_from_gemini
import uuid #random number
from speak import speak

def add_file(filename):
    with open(filename, 'w') as f:
        f.write("")
    msg = f"File '{filename}' created successfully."
    print(msg)
    speak(msg)


def del_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        msg = f"File '{filename}' deleted successfully."
    else:
        msg = f"File '{filename}' does not exist."
    print(msg)
    speak(msg)

def list_files():
    files = os.listdir()
    if files:
        speak("Here are the files in the current directory.")
        for f in files:
            print(" -", f)
            speak(f)
    else:
        speak("There are no files in the current directory.")

# if __name__ =="__main__":
#     print("🧠 AI CLI - Smart File Manager")
#     print("1. Add file")
#     print("2. Delete file")

#     choice = input("Enter your choice (1/2)")

#     if choice =='1':
#         file  =input("Enter filename")
#         add_file(file)

#     elif choice=='2':
#         file = input("Enter the file name")
#         del_file(file)

#     else : print("Invalid choice")

spoken_text = get_voice_input()

if spoken_text :
    command = get_command_from_gemini(spoken_text)
    print(f"Gemini interprete : {command}")

else:
    print("No speech detected please check your microphone")

clean_txt = command.strip().split()
# print("🔍 Parts:", clean_txt) 

cmd = clean_txt[0]
if len(clean_txt)>1 :
    filename = clean_txt[1]
else :
    random_id = uuid.uuid4().hex 
    filename = f"untitled_{round(random_id,4)}.txt" #random dedega

if cmd == "add_file" and filename:
    add_file(filename)
elif cmd == "delete_file" and filename:
    del_file(filename)
elif cmd == "list_files":
    list_files()
else:
    print("⚠️ Invalid or incomplete command.")


    