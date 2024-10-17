from pathlib import Path
import os
import subprocess

# BUSCAR NOME DA PASTA DE USUÁRIO
diretorio_home = Path.home()
# ENTRAR NA PASTA DE USUÁRIO
os.chdir(diretorio_home)

# VARIAVÉL PARA DIRETÓRIO PADRÃO DOS PROJETOS
diretorio_projetos = f'{diretorio_home}/Projetos'

# VERIFICA SE EXISTE O DIRETÓRIO PADRÃO CASO NÃO ELE O CRIA
if os.path.exists(diretorio_projetos) == False:
    os.mkdir(diretorio_projetos)

# ENTRA NO DIRETÓRIO PADRÃO
os.chdir(diretorio_projetos)

# SOLICITA AO USUÁRIO UM NOME PARA O PROJETO A SER CRIADO
dir_novo_projeto = input('Digite o nome do Projeto a ser criado: ')

# VARIÁVEL COM O CAMINHO COMPLETO DO PROJETO A SER CRIADO
path_full_novo_projeto = f'{diretorio_projetos}/{dir_novo_projeto}'

if os.path.exists(path_full_novo_projeto) == False:
    os.mkdir(path_full_novo_projeto)

# ATUALIZA O LINUX
subprocess.run(f'''sudo apt update -y && sudo apt-get upgrade -y''', shell=True, check=True, executable='/bin/bash')

# ENTRA NO DIRETÓRIO DO USUÁRIO
subprocess.run(f'''cd ~''', shell=True, check=True, executable='/bin/bash')

# INSTALA O NODEJS V20
subprocess.run(f'''curl -sL https://deb.nodesource.com/setup_20.x -o /tmp/nodesource_setup.sh''', shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''sudo bash /tmp/nodesource_setup.sh''', shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''sudo apt install nodejs -y''', shell=True, check=True, executable='/bin/bash')

subprocess.run(f'''sudo npm install -g yarn''', shell=True, check=True, executable='/bin/bash')

os.chdir(path_full_novo_projeto)
subprocess.run(f'''yarn init -y''', shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''touch index.js''', shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''yarn add commander''', shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''yarn add chalk''', shell=True, check=True, executable='/bin/bash')

subprocess.run(f'''echo "O seu path é " $(pwd)''', shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''code .''', shell=True, check=True, executable='/bin/bash')
