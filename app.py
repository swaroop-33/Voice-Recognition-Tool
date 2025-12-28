import os

if st.button("🎧 Start Listening"):
    # Detect Streamlit Cloud
    if os.getenv("STREAMLIT_SERVER_RUNNING"):
        st.warning(
            "Microphone access is not available on Streamlit Cloud. "
            "Please run this application locally for full voice recognition."
        )
    else:
        result = recognize_voice()

        if result["success"]:
            st.success("Voice recognized")
            st.markdown("### Recognized Speech")
            st.write(result["text"])
        else:
            st.error(result["error"])
