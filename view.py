import sqlite3

# Create or Connect a database
conn = sqlite3.connect("BARONIC.db")

# CRUD
# C - Create
def create_info(i):
    with conn:
        # Create  cursor
        c = conn.cursor()
        query = "INSERT INTO INGREDIENTES(NOME_INGREDIENTE, NUMERO_LOCALIZACAO, PRECO, QUANTIDADE) VALUES (?, ?, ?, ?)"
        c.execute(query, i)

# R - Read
def read_info():
    datas = []
    with conn:
        # Create  cursor
        c = conn.cursor()
        query = "SELECT * FROM INGREDIENTES"
        c.execute(query)
        data = c.fetchall()
        
        for d in data:
            datas.append(d)
    
    return datas



# # list = ['Água', 1]
# # # U - Update
# with conn:
#     # Create  cursor
#     c = conn.cursor()
#     query = "UPDATE INGREDIENTES SET NOME_INGREDIENTE=? WHERE CODIGO_INGREDIENTE=? "
#     c.execute(query, list)

# # D - Delete
# list = [1]
# with conn:
#     # Create  cursor
#     c = conn.cursor()
#     query = "DELETE FROM INGREDIENTES WHERE CODIGO_INGREDIENTE=?"
#     c.execute(query, list)