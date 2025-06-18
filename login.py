import tkinter as tk
from db import conectar
from tkinter import messagebox


def cadastrar_usuario(nome_entry, senha_entry):
    nome = nome_entry.get()
    senha = senha_entry.get()

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE nome=?', (nome,))
    if cursor.fetchone():
        messagebox.showerror("Erro", "Usuário já existe")
    else:
        cursor.execute('INSERT INTO usuarios (nome, senha) VALUES (?, ?)', (nome, senha))
        messagebox.showinfo("Info", "Usuário(a) cadastrado (a) com sucesso!")
        conn.commit()
        conn.close()


def validar_usuario(nome_entry, senha_entry, root, tela_pesquisa):
    nome = nome_entry.get()
    senha = senha_entry.get()
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM USUARIOS WHERE nome=? AND senha=?', (nome, senha))
    user = cursor.fetchone()
    if user:
        messagebox.showinfo("Info", "Login efetuado com sucesso!")
        root.destroy()
        tela_pesquisa()
        
    else:
        messagebox.showwarning("Atenção", "Usuário (a) não cadastrado (a).")
        conn.close()

def tela_login(tela_pesquisa):
    root = tk.Tk()
    root.title("Login")
    root.geometry("300x200")

    tk.Label(root, text="Usuário").pack()
    nome_entry = tk.Entry(root)
    nome_entry.pack()

    tk.Label(root, text="Senha").pack()
    senha_entry = tk.Entry(root, show="*")
    senha_entry.pack()

    tk.Button(root, text="Cadastrar", command=lambda:cadastrar_usuario(nome_entry, senha_entry)).pack(pady=5)
    tk.Button(root, text="Login", command=lambda:validar_usuario(nome_entry, senha_entry, root, tela_pesquisa)).pack(pady=5)
    root.mainloop()