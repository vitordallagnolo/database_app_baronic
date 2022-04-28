from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("BaronicRobotics - baronicrobotics.com"
)
root.geometry("500x500")

# Create or Connect a database
conn = sqlite3.connect("BARONIC.db")

# Create  cursor
c = conn.cursor()

# Create submit function for database
def submit():
    # Create or Connect a database
    conn = sqlite3.connect("BARONIC.db")

    # Create  cursor
    c = conn.cursor()
    
    # Insert into table
    c.execute("INSERT INTO INGREDIENTES VALUES (:code_ing, :n_ing, :n_loc, :preco, :qtd)",
              {
                  'code_ing': code_ing.get(),
                  'n_ing': n_ing.get(),
                  'n_loc': n_loc.get(),
                  'preco': preco.get(),
                  'qtd': qtd.get()
                  }
              
              )              
    
    # Commit changes
    conn.commit()

    # Close connection
    conn.close()
    
    
    # Clear the text boxes
    code_ing.delete(0, END)
    n_ing.delete(0, END)
    n_loc.delete(0, END)
    preco.delete(0, END)
    qtd.delete(0, END)

# Create query funcion
def query():
    # Create or Connect a database
    conn = sqlite3.connect("BARONIC.db")

    # Create  cursor
    c = conn.cursor()
    
    # Executar a query na base de dados
    c.execute("SELECT *, oid FROM INGREDIENTES")
    records = c.fetchall()
    
    
    # Loop dos resultados
    print_records = ''    
    for record in records:
        print_records += "Código: " + str(record[0]) + " " + "Ingrediente: " + str(record[1]) + "\n"
        
    query_label = Label(root, text=print_records)
    query_label.grid(row=7, column=0, columnspan=2)
    
    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Create text boxes
code_ing = Entry(root, width=30)
code_ing.grid(row=0, column=1, padx=20)
n_ing = Entry(root, width=30)
n_ing.grid(row=1, column=1)
n_loc = Entry(root, width=30)
n_loc.grid(row=2, column=1)
preco = Entry(root, width=30)
preco.grid(row=3, column=1)
qtd = Entry(root, width=30)
qtd.grid(row=4, column=1)

# Create text box labels
code_ing_label = Label(root, text="Código do Ingrediente")
code_ing_label.grid(row=0, column=0)
n_ing_label = Label(root, text="Nome do Ingrediente")
n_ing_label.grid(row=1, column=0)
n_loc_label = Label(root, text="Nº Localização do Ingrediente")
n_loc_label.grid(row=2, column=0)
preco_label = Label(root, text="Preço do Ingrediente")
preco_label.grid(row=3, column=0)
qtd_label = Label(root, text="Quantidade do Ingrediente (Kg)")
qtd_label.grid(row=4, column=0)

# Create submit button
submit_btn = Button(root, text="Adicionar Registro à Base de Dados", command=submit)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a query button
query_btn = Button(root, text="Mostrar Registros", command=query)
query_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=159)

# Commit changes
conn.commit()

# Close connection
conn.close()
