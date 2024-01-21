from tkinter import*
from tkinter import PhotoImage, messagebox, ttk
import customtkinter
import funcoes
#conexão de banco de dados Sqlite
import sqlite3
import conexao_sqlite3
banco = sqlite3.connect('bd_biblioteca.db')
cursor = banco.cursor()

            
#def sistema():
janela = Tk()
janela.title("Biblioteca")
janela.geometry("1000x520+250+100") 
janela.config(background='white')
janela.iconphoto(False, PhotoImage(file='imagens/favicon.png'))
janela.resizable(False,False)
frame_topo = Frame(janela, width=1000, height=44, bg='#302796')
frame_topo.pack(side='top')   
img = PhotoImage(file="imagens/icone.png")
label_imagem = Label(frame_topo, image=img, bg='#302796')
label_imagem.place(x=17, y=8)                                                                                                                       
texto = Label(frame_topo, text='Nossa Livraria!', font='Inter 16', bg='#302796', fg='white')
texto.place(x=53, y=10)
frame_principal = Frame (width=800, height=358)
frame_principal.pack(side=RIGHT)  
#funçoes
# essa função controla os botões de ações e chamar outras funções 
def control(i):
    if i == 'cadastrarLivros':
        for widget in frame_principal.winfo_children():
            widget.destroy()
        cadastrarLivros()
    if i == 'cadastrarUsuarios':
        for widget in frame_principal.winfo_children():
            widget.destroy()
        cadastrarUsuarios()    
    
def cadastrarUsuarios():
    #frame entrada de dados
    frame_conteudo_usuarios = Frame(frame_principal, width=800, height=358, bg='white')
    frame_conteudo_usuarios.pack(side='left')

    #cadastro de usuários
    titulo_usuarios = Label(frame_conteudo_usuarios, text='Cadastro de Usuários', fg='black' , bg='white', font=('Inter 14'))
    titulo_usuarios.place(x=20,y=0)
    #entrada de dados nome
    nome = Label(frame_conteudo_usuarios, text='Nome:', fg='#8C8B8B' , font=('Inter 12'), bg='white')
    nome.place(x=20,y=25)
    entry_nome = customtkinter.CTkEntry(frame_conteudo_usuarios, width=296, height=30, fg_color='white', border_color='#B6B6B6', border_width=1, text_color='black' )
    entry_nome.place(x=20, y=47)

    #entrada de endereço
    endereco = Label(frame_conteudo_usuarios, text='Endereço:', fg='#8C8B8B' , font=('Inter 12'), bg='white')
    endereco.place(x=322,y=25)
    entry_endereco = customtkinter.CTkEntry(frame_conteudo_usuarios, width=330, height=30, fg_color='white', border_color='#B6B6B6', border_width=1, text_color='black')
    entry_endereco.place(x=320, y=47)

    #entrada de telefone
    telefone = Label(frame_conteudo_usuarios, text='Telefone:', fg='#8C8B8B' , font=('Inter 12'), bg='white')
    telefone.place(x=20,y=80)
    entry_telefone = customtkinter.CTkEntry(frame_conteudo_usuarios, width=160, height=30, fg_color='white', border_color='#B6B6B6', border_width=1, text_color='black')
    entry_telefone.place(x=20, y=102)
    
    #entrada de cpf
    cpf = Label(frame_conteudo_usuarios, text='CPF:', fg='#8C8B8B' , font=('Inter 12'), bg='white')
    cpf.place(x=185,y=80)
    entry_cpf = customtkinter.CTkEntry(frame_conteudo_usuarios, width=150, height=30, fg_color='white', border_color='#B6B6B6', border_width=1, text_color='black')
    entry_cpf.place(x=185, y=102) 
    #botão cadastrar usuários
    bottom = customtkinter.CTkButton(frame_conteudo_usuarios, text="Cadastrar",font=('Inter',12), fg_color='#5DAA2A', corner_radius=40,width=83, height=24)
    bottom.place(x=565, y=300)

 
def cadastrarLivros():

    #frame entrada de dados
    frame_conteudo = Frame(frame_principal, width=800, height=358, bg='white')
    frame_conteudo.pack(side='left')

    #cadastro de livros titulos
    titulo = Label(frame_conteudo, text='Cadastro de Livros', fg='black' , bg='white', font=('Inter 14'))
    titulo.place(x=20,y=0)
    #entrada de dados titulo
    titulo = Label(frame_conteudo, text='Título:', fg='#8C8B8B' , font=('Inter 12'), bg='white')
    titulo.place(x=20,y=25)
    entry_titulo = customtkinter.CTkEntry(frame_conteudo, width=296, height=30, fg_color='white', border_color='#B6B6B6', border_width=1, text_color='black' )
    entry_titulo.place(x=20, y=47)

    #entrada de dados autor
    autor = Label(frame_conteudo, text='Autor:', fg='#8C8B8B' , font=('Inter 12'), bg='white')
    autor.place(x=322,y=25)
    entry_autor = customtkinter.CTkEntry(frame_conteudo, width=150, height=30, fg_color='white', border_color='#B6B6B6', border_width=1, text_color='black')
    entry_autor.place(x=320, y=47)

    #entrada de dados editora
    editora = Label(frame_conteudo, text='Editora:', fg='#8C8B8B' , font=('Inter 12'), bg='white')
    editora.place(x=20,y=80)
    entry_editora = customtkinter.CTkEntry(frame_conteudo, width=124, height=30, fg_color='white', border_color='#B6B6B6', border_width=1, text_color='black')
    entry_editora.place(x=20, y=102)
    
    
    #entrada de dados ano de publicação
    ano = Label(frame_conteudo, text='Ano de publicação:', fg='#8C8B8B' , font=('Inter 12'), bg='white')
    ano.place(x=160,y=80)
    entry_ano = customtkinter.CTkEntry(frame_conteudo, width=150, height=30, fg_color='white', border_color='#B6B6B6', border_width=1, text_color='black')
    entry_ano.place(x=160, y=102)
    
    

 #função para exibir livros
    def exibirlivros():
        c = banco.cursor()
        c.execute("SELECT * FROM livros")
        livros = c.fetchall()
        
        for item in livros:
            print(item)
            treeview.insert("",END, values=item)
        
         
