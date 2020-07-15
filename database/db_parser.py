import os
import sqlite3
from .encryption.encryptions import *

DB_FILE = os.path.join(os.path.dirname(__file__), 'database.db')

def register(username, email, password):
    db = sqlite3.connect(DB_FILE)
    conn = db.cursor()
    used = isUsed(email, username)

    if not used:
        conn.execute("INSERT INTO users VALUES(?, ?, ?)", (username, email, encrypt(password)))

    elif used:
        return used

    db.commit()
    conn.close()

    return True


def login(email, password):
    db = sqlite3.connect(DB_FILE)
    conn = db.cursor()
    
    try:
        conn.execute("SELECT password FROM users WHERE email=?", (email,))
        encrypted_password = conn.fetchone()[0]

        if decrypt(encrypted_password) == password:
            return "OK"

        elif decrypt(encrypted_password) != password:
            return "wrong password!"

    except TypeError:
        return "email does not exist" # email does not exist

    db.commit()
    conn.close()

def isUsed(email, username):
    db = sqlite3.connect(DB_FILE)
    conn = db.cursor()
    conn.execute("SELECT email FROM users WHERE email=?", (email,))
    db_email = conn.fetchone()
    conn.execute("SELECT username FROM users WHERE username=?", (username,))
    db_username = conn.fetchone()

    if db_username:
        return "username in use"

    if db_email:
        return "email in use"

    db.commit()
    conn.close()

    return False


