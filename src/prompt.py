from langchain_core.prompts import PromptTemplate

prompt=PromptTemplate(
 template= """
use the following pieces of information to answer the user's question.
If you dont know the  answer,just say that you dont know, dont try to make up the answer.

Context:{context}
Question:{input}

Only return the helpful answer below and nothing else.

Helpful answer:  
""",
input_variables=['context','input']
)