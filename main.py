import os
import threading
import tkinter as tk
from tkinter import scrolledtext, ttk, simpledialog, messagebox
import queue
import json

from listen import get_voice_input
from gemini_ai import get_code_from_gemini
from speak import speak, set_voice_by_id, list_voices
from execute import execute_command, strip_clear
from write_code import handle_code_write

q = queue.Queue()
running = False
voice_list = []

# --- CONFIG LOGIC START ---
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            try:
                data = json.load(f)
                if 'GEMINI_API_KEY' in data and data['GEMINI_API_KEY']:
                    return data
            except Exception:
                pass
    # Prompt for keys if missing or invalid
    root = tk.Tk()
    root.withdraw()  # Hide main window for prompt
    while True:
        gemini_key = simpledialog.askstring("Gemini API Key Required", "Enter your Gemini API Key:")
        if gemini_key:
            break
        messagebox.showerror("Error", "Gemini API Key is required!")
    eleven_key = simpledialog.askstring("Eleven Labs API Key (Optional)", "Enter your Eleven Labs API Key (leave blank for default voice):")
    config = {"GEMINI_API_KEY": gemini_key, "ELEVENLABS_API_KEY": eleven_key or ""}
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)
    root.destroy()
    return config
config = load_config()
# --- CONFIG LOGIC END ---


def main():
    global running
    q.put("Kuro is Listening...")
    while running:
        spoken_text = get_voice_input()
        check = 0
        if spoken_text:
            q.put("You said: " + spoken_text)
            if spoken_text.strip().lower() in ["exit", "quit"]:
                q.put("Exiting on command.")
                speak("Goodbye.")
                root.quit()
                return
            elif spoken_text.strip().lower() in ["stop", "close"]:
                stop_main()
                continue
            command = get_code_from_gemini(spoken_text)
            if not check:
                cmd = strip_clear(command)
                if cmd.startswith("cd "):
                    path = cmd[3:].strip()
                    try:
                        os.chdir(path)
                        current_dir.set("Current Directory: " + os.getcwd())
                        q.put("Changed directory to: " + os.getcwd())
                        speak("Changed directory to " + path)
                    except Exception as e:
                        q.put("[Error] " + str(e))
                        speak("Directory change failed")
                else:
                    try:
                        execute_command(cmd)
                        q.put(cmd)
                        speak(cmd)
                    except Exception as e:
                        q.put("[Error] " + str(e))
                        speak("Execution failed")
        else:
            q.put("No speech detected, please check your microphone.")


def threaded_main():
    global running
    if not running:
        running = True
        start_btn.config(state=tk.DISABLED)
        stop_btn.config(state=tk.NORMAL)
        threading.Thread(target=main, daemon=True).start()


def stop_main():
    global running
    running = False
    start_btn.config(state=tk.NORMAL)
    stop_btn.config(state=tk.DISABLED)
    q.put("Kuro stopped.")


def update_output():
    while not q.empty():
        message = q.get()
        output.insert(tk.END, message + "\n")
        output.see(tk.END)
    root.after(100, update_output)


def populate_voice_dropdown():
    global voice_list
    voice_list = list_voices()
    voice_dropdown['values'] = [f"{v['name']} ({v['voice_id'][:6]})" for v in voice_list]
    if voice_list:
        voice_dropdown.current(0)
        set_voice_by_id(voice_list[0]['voice_id'])


def on_voice_select(event):
    selection = voice_dropdown.current()
    if 0 <= selection < len(voice_list):
        set_voice_by_id(voice_list[selection]['voice_id'])
        q.put(f"Voice set to: {voice_list[selection]['name']}")


root = tk.Tk()
root.title("Kuro Voice Assistant")
root.geometry("800x560")

# Gradient Background Simulation (using Canvas)
canvas = tk.Canvas(root, width=800, height=560)
canvas.pack(fill="both", expand=True)
canvas.create_rectangle(0, 0, 800, 560, fill="#1f1c2c", outline="")
canvas.create_rectangle(0, 0, 800, 560, fill="", outline="", stipple="gray25")

# Use stylish fonts and overlay widgets on canvas
font_name = "Segoe UI"
current_dir = tk.StringVar()
current_dir.set("Current Directory: " + os.getcwd())

style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", font=(font_name, 12), padding=6)
style.configure("TLabel", background="#1f1c2c", foreground="white", font=(font_name, 11))
style.configure("TCombobox", padding=5)

frame = tk.Frame(root, bg="#1f1c2c")
frame.place(relx=0.5, rely=0.05, anchor="n")

start_btn = ttk.Button(frame, text="Start", width=20, command=threaded_main)
start_btn.grid(row=0, column=0, padx=10)

stop_btn = ttk.Button(frame, text="Stop", width=20, command=stop_main, state=tk.DISABLED)
stop_btn.grid(row=0, column=1, padx=10)

voice_label = ttk.Label(frame, text="Select Voice:")
voice_label.grid(row=1, column=0, padx=10, pady=10)

voice_dropdown = ttk.Combobox(frame, state="readonly", width=40)
voice_dropdown.grid(row=1, column=1, padx=10, pady=10)
voice_dropdown.bind("<<ComboboxSelected>>", on_voice_select)

output = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=22, width=90, bg="#2e2e3e", fg="white", font=(font_name, 10))
output.place(relx=0.5, rely=0.25, anchor="n")

current_dir_label = ttk.Label(root, textvariable=current_dir, anchor="w")
current_dir_label.place(relx=0.02, rely=0.94, anchor="w")

populate_voice_dropdown()
update_output()
root.mainloop()
