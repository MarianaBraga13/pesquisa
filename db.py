import sqlite3

def conectar():
    return sqlite3.connect("entrevistas.db")

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   senha TEXT NOT NULL
               );
        """)
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS entrevistas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    resposta1 TEXT NOT NULL,
                    resposta2 TEXT NOT NULL,
                    resposta3 TEXT NOT NULL
                );
        """)
    
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS entrevistados (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   idade INT NOT NULL,
                   genero TEXT NOT NULL,
                   renda REAL NOT NULL,
                   escolaridade TEXT NOT NULL,
                   estado TEXT NOT NULL
                );
        """)
    conn.commit()
    conn.close()