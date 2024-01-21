#Autor: Alex Santos  / programa: Livraria 
from tkinter import *
from tkinter import messagebox
import customtkinter
import biblioteca
import funcoes

root = Tk()

#titulo da janela, tamanho, favicon 
root.title("Login")
root.geometry("700x432+350+100")
root.iconphoto(False, PhotoImage(file='imagens/favicon.png'))
root.resizable(False,False)
root.config(background='white')

#Funções 
def fechar(event):
    frame_direito.destroy()
    alterarsenha()
    
def validarLogin():
    
    user = entry_nome.get()
    senha = entry_senha.get()
    
    user1 = 'Alex'
    senha1 = '123'
    
    if user =='' or user1 == '':
        messagebox.showerror(title='login', message='Preenchar os campos')
    elif user!= user1:
        messagebox.showerror(title='login', message='usuário incorreto! tente novamente')
        
        
    else:
        root.destroy()
        biblioteca.sistema()

#frame direito
frame_direito = customtkinter.CTkFrame(root, width=320, height=416, fg_color='white' )
frame_direito.pack(side=RIGHT)
#título login 
titulo_login = Label(frame_direito, text="Login", font=('Inter 24'), bg='white' )
titulo_login.place(x=110, y=100)   
#entrada de dados
entry_nome = customtkinter.CTkEntry(frame_direito, fg_color='#E4E3E3', corner_radius=40, border_color='#E0E0E0', width=237, height=37, text_color='#464646', placeholder_text='Usuário:')
entry_nome.place(x=35, y=147)
entry_senha = customtkinter.CTkEntry(frame_direito, fg_color='#E4E3E3', corner_radius=40, border_color='#E0E0E0', width=237, height=37, text_color='#464646', placeholder_text='Senha:', show='*')
entry_senha.place(x=35, y=205)
#botões de ação
button = customtkinter.CTkButton(frame_direito, text="Entrar",font=('Inter',18), fg_color='#144F7F', corner_radius=40,width=157, height=30, command=validarLogin)
button.place(x=70, y=258)
#titulo (esqueceu a senha?)
label = Label(frame_direito, text="Esqueceu a senha?",font=('Inter',12), fg='#144F7F',bg='white', cursor="hand2")
label.place(x=80, y=290)
label.bind("<Button-1>", fechar)
# titulo (Ainda não tem conta?)
texto_senha = Label(frame_direito, text='Ainda não tem conta?', font=('Inter 13'), bg='white' )
texto_senha.place(x=70, y=360)
#botões de ação cadastra-se
button = customtkinter.CTkButton(frame_direito, text="Cadastre-se",font=('Inter',12), fg_color='black', corner_radius=40,width=96, height=22)
button.place(x=100, y=385) 
    

#frame esquerdo 
frame_esquerdo = Frame(root,width=380, height=432, bg='#302796')
frame_esquerdo.pack(side=LEFT)
#icone de livro
img = PhotoImage(file="imagens/iconep.png" )
label_imagem = Label(frame_esquerdo, image=img, bg='#302796', width=86, height=86)
label_imagem.place(x=150, y=100)
#titulo
titulo_principal = Label(root, text="Seja Bem Vindo!", font='Inter 24', fg='white', bg='#302796')
titulo_principal.place(x=70, y=180)
titulo_principal = Label(root, text="Nossa Livraria", font='Inter 32', fg='white', bg='#302796')
titulo_principal.place(x=50, y=215)


def alterarsenha():
    #frame alterar senha
    frame_alterarsenha = customtkinter.CTkFrame(root, width=320, height=416, fg_color='white' )
    frame_alterarsenha.pack(side=RIGHT)
    
    #icone cadeado
    
    imagem = PhotoImage(file="imagens/cadeado.png")
    w = Label(frame_alterarsenha, image=imagem, bg='white')
    w.imagem = imagem
    w.place(x=130, y=60)
     
    #título  
    titulo_login = Label(frame_alterarsenha, text="Alterar senha de acesso", font=('Inter 14'), bg='white' )
    titulo_login.place(x=50, y=100)

    #entrada de dados
    entry_nome = customtkinter.CTkEntry(frame_alterarsenha, fg_color='#E4E3E3', corner_radius=40, border_color='#E0E0E0', width=237, height=37, text_color='#464646', placeholder_text='Nova senha:')
    entry_nome.place(x=35, y=147)
    entry_senha = customtkinter.CTkEntry(frame_alterarsenha, fg_color='#E4E3E3', corner_radius=40, border_color='#E0E0E0', width=237, height=37, text_color='#464646', placeholder_text='Confirmar senha:')
    entry_senha.place(x=35, y=205)

    #botões de ação
    button = customtkinter.CTkButton(frame_alterarsenha, text="atualizar",font=('Inter',18), fg_color='#5DAA2A', corner_radius=40,width=157, height=30)
    button.place(x=70, y=258)
    #botões de ação voltar
    button = customtkinter.CTkButton(frame_alterarsenha, text="< voltar",font=('Inter',12), fg_color='#144F7F', corner_radius=40,width=96, height=22)
    button.place(x=100, y=385)   

root.mainloop()
