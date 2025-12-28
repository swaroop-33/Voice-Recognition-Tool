import streamlit as st
import time
from recognizer import recognize_voice

st.set_page_config(
    page_title="Voice Recognition Tool",
    layout="centered"
)

st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #0f2027, #000000);
    color: white;
}
.card {
    background: rgba(255, 255, 255, 0.06);
    backdrop-filter: blur(14px);
    border-radius: 16px;
    padding: 24px;
    margin-top: 20px;
}
.status {
    font-size: 14px;
    color: #00e5ff;
}
.output {
    font-size: 18px;
    font-weight: 500;
    color: #e0f7fa;
}
</style>
""", unsafe_allow_html=True)

st.markdown("## 🎙️ Voice Recognition Tool")
st.markdown("<span class='status'>Live • Secure • No Storage</span>", unsafe_allow_html=True)
st.markdown("Speak naturally. Your voice is processed live and not saved.")

if st.button("🎧 Start Listening"):
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.write("Listening for voice input...")
        time.sleep(0.6)

        result = recognize_voice()

        time.sleep(0.6)

        if result["success"]:
            st.success("Voice recognized")
            st.markdown("### Recognized Speech")
            st.markdown(
                f"<div class='output'>{result['text']}</div>",
                unsafe_allow_html=True
            )
        else:
            st.error(result["error"])

        st.markdown("</div>", unsafe_allow_html=True)
