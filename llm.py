from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
import requests
import os
from dotenv import load_dotenv



def ask_groq(query, context):
    prompt = f"""
    You are a helpful lawyer assistant. yumi  you are made by genuis shivanshu prajapati to answer Use the following context to answer the user's question.

    Context:
    {context}

    Question: {query}
    Answer:
    """
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("api_key_grok") 
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.environ['GROQ_API_KEY']}",
            "Content-Type": "application/json",
        },
        json={
            "model": "llama3-70b-8192",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.7
        }
    )
    return response.json()["choices"][0]["message"]["content"]



def vector_search(query):
    embedings= HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore= Chroma(
        persist_directory="chroma_db",
        embedding_function=embedings
    )

    docs= vectorstore.similarity_search(query, k=1)
    temp=""
    for i,doc in enumerate(docs):
        temp+=f"Doc {i+1}:\n{doc.page_content}\n\n"
    
    re= ask_groq(query, temp)
    return re

if __name__ == "__main__":
    #query = "What is the Preamble of the Indian Constitution"
    query = input("Enter your query: ")
    answer = vector_search(query)
    print(f"Answer: {answer}")



























