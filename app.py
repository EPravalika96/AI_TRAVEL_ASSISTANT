import streamlit as st
import google.generativeai as genai
import time

st.title("💬Chat with Robo-TravelSaathi")

file1 = open("gemini_key.txt")
key = file1.read()
genai.configure(api_key=key)

with st.sidebar:
    st.title("AI Travel Assistant")
    st.markdown('''
    ## About
    This app provides assistance in answering the user queries related to travel and helps in planning your trips:
    - [Streamlit](https://streamlit.io/)
    - [GoogleAI](https://ai.google.dev/)
    ''')
    st.write('Made by Pravalika')

model = genai.GenerativeModel(model_name='gemini-1.5-pro-latest',
                              system_instruction="""You are a AI Travel Assistant. Your name is Robo-TravelSaathi. You should take the travel place from user, help personalization in trip planning and resolve travel queries. Anything asked other than
                              travel related queries, politely say no"""
                             )


if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello, How may I help you?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_query = st.chat_input()

if user_query is not None:
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.write(user_query)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        ai_response = model.generate_content(user_query)
        st.write(ai_response.text)
    ai_message = {"role": "assistant", "content": ai_response.text}
    st.session_state.messages.append(ai_message)