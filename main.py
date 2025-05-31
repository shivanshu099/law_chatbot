import streamlit as st
import requests
import os
from llm import vector_search

st.set_page_config(page_title="Groq Chatbot", layout="centered")
st.title("⚖️ law Chatbot")
st.markdown(
    """
    <p>This is a law chatbot that uses Groq's LLM to answer questions about law. It uses vector search to find relevant documents and then generates answers based on those documents.</p>
    """,
    unsafe_allow_html=True
)

# Keep chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Ask me about law..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call Groq and show response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = vector_search(prompt)
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})

# --- Footer ---

st.markdown("<div style='height: 150px;'></div>", unsafe_allow_html=True)



st.markdown(
    """
    <hr style="margin-top: 2rem; margin-bottom: 0.5rem;">
    <div style='text-align: center; color: gray; font-size: 0.9rem;'>
        Built by <b>Shivanshu Prajapati</b>
    </div>
    """,
    unsafe_allow_html=True
)


#streamlit run main.py




