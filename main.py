import time

from config import ESCAPE_PREFIX, POLLING_INTERVAL
from llm_utils import generate_response, initialize_llm
from vector_store_utils import add_to_vector_store, initialize_vector_store
from whatsapp_client import initialize_whatsapp_client


def run_whatsapp_client():
    client, creator = initialize_whatsapp_client()
    llm = initialize_llm()
    vector_store, embedding_model = initialize_vector_store()

    # Example of adding a common reply to the vector store
    add_to_vector_store(vector_store, "Hello! How can I assist you today?")

    last_processed_message_id = {}

    try:
        while True:
            chats = client.getAllChats()
            for chat in chats:
                chat_id = chat['id']['_serialized']  # Extract the serialized chat ID
                messages = client.getAllMessagesInChat(chat_id)
                
                # Process only new messages
                new_messages = [msg for msg in messages if msg['id'] not in last_processed_message_id.get(chat_id, [])]
                
                for message in new_messages:
                    sender = message['sender']['id']
                    content = message['content']
                    
                    print(f"New message from {sender}: {content}")

                    if content.startswith(ESCAPE_PREFIX):
                        # Remove the escape prefix and send the message as is
                        human_message = content[len(ESCAPE_PREFIX):].strip()
                        client.sendText(sender, human_message)
                        print(f"Sent human message to {sender}: {human_message}")
                    else:
                        # Process with the bot
                        response = generate_response(llm, vector_store, content)
                        client.sendText(sender, response)
                        print(f"Sent bot response to {sender}: {response}")

                    # Update the last processed message ID for this chat
                    if chat_id not in last_processed_message_id:
                        last_processed_message_id[chat_id] = set()
                    last_processed_message_id[chat_id].add(message['id'])

            time.sleep(POLLING_INTERVAL)
    finally:
        creator.__exit__()

if __name__ == "__main__":
    run_whatsapp_client()