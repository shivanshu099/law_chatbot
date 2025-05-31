from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

loader= PyPDFLoader("indian_constitution.pdf")
documents= loader.load()

spllitter= CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks= spllitter.split_documents(documents)
print(f"Total number of chunks: {len(chunks)}")
print(f"First chunk: {chunks[0].page_content[:500]}...")

embedings= HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore= Chroma.from_documents(chunks, embedings, persist_directory="chroma_db")
vectorstore.persist()











