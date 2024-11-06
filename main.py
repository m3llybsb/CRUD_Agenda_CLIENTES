from tkinter.ttk import *
from tkinter import*
from tkinter import messagebox
from tkinter import ttk

from dados import *

# Cores 
cor0 = "#f0f3f5"  # Preta
cor1 = "#f0f3f5"  # cizenta / grey
cor2 = "#feffff"  # branca
cor3 = "#38576b"  # preta / black
cor4 = "#403d3d"   # letra
cor5 = "#6f9fbd"  # azul
cor6 = "#ef5350"   # vermelha
cor7 = "#93cd95"   # verde

# Criando janela

janela = Tk()
janela.title("")
janela.geometry('500x450')
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

frame_cima = Frame(janela, width=500, height=50, bg=cor3, relief="flat")
frame_cima.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=500, height=150, bg=cor1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_tabela = Frame(janela, width=500, height=247, bg=cor2, relief="flat")
frame_tabela.grid(row=2, column=0, columnspan=2, padx=10, pady=1, sticky=NW)

# Configurando o FRAME

l_nome = Label(frame_cima, text='AGENDA CONTATOS DE CLIENTES', anchor=NE, font=('arial 20 bold'), bg=cor3, fg=cor1)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, width=500, anchor=NE, font=('arial 1'), bg=cor2, fg=cor1)
l_linha.place(x=0, y=45)


global tree
# Configurando o FRAME Tabela
def mostrar_dados():
    global tree
    dados_h =  ['Nome','Sexo','Telefone', 'Email']

    dados = ver_dados()

    tree = ttk.Treeview(frame_tabela, selectmode="extended",columns=dados_h, show="headings")

    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)

    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    tree.heading(0, text='Nome', anchor=NW)
    tree.heading(1, text='Sexo', anchor=NW)
    tree.heading(2, text='Telefone',anchor=NW)
    tree.heading(3, text='Email', anchor=NW)

    tree.column(0, width=120, anchor='nw')
    tree.column(1, width=40, anchor='nw')
    tree.column(2, width=110, anchor='nw')
    tree.column(3, width=165, anchor='nw')

    for item in dados:
        tree.insert('', 'end', values=item)

mostrar_dados()


#Função Adicionar

def inserir():
    nome = e_nome.get()
    sexo = c_sexo.get()
    telefone = e_tel.get()
    email = e_email.get()

    dados = [nome,sexo,telefone,email]
    if nome == '' or sexo =='' or telefone =='' or email =='':
        messagebox.showwarning('Dados','POR GENTILEZA PREENCHA TODOS OS CAMPOS!')
    else:
        adicionar_dados(dados)
        messagebox.showinfo('Dados','DADOS FORAM ADICIONADOS COM SUCESSO!')

        e_nome.delete(0,'end')
        c_sexo.delete(0,'end')
        e_tel.delete(0,'end')
        e_email.delete(0,'end')

        mostrar_dados()


def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        nome = tree_lista[0]
        sexo = tree_lista[1]
        telefone = str(tree_lista[2])
        email = tree_lista[3]

        e_nome.insert(0,nome)
        c_sexo.insert(0,sexo)
        e_tel.insert(0,telefone)
        e_email.insert(0,email)

        
        def confirmar():
            nome = e_nome.get()
            sexo = c_sexo.get()
            telefone_novo = e_tel.get()
            email = e_email.get()

            dados = [telefone,nome,sexo,telefone_novo,email]

            atualizar_dados(dados)

            
            messagebox.showinfo('Dados','DADOS FORAM ATUALIZADOS COM SUCESSO!')

            e_nome.delete(0,'end')
            c_sexo.delete(0,'end')
            e_tel.delete(0,'end')
            e_email.delete(0,'end')

            b_confirmar.destroy

            mostrar_dados()
        b_confirmar = Button(frame_baixo, command=confirmar, text='CONFIRMAR', width=10, font=('Ivy 8 bold'), bg=cor2, fg=cor4, relief=RAISED, overrelief=RIDGE)
        b_confirmar.place(x=290, y=110)

    except:
        messagebox.showwarning('Dados','POR GENTILEZA SELECIONE UM USUÁRIO!')

def remover():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']
        
        telefone = str(tree_lista[2])
        remover_dados(telefone)
        messagebox.showinfo('Dados','DADOS FORAM DELETADOS COM SUCESSO!')
        
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        mostrar_dados()

    except:
        messagebox.showwarning('Dados','POR GENTILEZA SELECIONE UM USUÁRIO!')


def procurar():
    telefone = e_procurar.get()

    dados = pesquisar_dados(telefone)

    tree.delete(*tree.get_children())

    for item in dados:
        tree.insert('', 'end', values=item)

    e_procurar.delete(0, 'end')


# Configurando o FRAME baixo
l_nome = Label(frame_baixo, text='Nome', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left',relief=FLAT, font=('', 10), highlightthickness=1)
e_nome.place(x=80, y=20)

l_sexo = Label(frame_baixo, text='Sexo', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_sexo.place(x=10, y=50)
c_sexo = Combobox(frame_baixo, width=27)
c_sexo['value'] = ('', 'F', 'M')
c_sexo.place(x=80, y=50)

l_tel = Label(frame_baixo, text='Telefone', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_tel.place(x=10, y=80)
e_tel = Entry(frame_baixo, width=25, justify='left', relief=FLAT,font=('', 10), highlightthickness=1)
e_tel.place(x=80, y=80)

l_email = Label(frame_baixo, text='Email', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_email.place(x=10, y=110)
e_email = Entry(frame_baixo, width=25, justify='left',relief=FLAT, font=('', 10), highlightthickness=1)
e_email.place(x=80, y=110)

b_procurar = Button(frame_baixo, command=procurar, text='Procurar', font=('Ivy 8 bold'), bg=cor5, fg=cor4, relief=RAISED, overrelief=RIDGE)
b_procurar.place(x=290, y=20)
e_procurar = Entry(frame_baixo, width=16, justify='left',relief=FLAT, font=('', 11), highlightthickness=1)
e_procurar.place(x=347, y=21)


b_ver = Button(frame_baixo,command=mostrar_dados, text='Ver Dados', width=10, font=('Ivy 8 bold'), bg=cor5, fg=cor4, relief=RAISED, overrelief=RIDGE)
b_ver.place(x=290, y=50)

b_adcionar = Button(frame_baixo, command=inserir, text='Adicionar', width=10, font=('Ivy 8 bold'), bg=cor2, fg=cor4, relief=RAISED, overrelief=RIDGE)
b_adcionar.place(x=400, y=50)

b_atualizar = Button(frame_baixo, command=atualizar, text='Atualizar', width=10, font=('Ivy 8 bold'), bg=cor7, fg=cor4, relief=RAISED, overrelief=RIDGE)
b_atualizar.place(x=400, y=80)

b_deletar = Button(frame_baixo, command=remover, text='Deletar', width=10, font=('Ivy 8 bold'), bg=cor6, fg=cor4, relief=RAISED, overrelief=RIDGE)
b_deletar.place(x=400, y=110)



janela.mainloop()