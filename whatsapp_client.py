from WPP_Whatsapp import Create

from config import WHATSAPP_SESSION_NAME


def initialize_whatsapp_client():
    creator = Create(session=WHATSAPP_SESSION_NAME, logQR=True, headless=False, saveQR=True)
    client = creator.start()

    if creator.state != 'CONNECTED':
        raise Exception(creator.state)
    else:
        print("Connected to WhatsApp")

    return client, creator