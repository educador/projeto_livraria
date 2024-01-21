import sqlite3
#conexão de banco de dados Sqlite
import sqlite3
banco = sqlite3.connect('bd_biblioteca.db')
cursor = banco.cursor()

banco = sqlite3.connect('bd_biblioteca.db')

cursor = banco.cursor()

#criando tabela e inserindo 
#cursor.execute("CREATE TABLE livros  (titulo text, autor text) ")
#inserindo dados
#cursor.execute("INSERT INTO livros VALUES ('++','jorge')")

#banco.commit()

#cursor.execute("SELECT * FROM livros  ")
 
#print(cursor.fetchall())

#função para contar quantos livro cadastrado 
def qtlivros():
        cursor.execute("SELECT count(titulo) FROM livros")
        lista = cursor.fetchall()   
        for i in lista:
            print(i)  
