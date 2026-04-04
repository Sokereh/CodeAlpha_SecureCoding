import sqlite3

# VULNERABILITY 1: Hardcoded sensitive information
ADMIN_TOKEN = "SUPER_SECRET_12345" 

def login_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABILITY 2: SQL Injection (Directly inserting user input into a query)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    print(f"Executing Query: {query}")
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        return "Login Successful!"
    else:
        return "Invalid Credentials."

# VULNERABILITY 3: Lack of Input Validation
user_input = "admin' OR '1'='1" # A classic SQL Injection string
print(login_user(user_input, "any_password"))