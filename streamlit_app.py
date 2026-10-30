import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = os.getenv("OPENAI_MODEL", "gpt-6-luna")

# Show title and description.
st.title("💬 Chatbot")
st.write(
    f"This is a simple chatbot that uses OpenAI's `{MODEL}` model to generate responses. "
    "To use this app, you need an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
    "Put it in a `.env` file (see README) or paste it below."
)

# Read the key from .env first; fall back to asking in the UI.
openai_api_key = os.getenv("OPENAI_API_KEY") or st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝")
else:
    client = OpenAI(api_key=openai_api_key)

    # Store chat messages in session state so they persist across reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        stream = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