#função deletar itens treeviw 
    def deletar():
        itemSelecionado = treeview.selection()
        treeview.delete(itemSelecionado) 
        
#função inserir itens treeview
    def inserir():
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        editora = entry_editora.get()
        ano = entry_ano.get()
        if titulo =='' or autor == '' or editora=='' or ano =='':
            messagebox.showerror(title='cadastro', message='Preenchar os campos')
        else: 
            messagebox.showinfo(title='cadastro', message='cadastrado realizado!')
            treeview.insert('', END, values=(entry_titulo.get(), entry_autor.get(), entry_editora.get(), entry_ano.get()))
            #codigo abaixo insere dados no banco de dados
            cursor.execute("INSERT INTO livros VALUES ('"+titulo+"','"+autor+"','"+editora+"','"+ano+"')")
            banco.commit()  
            
            
     
           
    #botão cadastrar livros
    bottom = customtkinter.CTkButton(frame_conteudo, text="Cadastrar",font=('Inter',12), fg_color='#144F7F', corner_radius=40,width=83, height=24, command=inserir)
    bottom.place(x=565, y=300)
    
    #botão deletar
    bottom = customtkinter.CTkButton(frame_conteudo, text="deletar",font=('Inter',12), fg_color='red', corner_radius=40,width=83, height=24, command=deletar)
    bottom.place(x=565, y=270)

    #crinado treeview para inserir dados dos livros
    treeview = ttk.Treeview(frame_conteudo,selectmode='browse', height=9, columns=("titulo", "autor","editora","ano da publicacao"), show='headings' )
    treeview.column("titulo",width=140, minwidth=50)
    treeview.heading("#1", text="Título")
    treeview.column("autor",width=125)
    treeview.heading("#2", text="Autor")
    treeview.column("editora",width=140)
    treeview.heading("#3", text="Editora")
    treeview.column("ano da publicacao",width=115)
    treeview.heading("#4", text="Ano")
    treeview.place(x=20, y=140)
        
        
    #barra de rolagem teeview
    sb = Scrollbar(treeview, orient=VERTICAL)
    sb.place(x=500, y=100)
    treeview.config(yscrollcommand=sb.set)
    sb.config(command=treeview.yview)


#menus Frame
fram_menus = Frame(janela, width=200, height=378)
fram_menus.pack(side=LEFT)
#menu título 
texto = Label(fram_menus, text='Menus: ' ,fg='black' , font=('Inter 14'))
texto.place(x=10, y=5)

#menu cadastrar livros
imagem = PhotoImage(file="imagens/01.png")
button = customtkinter.CTkButton(fram_menus, image=imagem , text="Cadastrar Livros",font=('Inter',12), fg_color='#302796', corner_radius=40,width=173, height=30, command=lambda:control('cadastrarLivros'))
button.place(x=8, y=35)

#menu Cadastrar usuários
imagem = PhotoImage(file="imagens/02.png")
button = customtkinter.CTkButton(fram_menus, image=imagem ,text="Cadastrar usuários",font=('Inter',12), fg_color='#302796', corner_radius=40,width=173, height=30, command=lambda:control('cadastrarUsuarios') )
button.place(x=8, y=75)   

#menu Fazer empréstimos
imagem = PhotoImage(file="imagens/03.png")
button = customtkinter.CTkButton(fram_menus, image=imagem ,text="Fazer empréstimos",font=('Inter',12), fg_color='#302796', corner_radius=40,width=173, height=30,)
button.place(x=8, y=115)

#menu Todos Livros
imagem = PhotoImage(file="imagens/04.png")
button = customtkinter.CTkButton(fram_menus, image=imagem ,text="Todos Livros",font=('Inter',12), fg_color='#302796', corner_radius=40,width=173, height=30, command=conexao_sqlite3.qtlivros)
button.place(x=8, y=155)

#menu Todos usuários
imagem = PhotoImage(file="imagens/05.png")
button = customtkinter.CTkButton(fram_menus, image=imagem ,text="Todos usuários",font=('Inter',12), fg_color='#302796', corner_radius=40,width=173, height=30,)
button.place(x=8, y=190)

#menu Livros emprestados
imagem = PhotoImage(file="imagens/06.png")
button = customtkinter.CTkButton(fram_menus, image=imagem ,text="Livros emprestados",font=('Inter',12), fg_color='#302796', corner_radius=40,width=173, height=30,)
button.place(x=8, y=232) 


    

    
janela.mainloop()