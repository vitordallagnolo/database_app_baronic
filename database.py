import sqlite3

# Databases

# Create or Connect a database
conn = sqlite3.connect("BARONIC.db")

# Create  cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE INGREDIENTES (
        CODIGO_INGREDIENTE integer,
        NOME_INGREDIENTE text,
        NUMERO_LOCALIZACAO integer,
        PRECO float,
        QUANTIDADE float
        )""")

# Commit changes
conn.commit()

# Close connection
conn.close()