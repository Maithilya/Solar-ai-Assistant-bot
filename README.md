# Solar-ai-Assistant-bot
AI assistant that provides accurate, helpful information about solar energy to both technical and non-technical users.

##  Project Overview
The **Solar AI Assistant** is an interactive chatbot designed to provide information and assistance on solar energy topics. It is powered by Google's **Gemini API** and built using **Streamlit** for a user-friendly UI. The assistant can answer solar-related queries, guide users on solar panel installations, and provide insights into renewable energy.

## Technologies Used
- **Python**
- **Google Gemini API** (Generative AI model)
- **Streamlit** (for UI)
- **PyCharm** (IDE)

## Features
- **Conversational AI Chatbot** for solar energy-related queries
- **User-friendly UI** using Streamlit
- **Remembers chat history** for a more natural conversation flow
- **Humorous & engaging responses** with Bollywood references (customizable)

## Setup Instructions

###  Prerequisites
Ensure you have the following installed:
- **Python 3.8+**
- Required Python libraries:
  ```bash
  pip install google-generativeai streamlit
  ```
- **Google API Key** (for Gemini API)
  - Save your API key in a `config2.py` file:
    ```python
    apikey = "YOUR_GOOGLE_API_KEY"
    ```

###  Running the Chatbot
1. Clone this repository:
   ```bash(install all libraries )
   
2. Run the Streamlit app:(dont'n forgot to add you appikey)
   ```bash
   streamlit run bot.py
   ```
3. The chatbot UI will open in your browser.

## 🛠 How It Works
1. User inputs a query related to solar energy.
2. The chatbot **processes the query** using Gemini API.
3. A response is generated and displayed in the UI.
4. Chat history is maintained for context-aware conversations.

##  Future Improvements
-  **Voice input & output** for hands-free interaction
-  **Integration with IoT devices** to monitor solar panels
-  **Database storage** for frequently asked questions
-  **Mobile-friendly UI** for better accessibility


---

 **Developed by Maithilya Patle** 

