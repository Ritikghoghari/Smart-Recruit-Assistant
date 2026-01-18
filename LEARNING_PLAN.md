# Learning Plan: Building "AgileHire"

We will build this project in **4 Phases**. I will set up the skeleton for each phase, and you will complete the "Mission" (coding task) to make it work.

## Phase 1: Environment & Data Ingestion (Today)
**Goal**: Get Python running, install libraries, and verify we can read a PDF resume.
*   **Concepts**: Virtual Environments, Python I/O, PDF Parsing.
*   **Your Mission**: Write a function `extract_text_from_pdf` that takes a file and returns clean string text.

## Phase 2: The Brain (Embeddings & Vector DB)
**Goal**: Convert text into numbers (vectors) so the computer can understand "meaning".
*   **Concepts**: Embeddings (OpenAI/HuggingFace), Vector Stores (ChromaDB).
*   **Your Mission**: Configure the "Chunking" strategy – deciding how to split the resume into small pieces for the AI to read.

## Phase 3: The Intelligence (RAG & LLM)
**Goal**: Connect the Database to GPT-4 so we can ask questions.
*   **Concepts**: Retrieval Augmented Generation (RAG), Prompt Engineering.
*   **Your Mission**: Write the "System Prompt" that tells the AI how to behave (e.g., "You are a critical HR Manager...").

## Phase 4: The Interface (Streamlit)
**Goal**: Build a web UI so you can show this to recruiters.
*   **Concepts**: Web Development (Streamlit), UI/UX.
*   **Your Mission**: Build the "File Uploader" and "Result Display" components.

---

## Prerequisites (Do this now)
1.  **Python Installed**: Ensure you have Python 3.9+ installed.
2.  **API Key**: You will need an OpenAI API Key. (If you don't have one, we can use open-source models, but it's harder to set up. Do you have one?)
3.  **VS Code**: Open the `AgileHire` folder in VS Code.
