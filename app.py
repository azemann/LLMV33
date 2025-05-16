import streamlit as st
from modules.loader_text import load_text_file
from modules.loader_audio import transcribe_audio
from modules.loader_video import transcribe_video_audio
from modules.utils_chat import init_chat, update_chat

import tempfile
import os

st.set_page_config(page_title="AZE LLM", layout="wide")

st.title("🤖 Bienvenue sur ton assistant AZE LLM v3")
st.info("Dépose un fichier texte, audio ou vidéo pour lancer l'analyse.")

uploaded_file = st.file_uploader("Dépose ton fichier ici", type=["txt", "md", "pdf", "docx", "mp3", "wav", "mp4", "mov"])

chat_history = init_chat()

if uploaded_file:
    file_ext = uploaded_file.name.split('.')[-1].lower()
    with tempfile.NamedTemporaryFile(delete=False, suffix='.' + file_ext) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    if file_ext in ["txt", "md", "pdf", "docx"]:
        content = load_text_file(tmp_path)
    elif file_ext in ["mp3", "wav"]:
        content = transcribe_audio(tmp_path)
    elif file_ext in ["mp4", "mov"]:
        content = transcribe_video_audio(tmp_path)
    else:
        content = "Format non supporté."

    st.success("✅ Fichier traité.")
    st.text_area("📄 Contenu extrait :", content, height=200)

    chat_history.append({"role": "system", "content": content})

user_input = st.chat_input("💬 Pose ta question")
if user_input:
    response = update_chat(user_input, chat_history)
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(response)
