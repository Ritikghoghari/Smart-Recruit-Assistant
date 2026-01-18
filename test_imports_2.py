
try:
    print("Testing new imports...")
    from langchain_core.prompts import PromptTemplate
    print("PromptTemplate found in core!")
    
    try:
        from langchain.chains import RetrievalQA
        print("RetrievalQA found in langchain.chains!")
    except:
        print("Not in langchain.chains")
        
    try:
        from langchain_community.chains import RetrievalQA
        print("RetrievalQA found in community!")
    except:
        print("Not in community either")

except Exception as e:
    print(f"Error: {e}")
