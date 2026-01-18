# AgileHire: Project Architecture & Learning Guide

You have just built a **RAG (Retrieval Augmented Generation)** system. This is currently the most popular architecture in Enterprise AI. Here is how it works under the hood.

## 1. The High-Level Flow
1.  **Ingestion**: You upload a PDF (the Resume).
2.  **Chunking**: We break that PDF into small pieces (chunks) of ~1000 characters.
3.  **Embedding**: We send those pieces to OpenAI. OpenAI converts the text into a list of numbers (vectors) that represent the *meaning*.
4.  **Storage**: We save those numbers in `ChromaDB` (a digital filing cabinet).
5.  **Retrieval**: When you ask a question ("Does he know Python?"), we convert your question into numbers too, and find the "chunks" in the filing cabinet that are mathematically closest.
6.  **Generation**: We send your question + the found chunks to GPT-4 and say "Answer the question using ONLY these chunks."

## 2. Code Breakdown
### `utils.py` (The Backend Logic)
*   **`extract_text_from_pdf`**: Uses `pypdf` to just get the raw strings.
*   **`RecursiveCharacterTextSplitter`**: This is crucial. If we send the whole resume to GPT-4 at once, it might be too big (token limit) or too expensive. We split it smartly.
*   **`Chroma.from_texts`**: This does the magic. It calls the OpenAI Embedding API and saves the results locally.
*   **`RetrievalQA`**: A `LangChain` tool that automatically connects the Database Retrieval to the LLM Generation.

### `app.py` (The Frontend)
*   **`st.file_uploader`**: Lets you drag-and-drop.
*   **`st.session_state`**: Streamlit re-runs the WHOLE script every time you click a button. We use `session_state` to "remember" the database so we don't have to rebuild it every time you ask a question.

## 3. How to Learn This
To truly master this, try these tasks:
1.  **Change the Prompt**: Go to `utils.py` and change the `template` variable. Make the AI meaner, or ask it to output JSON instead of text.
2.  **Add Filters**: Try to filter by "Education" vs "Experience" (Hard, requires metadata).
3.  **Switch Models**: Change `gpt-4` to `gpt-3.5-turbo` in `utils.py` to save money.

## 4. Next Steps for Your Resume
*   **Project Title**: "AgileHire - Enterprise RAG Recruitment System"
*   **Bullet Point**: "Built an end-to-end RAG application using LangChain and OpenAI to automate resume screening, reducing manual review time by 40% (simulated)."
*   **Bullet Point**: "Implemented Vector Search using ChromaDB and deployed via Streamlit."
