import os
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# 1. PDF Text Extraction
def extract_text_from_pdf(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# 2. Text Chunking
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_text(text)
    return chunks

# 3. Vector Store
def get_vector_store(text_chunks, api_key):
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    vector_store = Chroma.from_texts(
        texts=text_chunks, 
        embedding=embeddings
    )
    return vector_store

# 4. The RAG Chain (Refactored to avoid 'langchain.chains')
def get_rag_chain(vector_store, api_key):
    llm = ChatOpenAI(
        model_name="gpt-4", 
        temperature=0.3, 
        openai_api_key=api_key
    )

    template = """
    You are an expert Technical Recruiter and AI Hiring Manager.
    Use the following pieces of context (Resume content) to answer the user's question.
    
    If the answer is not found in the resume, you are allowed to use your own knowledge to provide a helpful answer, 
    but please explicitly state: "This information is not in the resume, but generally..."
    
    Context:
    {context}
    
    Question: {question}
    
    Structured Answer:
    """
    
    prompt = PromptTemplate.from_template(template)
    
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    retriever = vector_store.as_retriever()
    
    # Modern LCEL Chain
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return rag_chain
