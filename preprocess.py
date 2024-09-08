import json
import os

from vector_store_utils import add_to_vector_store, initialize_vector_store


def preprocess_chat_files(directory):
    index, _ = initialize_vector_store()
    
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = json.load(file)
                for item in content:
                    question = item.get('question', '')
                    answer = item.get('answer', '')
                    formatted_content = f"""###QUESTION
{question}

###ANSWER
{answer}"""
                    add_to_vector_store(index, formatted_content, {"source": filename})
                print(f"Added content from {filename} to vector store")

if __name__ == "__main__":
    chat_files_directory = "path/to/your/chat/files"
    preprocess_chat_files(chat_files_directory)
