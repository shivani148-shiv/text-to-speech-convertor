import pyttsx3
from gtts import gTTS
from playsound import playsound
import os

def tts_offline(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def tts_online(text, filename="output.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    print(f"[+] Saved audio as {filename}")
    try:
        playsound(filename)
    except Exception as e:
        print(f"[!] Could not play audio: {e}")

def main():
    print("===== Text to Speech Converter =====")
    print("1. Offline TTS (pyttsx3)")
    print("2. Online TTS (gTTS)")
    choice = input("C"
                   "hoose method (1/2): ")

    text = input("Enter the text to convert: ")

    if choice == '1':
        print("[*] Converting using offline method...")
        tts_offline(text)
    elif choice == '2':
        print("[*] Converting using online method...")
        tts_online(text)
    else:
        print("[!] Invalid choice.")

if __name__ == "__main__":
    main()
