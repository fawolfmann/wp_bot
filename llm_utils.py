from llama_cpp import Llama

from config import LLM_MODEL_PATH
from vector_store_utils import query_vector_store


def initialize_llm():
    return Llama(model_path=LLM_MODEL_PATH)

def generate_response(llm, vector_store, message):
    # Retrieve relevant context from the vector store
    relevant_docs = query_vector_store(vector_store, message)
    context = "\n".join(relevant_docs)
    breakpoint()    
    # Create a prompt with the retrieved context and Q&A format
    prompt = f"""Context:
{context}

###QUESTION
{message}

###ANSWER
"""

    # Generate response using the LLM with the context-enhanced prompt
    response = llm(prompt, max_tokens=100, stop=["###QUESTION"])
    return response['choices'][0]['text'].strip()