import speech_recognition as sr

def recognize_voice():
    try:
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.6)
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)
        return {"success": True, "text": text}

    except AttributeError:
        # PyAudio not available (Streamlit Cloud)
        return {
            "success": False,
            "error": "Microphone access is not supported in this environment."
        }

    except sr.UnknownValueError:
        return {"success": False, "error": "Speech not clear enough"}

    except sr.RequestError:
        return {"success": False, "error": "Recognition service unavailable"}
