from tkinter import messagebox
import biblioteca
import customtkinter
import main

#Funções 
def fechar(event):
    main.frame_direito.destroy()
    main.alterarsenha()
    
def validarLogin():
    
    user = main.entry_nome.get()
    senha = main.entry_senha.get()
    
    user1 = 'Alex'
    senha1 = '123'
    
    if user =='' or user1 == '':
        messagebox.showerror(title='login', message='Preenchar os campos')
    elif user!= user1:
        messagebox.showerror(title='login', message='usuário incorreto! tente novamente')
        
        
    else:
        main.root.destroy()
        biblioteca.sistema()
        
        


