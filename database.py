import sqlite3

DATABASE = "database.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS pacientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            telefone TEXT,
            email TEXT,
            tipo_pele TEXT,
            queixa_principal TEXT,
            data_cadastro TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS estatisticas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            total_pacientes INTEGER,
            pele_oleosa INTEGER,
            pele_seca INTEGER,
            pele_mista INTEGER,
            pele_normal INTEGER,
            data_registro TEXT
        )
    """)

    conn.commit()
    conn.close()
