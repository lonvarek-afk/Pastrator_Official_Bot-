import sqlite3
import json

DB_FILE = "pastrator.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # User Preferences
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            language TEXT DEFAULT 'so'
        )
    ''')
    # History Memory
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            user_id INTEGER PRIMARY KEY,
            messages TEXT
        )
    ''')
    conn.commit()
    conn.close()

def set_user_language(user_id: int, lang_code: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (user_id, language) VALUES (?, ?)
        ON CONFLICT(user_id) DO UPDATE SET language=excluded.language
    ''', (user_id, lang_code))
    conn.commit()
    conn.close()

def get_user_language(user_id: int) -> str:
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT language FROM users WHERE user_id = ?', (user_id,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else 'so'

def get_user_history(user_id: int) -> list:
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT messages FROM history WHERE user_id = ?', (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row and row[0]:
        return json.loads(row[0])
    return []

def save_user_history(user_id: int, history: list):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO history (user_id, messages) VALUES (?, ?)
        ON CONFLICT(user_id) DO UPDATE SET messages=excluded.messages
    ''', (user_id, json.dumps(history)))
    conn.commit()
    conn.close()
