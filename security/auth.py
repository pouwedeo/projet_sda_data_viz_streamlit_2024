import sqlite3
import streamlit as st
import bcrypt

# Connexion à la base de données SQLite
# Create a database and users table
conn = sqlite3.connect('data/users.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Add a sample user (Optional: Remove in production)
hashed_password = bcrypt.hashpw("password23".encode(), bcrypt.gensalt()).decode()
cursor.execute('''
INSERT OR IGNORE INTO users (username, hashed_password, name, email) VALUES (?, ?, ?, ?)
''', ("user1", hashed_password, "John Doe", "john@example.com"))

conn.commit()
conn.close()

# Vérification des identifiants
def fetch_users():
    conn = sqlite3.connect('data/users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username, hashed_password, name, email FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

# Création d'un compte utilisateur
def register_user(username, password):
    conn = sqlite3.connect("data/users.db")
    cursor = conn.cursor()
    try:
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

# Déconnexion
def logout_user():
    st.session_state.logged_in = False
    st.session_state.username = None
