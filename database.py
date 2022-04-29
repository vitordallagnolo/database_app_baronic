import sqlite3

# Databases

# Create or Connect a database
conn = sqlite3.connect("BARONIC.db")

with conn:
    # Create  cursor
    c = conn.cursor()

    # Create table
    c.execute("""CREATE TABLE INGREDIENTES(
            CODIGO_INGREDIENTE INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            NOME_INGREDIENTE TEXT NOT NULL,
            NUMERO_LOCALIZACAO INTEGER NOT NULL,
            PRECO REAL NOT NULL,
            QUANTIDADE REAL NOT NULL
            )""")






# Including first codigo_ingrediente 000
c.execute("""UPDATE SQLITE_SEQUENCE SET seq = 000 WHERE name = 'INGREDIENTES'""")

# Commit changes
conn.commit()

# Close connection
conn.close()