import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# # Initialize Groq client
# client = Groq(api_key =st.secrets.get("GROQ_API_KEY"))


# Streamlit Interface for title
st.title("💬 Hi, I'm Nexus.ai!")
st.title("How can I help you Today??")
st.markdown("<hr style='border: 1px solid #ccc; opacity: 0.5;'>", unsafe_allow_html=True)


st.sidebar.markdown(r"""
   ---
    <h3 style="font-size: 2.0em; font-weight: bold;">🤖 Nexus.ai</h3>
    """, unsafe_allow_html=True)

# introduction 
st.sidebar.markdown(r"""
    ---
    ### 🖐 Banana Facts:
    * I use multiple LLMs.
    * You can select different models here.
    """)

# Create a dropdown menu in the sidebar for model selection
model = st.sidebar.selectbox(
    'Choose your LLM', ['Llama3-8b-8192', 'Llama3-70b-8192','Mixtral-8x7b-32768','Gemma-7b-It']
)


# Chat history initialization
if "history" not in st.session_state:
    st.session_state.history = []


# Groq client
client = Groq(api_key = st.secrets.get("GROQ_API_KEY"))
# print("API Key:", groq_api_key)  

# Initialize sessesion state for history
if "history" not in st.session_state:
    st.session_state.history = []

# User input text box in the main area of the application.
user_input = st.text_input("Enter your query: ", "")

# Button that triggers the LLM query when clicked.
if st.button("Submit"):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role" : "user",
                "content" : user_input,
            }
        ],
        model = model,
    )
    # Store the query and response in history
    response = chat_completion.choices[0].message.content
    st.session_state.history.append({"query" : user_input, "response" : response})

    # Display the response
    st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)

# Sidebar section for displaying the chat history. 
st.sidebar.markdown(r"""
   ---
    <h5 style="font-size: 1.0em; font-weight: bold;">Chat History</h5>
    """, unsafe_allow_html=True)

# Iterate through the stored chat history and display each entry as a button in the sidebar.
for i, entry in enumerate(st.session_state.history):
    if st.sidebar.button(f'🤖 {entry["query"][:20]}...', key=f"hist_{i}", help=entry["query"]):
        st.markdown(f'<div class="response-box">{entry["response"]}</div>', unsafe_allow_html=True)
