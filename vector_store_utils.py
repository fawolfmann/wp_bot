import chromadb
from llama_index.core import Document, VectorStoreIndex
from llama_index.core.storage import StorageContext
from llama_index.embeddings.llama_cpp import LlamaCppEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

from config import LLM_MODEL_PATH, TOP_K_RESULTS, VECTOR_DB_PATH


def initialize_vector_store():
    chroma_client = chromadb.PersistentClient(path=VECTOR_DB_PATH)
    chroma_collection = chroma_client.get_or_create_collection("common_replies")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    embedding_model = LlamaCppEmbedding(model_path=LLM_MODEL_PATH)
    index = VectorStoreIndex.from_vector_store(vector_store, storage_context=storage_context, embed_model=embedding_model)
    return index, embedding_model

def add_to_vector_store(index, text_or_document, metadata=None):
    if isinstance(text_or_document, str):
        document = Document(text=text_or_document)
    else:
        document = text_or_document
    
    index.insert(document)

def query_vector_store(index, query):
    query_engine = index.as_query_engine(similarity_top_k=TOP_K_RESULTS)
    response = query_engine.query(query)
    return [node.text for node in response.source_nodes]