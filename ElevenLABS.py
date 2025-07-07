def main():
    import json
    from elevenlabs.client import ElevenLabs
    from elevenlabs import play
    with open("config.json", "r") as f:
        ELEVENLABS_API_KEY = json.load(f)["ELEVENLABS_API_KEY"]
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    voices = client.voices.search().voices
    print(f"Total Voices: {len(voices)}\n")
    for v in voices:
        print(f"Name: {v.name}")
        print(f"Voice ID: {v.voice_id}")
        print(f"Gender: {v.labels.get('gender', 'Unknown')}")
        print(f"Age: {v.labels.get('age', 'Unknown')}")
        print("-" * 30)

if __name__ == "__main__":
    main()
