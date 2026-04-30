import sqlite3

# --- SETUP CODE (Make sure this is at the very top) ---
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
# Create the table and add one real user to test against
cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
cursor.execute("INSERT OR IGNORE INTO users VALUES ('admin', 'real_password_123')")
conn.commit()
# -----------------------------------------------------

def login_user(username, password):
    # Connect again inside the function to run the query
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # The vulnerable query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing Query: {query}")
    
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        return "Login Successful!"
    else:
        return "Invalid Credentials."

# Use input() so YOU can type the attack during the video
print("--- SQL Injection Demo ---")
u_input = input("Enter Username: ")
p_input = input("Enter Password: ")
print(login_user(u_input, p_input))
