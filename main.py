from db import criar_tabelas
from login import tela_login
from entrevistas import tela_pesquisa
from imprimir import imprimir_todas_respostas
criar_tabelas()

if __name__ == "__main__":
    # criar_tabelas()
    # tela_login(tela_pesquisa)
    imprimir_todas_respostas()
    
