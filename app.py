import streamlit as st
import os
from utils import extract_text_from_pdf, get_text_chunks, get_vector_store, get_rag_chain

st.set_page_config(page_title="Smart Recruit Assistant", page_icon="🕵️", layout="wide")

st.title("🕵️ Smart Recruit Assistant")
st.markdown("### Upload a Resume & Ask Questions (RAG)")

# Sidebar
with st.sidebar:
    st.header("1. Setup")
    api_key = st.text_input("OpenAI API Key", type="password")
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    
    st.header("2. Upload Resume")
    pdf_docs = st.file_uploader(
        "Upload Resume (PDF)", accept_multiple_files=True, type="pdf"
    )
    
    if st.button("Process Resume"):
        if not api_key:
            st.error("Please enter an OpenAI API Key first!")
        elif not pdf_docs:
            st.error("Please upload a PDF file.")
        else:
            with st.spinner("Processing... Extracting Text & Creating Embeddings"):
                # 1. Extract Text
                raw_text = extract_text_from_pdf(pdf_docs)
                
                # 2. Split Texts
                text_chunks = get_text_chunks(raw_text)
                
                # 3. Create Vector Store
                vector_store = get_vector_store(text_chunks, api_key)
                
                # 4. Save to Session State
                st.session_state.vector_store = vector_store
                st.success("Resume Processed! You can now ask questions.")

# Main Area
if "vector_store" in st.session_state:
    st.header("3. Recruitment Chat")
    
    option = st.selectbox(
        "Quick Questions",
        (
            "Select a question...",
            "What are the candidate's core technical skills?",
            "Does this candidate have experience with LLMs or RAG?",
            "Summarize the candidate's last project.",
            "Why is this candidate a good fit for a Data Science Internship?"
        )
    )
    
    user_question = st.text_input("Or ask your own question:")
    
    final_question = None
    if user_question:
        final_question = user_question
    elif option != "Select a question...":
        final_question = option
        
    if final_question:
        with st.spinner("Analyzing..."):
            qa_chain = get_rag_chain(st.session_state.vector_store, api_key)
            
            # LCEL chain invoke takes the question string directly
            result = qa_chain.invoke(final_question)
            
            st.write("### 🤖 AI Assessment:")
            st.write(result)
            
else:
    st.info("👈 Please upload a PDF and click 'Process Resume' to start.")
