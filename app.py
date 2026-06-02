import streamlit as st

st.set_page_config(
    page_title="7BROTHER'S INDIAN AI CREATOR",
    page_icon="🎵",
    layout="wide"
)

st.title("🎵 7BROTHER'S INDIAN AI CREATOR")

st.markdown("""
### 🇮🇳 India's AI Music Platform

Create Rajasthani, Punjabi, Haryanvi and Bhajan Style Music with AI
""")

st.divider()

genre = st.selectbox(
    "🎼 Select Genre / शैली चुनें",
    [
        "Rajasthani Rasiya",
        "Punjabi Folk",
        "Haryanvi",
        "Bhajan"
    ]
)

prompt = st.text_area(
    "📝 Describe Your Song",
    placeholder="Example: Romantic Rajasthani Rasiya about village love..."
)

if st.button("🚀 Generate Song"):
    st.success(f"Selected Genre: {genre}")
    st.info(f"Song Idea: {prompt}")

st.divider()

st.markdown("""
### 🎵 Supported Genres

✅ Rajasthani Rasiya

✅ Punjabi Folk

✅ Haryanvi

✅ Bhajan
""")
