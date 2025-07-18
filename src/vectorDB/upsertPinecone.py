import os
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from pinecone import ServerlessSpec,Pinecone
from langchain_core.documents import Document
from src.dataLoader.loadData import text_split,load_pdf,DirectoryLoader
from src.embeddings.huggingfaceEmbeddings import huggingface_embeddings
load_dotenv()

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
extracted_data=load_pdf('data/')
text_chunks=text_split(extracted_data)
embeddings= huggingface_embeddings()

pc =Pinecone(api_key=PINECONE_API_KEY)

index_name='medical-chatbot'

if not  pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric='cosine',
        spec=ServerlessSpec(cloud='aws',region='us-east-1'),
    )

index= pc.Index(index_name)


vector_store=PineconeVectorStore(index=index,embedding=embeddings)
vector_store.add_documents(text_chunks)