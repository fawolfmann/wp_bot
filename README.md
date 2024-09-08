# WhatsApp AI Assistant

This project implements an AI-powered WhatsApp assistant using a local language model and vector store for context-aware responses.

## Features

- WhatsApp integration using WPP_Whatsapp
- Local LLM support with llama.cpp
- Vector store for efficient context retrieval
- Preprocessing of chat files for improved responses

## Setup

1. Install dependencies using Poetry:
   ```
   poetry install
   ```

2. Configure the project in `config.py`:
   - Set `WHATSAPP_SESSION_NAME`
   - Specify `LLM_MODEL_PATH` (path to your Llama model)
   - Set `VECTOR_DB_PATH` for persistent storage

3. Preprocess chat files:
   - Place text files in a directory
   - Update `chat_files_directory` in `preprocess.py`
   - Run `python preprocess.py`

## Usage

1. Start the WhatsApp client using Poetry:
   ```
   poetry run python main.py
   ```

2. The bot will automatically respond to incoming messages.

3. To send a message as a human, prefix it with `!human`:
   ```
   !human Hello, this is a human message.
   ```

## Components

- `whatsapp_client.py`: WhatsApp integration
- `vector_store_utils.py`: Vector store operations
- `llm_utils.py`: LLM initialization and response generation
- `preprocess.py`: Chat file preprocessing
- `main.py`: Main application logic

## Configuration

Adjust settings in `config.py` to customize:
- WhatsApp session name
- LLM model path
- Vector store path
- Polling interval
- Escape prefix for human messages

## How LLM with RAG Works

This project uses a Language Model (LLM) with Retrieval-Augmented Generation (RAG) for context-aware responses. Here's a conceptual overview:

1. **Vector Store**: Chat history is preprocessed and stored in a vector database, where each message is converted into a numerical representation (embedding).

2. **Query Processing**: When a new message is received, it's converted into an embedding and used to search the vector store for similar content.

3. **Context Retrieval**: The most relevant previous messages are retrieved based on similarity to the current query.

4. **LLM Integration**: The retrieved context is combined with the current query and sent to the LLM.

5. **Response Generation**: The LLM generates a response considering both the query and the retrieved context, resulting in more informed and contextually appropriate answers.

This approach allows the AI assistant to leverage past conversations for more accurate and context-aware responses.
