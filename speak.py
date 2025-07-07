import sys
import os
import json

# Ensure the correct ElevenLabs path is used
if "C:/PythonLibs" not in sys.path:
    sys.path.insert(0, "C:/PythonLibs")

def get_elevenlabs_key():
    try:
        with open("config.json", "r") as f:
            return json.load(f)["ELEVENLABS_API_KEY"]
    except Exception:
        return ""

_elevenlabs_client = None
_voices_cache = None
_current_voice_id = None

def get_elevenlabs_client():
    global _elevenlabs_client, _voices_cache, _current_voice_id
    if _elevenlabs_client is None:
        from elevenlabs.client import ElevenLabs
        key = get_elevenlabs_key()
        _elevenlabs_client = ElevenLabs(api_key=key)
        _voices_cache = _elevenlabs_client.voices.search().voices
        female = next((v for v in _voices_cache if "female" in v.name.lower()), None)
        _current_voice_id = female.voice_id if female else _voices_cache[0].voice_id
    return _elevenlabs_client

def speak(text: str) -> None:
    key = get_elevenlabs_key()
    if key:
        client = get_elevenlabs_client()
        from elevenlabs import play
        global _current_voice_id
        audio = client.text_to_speech.convert(
            text=text,
            voice_id=_current_voice_id,
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128"
        )
        play(audio)
    else:
        import pyttsx3
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

def list_voices():
    key = get_elevenlabs_key()
    if key:
        client = get_elevenlabs_client()
        return [{"name": v.name, "voice_id": v.voice_id} for v in _voices_cache]
    else:
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        return [{"name": v.name, "voice_id": v.id} for v in voices]

def set_voice_by_id(voice_id: str):
    key = get_elevenlabs_key()
    if key:
        global _current_voice_id
        _current_voice_id = voice_id
    else:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('voice', voice_id)
