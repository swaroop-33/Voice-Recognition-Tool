import streamlit as st
import os
from recognizer import recognize_voice

st.set_page_config(page_title="Voice Recognition Tool")

st.title("🎙️ Voice Recognition Tool")
st.caption("Live • Privacy-focused • No storage")

if st.button("🎧 Start Listening"):
    if os.getenv("STREAMLIT_SERVER_RUNNING"):
        st.warning(
            "Microphone access is not available on Streamlit Cloud. "
            "Please run this application locally for full functionality."
        )
    else:
        result = recognize_voice()

        if result["success"]:
            st.success("Voice recognized")
            st.write(result["text"])
        else:
            st.error(result["error"])
