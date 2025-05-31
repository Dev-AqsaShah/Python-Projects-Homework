import streamlit as st
import sqlite3
import hashlib
import os
from cryptography.fernet import Fernet

# File to store encryption key
KEY_FILE = "simple_secret.key"

# Load or generate encryption key
def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return key

# Setup
key = load_key()
cipher = Fernet(key)

# Initialize the database
def init_db():
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

init_db()

# Helper functions
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt(encrypted_text):
    return cipher.decrypt(encrypted_text.encode()).decode()

# Streamlit UI
st.title("🔐 Secure Data Vault")

menu = ["Store Secret", "Retrieve Secret"]
choice = st.sidebar.selectbox("Choose an option", menu)

# Store secret section
if choice == "Store Secret":
    st.subheader("📝 Store a New Secret")
    label = st.text_input("Label (unique):")
    secret = st.text_area("Your Secret:")
    passkey = st.text_input("Passkey (to protect):", type="password")

    if st.button("Encrypt and Save"):
        if label and secret and passkey:
            encrypted = encrypt(secret)
            hashed_key = hash_passkey(passkey)

            try:
                conn = sqlite3.connect("simple_data.db")
                c = conn.cursor()
                c.execute("INSERT INTO vault (label, encrypted_text, passkey) VALUES (?, ?, ?)",
                          (label, encrypted, hashed_key))
                conn.commit()
                st.success("✅ Secret saved successfully!")
            except sqlite3.IntegrityError:
                st.error("❗ Label already exists.")
            finally:
                conn.close()
        else:
            st.warning("⚠️ Please fill all fields.")

# Retrieve secret section
elif choice == "Retrieve Secret":
    st.subheader("🔍 Retrieve Your Secret")
    label = st.text_input("Secret Label:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Decrypt"):
        conn = sqlite3.connect("simple_data.db")
        c = conn.cursor()
        c.execute("SELECT encrypted_text, passkey FROM vault WHERE label = ?", (label,))
        result = c.fetchone()
        conn.close()

        if result:
            encrypted_text, stored_hash = result
            if hash_passkey(passkey) == stored_hash:
                decrypted_text = decrypt(encrypted_text)
                st.success("🔓 Your decrypted secret:")
                st.code(decrypted_text)
            else:
                st.error("❌ Incorrect passkey.")
        else:
            st.warning("⚠️ No such label found.")
