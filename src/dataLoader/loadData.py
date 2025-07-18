from langchain.document_loaders import DirectoryLoader,PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_huggingface import HuggingFaceEmbeddings

def load_pdf(data):
    loader= DirectoryLoader(data,loader_cls=PyPDFLoader,glob='*.pdf')
    
    documents=loader.load()
    return documents

def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
    text_chunks=text_splitter.split_documents(extracted_data)

    return text_chunks

def huggingface_embeddings():
    embeddings=HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    return embeddings