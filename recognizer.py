import speech_recognition as sr
import os

def recognize_voice():
    # Detect Streamlit Cloud environment
    if os.getenv("STREAMLIT_SERVER_RUNNING"):
        return {
            "success": False,
            "error": "Microphone access is not available in the cloud. Please run locally."
        }

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.6)
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)
        return {"success": True, "text": text}

    except sr.UnknownValueError:
        return {"success": False, "error": "Speech not clear enough"}
    except Exception as e:
        return {"success": False, "error": str(e)}
