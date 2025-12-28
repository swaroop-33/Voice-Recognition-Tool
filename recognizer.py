import speech_recognition as sr

def recognize_voice():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.6)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return {"success": True, "text": text}
    except sr.UnknownValueError:
        return {"success": False, "error": "Speech not clear enough"}
    except sr.RequestError:
        return {"success": False, "error": "Recognition service unavailable"}
