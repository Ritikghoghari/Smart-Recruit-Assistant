# AgileHire: AI-Powered Recruitment System 🕵️‍♂️

**AgileHire** is an intelligent RAG (Retrieval Augmented Generation) application designed to automate the initial screening process for recruitment. It uses LLMs to "read" resumes and answer recruiter questions with evidence-based responses.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=LangChain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=OpenAI&logoColor=white)

## 🚀 Features
*   **Resume Parsing**: Automatically extracts text from PDF resumes.
*   **Semantic Search**: Uses OpenAI Embeddings & ChromaDB to find relevant skills.
*   **AI Reasoning**: GPT-4 provides structured feedback on candidate fit.
*   **Interactive UI**: Built with Streamlit for easy drag-and-drop usage.

## 🛠️ Tech Stack
*   **Frontend**: Streamlit
*   **Orchestration**: LangChain (LCEL)
*   **Vector DB**: ChromaDB
*   **Model**: GPT-4o / GPT-3.5-turbo

## 🏃‍♂️ Quick Start
1.  Clone the repo:
    ```bash
    git clone https://github.com/YOUR_USERNAME/AgileHire.git
    cd AgileHire
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the app:
    ```bash
    streamlit run app.py
    ```

## 📂 Project Structure
*   `app.py`: Frontend UI logic.
*   `utils.py`: RAG pipeline (PDF -> Vectors -> Chat).
*   `requirements.txt`: Python dependencies.

---
*Built by **Ritik Ghoghari** as part of a Data Science Portfolio.*
