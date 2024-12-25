import streamlit as st

import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
model = os.getenv("AZURE_OPENAI_MODEL_NAME")

st.title("AOAI Chat App")

client = AzureOpenAI(
    api_key = api_key,
    azure_endpoint = azure_endpoint,
    api_version = api_version
)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = model

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model = model,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            max_tokens = 1024,
            temperature = 0.95,
            stream=True
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})