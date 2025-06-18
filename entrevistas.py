import tkinter as tk
from tkinter import messagebox
from db import conectar
from fpdf import FPDF
import datetime

def salvar_pesquisa(resposta1_entry, resposta2_entry, resposta3_entry):
    resposta1 = resposta1_entry.get()
    resposta2 = resposta2_entry.get()
    resposta3 = resposta3_entry.get()
    try:
        if not resposta1 or not resposta2 or not resposta3:
            messagebox.showerror("Erro", "Favor responder a todas as questões.")
        else:    
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO entrevistas (resposta1, resposta2, resposta3) VALUES (?, ?, ?)',(resposta1, resposta2, resposta3))
            messagebox.showinfo("Info", "Respostas salvas com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível salvar as respostas :{e}")
    finally:
        try:
            conn.commit()
            conn.close()
        except:
            pass

def salvar_respostas_em_pdf(resposta1, resposta2, resposta3, nome_arquivo="respostas.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)

    pdf.cell(200, 10, txt="Respostas da Entrevista", ln=True, align='C')
    pdf.ln(10)

    pdf.multi_cell(0, 10, txt=f"Pergunta 1: O que você entende por Inteligência Artificial?\nResposta: {resposta1}\n")
    pdf.multi_cell(0, 10, txt=f"Pergunta 2: O que você acha que Platão diria sobre o progresso da tecnologia?\nResposta: {resposta2}\n")
    pdf.multi_cell(0, 10, txt=f"Pergunta 3: Você considera que o mundo está vivenciando uma revolução?\nResposta: {resposta3}\n")

    pdf.output(nome_arquivo)            

def exportar_pdf(resposta1_entry, resposta2_entry, resposta3_entry):
    resposta1 = resposta1_entry.get()
    resposta2 = resposta2_entry.get()
    resposta3 = resposta3_entry.get()

    if not resposta1 or not resposta2 or not resposta3:
        messagebox.showerror("Erro", "Preencha todas as respostas antes de exportar.")
        return

    data = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"respostas{data}.pdf"

    salvar_respostas_em_pdf(resposta1, resposta2, resposta3, nome_arquivo)

def tela_pesquisa():
    root = tk.Tk()
    root.title("Tela de Pesquisa")
    root.geometry("800x600")

    tk.Label(root, text="Perguntas sobre tecnologia").pack()
    
    tk.Label(root,text="Pergunta 1 - O que você entende por Inteligência Artificial?").pack()
    resposta1_entry = tk.Entry(root)
    resposta1_entry.pack(pady=5)

    tk.Label(root,text="Pergunta 2 - O que você acha que Platão diria a respeito do progresso da tecnologia em nosso tempo?").pack()
    resposta2_entry = tk.Entry(root)
    resposta2_entry.pack(pady=5)

    tk.Label(root,text="Pergunta 3 - Você considera que o mundo está vivenciando uma revolução?").pack()
    resposta3_entry = tk.Entry(root)
    resposta3_entry.pack(pady=5)
    
    tk.Button(root, text="Salvar respostas", command=lambda:salvar_pesquisa(resposta1_entry, resposta2_entry, resposta3_entry)).pack(pady=5)
    tk.Button(root, text="Exportar respostas em .pdf", command=lambda:exportar_pdf(resposta1_entry, resposta2_entry, resposta3_entry)).pack(pady=5)