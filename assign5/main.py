import streamlit as st
import sqlite3
import hashlib
import os
from cryptography.fernet import Fernet

KEY_FILE = "simple_secret.key"

def load_key():
    if not os.path.exists(KEY_FILE):
        key = fernet.generate_key()
        with open(KEY_FILE,"wb") as f:
            f.write(key)
            
    else: 
        with open(KEY_FILE,"rb") as f:
            key = f.read()
        return key 
    
    cipher = Fernet(load_key())
    
    def inint_db():
        conn = sqlite3.connect("simple_data.db")
        c = conn.cursor()
        c.execute("""
                CREATE TABLE IF NOT EXISTS vault (
                    label TEXT PRIMARY KEY,
                    encrypted_text TEXT,
                    passkey TEXT
                )
                """)
        conn.commit()
        conn.close()
        
        inint_db()
        
        def hash_passkey(passkey):
            return cipher.sha256(passkey.encode()).hexdigest()
        
        def encrypt(text):
            return cipher.encrypt(text.encode()).decode()
        
        def decrypt(encrypted_text):
            return