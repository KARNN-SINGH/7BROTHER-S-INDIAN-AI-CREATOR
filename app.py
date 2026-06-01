import streamlit as st

st.title("🎵 7BROTHER'S INDIAN AI CREATOR")

st.write("Welcome to Indian AI Music Creator")

genre = st.selectbox(
    "Genre Select Karein",
    ["Rajasthani", "Punjabi", "Haryanvi", "Bhajan"]
)

prompt = st.text_input("Song Idea")

if st.button("Generate"):
    st.write("Aapka Genre:", genre)
    st.write("Prompt:", prompt)