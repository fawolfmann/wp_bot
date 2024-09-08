from WPP_Whatsapp import Create


# start client with your session name
def run_whatsapp_client():
    your_session_name = "test"
    creator = Create(session=your_session_name, logQR=True, headless=False, saveQR=True)
    client = creator.start()
    # Now scan Whatsapp Qrcode in browser

    # check state of login
    if creator.state != 'CONNECTED':
        raise Exception(creator.state)
    else:
        print("Connected to Whatsapp")

    phone_number = "+5493515438836"  # or "+*********"
    message = "hello from wpp"

    # Simple message
    result = client.sendText(phone_number, message)
    print(result)
    creator.__exit__()

if __name__ == "__main__":
    run_whatsapp_client()