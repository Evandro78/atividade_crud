import sqlite3

def criar_banco():
    conn = sqlite3.connect('jogos.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jogos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        genero TEXT NOT NULL,
        plataforma TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
    )
    """)

    conn.commit()
    conn.close()
    print("Banco de dados e tabela criados com sucesso!")

if __name__ == "__main__":
    criar_banco()