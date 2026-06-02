import streamlit as st
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #0f0f0f, #1a0033);
}

h1 {
    color: #c77dff;
    text-align: center;
}
.stButton > button {
    background-color: #8a2be2;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #a855f7;
}

.stButton > button:active {
    background-color: #6a0dad;
}


</style>
""", unsafe_allow_html=True)
st.set_page_config(
    page_title="7BROTHER'S INDIAN AI CREATOR",
    page_icon="🎵",
    layout="wide"
)
col1, col2, col3 = st.columns([2,1,2])

with col2:
    st.image("logo.png", width=250)

st.title("🎵 7BROTHER'S INDIAN AI CREATOR")
st.markdown("""
## 🚀 Create Indian Folk Music with AI

### 🎵 Rajasthani • Punjabi • Haryanvi • Bhajan

India's AI-Powered Music Creation Platform
""")

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

    st.subheader("🎵 Generated Lyrics")

    lyrics = f"""
    [{genre} Song]

    {prompt}

    ये एक डेमो AI गीत है।

    तेरी यादों का मौसम आया,
    दिल ने फिर तेरा नाम बुलाया।

    सपनों में तेरा चेहरा दिखे,
    हर धड़कन में तेरा साया।

    ओ साथी मेरे,
    तू ही मेरी कहानी।
    """

    st.write(lyrics)


st.divider()

st.markdown("""
### 🎵 Supported Genres

✅ Rajasthani Rasiya

✅ Punjabi Folk

✅ Haryanvi

✅ Bhajan
""")
st.divider()

st.markdown("""
<div style='text-align: center;'>

Made with ❤️ in India 🇮🇳

© 2026–27 7BROTHER'S

</div>
""", unsafe_allow_html=True)
