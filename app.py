import streamlit as st
import google.generativeai as genai
import os
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
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("models/gemini-2.5-flash")

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
    
try:
    response = model.generate_content(
        f"Write a short {genre} style song about: {prompt}"
    )
    st.write(response.text)

except Exception as e:
    st.error(str(e))

    if genre == "Rajasthani Rasiya":
        title = "🎵 Thari Yaadan Ro Geet"
        lyrics = f"""
        म्हारी धरती रो रंग निरालो,
        {prompt}

        रेत रा धोरां में थारी याद आवे,
        दिल रो पंछी थारो नाम गावै।

        चांदणी रातां में सपनां सजावूं,
        थारी याद में गीत सुनावूं।
        """

    elif genre == "Punjabi Folk":
        title = "🎵 Dil Da Safar"
        lyrics = f"""
        {prompt}

        ni tere bina dil lagda nahi,
        tere naam di dhun vajdi rahi।

        sajna ve tu meri jaan,
        tere naal hi meri pehchaan।
        """

    elif genre == "Haryanvi":
        title = "🎵 Gaam Ki Yaad"
        lyrics = f"""
        {prompt}

        tere bina dil konya manne,
        yaad teri roj satave se।

        gaam ki galiyan yaad karave,
        dil tera naam bulave se।
        """

    else:
        title = "🎵 Bhakti Ki Dhun"
        lyrics = f"""
        {prompt}

        hey prabhu tera naam pyara,
        tu hi jag ka sahara।

        bhakti ras mein mann rang jaaye,
        tera gun gaan sab gaaye।
        """

    st.markdown(f"## {title}")
    st.write(lyrics)

    st.download_button(
        label="⬇️ Download Lyrics",
        data=lyrics,
        file_name="7brothers_song.txt",
        mime="text/plain"
    )


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
