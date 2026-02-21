import streamlit as st
from ocr_engine import extract_text, clean_text, detect_medicine_name
from medicine_engine import get_medicine_info, simplify_text
from language_engine import translate_telugu, generate_voice
import pandas as pd

db = pd.read_csv("medicine_db.csv")
medicine_names = db['name'].tolist()

st.title("Smart Medicine Assistant")

uploaded_file = st.file_uploader("Upload Medicine Image")

if uploaded_file:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    text = extract_text("temp.jpg")
    text = clean_text(text)

    medicine_name = detect_medicine_name(text, medicine_names)

    if medicine_name:
        info = get_medicine_info(medicine_name)

        simple_text = simplify_text(info)

        telugu_text = translate_telugu(simple_text)

        st.header("Medicine Name")
        st.write(medicine_name)

        st.header("Simple Explanation")
        st.write(simple_text)

        st.header("Telugu")
        st.write(telugu_text)

        if st.button("Play English Voice"):
            audio = generate_voice(simple_text, "en")
            st.audio(audio)

        if st.button("Play Telugu Voice"):
            audio = generate_voice(telugu_text, "te")
            st.audio(audio)

    else:
        st.error("Medicine not detected")