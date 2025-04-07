import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key = os.environ["GROQ_API_KEY"] )

# ======== FIGMA INTEGRATION ========
# Add Figma-designed CSS (generated from Figma-to-Streamlit plugin)
# Streamlit Interface
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
client = Groq(api_key = os.environ["GROQ_API_KEY"] )
# print("API Key:", groq_api_key)  

# Initialize sessesion state for history
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Enter your query: ", "")

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

# Display history
# Display history with light gray background
# st.sidebar.markdown('<div style="background-color: #f0f0f0; padding: 10px; border-radius: 5px;">Chat History</div>', unsafe_allow_html=True)  # Light gray background

# # Display history as a full-width white tab in the sidebar
# st.sidebar.markdown(
#     """
#     <style>
#         .history-tab {
#             background-color: white;
#             color: black;
#             padding: 10px;
#             border-radius: 5px;
#             width: 100%;
#             text-align: center;
#             margin-bottom: 10px; /* Add some spacing below the tab */
#         }
#     </style>
#     <div class="history-tab">Chat History</div>
#     """,
#     unsafe_allow_html=True,
# )
st.sidebar.markdown(r"""
   ---
    <h5 style="font-size: 1.0em; font-weight: bold;">Chat History</h5>
    """, unsafe_allow_html=True)


for i, entry in enumerate(st.session_state.history):
    if st.sidebar.button(f'🤖 {entry["query"][:20]}...', key=f"hist_{i}", help=entry["query"]):
        st.markdown(f'<div class="response-box">{entry["response"]}</div>', unsafe_allow_html=True)
