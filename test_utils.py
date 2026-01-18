
try:
    print("Attempting imports...")
    import os
    print("os ok")
    from pypdf import PdfReader
    print("pypdf ok")
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    print("RecursiveCharacterTextSplitter ok")
    from langchain_openai import OpenAIEmbeddings
    print("OpenAIEmbeddings ok")
    from langchain_community.vectorstores import Chroma
    print("Chroma ok")
    from langchain_openai import ChatOpenAI
    print("ChatOpenAI ok")
    try:
        from langchain.chains import RetrievalQA
        print("langchain.chains RetrievalQA ok")
    except ImportError as e:
        print(f"FAILED: langchain.chains RetrievalQA: {e}")
        
    try:
        from langchain.prompts import PromptTemplate
        print("langchain.prompts PromptTemplate ok")
    except ImportError as e:
        print(f"FAILED: langchain.prompts PromptTemplate: {e}")

    # Also try the community import which sometimes replaces it
    try:
        from langchain.chains import RetrievalQA
    except:
        pass
        
except Exception as e:
    print(f"CRITICAL ERROR: {e}")
