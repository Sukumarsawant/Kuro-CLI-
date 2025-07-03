import sys
import os

# Ensure the correct ElevenLabs path is used
if "C:/PythonLibs" not in sys.path:
    sys.path.insert(0, "C:/PythonLibs")

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play

load_dotenv()
client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

voices = client.voices.search().voices
female = next((v for v in voices if "female" in v.name.lower()), None)
VOICE_ID = female.voice_id if female else voices[0].voice_id
_current_voice_id = "oVTazm7oXEiFKgHSNqS8"

def speak(text: str) -> None:
    audio = client.text_to_speech.convert(
        text=text,
        voice_id=_current_voice_id,
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128"
    )
    play(audio)

def list_voices():
    return [{"name": v.name, "voice_id": v.voice_id} for v in voices]

def set_voice_by_id(voice_id: str):
    global _current_voice_id
    _current_voice_id = voice_id
