from select import select
import site
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
from view import *

## Colors ##
co1 = "#f0f3f5" # Black
co0 = "#feffff" # White
co2 = "#4fa882" # Green
co3 = "#38576b" # Value
co4 = "#403d3d" # Letter
co5 = "#e06636" # - Profit Orange
co6 = "#038cfc" # Blue
co7 = "#ef5350" # Red
co8 = "#263238" # Light Blue
co9 = "#e9edf5" # Sky Blue

# Var tree global
global tree

# Create window
root = Tk()
root.title("BaronicRobotics - baronicrobotics.com"
)
root.geometry("1043x453")
root.configure(background=co9)
root.resizable(width=FALSE, height=FALSE)

# Create frames
frame_top_left = Frame(root, width=310, height=50, background=co2, relief='flat')
frame_top_left.grid(row=0, column=0)

frame_bot_left = Frame(root, width=310, height=403, background=co1, relief='flat')
frame_bot_left.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_right = Frame(root, width=588, height=403, background=co1, relief='flat')
frame_right.grid(row=0, column=1, rowspan=2, sticky=NSEW, padx=1, pady=0)

# Label Top
app_name = Label(frame_top_left, text="Estoque de Ingredientes", anchor=NW, font=("Ivy 13 bold") , background=co2, fg=co1, relief='flat')
app_name.place(x=50, y=11)

# Function insert
def insert():
    nome_igrediente = ei_nome.get().strip().capitalize()
    localizacao = ei_loc.get()
    preco = ei_preco.get()
    qtd = ei_qtd.get()

    list = [nome_igrediente, localizacao, preco, qtd]

    if nome_igrediente == "":
        messagebox.showerror("Erro", "O nome não pode ser vazio!")
    elif localizacao == "":
        messagebox.showerror("Erro", "A localização não pode ser vazia!")
    elif preco == "":
        messagebox.showerror("Erro", "O preço não pode ser vazio!")
    elif qtd == "":
        messagebox.showerror("Erro", "A quantidade não pode estar vazia!")         
    else:
        create_info(list)
        messagebox.showinfo("Sucesso", "Os dados foram inseridos com sucesso!")

        ei_nome.delete(0, "end")
        ei_loc.delete(0, "end")
        ei_preco.delete(0, "end")
        ei_qtd.delete(0, "end")

    for widget in frame_right.winfo_children():
        widget.destroy()

    show()
    
# Function update    
def update():
    try:
        treev_data = tree.focus()
        treev_dic = tree.item(treev_data)
        tree_list = treev_dic['values']

        cod_ing= tree_list[0]

        ei_nome.delete(0, "end")
        ei_loc.delete(0, "end")
        ei_preco.delete(0, "end")
        ei_qtd.delete(0, "end")

        ei_nome.insert(0, tree_list[1])
        ei_loc.insert(0, tree_list[2])
        ei_preco.insert(0, tree_list[3])
        ei_qtd.insert(0, tree_list[4])

        # Function insert
        def update_confirm():
            nome_igrediente = ei_nome.get().strip().capitalize()
            localizacao = ei_loc.get()
            preco = ei_preco.get()
            qtd = ei_qtd.get()

            list = [nome_igrediente, localizacao, preco, qtd, cod_ing]

            if nome_igrediente == "":
                messagebox.showerror("Erro", "O nome não pode ser vazio!")
            elif localizacao == "":
                messagebox.showerror("Erro", "A localização não pode ser vazia!")
            elif preco == "":
                messagebox.showerror("Erro", "O preço não pode ser vazio!")
            elif qtd == "":
                messagebox.showerror("Erro", "A quantidade não pode estar vazia!")
      
            else:
                update_info(list)
                messagebox.showinfo("Sucesso", "Os dados foram atualizados com sucesso!")

                ei_nome.delete(0, "end")
                ei_loc.delete(0, "end")
                ei_preco.delete(0, "end")
                ei_qtd.delete(0, "end")

            for widget in frame_right.winfo_children():
                widget.destroy()

                show()

        # Confirm Button
        b_confirm = Button(frame_bot_left, command=update_confirm, text="Confirmar", width=10, font=("Ivy 7 bold") , background=co6, fg=co1, relief='raised', overrelief='ridge')
        b_confirm.place(x=115, y=350)

    except IndexError:
        messagebox.showerror("Erro", "Selecione alguma linha da tabela")



# Building frame_bot_left
# Nome do Ingrediente
i_nome = Label(frame_bot_left, text="Nome do Ingrediente *", anchor=NW, font=("Ivy 10 bold") , background=co1, fg=co4, relief='flat')
i_nome.place(x=10, y=10)
ei_nome = Entry(frame_bot_left, width=45, justify='left', relief='solid')
ei_nome.place(x=15, y=40)

# Número de Localização
i_loc = Label(frame_bot_left, text="Nº de Localização *", anchor=NW, font=("Ivy 10 bold") , background=co1, fg=co4, relief='flat')
i_loc.place(x=10, y=70)
ei_loc = Entry(frame_bot_left, width=45, justify='left', relief='solid')
ei_loc.place(x=15, y=100)

# Preço
i_preco = Label(frame_bot_left, text="Preço *", anchor=NW, font=("Ivy 10 bold") , background=co1, fg=co4, relief='flat')
i_preco.place(x=10, y=130)
ei_preco = Entry(frame_bot_left, width=45, justify='left', relief='solid')
ei_preco.place(x=15, y=160)

# Quantidade em mL
i_qtd = Label(frame_bot_left, text="Quantidade (mL) *", anchor=NW, font=("Ivy 10 bold") , background=co1, fg=co4, relief='flat')
i_qtd.place(x=10, y=190)
ei_qtd = Entry(frame_bot_left, width=45, justify='left', relief='solid')
ei_qtd.place(x=15, y=220)

# Add Button
b_inserir = Button(frame_bot_left, command=insert, text="Inserir", width=10, font=("Ivy 9 bold") , background=co2, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=20, y=310)

# Update Button
b_atualizar = Button(frame_bot_left, command=update, text="Atualizar", width=10, font=("Ivy 9 bold") , background=co6, fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=110, y=310)

# Delete Button
b_deletar = Button(frame_bot_left, text="Deletar", width=10, font=("Ivy 9 bold") , background=co7, fg=co1, relief='raised', overrelief='ridge')
b_deletar.place(x=200, y=310)

# Creating Right Frame for Table
def show():

    global tree

    lista = read_info()

    lista_header = ['Cód.', 'Nome do Ingrediente', 'Localização', 'Preço', 'Quantidade (mL)']

    tree = ttk.Treeview(frame_right, selectmode="extended", columns=lista_header, show="headings")

    # Vertical Scrollbar
    vsb = ttk.Scrollbar(frame_right, orient="vertical", command=tree.yview)

    # Horizontal Scrollbar
    hsb = ttk.Scrollbar(frame_right, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky="nsew")
    vsb.grid(column=1, row=0, sticky="ns")
    hsb.grid(column=0, row=1, sticky="ew")

    frame_right.grid_rowconfigure(0, weight=12)

    # Headers align
    hd = ["center", "center", "center", "center", "center"]
    # Columns width
    h = [40, 170, 170, 170, 170]
    n = 0

    # Loop for show data rows
    for col in lista_header:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # Adjust the col width to the header string
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in lista:
        tree.insert("", "end", values=item)


# Call show function
show()

root.mainloop()