from db import criar_tabelas
from login import tela_login
from entrevistas import tela_pesquisa
criar_tabelas()

if __name__ == "__main__":
    criar_tabelas()
    tela_login(tela_pesquisa)
    
