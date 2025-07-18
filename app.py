from flask import Flask,render_template,jsonify,request
from src.embeddings.huggingfaceEmbeddings import huggingface_embeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from src.prompt import *
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
embeddings= huggingface_embeddings()

pc =Pinecone(api_key=PINECONE_API_KEY)
index_name='medical-chatbot'
index= pc.Index(index_name)
vector_store=PineconeVectorStore(index=index,embedding=embeddings)

prompt=PromptTemplate(
 template= TEMPLATE,
input_variables=['context','input']
)

from langchain_community.llms import CTransformers
llm = CTransformers(model='model/llama-2-7b-chat.ggmlv3.q4_0.bin',
                    model_type='llama',
                    config={'max_new_tokens':512,
                            'temperature':0.3})

retriever= vector_store.as_retriever(search_kwargs={'k':2})

question_answer_chain = create_stuff_documents_chain(llm, prompt)
chain = create_retrieval_chain(retriever, question_answer_chain)

#llm_response= chain.invoke({"input": 'what is acne'})


@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/get', methods=['POST'])
def chat():
    msg = request.form.get('msg', '')
    if not msg:
        return jsonify({"error": "No message provided"}), 400

    print("User Input:", msg)
    result = chain.invoke({'input': msg})
    print("LLM Response:", result.get('answer') or result.get('result'))
    return str(result.get('answer') or result.get('result'))

if __name__ == '__main__':
    app.run(debug=True)
