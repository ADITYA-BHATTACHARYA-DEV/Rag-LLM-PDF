import streamlit as st
import ollama
import time


def stream_data(text,delay:float=0.02):
    for word in text.split():
        yield word + " "
        time.sleep(delay)



#input for the prompt prompt
prompt=st.chat_input("Ask ME Anything")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    with st.spinner("Processing...."):
        result=ollama.chat(model="llama3:latest",messages=[{
            "role":"user",
            "content":prompt,
        }])
        response=result["message"]["content"]
        st.write(ollama.list())

        

