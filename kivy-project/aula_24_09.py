from pathlib import Path
import os
import subprocess
#Buscar nome da pasta dde usuário
diretorio_home = Path.home()
#entrar na pasta de usuário
os.chdir(diretorio_home)

#VARIAVEL PARA DIRETORIO PADRÃO DOS PROJETOS
diretorio_projetos = f'{diretorio_home}/Projetos'

#variavel para diretorio padrão caso não ele o cria
if os.path.exists(diretorio_projetos) == False:
    os.mkdir(diretorio_projetos)

#entra no diretório padrão
os.chdir(diretorio_projetos)

#solicita ao usuário um nome para o projeto a ser criado
dir_novo_projeto = input('Digite o nome do projeto a ser criado: ')

#Variável com o caminho completo do projeto a ser criado
path_full_novo_projeto = f'{diretorio_projetos}/{dir_novo_projeto}'

#Caso não exista o diretorio cria
if os.path.exists(path_full_novo_projeto) == False:
    os.mkdir(path_full_novo_projeto)

#Entra no diretorio
os.chdir(path_full_novo_projeto)

#verifica se na raiz do projeto existe um arquivo main
#caso não ele não é criado
if os.path.isfile(f'{path_full_novo_projeto}/main.py') == False:
    os.mknod('main.py')

#Exibe o caminho completo do novo projeto criado
print(f'{path_full_novo_projeto}/main.py')

subprocess.run(f'''sudo apt update -y && sudo apt-get upgrade -y''', shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''sudo apt install python3-pip''',shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''sudo apt install python3-venv''',shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''sudo apt install python3 -m venv.venv''',shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''source.venv/bin/activate''',shell=True, check=True, executable='/bin/bash')

#Instala dependencias do kivy
subprocess.run(f'''sudo apt-get update && sudo apt-get install libgl1''',shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''python -m pip install -- upgrade pip setuptools virtualenv''',shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''python -m pip install "kivy[base]" kivy_examples''',shell=True, check=True, executable='/bin/bash')
#Abre o VS CODE na pasta do projeto novo criado
subprocess.run(f'''code{path_full_novo_projeto}''',shell=True, check=True, executable='/bin/bash')


#uma função recursiva é uma função que chama ela mesma.,
#conseguimos escrever os métodos da classe quando



