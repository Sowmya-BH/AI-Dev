import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.environ["GROQ_API_KEY"])


def initialize_session_state():
    """Initializes session state for chat history."""
    if "history" not in st.session_state:
        st.session_state.history = []


def display_title():
    """Displays the title of the application."""
    st.title("💬 Hi, I'm Nexus.ai!")
    st.title("How can I help you Today??")
    st.markdown("<hr style='border: 1px solid #ccc; opacity: 0.5;'>", unsafe_allow_html=True)


def display_sidebar():
    """Displays the sidebar with the bot information and model selection."""
    st.sidebar.markdown(r"""
        ---
        <h3 style="font-size: 2.0em; font-weight: bold;">🤖 Nexus.ai</h3>
    """, unsafe_allow_html=True)

    st.sidebar.markdown(r"""
        ---
        ### 🖐 Banana Facts:
        * I use multiple LLMs.
        * You can select different models here.
    """)

    model = st.sidebar.selectbox(
        'Choose your LLM',
        ['Llama3-8b-8192', 'Llama3-70b-8192', 'Mixtral-8x7b-32768', 'Gemma-7b-It']
    )
    return model


def get_user_input():
    """Gets user input from the text input box."""
    user_input = st.text_input("Enter your query: ", "")
    return user_input


def query_llm(user_input, model):
    """Queries the Groq LLM with the user input and selected model."""
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model=model,
    )
    response = chat_completion.choices[0].message.content
    return response


def display_response(response):
    """Displays the LLM response in the main area."""
    st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)


def update_chat_history(query, response):
    """Stores the user query and LLM response in the session history."""
    st.session_state.history.append({"query": query, "response": response})


def display_chat_history():
    """Displays the chat history in the sidebar."""
    st.sidebar.markdown(r"""
        ---
        <h5 style="font-size: 1.0em; font-weight: bold;">Chat History</h5>
    """, unsafe_allow_html=True)

    for i, entry in enumerate(st.session_state.history):
        if st.sidebar.button(f'🤖 {entry["query"][:20]}...', key=f"hist_{i}", help=entry["query"]):
            display_response(entry["response"])


def main():
    """Main function to run the Streamlit application."""
    initialize_session_state()
    display_title()
    model = display_sidebar()
    user_input = get_user_input()

    if st.button("Submit"):
        if user_input:
            response = query_llm(user_input, model)
            update_chat_history(user_input, response)
            display_response(response)

    display_chat_history()


if __name__ == "__main__":
    main()
