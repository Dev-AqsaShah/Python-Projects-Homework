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
            return cipher.decrypt(encrypted_text.encode()).decode()
        
        st.title("secure Data Encryption App")
        menu = ["store secrete", "reteieve secret"]
        choice = st.sidebar.selectbox("choose option",menu)
        
        if choice == "store secret":
            st.header("store a new secret")
            
            label= st.text_input("Label (Unique 10): ")
            secret = st.text_area("Your Secret")
            passkey = st.text_input("Passkey (to protect it):", type="password")
            
            if st.button("Encrypt and save"):
                if label and secret and passkey:
                    conn = sqlite3.connect("simple_data.db")
                    c = conn.cursor()
                    
                    encrypted = encrypt(secret)
                    hashed_key = hash_passkey(passkey)
                    
                    try:
                        c.execute("INSERT INTO vault (label, encrypted_text, passkey) VALUES (?,?,?)"
                                (label,encrypted,hashed_key))
                        conn.commit()
                        st.success("secret saved successfully")
                    except sqlite3.IntegrityError:
                        st.error("Label already exists!")
                    conn.close
                else:
                    st.warning("fill all fields")
                    
            elif choice == "reteieve secret":
                st.header("reteieve your secret")
                
                label = st.text_input("secret label")
                passkey = st.text_input("enter passkey", type = "password")
                
                if st.button("decrypt"):
                    conn = sqlite3.connect("simple_data_db")
                    c = conn.cursor()
                    c.execute("select encrypted_text passkey from ")