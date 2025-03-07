import os
import streamlit as st
from config2 import apikey
import google.generativeai as genai

# Set API key
os.environ["GOOGLE_API_KEY"] = apikey
genai.configure(api_key=apikey)

# Model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="You are an AI assistant for the solar industry, providing expert advice on solar panels, installation, and maintenance and make sure not to give answer to any question not related to solar industry just say that this is out of my syllabus.",
)

# Initialize Streamlit app
st.title("🔆 Solar Industry AI Assistant")

# Session state for chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Chat interface
user_input = st.text_input("Ask me anything about solar energy:", key="input")

if st.button("Send"):
    if user_input:
        # Start chat session
        chat_session = model.start_chat(history=st.session_state.history)

        # Get response
        response = chat_session.send_message(user_input)
        model_response = response.text

        # Display response
        st.markdown(f"**AI Assistant:** {model_response}")

        # Append messages to history (Corrected format)
        st.session_state.history.append({"role": "user", "parts": [{"text": user_input}]})
        st.session_state.history.append({"role": "model", "parts": [{"text": model_response}]})

# Display chat history
st.subheader("Chat History")
for message in st.session_state.history:
    role = "👤 You" if message["role"] == "user" else "🤖 AI Assistant"
    st.markdown(f"**{role}:** {message['parts'][0]['text']}")
