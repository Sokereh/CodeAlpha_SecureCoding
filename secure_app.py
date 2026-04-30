import sqlite3

# --- SETUP CODE (To ensure the database exists for the demo) ---
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
cursor.execute("INSERT OR IGNORE INTO users VALUES ('admin', 'real_password_123')")
conn.commit()
conn.close()
# ---------------------------------------------------------------

def login_user_secure(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # REMEDIATION: Parameterized Queries (The "Fix")
    # We use '?' placeholders so the input is never treated as a command
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    
    print(f"Executing Secure Query with placeholders for: {username}")
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    
    if user:
        return "Login Successful!"
    return "Invalid Credentials."

print("--- Secure Login Demo ---")
u_input = input("Enter Username: ")
p_input = input("Enter Password: ")
print(login_user_secure(u_input, p_input))
