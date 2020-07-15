import rsa
import os
from base64 import b64decode, b64encode

PUBLIC_KEY_FILE = os.path.join(os.path.dirname(__file__), 'public')
PRIVATE_KEY_FILE = os.path.join(os.path.dirname(__file__), 'private')

PUBLIC_KEY = rsa.PublicKey.load_pkcs1(open(PUBLIC_KEY_FILE).read())
PRIVATE_KEY = rsa.PrivateKey.load_pkcs1(open(PRIVATE_KEY_FILE).read())

def encrypt(message):
    global PRIVATE_KEY
    global PUBLIC_KEY 

    return b64encode(rsa.encrypt(message.encode(), PUBLIC_KEY)).decode()


def decrypt(message):
    global PRIVATE_KEY
    global PUBLIC_KEY

    return rsa.decrypt(b64decode(message), PRIVATE_KEY).decode()