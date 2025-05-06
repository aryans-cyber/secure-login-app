
import sqlite3
import bcrypt

# Create database and users table
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
''')

# Add a default user
username = 'admin'
password = 'securepass123'
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

cursor.execute("INSERT OR REPLACE INTO users (username, password) VALUES (?, ?)", (username, hashed.decode()))
conn.commit()
conn.close()

print("Database initialized with default user: admin / securepass123")
