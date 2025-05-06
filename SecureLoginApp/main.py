
import bcrypt
import sqlite3
import time

# Connect to database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Track failed login attempts
attempts = {}

def login(username, password):
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    if result:
        stored_hash = result[0]
        if bcrypt.checkpw(password.encode(), stored_hash.encode()):
            print("✅ Login successful!")
            attempts[username] = 0
            return True
        else:
            print("❌ Incorrect password.")
    else:
        print("❌ User not found.")

    attempts[username] = attempts.get(username, 0) + 1
    if attempts[username] >= 3:
        print("🚫 Account temporarily locked. Try again later.")
        time.sleep(10)
    return False

# Simple prompt
if __name__ == "__main__":
    print("=== Secure Login App ===")
    user = input("Username: ")
    pw = input("Password: ")
    login(user, pw)
