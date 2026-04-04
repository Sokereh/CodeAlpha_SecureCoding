import sqlite3
import os
from dotenv import load_dotenv

# REMEDIATION 1: Use environment variables for secrets (not hardcoded)
load_dotenv()
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")

def login_user_secure(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # REMEDIATION 2: Parameterized Queries (Prevents SQL Injection)
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    
    # Passwords should also be hashed in a real DB, but we start with safe queries
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    
    if user:
        return "Login Successful!"
    return "Invalid Credentials."