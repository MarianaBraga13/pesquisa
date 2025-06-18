import tkinter as tk
from tkinter import messagebox
from db import conectar

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
    
    tk.Button(root, text="Salvar respostas", command=lambda:salvar_pesquisa(resposta1_entry, resposta2_entry, resposta3_entry)).pack(pady=10)