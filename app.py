import streamlit as st
import os
from recognizer import recognize_voice

st.set_page_config(page_title="Voice Recognition Tool")

st.title("🎙️ Voice Recognition Tool")
st.caption("Live • Privacy-Focused • No Storage")

st.info(
    "Note: Full voice recognition works when run locally. "
    "Cloud deployment is for UI demonstration."
)

if st.button("🎧 Start Listening"):
    # HARD BLOCK for Streamlit Cloud
    if "STREAMLIT_SERVER_RUNNING" in os.environ:
        st.warning(
            "Microphone access is not available on Streamlit Cloud.\n\n"
            "Please run this application locally for full functionality."
        )
    else:
        result = recognize_voice()

        if result["success"]:
            st.success("Voice recognized")
            st.write(result["text"])
        else:
            st.error(result["error"])
