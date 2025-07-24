import sqlite3
from config import DATABASE_PATH

def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS candidats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            email TEXT,
            niveau TEXT,
            motivation TEXT,
            photo_path TEXT
        )
    ''')
    conn.commit()
    conn.close()

def ajouter_candidat(nom, email, niveau, motivation, photo_path):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO candidats (nom, email, niveau, motivation, photo_path)
        VALUES (?, ?, ?, ?, ?)
    ''', (nom, email, niveau, motivation, photo_path))
    conn.commit()
    conn.close()

def recuperer_candidats():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nom, email, niveau, motivation, photo_path FROM candidats")
    data = cursor.fetchall()
    conn.close()
    return data

def mise_a_jour():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE nom, email, niveau, motivation, photo_path FROM candidats")
    data = cursor.fetchall()
    conn.close()
    return data

def recherche(rech):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    query = "SELECT nom, email, niveau, motivation FROM candidats WHERE nom LIKE ? "#OR ? email LIKE?
    cursor.execute(query,(f"%{rech}%",))
    data = cursor.fetchall()
    conn.close()
    return data

