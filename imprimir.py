from fpdf import FPDF
import datetime
from db import conectar

def imprimir_todas_respostas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM entrevistas')
    encontradas = cursor.fetchall()
    conn.close()
    if encontradas:
        for respostas in encontradas:
            print(f"Seguem todas as respostas: {respostas}")

    



    