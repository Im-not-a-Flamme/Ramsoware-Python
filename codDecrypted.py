import os  # Importe a biblioteca os para trabalhar com arquivos e diretórios
from cryptography.fernet import Fernet  # Importe o módulo Fernet para criptografia e descriptografia

key_path = "chave.key"  # Defina o caminho para o arquivo da chave
exclude_files = ["ramsoware.py", key_path, "codDecrypted.py"]  # Defina uma lista de arquivos a serem excluídos da descriptografia

with open(key_path, "rb") as f:  # Abra o arquivo da chave em modo de leitura binária
    key = f.read()  # Armazene a chave lida do arquivo em uma variável

for file in os.listdir():  # Para cada arquivo no diretório atual...
    if file in exclude_files or not os.path.isfile(file):  # Verifique se o arquivo deve ser excluído ou não é um arquivo
        continue  # Pule para o próximo arquivo se necessário

    with open(file, "rb") as f:  # Abra o arquivo em modo de leitura binária
        content = f.read()  # Armazene o conteúdo lido do arquivo em uma variável

    content_decrypted = Fernet(key).decrypt(content)  # Descriptografe o conteúdo do arquivo usando a chave

    with open(file, "wb") as f:  # Abra o arquivo em modo de gravação binária
        f.write(content_decrypted)  # Escreva o conteúdo descriptografado no arquivo
