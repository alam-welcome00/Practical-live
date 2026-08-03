import sqlite3
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(BASE_DIR, "data", "documents.db")

print("database.py loaded")
print("BASE_DIR:", BASE_DIR)
print("DB_PATH:", DB_PATH)

def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    print("Connecting to:", DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    print("Connected successfully")

    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            path TEXT,
            thumbnail_path TEXT,
            tag TEXT,
            description TEXT,
            upload_date TEXT,
            lecture_date TEXT,
            total_pages INTEGER
        )
    """)

    conn.commit()
    print("DB initialized successfully")
    conn.close()