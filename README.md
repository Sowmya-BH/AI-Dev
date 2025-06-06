# **Nexus.ai Chatbot Application**   
 A Streamlit-based conversational AI application powered by Groq's LLMs.

## **Overview**
## 🧠 Nexus.ai - Your Multi-LLM Chat Assistant

    Welcome to Nexus.ai, an interactive chat application designed to showcase the power
    of multiple Large Language Models (LLMs). This project allows you to engage in
    conversations powered by different AI models, currently featuring those from Groq.

    Explore the unique capabilities and responses of various LLMs by selecting your
    preferred model from the sidebar. Ask questions, generate creative text, or
    simply chat with the AI of your choice.

  Check out the live app: [Nexus.ai](https://mynexus.streamlit.app/) 

---

## **Features**

- **Multi-LLM Support**: Users can choose from multiple LLM models (e.g., Llama3-8b-8192, Llama3-70b-8192, Gemma-7b-It) to tailor responses based on specific needs.
- **Chat History**: Persistent chat history allows users to revisit previous conversations.
- **User-Friendly Interface**: Streamlit provides an intuitive web interface for easy interaction.


---

## **Installation Guide**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/nexus-ai.git
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` File**:
   Add your Groq API key:
   ```plaintext
   GROQ_API_KEY=YOUR_API_KEY_HERE
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

---

## **Usage**

1. **Launch the Application**: Open a web browser and navigate to `http://localhost:8501`.
2. **Select an LLM Model**: Choose from the available models in the sidebar.
3. **Enter Your Query**: Type your question or prompt in the main input box.
4. **View Responses**: See the LLM's response displayed below your query.
5. **Explore Chat History**: Click on past queries in the sidebar to view their responses.

---

## ** Actively Working On (Towards Phase Two) **
The next stage of development will focus on customizing and specializing the AI capabilities of Nexus.ai which may involve customizing existing LLMs with specific datasets to create specialized bots tailored for particular domains or tasks.
Multimodal Input Support: Expanding the application to handle various input types beyond text, such as images and potentially audio.

- **Text Generation**: Advanced and contextually rich text responses tailored for specific domain.
- **Code Generation**: Assisting with programming tasks by generating code snippets.


---

## **Contributing**

Contributions are welcome! Please submit pull requests with detailed explanations of changes.


---

## **Acknowledgments**

- **Groq**: For providing access to their LLMs.
- **Streamlit**: For the intuitive web interface framework.

---

This README provides a comprehensive overview of the application, including setup instructions, features, and future development plans. Feel free to customize it further based on your specific needs!


