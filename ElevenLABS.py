import sys
import os

# Ensure the correct ElevenLabs path is used
if "C:/PythonLibs" not in sys.path:
    sys.path.insert(0, "C:/PythonLibs")

from config import ELEVENLABS_API_KEY as api_key  # Using config.py instead of .env

from elevenlabs.client import ElevenLabs
from elevenlabs import play

client = ElevenLabs(api_key=api_key)

voices = client.voices.search().voices

print(f"Total Voices: {len(voices)}\n")

for v in voices:
    print(f"Name: {v.name}")
    print(f"Voice ID: {v.voice_id}")
    print(f"Gender: {v.labels.get('gender', 'Unknown')}")
    print(f"Age: {v.labels.get('age', 'Unknown')}")
    print("-" * 30)
